# LLMWiki Architecture — 동작 설계 문서

> 이 문서는 구현된 시스템의 동작 방식을 설명합니다.
> Karpathy 패턴 원문: `KARPATHY_LLMWIKI.md` / 전체 요구사항: `PRD.md`

---

## 1. 시스템 전체 구조

```
┌──────────────────────────────────────────────────────────────┐
│                        사용자 / sdmAnalyzer                   │
└────────────────┬──────────────────────────┬──────────────────┘
                 │ 터미널 CLI                │ GUI (subprocess)
                 ▼                           ▼
        orchestrate.py               wiki_client.py
                 │                           │
                 │          JSON stdio       │
                 └──────────────────────────►│
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│              Orchestrator LLM (에이전트)                      │
│                                                               │
│   tool 호출로 각 서브에이전트 실행:                            │
│                                                               │
│   run_plan() ──► plan.py        Phase 1: Planner             │
│   run_generate() ► generate.py  Phase 2: Generator           │
│   run_link() ──► link.py        Phase 3: Linker              │
│   run_evaluate() ► evaluate.py  Phase 4: Evaluator           │
│   run_lint() ──► lint.py        Phase 6: Lint                │
│   run_chat() ──► chat.py        Chat REPL                    │
│   run_server() ► server.py      Server                       │
│                                                               │
│   query.py  ← 예외: tool 방식 아님, 2-step stateless 독립 동작 │
│                                                               │
│   공통: api.py (call_simple), prompts.py                     │
└──────────────────────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────┐
│         wiki/                │  ← 영구 상태 (Obsidian으로 열람)
│  index.md  log.md            │
│  entities/  concepts/        │
│  internal/  query/           │
└──────────────────────────────┘
```

**핵심 원칙:**
- Orchestrator LLM이 tool 호출로 Phase 실행 순서·여부를 결정
- 각 서브에이전트(Phase)는 독립 LLM 호출 — history 누적 없음
- Query만 예외: Orchestrator 개입 없이 2-step stateless로 직접 동작
- wiki가 영구 상태

---

## 2. 빌드 파이프라인 (Phase 1~4)

### Phase 1 — Plan

**목적**: 소스 문서에서 생성할 wiki 페이지 목록 추출

```
sources/3gpp/38211-i90.docx
        │
        ▼ chunk_text.py (섹션 경계 우선, 40~50K자 청크)
   [청크 1] [청크 2] [청크 3] ...
        │
        ▼ LLM (PLANNER_SYSTEM + PLANNER_USER)
   각 청크 → 생성할 페이지 목록 (JSON)
        │
        ▼ 중복 제거, 통합
   plan.json  ← 체크포인트. 절대 삭제 금지.
```

**plan.json 예시**:
```json
{
  "phase": "generate",
  "planned_sources": ["sources\\3gpp\\38211-i90.docx", "sources\\3gpp\\38212-i80.docx"],
  "pages": [
    {
      "path": "entities/PUSCH.md",
      "description": "Physical Uplink Shared Channel",
      "generated": false,
      "linked": false,
      "sources": [
        {"file": "sources\\3gpp\\38211-i90.docx", "sections": ["6.3"]},
        {"file": "sources\\3gpp\\38212-i80.docx", "sections": ["6.2.1"]}
      ]
    }
  ]
}
```

`planned_sources`: 이미 플래닝된 소스 목록. 새 소스 추가 시 해당 소스만 증분 처리.
멀티소스: 같은 entity가 여러 스펙에 등장하면 sources 배열에 머지됨.

**재실행 동작**: plan.json의 `planned_sources`와 현재 소스 파일 비교 → 새 소스만 증분 플래닝, 기존 pages/generated/linked 보존.

---

### Phase 2 — Generate

**목적**: plan.json의 각 페이지를 스펙 섹션 내용으로 생성

```
plan.json
   │
   ▼ generated=False인 페이지만 선택
   
각 페이지마다 (ThreadPoolExecutor, max_workers=1 기본; --workers N으로 변경):
   ├── extract_spec_content(page)
   │     └── 소스 파일에서 지정 섹션만 추출 (전체 파일 전달 금지)
   │
   ├── LLM 호출 (GENERATOR_SYSTEM + GENERATOR_USER)
   │     입력: 섹션 내용 + wiki 페이지 경로 목록(내용 없이)
   │     출력: 마크다운 wiki 페이지
   │
   ├── hallucination 감지
   │     3어절 이상 동일 구절 5회 이상 → 재시도 (최대 3회)
   │
   ├── check_quality() — 8점 만점 평가
   │     합격(7점↑) → 파일 저장, generated=True, plan.json 갱신
   │     불합격     → failed 리스트에 추가 (파일 저장 안함)
   │
   └── 반환: failed_pages 리스트
```

**불합격 페이지는 evaluate로 직접 전달** (orchestrate가 연결).

---

### Phase 3 — Link

**목적**: wiki 페이지 간 역방향 링크 보완

```
wiki/ 전체 스캔
   │
   ▼ Python이 링크 맵 계산
   {
     "entities/PUSCH.md": ["concepts/PUSCH_Scrambling.md", ...],
     ...
   }
   
각 페이지마다:
   ├── inbound 링크 목록 계산
   │     "이 페이지를 링크하는 페이지들"
   │
   └── LLM 호출 (LINKER_SYSTEM + LINKER_USER)
         입력: 파일 내용 + inbound 링크 목록
         출력: 역방향 링크가 추가된 수정본
```

**규칙**: A→B 링크가 있으면 B의 `## 관련 개념`에 `[[A]] (관계타입)` 추가.

---

### Phase 4 — Evaluate (자동 품질 개선)

**목적**: 불합격 페이지 패턴 분석 → 프롬프트 개선 → 재생성 반복

```
불합격 페이지 수집:
  ├── generate에서 직접 넘어온 initial_failed (파일 없음)
  └── generated=True지만 재평가 불합격 (파일 있음)
        │
        ▼
[라운드 반복, 최대 5회]
  │
  ├── EvalHistory.add_round(before_snapshot)    ← 변경 전 기록
  │     {page별 score, issues, prompt hash}
  │
  ├── LLM 분석 (EVALUATOR_SYSTEM)
  │     입력: 불합격 페이지 목록 + 현재 프롬프트
  │     출력: {root_cause, prompt_fix, confidence}
  │
  ├── 터미널에 분석 결과 출력 → 사람 컨펌 [y/N]
  │
  ├── y → 불합격 페이지 generated=False 리셋 → run_generate() 재실행
  │
  ├── EvalHistory.add_round(after_snapshot)    ← 변경 후 기록
  │     {page별 score_before→after, delta, 신규 합격 목록}
  │
  └── 모두 합격 or 사용자 거부 → 종료
```

**eval_history.json 구조** (인과관계 추적):
```json
{
  "sessions": [{
    "id": "2026-05-02T10:00:00",
    "rounds": [{
      "round": 1,
      "before": {
        "pages": [{"path": "BWP.md", "score": 5, "issues": ["관계 타입 누락"]}],
        "prompt_hashes": {"GENERATOR_SYSTEM": "a1b2c3d4"}
      },
      "change": {
        "root_cause": "관련 개념 섹션에 관계 타입 누락 패턴",
        "prompt_fix": {"target": "GENERATOR_SYSTEM", "change": "예시 추가"},
        "user_confirmed": true
      },
      "after": {
        "results": [{"path": "BWP.md", "score_before": 5, "score_after": 7, "delta": 2}]
      },
      "delta": {"net_fixed": 1, "avg_score_delta": 2.0}
    }],
    "summary": {
      "started_failing": 3, "ended_failing": 0,
      "best_round": 1, "net_fixed": 3
    }
  }]
}
```

---

## 3. 운영 기능 (Phase 5~6 + Chat + Server)

### Phase 5 — Query

**목적**: 자연어 질문 → wiki 기반 답변 합성

```
질문: "PUSCH scrambling 절차는?"
   │
   ▼ Step 1: 페이지 선택 (LLM 1회)
   입력: index.md + 질문
   출력: ["entities/PUSCH.md", "concepts/PUSCH_Scrambling.md"]
   │
   ▼ Step 2: 답변 합성 (LLM 1회)
   입력: 선택된 페이지 내용(최대 5개) + 질문
   출력: 마크다운 답변 + 출처 명시
   │
   ▼ (선택) wiki/query/2026-05-02_PUSCH_scrambling.md 저장
   ▼ wiki/log.md에 기록: "## [2026-05-02] query | PUSCH scrambling 절차는?"
```

**특징**: 총 LLM 2회 호출, stateless. wiki에 없는 내용은 생성 안함.

---

### Phase 6 — Lint

**목적**: wiki 건강 검진 (주기적으로 실행)

```
Python 직접 계산 (빠름, LLM 없음):
  ├── 고아 페이지: inbound 링크 0개인 페이지
  ├── 깨진 링크: [[X]] 있는데 X.md 없음
  └── 역방향 링크 누락: A→B인데 B→A 없음

LLM 분석 (5페이지 배치 단위):
  ├── 내용 모순: 두 페이지 간 서로 다른 주장
  ├── 오래된 주장: 다른 페이지가 supersede한 내용
  └── 데이터 공백: 중요하지만 누락된 정보

결과: wiki/lint_2026-05-02.md 리포트 저장
```

---

### Chat REPL (터미널)

**목적**: 터미널에서 Orchestrator를 통한 자연어 대화형 인터페이스

```
$ python wiki_builder/orchestrate.py --phase chat --backend gemini
(또는 C:/llmwiki_runner에서: run.bat)

> PUSCH scrambling 절차는?
      → Orchestrator → run_query() 호출 → 답변 출력

> generate 시작해
      → Orchestrator → run_generate() 호출

> lint 돌려줘
      → Orchestrator → run_lint() 호출

> exit     → 종료
```

**내부 동작**: 사용자 입력 → Orchestrator LLM → 적절한 tool 선택·실행.
매 입력마다 독립 Orchestrator 실행 (대화 history 누적 없음).
wiki가 영구 상태 — 질문할수록 wiki가 풍부해짐.

---

### Server 모드 (sdmAnalyzer 연동)

**목적**: GUI 프로그램(sdmAnalyzer)에서 wiki 기능 사용

```
sdmAnalyzer (GUI)
   │
   ├── WikiClient.start()
   │     subprocess.Popen(orchestrate.py --phase server)
   │     stdin/stdout pipe 연결
   │     reader 스레드 시작
   │
   ├── WikiClient.query("PUSCH scrambling?")  ← 동기
   │     stdin: {"id": "r1", "action": "query", "question": "..."}
   │     stdout: {"id": "r1", "status": "ok", "answer": "...", "sources": [...]}
   │
   ├── WikiClient.query_async("...", callback)  ← 비동기 (GUI 메인 스레드 블로킹 없음)
   │
   ├── WikiClient.lint()
   ├── WikiClient.status()
   ├── WikiClient.ping()
   │
   └── WikiClient.stop()
         stdin EOF → 서버 정상 종료
```

**stdout은 JSON 전용**. 서버 내부 로그는 stderr/파일로만 출력.

---

## 4. LLM API 추상화

**목적**: 백엔드 전환 시 파이프라인 코드 무변경

```python
# 어디서나 동일한 인터페이스
call_simple(system: str, user: str, temperature=0.3) -> str

# 백엔드 전환 방법
os.environ["WIKI_BACKEND"] = "claude"   # 또는 "gptoss", "gemini"

# 실패 시 예외 raise 금지 → "[LLM 호출 실패] ..." 반환
```

| 백엔드 | 사용 환경 | 인증 |
|--------|-----------|------|
| claude | 집 | ANTHROPIC_API_KEY |
| gptoss | 회사 (Samsung 내망) | --api-key, --knox-id, --ad-id |
| gemini | 무료 개발/테스트 | GEMINI_API_KEY |

**에러 처리**: 재시도 3회 (5→10→20초 backoff), 429는 65초 대기 (재시도 횟수 카운트 제외).

---

## 5. 데이터 흐름 요약

```
sources/                     (불변 원본)
   │
   ▼ Phase 1 (Plan)
plan.json                    (체크포인트, 삭제 금지)
   │
   ▼ Phase 2 (Generate)
wiki/entities/*.md
wiki/concepts/*.md           (LLM 생성)
wiki/internal/*.md
   │
   ▼ Phase 3 (Link)
wiki/**/*.md                 (역방향 링크 보완)
   │
   ▼ Phase 4 (Evaluate)
eval.log                     (라운드별 append)
eval_history.json            (세션/라운드별 before→after 스코어 추적)

   ▼ Phase 5 (Query)
wiki/query/*.md              (선택적 저장)
wiki/log.md                  (활동 이력)

   ▼ Phase 6 (Lint)
wiki/lint_YYYY-MM-DD.md      (건강 검진 리포트)
wiki/log.md
```

---

## 6. wiki 페이지 포맷

모든 wiki 페이지는 아래 구조를 엄수 (AGENTS.md Part 1 기준):

```markdown
# [페이지명]

## 정의
[한 줄 정의]

## 요약
[3~5줄 요약]

## 상세 설명
[스펙 원문 기반 상세. 수식/파라미터/절차 포함]

## 인과 관계
[이 개념이 원인/결과인 관계들]

## 관련 개념
- [[DMRS]] (part_of)       ← 관계 타입 필수
- [[Slot]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.1

## 소스
- sources/3gpp/38211-i90.docx §6.3.1
```

**절대 금지**: `**bold**` (→ `[[wikilink]]`), 영어 기술 용어 한국어 번역, 비표준 섹션명.

---

## 7. CLI 치트시트

```bash
# 전체 빌드
python wiki_builder/orchestrate.py --phase all --backend claude

# 단계별
python wiki_builder/orchestrate.py --phase plan     --backend claude
python wiki_builder/orchestrate.py --phase generate --backend claude
python wiki_builder/orchestrate.py --phase link     --backend claude
python wiki_builder/orchestrate.py --phase evaluate --backend claude

# 운영
python wiki_builder/orchestrate.py --phase query --question "PUSCH scrambling 절차는?"
python wiki_builder/orchestrate.py --phase lint
python wiki_builder/orchestrate.py --phase chat

# sdmAnalyzer 서버 (직접 실행은 테스트용)
python wiki_builder/orchestrate.py --phase server --backend gptoss --api-key XXX

# 회사망 (gpt-oss)
python wiki_builder/orchestrate.py --phase all \
  --backend gptoss --api-key XXX --knox-id XXX --ad-id XXX

# 재실행 (완료 페이지 자동 스킵)
python wiki_builder/orchestrate.py --phase generate  # plan.json 있으면 generated=True 스킵
```

---

## 8. 파일 목록

| 파일 | 역할 | 수정 가능 |
|------|------|-----------|
| `orchestrate.py` | CLI 진입점, Orchestrator LLM 에이전트 | ✓ |
| `api.py` | LLM 추상화 (Claude/gptoss/Gemini) | ✓ |
| `prompts.py` | 모든 LLM 프롬프트 | Evaluator만 (전체 재작성) |
| `plan.py` | Phase 1: Planner | ✓ |
| `generate.py` | Phase 2: Generator + hallucination 감지 | ✓ |
| `link.py` | Phase 3: Linker | ✓ |
| `evaluate.py` | Phase 4: Evaluator + Quality Checker | ✓ |
| `query.py` | Phase 5: Query | ✓ |
| `lint.py` | Phase 6: Lint | ✓ |
| `chat.py` | 터미널 REPL | ✓ |
| `server.py` | JSON stdio 서버 | ✓ |
| `wiki_client.py` | sdmAnalyzer용 클라이언트 | ✓ |
| `chunk_text.py` | 소스 파일 청킹 유틸 | ✓ |
| `AGENTS.md` | wiki 작성 규칙 | Part 2만 (전체 재작성) |
| `KARPATHY_LLMWIKI.md` | 패턴 원문 | 수정 금지 |

---

## 9. 미구현 / 알려진 이슈

| 항목 | 상태 | 비고 |
|------|------|------|
| orchestrate.py LLM Orchestrator + tool 구조 | **완료** | Orchestrator LLM이 tool 호출로 Phase 실행 |
| Phase 1 Plan (증분 플래닝 + 멀티소스) | 완료 | planned_sources 기반 증분, sources 머지 |
| Phase 2 Generate | 완료 | hallucination 감지, quality check |
| Phase 3 Link | 완료 | |
| Phase 4 Evaluate | 완료 | 사람 컨펌 필요 |
| Phase 5 Query | 완료 | Orchestrator tool + --phase query 직접 경로 모두 지원 |
| Phase 6 Lint | 완료 | |
| Lint → Generate 피드백 루프 | **예정** | lint 결과 → plan 보완 → 재생성 |
| Chat REPL (Orchestrator 기반) | 완료 | 자연어 입력 → Orchestrator 판단 |
| Server / WikiClient | 완료 | sdmAnalyzer 연동 미테스트 |
| index.md 자동 갱신 | 미구현 | Generate 완료 후 수동 필요 |
| log.md 초기화 | 미구현 | 없으면 query/lint가 append 생성 |
| llmwiki_runner 독립 실행 패키지 | 완료 | run.bat으로 venv 자동 설치 + chat 실행 |
