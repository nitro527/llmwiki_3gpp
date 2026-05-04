"""
test_api.py — api.py 단위 테스트

테스트 대상:
- truncate_content(): 길이 제한
- call_simple(): 알 수 없는 백엔드 처리
- call_simple(): 재시도 로직 (MAX_RETRIES=3, exponential backoff)
- call_simple(): 429 응답 시 별도 처리 (재시도 카운트 제외)
- "[LLM 호출 실패]" prefix 형식 보장

LLM 호출 mock — 실제 API 호출 없음.
"""
import sys
import time
from pathlib import Path
from unittest.mock import patch, MagicMock

import pytest

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

import wiki_builder.api as api_module
from wiki_builder.api import truncate_content, call_simple, _RateLimitError, _RetryableError


# ──────────────────────────────────────────────
# truncate_content 테스트
# ──────────────────────────────────────────────

class TestTruncateContent:
    def test_short_text_unchanged(self):
        text = "hello world"
        result = truncate_content(text, max_chars=100)
        assert result == text

    def test_exact_limit_unchanged(self):
        text = "a" * 100
        result = truncate_content(text, max_chars=100)
        assert result == text

    def test_over_limit_truncated(self):
        text = "a" * 200
        result = truncate_content(text, max_chars=100)
        assert len(result) == 100

    def test_truncated_content_is_prefix(self):
        text = "abcdefghij" * 20
        result = truncate_content(text, max_chars=50)
        assert result == text[:50]

    def test_label_does_not_affect_output(self):
        text = "x" * 200
        result = truncate_content(text, max_chars=100, label="test_label")
        assert len(result) == 100


# ──────────────────────────────────────────────
# call_simple — 알 수 없는 백엔드
# ──────────────────────────────────────────────

class TestCallSimpleUnknownBackend:
    def test_unknown_backend_returns_failure_prefix(self):
        result = call_simple("system", "user", backend="nonexistent_backend")
        assert result.startswith("[LLM 호출 실패]")

    def test_unknown_backend_mentions_backend_name(self):
        result = call_simple("system", "user", backend="fake_llm")
        assert "fake_llm" in result


# ──────────────────────────────────────────────
# call_simple — 재시도 로직
# ──────────────────────────────────────────────

class TestCallSimpleRetry:
    """_RetryableError 발생 시 MAX_RETRIES=3회 재시도 후 실패 메시지 반환."""

    def test_retries_three_times_then_fails(self):
        call_count = 0

        def failing_backend(system, user, temperature, **kwargs):
            nonlocal call_count
            call_count += 1
            raise _RetryableError("연결 오류")

        with patch.object(api_module, '_call_claude', side_effect=failing_backend):
            with patch('time.sleep'):  # sleep 스킵
                result = call_simple("sys", "user", backend="claude")

        assert result.startswith("[LLM 호출 실패]")
        assert call_count == api_module.MAX_RETRIES

    def test_succeeds_on_second_attempt(self):
        call_count = 0

        def backend_fails_once(system, user, temperature, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise _RetryableError("일시적 오류")
            return "성공 응답"

        with patch.object(api_module, '_call_claude', side_effect=backend_fails_once):
            with patch('time.sleep'):
                result = call_simple("sys", "user", backend="claude")

        assert result == "성공 응답"
        assert call_count == 2

    def test_failure_message_has_correct_prefix(self):
        def always_fail(system, user, temperature, **kwargs):
            raise _RetryableError("timeout")

        with patch.object(api_module, '_call_claude', side_effect=always_fail):
            with patch('time.sleep'):
                result = call_simple("sys", "user", backend="claude")

        assert result.startswith("[LLM 호출 실패]")

    def test_unexpected_exception_returns_failure(self):
        def raises_unexpected(system, user, temperature, **kwargs):
            raise ValueError("예상치 못한 오류")

        with patch.object(api_module, '_call_claude', side_effect=raises_unexpected):
            result = call_simple("sys", "user", backend="claude")

        assert result.startswith("[LLM 호출 실패]")


# ──────────────────────────────────────────────
# call_simple — 429 (RateLimitError) 처리
# ──────────────────────────────────────────────

class TestCallSimpleRateLimit:
    """
    _RateLimitError 발생 시:
    - MAX_RETRIES 카운트 증가 없이 대기 후 재시도
    - 이후 성공하면 정상 결과 반환
    """

    def test_rate_limit_does_not_count_against_retries(self):
        """RateLimitError 한 번 → 이후 성공 → 정상 반환 (attempt 소비 없음)."""
        call_count = 0

        def backend_429_then_ok(system, user, temperature, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise _RateLimitError("HTTP 429")
            return "성공"

        with patch.object(api_module, '_call_claude', side_effect=backend_429_then_ok):
            with patch('time.sleep'):
                result = call_simple("sys", "user", backend="claude")

        assert result == "성공"

    def test_rate_limit_sleeps_before_retry(self):
        """RateLimitError 발생 시 RATE_LIMIT_WAIT만큼 대기."""
        sleep_calls = []

        def record_sleep(seconds):
            sleep_calls.append(seconds)

        call_count = 0

        def backend_429_then_ok(system, user, temperature, **kwargs):
            nonlocal call_count
            call_count += 1
            if call_count == 1:
                raise _RateLimitError("HTTP 429")
            return "성공"

        with patch.object(api_module, '_call_claude', side_effect=backend_429_then_ok):
            with patch('time.sleep', side_effect=record_sleep):
                result = call_simple("sys", "user", backend="claude")

        assert result == "성공"
        # RATE_LIMIT_WAIT가 sleep_calls에 포함되어야 함
        assert api_module.RATE_LIMIT_WAIT in sleep_calls


# ──────────────────────────────────────────────
# call_simple — 입력 truncate
# ──────────────────────────────────────────────

class TestCallSimpleInputTruncate:
    def test_oversized_input_truncated_before_call(self):
        """system + user > MAX_CONTEXT_CHARS 이면 user 자동 truncate 후 호출."""
        received_user = {}

        def capture_call(system, user, temperature, **kwargs):
            received_user['val'] = user
            return "ok"

        big_user = "u" * (api_module.MAX_CONTEXT_CHARS + 10000)

        with patch.object(api_module, '_call_claude', side_effect=capture_call):
            result = call_simple("sys", big_user, backend="claude")

        assert result == "ok"
        # user가 truncate되어 실제 LLM에 전달된 크기가 MAX_CONTEXT_CHARS 이하
        total = len("sys") + len(received_user['val'])
        assert total <= api_module.MAX_CONTEXT_CHARS
