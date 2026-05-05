# LLMWiki PRD (Product Requirements Document)

## 프로젝트 개요

5G NR PHY 레이어 스펙 문서(3GPP)로부터 LLM이 모뎀 로그를 분석할 때
사용할 수 있는 고품질 지식베이스(wiki)를 자동으로 구축·유지·조회하는 도구.

Karpathy의 LLM Wiki 패턴을 직접 구현한 에이전트. 원문: `KARPATHY_LLMWIKI.md`

## 배경

- 대상 사용자: 5G NR PHY 펌웨어 엔지니어
- 목적: LLM이 로그 분석 시 도메인 지식(인과관계, 판단기준, 스펙근거)을 wiki에서 조회
- 소스: 3GPP TS 38.211, 38.212, 38.213 등 NR PHY 스펙 .docx 파일
- 핵심 차이: RAG(매번 재발견)가 아니라 **누적되는 wiki**(한 번 컴파일, 계속 최신화)

## 실행 환경

- **독립 실행**: logParser 없이 llmwiki/ 폴더 단독으로 동작
- **집**: Claude Sonnet API (anthropic)
- **회사**: gpt-oss API (Samsung 내부망)
- **인터페이스**: 터미널 CLI (대화형 chat 모드 포함)
- **SdmAnalyzer 연동**: subprocess 호출로 인터페이스만 연결 (선택사항)

## 디렉토리 구조

```
llmwiki/
├── AGENTS.md               # Orchestrator LLM 시스템 프롬프트
├── CLAUDE.md               # Claude Code 작업 지침
├── KARPATHY_LLMWIKI.md     # Karpathy 원문 보존 (수정 불가)
├── sample.md               # 목표 품질 샘플 문서 (사람이 제공)
├── plan.json               # Phase 1 결과 (재실행 체크포인트)
├── abbreviations.json      # 약어 사전 (자동 추출)
├── eval.log                # 평가 이력
├── build.log               # 빌드 로그
├── sources/                # 원본 소스 (불변)
│   └── 3gpp/
│       ├── 38211-i90.docx
│       └── 38212-i80.docx
├── wiki/                   # 생성된 wiki
│   ├── index.md            # 전체 페이지 카탈로그 (LLM이 갱신)
│   ├── log.md              # 작업 이력 (append-only)
│   ├── entities/
│   ├── concepts/
│   ├── internal/
│   └── query/              # 질의 응답 결과 보관 (선택적 filing)
├── sub_agents/             # phase별 LLM 프롬프트 (.md 파일)
├── chunk_text.py           # 파일 청킹 유틸
├── requirements.txt
└── wiki_builder/
    ├── orchestrate.py      # 파이프라인 조율
    ├── plan.py             # Phase 1: Planner
    ├── generate.py         # Phase 2: Generator
    ├── link.py             # Phase 3: Linker
    ├── evaluate.py         # Phase 4: Evaluator
    ├── query.py            # Phase 5: Query
    ├── lint.py             # Phase 6: Lint
    ├── chat.py             # 대화형 REPL 인터페이스 (터미널)
    ├── server.py           # JSON stdio 서버 (sdmAnalyzer 연동용)
    ├── wiki_client.py      # sdmAnalyzer에서 import하는 클라이언트 래퍼
    ├── prompt_loader.py    # 프롬프트 로더 (sub_agents/*.md 읽기)
    └── api.py              # LLM API 추상화 (Claude / gpt-oss 전환)
```

## 핵심 기능

### Phase 1: Plan
- 모든 소스 파일을 청크 단위로 읽음
- 각 청크에서 생성할 wiki 페이지 목록 추출 (LLM 호출)
- 각 페이지가 참조하는 섹션 번호 기록 (예: 38211 §6.3.1)
- 결과를 plan.json에 저장
- **재실행 시 plan.json이 있으면 스킵**

### Phase 2: Generate
- plan.json 기반으로 페이지별 wiki 문서 생성
- 페이지당 LLM 1회 독립 호출 (컨텍스트 오염 없음)
- 입력: plan에 명시된 섹션 내용 + wiki 페이지 path:description 목록
- 병렬 처리 (ThreadPoolExecutor)
- 생성 즉시 Quality Checker로 품질 평가
- 불합격 시 Evaluator 호출
- plan.json의 generated 플래그로 재실행 시 완료 페이지 스킵

### Phase 3: Link
- Python이 전체 wiki 읽고 링크 맵 구성
- 역방향 링크 누락 감지 및 추가 (LLM 호출)
- LLM에게는 자기 파일 내용 + inbound 링크 목록만 전달

### Phase 4: Evaluate (자동 품질 개선)
- 불합격 문서 원인 분석
- 로그 추가 후 재실행으로 더 자세한 정보 수집
- 프롬프트/방법론 개선안 도출
- 개선안으로 검증 재실행
- 보고서 생성 → 사람 컨펌 대기
- 승인 후 빌드 재개
- 최대 5회 반복 후 개선 없으면 사람에게 알림

### Phase 5: Query (신규)
- 자연어 질문을 받아 wiki에서 답변 합성
- **2-step stateless 호출**:
  1. `index.md` 읽고 → 관련 페이지 경로 선택 (LLM)
  2. 선택된 페이지 읽고 → 답변 합성 + 출처 명시 (LLM)
- 답변을 `wiki/query/YYYY-MM-DD_topic.md`로 선택적 보관
- `wiki/log.md`에 `## [날짜] query | 질문` 형식으로 기록

### Phase 6: Lint (신규)
- wiki 전체 건강 검진
- 감지 항목:
  - 고아 페이지 (inbound 링크 없음)
  - 역방향 링크 누락
  - 페이지 간 내용 모순
  - 언급은 있으나 페이지 없는 개념
  - 오래된 주장 (newer source가 supersede)
  - 데이터 공백 (조사 필요한 항목)
- `wiki/lint_YYYY-MM-DD.md`에 리포트 저장
- `wiki/log.md`에 기록

### Chat REPL (신규)
- 터미널 대화형 인터페이스
- 사용자 입력 → 자동으로 query / lint / ingest 라우팅
- 각 응답 후 wiki 파일로 filing 여부 묻기 (선택)
- 내부적으로는 stateless LLM 호출 — chat history 누적 없음
- wiki 자체가 영구 상태

### Server 모드 (신규) — sdmAnalyzer 연동용
- `--phase server` 로 실행 시 JSON stdio 서버로 동작
- stdin에서 JSON 한 줄씩 읽고 → stdout에 JSON 한 줄씩 응답
- sdmAnalyzer(GUI)가 subprocess로 spawn하여 pipe로 통신
- GUI 스레드를 블로킹하지 않음 (비동기 read 가능)
- sdmAnalyzer 측 `WikiClient` 래퍼 클래스 제공

## 품질 기준 (8점 만점, 7점 이상 합격)

| 항목 | 점수 |
|------|------|
| 필수 섹션 구조 준수 | 2점 |
| 기술 용어 번역 없음 | 1점 |
| 관련 개념에 관계 타입 있음 | 1점 |
| 소스 근거 명시 | 1점 |
| hallucination 없음 | 2점 |
| 상세 설명이 소스 원문 기반 | 1점 |

## API 지원

### Claude (집)
- Model: claude-sonnet-4-5 이상
- 환경변수: `ANTHROPIC_API_KEY`

### gpt-oss (회사)
- URL: `http://apigw-stg.samsungds.net:8000/gpt-oss/1/gpt-oss-120b/v1/chat/completions`
- 환경변수 또는 CLI: `--api-key`, `--knox-id`, `--ad-id`

## CLI 인터페이스

```bash
# 빌드 파이프라인
python wiki_builder/orchestrate.py --phase all
python wiki_builder/orchestrate.py --phase plan
python wiki_builder/orchestrate.py --phase generate
python wiki_builder/orchestrate.py --phase link

# 질의
python wiki_builder/orchestrate.py --phase query --question "PUSCH scrambling 절차는?"

# Lint
python wiki_builder/orchestrate.py --phase lint

# 대화형 chat (터미널)
python wiki_builder/orchestrate.py --phase chat

# sdmAnalyzer 연동 서버 모드 (JSON stdio)
python wiki_builder/orchestrate.py --phase server --backend gptoss --api-key X

# 백엔드 선택
python wiki_builder/orchestrate.py --backend claude --phase all
python wiki_builder/orchestrate.py --backend gptoss --api-key X --knox-id X --ad-id X --phase all
```

## sdmAnalyzer 연동 아키텍처

### 통신 방식: JSON stdio 프로토콜
- sdmAnalyzer(GUI)가 subprocess로 wiki server를 spawn
- stdin/stdout pipe로 JSON 메시지 교환
- 한 줄 = JSON 한 객체 (line-delimited JSON)
- GUI 스레드 블로킹 없음 — 별도 스레드에서 readline()

### 요청 포맷 (sdmAnalyzer → wiki server)
```json
{"id": "req-001", "action": "query", "question": "PUSCH scrambling 절차는?", "file": false}
{"id": "req-002", "action": "lint"}
{"id": "req-003", "action": "ping"}
{"id": "req-004", "action": "status"}
```

### 응답 포맷 (wiki server → sdmAnalyzer)
```json
{"id": "req-001", "status": "ok", "answer": "...", "sources": ["entities/PUSCH.md"], "filed": null}
{"id": "req-002", "status": "ok", "report": "...", "issues": 3}
{"id": "req-003", "status": "pong"}
{"id": "req-004", "status": "ok", "wiki_pages": 19, "last_build": "2026-05-01"}
{"id": "req-001", "status": "error", "message": "wiki/index.md not found"}
```

### sdmAnalyzer 측 사용 예시
```python
from wiki_builder.wiki_client import WikiClient

client = WikiClient(
    python_exe=r"D:\work\00_project\llmwiki\.venv\Scripts\python.exe",
    wiki_root=r"D:\work\00_project\llmwiki",
    backend="gptoss",
    api_key="...",
)
client.start()

# 동기 호출 (내부에서 스레드 대기)
result = client.query("PUSCH scrambling 절차는?")
print(result["answer"])

# 비동기 콜백 (GUI용)
client.query_async("PUSCH scrambling 절차는?", callback=self.on_wiki_response)

client.stop()
```

## 재개 메커니즘

plan.json에 상태 저장:
```json
{
  "phase": "generate",
  "pages": [
    {
      "path": "entities/PUSCH.md",
      "generated": false,
      "linked": false,
      "sources": [...]
    }
  ]
}
```

중간에 멈춰도 plan.json만 있으면 거기서 재개 가능.
