"""
test_generate.py — generate.py 단위 테스트

테스트 대상:
- _detect_hallucination(): 3어절 이상 구절 5회 반복 → True 반환
- _detect_hallucination(): 정상 텍스트 → False 반환
- run_generate(): generated=True 플래그 업데이트
- run_generate(): hallucination 감지 시 failed 반환

LLM 호출 mock — 실제 API 호출 없음.
"""
import json
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from wiki_builder.generate import _detect_hallucination, run_generate


# ──────────────────────────────────────────────
# _detect_hallucination 테스트
# ──────────────────────────────────────────────

class TestDetectHallucination:
    def test_normal_text_returns_false(self):
        text = """
## 정의
PUSCH는 Physical Uplink Shared Channel의 약자로 5G NR에서 사용된다.

## 상세 설명
PUSCH는 데이터 전송에 사용되는 채널이다.
UCI를 포함할 수 있으며 다양한 MCS를 지원한다.
"""
        assert _detect_hallucination(text) is False

    def test_short_text_returns_false(self):
        """단어 수가 15 미만이면 False."""
        text = "짧은 텍스트 네 단어"
        assert _detect_hallucination(text) is False

    def test_repeated_phrase_5_times_returns_true(self):
        """3어절 이상 구절이 5회 반복되면 True."""
        phrase = "PUSCH 채널 설명 내용"  # 4 words
        # 5회 반복
        text = " ".join([phrase] * 5 + ["추가 내용을 덧붙여서 최소 15어절 이상으로 만든다 여기에 더 많은 단어"])
        assert _detect_hallucination(text) is True

    def test_repeated_phrase_4_times_returns_false(self):
        """4회만 반복 → False."""
        phrase = "PUSCH 채널 설명 내용"
        text = " ".join([phrase] * 4 + ["다른 내용 추가하여 충분한 단어 수를 확보한다 더 많은 다양한 텍스트"])
        assert _detect_hallucination(text) is False

    def test_headers_excluded_from_check(self):
        """섹션 헤더(##)는 검사에서 제외된다."""
        header_repeat = "\n".join([f"## 정의 PUSCH 설명"] * 10)
        text = header_repeat + "\n실제 본문 내용이 여기 있습니다 다양하고 독창적인 내용입니다 반복이 없어야 한다"
        assert _detect_hallucination(text) is False

    def test_wikilink_lines_excluded(self):
        """- [[ 로 시작하는 관련 개념 목록 라인은 제외."""
        link_repeat = "\n".join([f"- [[PUSCH (affects)]]"] * 10)
        text = link_repeat + "\n본문에서는 반복 없이 다양한 내용을 기술하여 hallucination이 없어야 함"
        assert _detect_hallucination(text) is False

    def test_three_word_ngram_detected(self):
        """3어절 n-gram도 감지 대상."""
        phrase = "데이터 전송 채널"  # 3 words
        text = " ".join([phrase] * 5 + ["다양한 다른 내용 여기에 더 많은 단어가 있어야 15개 이상"])
        assert _detect_hallucination(text) is True


# ──────────────────────────────────────────────
# run_generate 통합 테스트
# ──────────────────────────────────────────────

class TestRunGenerate:
    def _make_plan(self, pages):
        return {"pages": pages}

    def _base_page(self, path="entities/PUSCH.md"):
        return {
            "path": path,
            "description": "PUSCH 채널 설명",
            "generated": False,
            "linked": False,
            "sources": [{"file": "sources/38211.docx", "sections": ["6.3.1"]}],
        }

    def test_successful_generation_sets_generated_true(self, tmp_path):
        """LLM이 정상 응답하면 page["generated"] = True."""
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        plan_path = tmp_path / "plan.json"

        page = self._base_page()
        plan = self._make_plan([page])

        def mock_llm(system, user, **kwargs):
            return """## 정의
PUSCH는 Physical Uplink Shared Channel이다.

## 요약
요약 내용이 여기 있습니다.

## 상세 설명
상세한 설명이 여기 있습니다.

## 인과 관계
인과 관계 내용

## 관련 개념
- [[UCI (uses)]]

## 스펙 근거
3GPP TS 38.211

## 소스
sources/38211.docx
"""

        def mock_extract(page):
            return "섹션 6.3.1 내용"

        def mock_check(content, spec, call_llm_fn, **kwargs):
            return {"score": 8, "pass": True, "issues": []}

        # parse_38822 import 오류 방지
        with patch('wiki_builder.generate._generate_page') as mock_gen:
            mock_gen.return_value = {"path": page["path"], "failed": False}

            run_generate(
                plan=plan,
                wiki_dir=str(wiki_dir),
                plan_path=str(plan_path),
                call_llm=mock_llm,
                extract_spec_fn=mock_extract,
                check_quality_fn=mock_check,
                backend="claude",
                max_workers=1,
            )

        assert page["generated"] is True

    def test_failed_generation_page_not_marked_generated(self, tmp_path):
        """LLM 실패(hallucination 등) 시 page["generated"]는 False 유지."""
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        plan_path = tmp_path / "plan.json"

        page = self._base_page()
        plan = self._make_plan([page])

        def mock_llm(system, user, **kwargs):
            return "[LLM 호출 실패] 연결 오류"

        def mock_extract(page):
            return "스펙 내용"

        def mock_check(content, spec, call_llm_fn, **kwargs):
            return {"score": 3, "pass": False, "issues": ["누락 섹션"]}

        with patch('wiki_builder.generate._generate_page') as mock_gen:
            mock_gen.return_value = {"path": page["path"], "failed": True, "reason": "llm_fail"}

            failed = run_generate(
                plan=plan,
                wiki_dir=str(wiki_dir),
                plan_path=str(plan_path),
                call_llm=mock_llm,
                extract_spec_fn=mock_extract,
                check_quality_fn=mock_check,
                backend="claude",
                max_workers=1,
            )

        assert page["generated"] is False
        assert len(failed) > 0

    def test_already_generated_page_skipped(self, tmp_path):
        """generated=True인 페이지는 스킵."""
        wiki_dir = tmp_path / "wiki"
        wiki_dir.mkdir()
        plan_path = tmp_path / "plan.json"

        page = self._base_page()
        page["generated"] = True
        plan = self._make_plan([page])

        call_count = [0]

        def mock_llm(system, user, **kwargs):
            call_count[0] += 1
            return "content"

        def mock_extract(p):
            return "spec"

        def mock_check(content, spec, fn, **kwargs):
            return {"score": 8, "pass": True, "issues": []}

        with patch('wiki_builder.generate._generate_page') as mock_gen:
            run_generate(
                plan=plan,
                wiki_dir=str(wiki_dir),
                plan_path=str(plan_path),
                call_llm=mock_llm,
                extract_spec_fn=mock_extract,
                check_quality_fn=mock_check,
                max_workers=1,
            )
            mock_gen.assert_not_called()
