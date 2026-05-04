"""
test_evaluate.py — evaluate.py 단위 테스트

테스트 대상:
- _quick_check(): 필수 섹션 누락 시 점수 차감
- _quick_check(): bold 감지 (**text**) 시 이슈 추가
- _quick_check(): 관계타입 없는 링크 감지
- EvalHistory: new_session → add_round → close_session 흐름
- _compute_delta(): net_fixed, avg_score_delta 계산
"""
import json
import sys
from pathlib import Path
from datetime import datetime

import pytest

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from wiki_builder.evaluate import (
    _quick_check,
    _compute_delta,
    EvalHistory,
    PASS_SCORE,
)


# ──────────────────────────────────────────────
# _quick_check 테스트
# ──────────────────────────────────────────────

FULL_CONTENT = """## 정의
PUSCH는 Physical Uplink Shared Channel이다.

## 요약
요약 내용

## 상세 설명
상세한 설명

## 인과 관계
인과 관계 설명

## 관련 개념
- [[UCI (uses)]]
- [[PUCCH (related)]]

## 스펙 근거
3GPP TS 38.211 Section 6.3.1

## 소스
sources/38211.docx
"""


class TestQuickCheck:
    def test_full_valid_content_passes(self):
        """모든 섹션 있고 bold 없고 관계타입 있으면 높은 점수."""
        result = _quick_check(FULL_CONTENT)
        assert result["pass"] is True
        assert result["score"] >= PASS_SCORE

    def test_missing_sections_lowers_score(self):
        """필수 섹션 3개 이상 누락 시 structure_score=0."""
        content = "## 정의\n내용만 있음"
        result = _quick_check(content)
        # 섹션 많이 누락 → structure_score = 0 → 전체 점수 낮아짐
        assert result["score"] < PASS_SCORE

    def test_missing_sections_adds_issue(self):
        """누락 섹션이 있으면 issues에 기록."""
        content = "## 정의\n내용"
        result = _quick_check(content)
        missing_issues = [i for i in result["issues"] if "누락 섹션" in i]
        assert len(missing_issues) >= 1

    def test_bold_text_detected(self):
        """**bold** 사용 시 이슈 추가."""
        content = FULL_CONTENT + "\n**중요한 내용**\n"
        result = _quick_check(content)
        bold_issues = [i for i in result["issues"] if "bold" in i or "**" in i]
        assert len(bold_issues) >= 1

    def test_bold_text_reduces_score(self):
        """**bold** 있으면 no_translation 점수 0."""
        content_with_bold = FULL_CONTENT + "\n**bold 텍스트**\n"
        result_bold = _quick_check(content_with_bold)
        result_clean = _quick_check(FULL_CONTENT)
        assert result_clean["score"] > result_bold["score"]

    def test_no_relation_type_in_links_detected(self):
        """관계타입 없는 [[링크]] 감지."""
        content = FULL_CONTENT.replace(
            "- [[UCI (uses)]]\n- [[PUCCH (related)]]",
            "- [[UCI]]\n- [[PUCCH]]"
        )
        result = _quick_check(content)
        relation_issues = [i for i in result["issues"] if "관계 타입" in i]
        assert len(relation_issues) >= 1

    def test_relation_type_links_no_issue(self):
        """관계타입 있는 링크들 → relation_types 이슈 없음."""
        result = _quick_check(FULL_CONTENT)
        relation_issues = [i for i in result["issues"] if "관계 타입" in i]
        assert len(relation_issues) == 0

    def test_score_max_8(self):
        """점수는 최대 8점."""
        result = _quick_check(FULL_CONTENT)
        assert result["score"] <= 8

    def test_result_has_required_keys(self):
        result = _quick_check(FULL_CONTENT)
        for key in ("score", "pass", "issues", "details", "method"):
            assert key in result

    def test_method_is_quick_check(self):
        result = _quick_check(FULL_CONTENT)
        assert result["method"] == "quick_check"

    def test_empty_related_section_no_false_relation_issue(self):
        """관련 개념 섹션에 링크가 없으면 관계타입 이슈 미발생."""
        content = """## 정의
정의

## 요약
요약

## 상세 설명
상세

## 인과 관계
인과

## 관련 개념
(없음)

## 스펙 근거
3GPP

## 소스
sources
"""
        result = _quick_check(content)
        relation_issues = [i for i in result["issues"] if "관계 타입" in i]
        assert len(relation_issues) == 0


# ──────────────────────────────────────────────
# _compute_delta 테스트
# ──────────────────────────────────────────────

class TestComputeDelta:
    def test_net_fixed_counts_newly_passed(self):
        before = {
            "pages": [
                {"path": "entities/A.md", "score": 4},
                {"path": "entities/B.md", "score": 3},
            ]
        }
        after = {
            "results": [
                {"path": "entities/A.md", "passed": True, "delta": 4},
                {"path": "entities/B.md", "passed": False, "delta": 1},
            ]
        }
        delta = _compute_delta(before, after)
        assert delta["net_fixed"] == 1
        assert "entities/A.md" in delta["newly_passed"]

    def test_still_failed_recorded(self):
        before = {
            "pages": [
                {"path": "entities/A.md", "score": 3},
                {"path": "entities/B.md", "score": 4},
            ]
        }
        after = {
            "results": [
                {"path": "entities/A.md", "passed": False, "delta": 1},
                {"path": "entities/B.md", "passed": False, "delta": 0},
            ]
        }
        delta = _compute_delta(before, after)
        assert "entities/A.md" in delta["still_failed"]
        assert "entities/B.md" in delta["still_failed"]

    def test_avg_score_delta_computed(self):
        before = {
            "pages": [
                {"path": "entities/A.md", "score": 4},
                {"path": "entities/B.md", "score": 3},
            ]
        }
        after = {
            "results": [
                {"path": "entities/A.md", "passed": True, "delta": 4},
                {"path": "entities/B.md", "passed": False, "delta": 2},
            ]
        }
        delta = _compute_delta(before, after)
        # avg = (4 + 2) / 2 = 3.0
        assert delta["avg_score_delta"] == 3.0

    def test_all_passed_net_fixed_equals_before_count(self):
        before = {
            "pages": [
                {"path": "entities/A.md", "score": 4},
                {"path": "entities/B.md", "score": 5},
            ]
        }
        after = {
            "results": [
                {"path": "entities/A.md", "passed": True, "delta": 3},
                {"path": "entities/B.md", "passed": True, "delta": 2},
            ]
        }
        delta = _compute_delta(before, after)
        assert delta["net_fixed"] == 2
        assert delta["still_failed"] == []

    def test_no_delta_entries_avg_zero(self):
        """delta 없는 결과 → avg_score_delta = 0."""
        before = {"pages": [{"path": "entities/A.md", "score": 4}]}
        after = {
            "results": [
                {"path": "entities/A.md", "passed": True},  # delta 없음
            ]
        }
        delta = _compute_delta(before, after)
        assert delta["avg_score_delta"] == 0


# ──────────────────────────────────────────────
# EvalHistory 테스트
# ──────────────────────────────────────────────

class TestEvalHistory:
    def test_new_session_returns_id(self, tmp_path):
        path = tmp_path / "eval_history.json"
        history = EvalHistory(path)
        session_id = history.new_session()
        assert isinstance(session_id, str)
        assert len(session_id) > 0

    def test_add_round_recorded(self, tmp_path):
        path = tmp_path / "eval_history.json"
        history = EvalHistory(path)
        session_id = history.new_session()

        before = {"pages": [{"path": "entities/A.md", "score": 4}]}
        after = {"results": [{"path": "entities/A.md", "passed": True, "delta": 3}]}
        change = {"root_cause": "테스트", "user_confirmed": True}

        history.add_round(session_id, before, change, after)
        history.save()

        data = json.loads(path.read_text(encoding="utf-8"))
        sessions = data["sessions"]
        assert len(sessions) == 1
        assert len(sessions[0]["rounds"]) == 1

    def test_close_session_adds_summary(self, tmp_path):
        path = tmp_path / "eval_history.json"
        history = EvalHistory(path)
        session_id = history.new_session()

        before = {"pages": [{"path": "entities/A.md", "score": 4}]}
        after = {
            "results": [{"path": "entities/A.md", "passed": True, "delta": 3}],
            "improved_count": 1,
            "still_failed_count": 0,
        }
        history.add_round(session_id, before, {"user_confirmed": True}, after)
        history.close_session(session_id)
        history.save()

        data = json.loads(path.read_text(encoding="utf-8"))
        summary = data["sessions"][0]["summary"]
        assert summary is not None
        assert "total_rounds" in summary

    def test_empty_session_summary_has_note(self, tmp_path):
        path = tmp_path / "eval_history.json"
        history = EvalHistory(path)
        session_id = history.new_session()
        history.close_session(session_id, note="테스트 메모")

        summary = history.get_session_summary(session_id)
        assert summary is not None
        assert "note" in summary

    def test_multiple_rounds_accumulated(self, tmp_path):
        path = tmp_path / "eval_history.json"
        history = EvalHistory(path)
        session_id = history.new_session()

        for i in range(3):
            before = {"pages": [{"path": f"entities/P{i}.md", "score": 3}]}
            after = {
                "results": [{"path": f"entities/P{i}.md", "passed": True, "delta": 4}],
                "improved_count": 1,
                "still_failed_count": 0,
            }
            history.add_round(session_id, before, {}, after)

        history.close_session(session_id)
        summary = history.get_session_summary(session_id)
        assert summary["total_rounds"] == 3

    def test_load_existing_history(self, tmp_path):
        """기존 eval_history.json이 있으면 로드한다."""
        path = tmp_path / "eval_history.json"
        existing = {"sessions": [{"id": "2026-01-01T00:00:00", "rounds": [], "summary": None}]}
        path.write_text(json.dumps(existing), encoding="utf-8")

        history = EvalHistory(path)
        session_id = history.new_session()

        # 기존 세션 + 새 세션 = 2개
        history.save()
        data = json.loads(path.read_text(encoding="utf-8"))
        assert len(data["sessions"]) == 2
