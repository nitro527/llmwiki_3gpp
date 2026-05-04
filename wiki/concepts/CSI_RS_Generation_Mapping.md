# CSI_RS_Generation_Mapping

## 정의
[[CSI_RS]] (Channel State Information Reference Signal)는 [[UE]]가 채널 상태 정보를 측정하고, 빔 관리, 이동성 관리 및 무선 링크 모니터링을 수행할 수 있도록 기지국이 전송하는 하향링크 참조 신호입니다.

## 요약
[[CSI_RS]]는 [[Sequence_Generation]]을 통해 생성되며, [[Physical_Resource_Grid]] 내의 특정 자원 요소(RE)에 매핑됩니다. 주요 용도로는 [[L1_RSRP]], [[L1_SINR]] 측정, 빔 관리, [[Radio_Link_Monitoring]] (RLM), 그리고 이동성(Mobility) 측정이 포함됩니다.

## 상세 설명
[[CSI_RS]]의 생성 및 매핑 절차는 다음과 같습니다.

1. **Sequence Generation**: [[CSI_RS]] 시퀀스는 의사 난수(pseudo-random) 시퀀스 생성기를 기반으로 생성됩니다. 이는 슬롯 번호, 심볼 인덱스, 그리고 상위 계층에서 설정된 스크램블링 ID를 입력값으로 사용합니다.
2. **Mapping to Physical Resources**: 생성된 시퀀스는 설정된 밀도와 패턴에 따라 [[Physical_Resource_Grid]]의 RE에 매핑됩니다. 이때 [[PDSCH]]와의 충돌을 피하기 위해 상위 계층에서 제공하는 RE 매핑 패턴을 준수해야 합니다.
3. **NZP CSI_RS**: Non-Zero Power [[CSI_RS]]는 실제 신호 전력을 가지고 전송되는 자원으로, 채널 추정 및 측정의 핵심이 됩니다.
4. **용도별 절차**:
   - **Tracking**: 시간 및 주파수 추적을 위해 사용됩니다.
   - **L1-RSRP/SINR**: 채널 품질 및 빔 품질을 평가하기 위해 측정됩니다.
   - **Mobility**: 핸드오버 및 셀 선택/재선택을 위한 측정에 활용됩니다.
   - **RLM**: [[Radio_Link_Monitoring]]을 위해 [[SS_PBCH_Block]]과 함께 또는 단독으로 사용됩니다.

## 인과 관계
- [[CSI_RS]] (depends_on) [[Sequence_Generation]]
- [[CSI_RS]] (affects) [[CSI_Reporting_Procedures]]
- [[CSI_RS]] (triggers) [[L1_RSRP]] 및 [[L1_SINR]] 측정
- [[CSI_RS]] (part_of) [[Reference_Signals]]

## 관련 개념
- [[Reference_Signals]] (part_of)
- [[SS_PBCH_Block]] (similar_to)
- [[Radio_Link_Monitoring]] (depends_on)
- [[PDSCH_Resource_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §7.4.1.5.2: [[CSI_RS]] 시퀀스 생성 절차 정의
- TS 38.211 §7.4.1.5.3: [[CSI_RS]]의 물리 자원 매핑 규칙
- TS 38.214 §5.1.6.1: [[CSI_RS]] 수신 절차 (Tracking, L1-RSRP/SINR, Mobility)
- TS 38.214 §5.2.2.3.1: [[NZP_CSI_RS]] 설정 및 운용
- UE Feature 2-33a: Supported [[PDSCH]] RE-mapping patterns (필수)
- UE Feature 1-7: [[CSI_RS]] based [[Radio_Link_Monitoring]] (필수)
- UE Feature 1-4, 1-5, 1-6, 16-1a-1, 16-1g, 16-1g-1, 1-8, 1-9, 1-11, 1-13: [[CSI_RS]] 기반 측정 관련 선택적 기능

## 소스
- 3GPP TS 38.211 V19.0.0 "Physical channels and modulation"
- 3GPP TS 38.214 V19.0.0 "Physical layer procedures for data"