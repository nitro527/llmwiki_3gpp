# TASKS.md — LLMWiki 구현 체크리스트

## 구현 순서

단계별로 완료 후 다음 단계로 넘어갈 것.
각 단계 완료 기준은 실제 실행 후 동작 확인.

---

## Task 1: 프로젝트 셋업 ✅

- [x] `llmwiki/` 폴더 구조 생성
- [x] `requirements.txt` 작성
- [x] `.venv` 생성 및 패키지 설치
- [x] `chunk_text.py` 확인
- [x] `sources/3gpp/` 에 소스 파일 준비

---

## Task 2: api.py 구현 ✅

- [x] `wiki_builder/api.py` 구현
- [x] `call_simple(system, user, **kwargs) -> str`
- [x] Claude / gpt-oss 전환

---

## Task 3: Phase 1 (Plan) 구현 ✅

- [x] `wiki_builder/plan.py` 구현
- [x] `wiki_builder/prompts.py` — PLANNER_SYSTEM, PLANNER_USER
- [x] `wiki_builder/orchestrate.py` — `run_plan()` 연결
- [x] plan.json 생성 확인
- [x] 소스 파일 단위 증분 저장 (처리 완료마다 plan.json 저장)
- [x] existing_pages를 `path: description` 형태로 LLM에 전달 (description 문맥 제공)
- [x] 멀티소스 머지 시 description도 더 넓은 범위로 업데이트

---

## Task 3.5: Phase 1.5 (Post-Plan) 구현 ← 신규

plan.json 완성 후 품질 검증 단계. Generate 시작 전 계획의 오류를 사전 차단.

- [ ] `wiki_builder/post_plan.py` 구현
  - `run_post_plan(plan, call_llm) -> dict`
  - **코드 검증** (LLM 불필요):
    - 동일 파일의 동일 섹션이 여러 페이지에 중복 배정된 경우 감지 → 로그 출력
  - **LLM 검증** (페이지 단위):
    - 페이지 path/description과 배정된 섹션이 의미적으로 맞는지 확인
    - 불일치 감지 시 해당 소스 항목 제거 또는 올바른 페이지로 이동
    - 결과를 plan.json에 반영하여 저장
- [ ] `wiki_builder/prompts.py` — POST_PLAN_SYSTEM, POST_PLAN_USER 추가
- [ ] `orchestrate.py` — plan → post_plan → generate 순서로 연결
- [ ] 테스트:
  ```bash
  python wiki_builder/orchestrate.py --phase plan --backend gemini
  # plan.json 검토 후
  python wiki_builder/orchestrate.py --phase post_plan --backend gemini
  ```

---

## Task 4: Phase 2 (Generate) 구현 ✅

- [x] `wiki_builder/generate.py` 구현
- [x] ThreadPoolExecutor 병렬 처리
- [x] generated 플래그 업데이트
- [x] wiki 파일 생성 확인

---

## Task 5: Quality Checker 구현 ✅

- [x] `wiki_builder/evaluate.py` — `check_quality()` 구현
- [x] 8점 체크리스트 평가

---

## Task 6: Phase 3 (Link) 구현

- [ ] `wiki_builder/link.py` 구현
  - `run_link(plan, wiki_dir, call_llm, ...)`
  - Python이 링크 맵 계산 (`_build_link_map`)
  - 파일별 Linker LLM 호출
  - 역방향 링크 추가
- [ ] `wiki_builder/prompts.py` — LINKER_SYSTEM, LINKER_USER 추가
- [ ] 실행 테스트:
  ```bash
  python wiki_builder/orchestrate.py --phase link --backend claude
  ```
- [ ] Obsidian에서 링크 확인

---

## Task 7: Phase 4 (Evaluate) 구현

- [ ] `wiki_builder/evaluate.py` — `run_evaluate()` 구현
  - 원인 분석 LLM 호출
  - prompts.py 개선안 도출
  - 개선안으로 검증 재실행
  - 보고서 생성
  - 사람 컨펌 대기 (터미널 입력)
- [ ] eval.log 포맷 확인
- [ ] 최대 5회 반복 후 알림 확인

---

## Task 8: 전체 파이프라인 테스트

- [ ] 소스 2개 이상으로 전체 실행
  ```bash
  python wiki_builder/orchestrate.py --phase all --backend claude
  ```
- [ ] plan.json → wiki 생성 → 링크 → 평가 전체 흐름 확인
- [ ] 중간 중단 후 재실행으로 재개 확인

---

## Task 9: Phase 5 (Query) 구현 ← 신규

Karpathy 패턴: 질문 → index.md 검색 → 관련 페이지 읽기 → 합성 → 선택적 filing

- [ ] `wiki_builder/query.py` 구현
  - `run_query(question, wiki_dir, call_llm) -> dict`
  - Step 1: `wiki/index.md` 읽고 관련 페이지 경로 선택 (LLM 1회)
  - Step 2: 선택된 페이지들 읽고 답변 합성 + 출처 명시 (LLM 1회)
  - 반환: `{"answer": str, "sources": [str], "pages_read": [str]}`
- [ ] `wiki_builder/prompts.py` — QUERY_SELECTOR_SYSTEM/USER, QUERY_SYNTHESIZER_SYSTEM/USER 추가
- [ ] filing 옵션: 답변을 `wiki/query/YYYY-MM-DD_topic.md`로 저장
- [ ] `wiki/log.md`에 `## [날짜] query | 질문` 형식으로 append
- [ ] `orchestrate.py` — `--phase query --question "..."` 연결
- [ ] 테스트:
  ```bash
  python wiki_builder/orchestrate.py --phase query --question "PUSCH scrambling 절차는?" --backend claude
  ```

---

## Task 10: Phase 6 (Lint) 구현 ← 신규

Karpathy 패턴: 주기적 wiki 건강 검진

- [ ] `wiki_builder/lint.py` 구현
  - `run_lint(wiki_dir, call_llm) -> dict`
  - Python이 직접 계산하는 항목:
    - 고아 페이지 (inbound 링크 0개)
    - 역방향 링크 누락
    - 언급은 있으나 페이지 없는 개념 (`[[X]]` 있는데 X.md 없음)
  - LLM 호출 항목 (페이지 묶음 단위):
    - 내용 모순 감지
    - 오래된 주장 감지
    - 데이터 공백 제안
- [ ] `wiki_builder/prompts.py` — LINT_SYSTEM, LINT_USER 추가
- [ ] 리포트를 `wiki/lint_YYYY-MM-DD.md`로 저장
- [ ] `wiki/log.md`에 lint 결과 기록
- [ ] `orchestrate.py` — `--phase lint` 연결
- [ ] 테스트:
  ```bash
  python wiki_builder/orchestrate.py --phase lint --backend claude
  ```

---

## Task 11: Chat REPL 구현 ← 신규

터미널 대화형 인터페이스. LLM Wiki의 human-facing 레이어.

- [ ] `wiki_builder/chat.py` 구현
  - `run_chat(wiki_dir, call_llm)` — 대화형 REPL 루프
  - 입력 파싱 및 라우팅:
    - `/lint` → `run_lint()` 호출
    - `/index` → `wiki/index.md` 출력
    - `/log` → `wiki/log.md` 최근 10개 출력
    - `/help` → 도움말
    - `/exit` → 종료
    - 그 외 → `run_query()` 호출
  - 답변 후 filing 여부 묻기: `"wiki에 저장할까요? (y/n)"`
  - 내부는 stateless: 각 질문마다 독립 LLM 호출, history 누적 없음
- [ ] `orchestrate.py` — `--phase chat` 연결
- [ ] 테스트:
  ```bash
  python wiki_builder/orchestrate.py --phase chat --backend claude
  ```
  - 일반 질문 → query 라우팅 확인
  - `/lint` → lint 실행 확인
  - `y` 입력 → wiki/query/ 저장 확인

---

## Task 12: index.md / log.md 자동 관리 ← 신규

Generate/Query/Lint 결과가 index.md와 log.md에 반영되도록.

- [ ] `wiki_builder/index_manager.py` 구현 (또는 `orchestrate.py`에 통합)
  - `update_index(wiki_dir)`: 전체 wiki 스캔 후 index.md 재생성
  - `append_log(wiki_dir, entry: str)`: log.md에 한 줄 추가
    - 형식: `## [YYYY-MM-DD] {type} | {title}`
- [ ] Generate phase 완료 후 `update_index()` 자동 호출
- [ ] Query/Lint 실행 시 `append_log()` 자동 호출

---

## Task 13: Server 모드 구현 (sdmAnalyzer 연동 핵심) ← 신규

JSON stdio 프로토콜 서버. GUI 프로그램이 subprocess로 spawn하여 통신.

- [ ] `wiki_builder/server.py` 구현
  - `run_server(wiki_dir, call_llm)` — stdin 루프
  - stdin에서 한 줄씩 JSON 읽기 → action 라우팅 → stdout에 JSON 응답
  - 지원 action: `query`, `lint`, `status`, `ping`
  - 각 요청은 독립 처리 (stateless)
  - stderr로만 로그 출력 (stdout은 JSON 전용)
  - 프로토콜:
    ```
    요청: {"id": "req-001", "action": "query", "question": "...", "file": false}
    응답: {"id": "req-001", "status": "ok", "answer": "...", "sources": [...]}
    ```
  - 에러 응답: `{"id": "...", "status": "error", "message": "..."}`
  - stdin EOF → 정상 종료
- [ ] `orchestrate.py` — `--phase server` 연결
- [ ] 테스트 (터미널에서 수동):
  ```bash
  echo '{"id":"1","action":"ping"}' | python wiki_builder/orchestrate.py --phase server --backend claude
  # 응답: {"id": "1", "status": "pong"}
  ```

---

## Task 14: WikiClient 구현 (sdmAnalyzer에서 import) ← 신규

sdmAnalyzer가 import하는 클라이언트 래퍼. llmwiki venv의 서버 프로세스를 관리.

- [ ] `wiki_builder/wiki_client.py` 구현
  - `WikiClient(python_exe, wiki_root, backend, api_key, knox_id, ad_id)`
  - `start()`: subprocess 생성, stdin/stdout pipe 연결, reader 스레드 시작
  - `stop()`: stdin EOF 전송, 프로세스 종료 대기
  - `query(question, file=False, timeout=60) -> dict`: 동기 호출
  - `query_async(question, callback, file=False)`: 비동기 콜백 (GUI용)
  - `lint(timeout=120) -> dict`: lint 동기 호출
  - `status() -> dict`: wiki 상태 조회
  - `ping() -> bool`: 서버 생존 확인
  - 내부: request id → Future/Event 매핑으로 응답 매칭
  - 프로세스 크래시 시 자동 재시작 (1회)
- [ ] 사용 예시 (sdmAnalyzer 측):
  ```python
  from wiki_builder.wiki_client import WikiClient
  
  client = WikiClient(
      python_exe=r"D:\work\00_project\llmwiki\.venv\Scripts\python.exe",
      wiki_root=r"D:\work\00_project\llmwiki",
      backend="gptoss",
      api_key="...",
  )
  client.start()
  result = client.query("PUSCH scrambling 절차는?")
  client.stop()
  ```
- [ ] 테스트: wiki server 실제 spawn 후 query 응답 확인

---

## Task 15: orchestrate.py 리팩토링 — LLM Orchestrator + tool 구조 ← 핵심 리팩토링

현재 Python 함수 파이프라인을 LLM 에이전트가 tool을 호출하는 구조로 전환.

- [ ] `orchestrate.py` — Orchestrator LLM 에이전트 루프 구현
  - 사용자 요청(--phase 인자)을 받아 Orchestrator LLM에게 전달
  - Orchestrator가 tool 호출로 각 Phase 실행 결정
- [ ] 각 Phase를 tool definition으로 wrapping
  - `run_plan()`, `run_generate()`, `run_link()`, `run_evaluate()` → tool
  - `run_lint()`, `run_chat()`, `run_server()` → tool
  - `query.py` — **예외: tool 방식 아님, 기존 2-step stateless 유지**
- [ ] tool 결과를 Orchestrator가 받아 다음 action 결정
  - 예: `run_generate()` 불합격 발생 → Orchestrator가 `run_evaluate()` 호출 여부 판단
- [ ] 테스트:
  ```bash
  python wiki_builder/orchestrate.py --phase all --backend claude
  python wiki_builder/orchestrate.py --phase plan --backend claude
  ```

---

## 완료 기준

### 빌드 파이프라인
- [ ] `--phase all --backend claude` 에러 없이 실행
- [ ] wiki/ 폴더에 AGENTS.md 규칙에 맞는 문서 생성
- [ ] Quality Checker 7/8점 이상 합격
- [ ] plan.json 기반 재실행 시 완료 페이지 스킵

### Query
- [ ] 자연어 질문 → 관련 wiki 페이지 기반 답변 + 출처 명시
- [ ] 답변 filing 후 index.md 갱신 확인

### Lint
- [ ] 고아 페이지, 모순, 공백 리포트 생성
- [ ] lint_YYYY-MM-DD.md 저장 확인

### Chat
- [ ] 터미널에서 대화형으로 질문/답변 동작
- [ ] `/lint`, `/index`, `/log`, `/exit` 커맨드 동작
