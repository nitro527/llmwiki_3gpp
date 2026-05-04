# CQI_Calculation_Procedures

## 정의
[[CQI]] (Channel Quality Indicator)는 [[UE]]가 하향링크 채널의 품질을 평가하여 기지국에 보고하는 지표로, 특정 [[PDSCH]] 전송 파라미터 조합을 사용하여 수신할 때 블록 오류율(BLER)이 0.1을 초과하지 않도록 하는 가장 높은 변조 및 부호화 방식(MCS) 인덱스를 의미합니다.

## 요약
CQI는 [[CSI]] 보고 절차의 핵심 요소로, UE는 [[CSI-RS]]를 기반으로 채널 및 간섭을 측정합니다. UE는 필수적으로 [[Basic_initial_access_channels_and_procedures]], [[Basic_PDSCH_reception]]을 지원해야 하며, [[PDSCH_beam_switching]], [[PDSCH_MIMO_layers]], [[TCI_states_for_PDSCH]], [[Additional_active_TCI_state_for_PDCCH]], [[Supported_PDSCH_RE-mapping_patterns]]과 같은 기능적 요구사항을 준수하여 CQI를 산출합니다. 또한, 선택적 기능으로 [[New_CQI_table]], [[1024QAM_for_PDSCH_for_FR1]], [[CSI_report_without_CQI]] 등이 활용될 수 있습니다.

## 상세 설명
CQI 산출을 위해 UE는 다음과 같은 가정을 기반으로 참조 자원을 설정합니다:
1. 첫 번째 [[OFDM]] 심볼은 [[PDSCH]] 전송을 위해 사용되지 않음.
2. [[DMRS]]를 제외한 추가적인 [[Reference_Signals]]는 존재하지 않음.
3. [[PDSCH_Resource_Mapping]]에서 정의된 RE 매핑 패턴을 준수함.
4. [[PDSCH_Scrambling]] 시퀀스는 기지국으로부터 설정된 파라미터를 따름.
5. [[PDSCH_Layer_Mapping]]에 따라 전송되는 레이어 수와 [[PMI_Codebook_Procedures]]에 따른 프리코딩 행렬을 적용함.

UE는 측정된 채널 상태를 바탕으로 CQI 테이블을 참조하여 가장 적합한 인덱스를 선택합니다. 이때, [[1024QAM_for_PDSCH_for_FR1]] 또는 [[1024QAM_for_PDSCH_for_FR1_with_maximum_2_MIMO_layers_restriction]]이 설정된 경우, 해당 변조 차수를 고려한 CQI 테이블이 적용됩니다. 또한, [[Supported_maximum_modulation_order_used_for_maximum_data_rate_calculation_for_multicast_PDSCH]]와 같은 멀티캐스트 관련 제약 사항이 있는 경우 이를 반영하여 CQI를 산출합니다.

## 인과 관계
- [[CSI_RS_Generation_Mapping]] (depends_on): CQI 산출을 위한 채널 측정의 기초 데이터를 제공함.
- [[PDSCH_Reception_Procedures]] (affects): CQI 산출 시 가정하는 PDSCH 수신 파라미터가 실제 수신 절차와 일치해야 함.
- [[CSI_Reporting_Procedures]] (triggers): 산출된 CQI는 주기적 또는 비주기적 CSI 보고를 통해 기지국으로 전달됨.

## 관련 개념
- [[CSI_RS]] (depends_on)
- [[PDSCH]] (depends_on)
- [[CSI_Reporting_Procedures]] (part_of)
- [[PMI_Codebook_Procedures]] (affects)
- [[BLER]] (affects)

## 스펙 근거
- TS 38.214 §5.2.2.1에 따르면, CQI는 특정 PDSCH 전송 파라미터 조합에 대해 0.1의 BLER을 만족하는 최대 MCS 인덱스로 정의됨.
- TS 38.214 §5.2.2.1에 따르면, CQI 산출 시 UE는 특정 RE 매핑, DMRS 구성, 및 레이어 매핑을 가정해야 함.

## 소스
- 3GPP TS 38.214 v19.0.0, "Physical layer procedures for data"