# HARQ_ACK_Codebook_Determination

## 정의
[[HARQ_ACK_Codebook_Determination]]은 [[UE]]가 수신한 [[PDSCH]] 또는 [[PDCCH]] 기반의 [[SPS]] PDSCH 릴리즈에 대한 [[HARQ_ACK]] 정보를 [[PUCCH]] 또는 [[PUSCH]]를 통해 상위 계층으로 보고하기 위해 구성하는 비트 집합 생성 절차를 의미한다.

## 요약
[[UE]]는 상위 계층 설정에 따라 하나 또는 두 개의 [[HARQ_ACK]] 코드북을 생성한다. 코드북은 동일한 우선순위 인덱스를 가진 [[HARQ_ACK]] 정보들로 구성되며, [[PDSCH_CBG_Transmission]] 설정 여부에 따라 [[TB]] 단위 또는 [[CBG]] 단위로 비트가 생성된다. [[DCI]]를 통한 [[One-shot_HARQ_ACK_feedback]] 요청 시 [[Type-3_HARQ_ACK_codebook]]이 사용될 수 있다.

## 상세 설명
TS 38.213 §9.1에 따른 [[HARQ_ACK]] 코드북 생성의 주요 절차는 다음과 같다.

- 코드북 구성: [[UE]]는 pdsch-HARQ-ACK-CodebookList 설정에 따라 하나 또는 두 개의 코드북을 생성한다. 두 개의 코드북을 생성하는 경우, 각각 우선순위 인덱스 0과 1에 대응하며, 각 우선순위에 대해 별도의 [[PUCCH_Config]], [[UCI_OnPUSCH]], [[PDSCH_CBG_Transmission]] 설정이 적용된다.
- [[HARQ_ACK]] 비트 생성:
  - [[PDSCH_CBG_Transmission]]이 설정되지 않은 경우, [[UE]]는 [[TB]]당 하나의 [[HARQ_ACK]] 비트를 생성한다.
  - [[PDCCH]] 없이 수신된 [[SPS]] PDSCH 또는 [[SPS]] PDSCH 릴리즈를 지시하는 [[DCI]] 수신 시, [[UE]]는 하나의 [[HARQ_ACK]] 비트를 생성한다.
  - [[ACK]]/[[NACK]] 판정: [[TB]]를 올바르게 복호화하거나 [[TCI_State_Management]] 업데이트를 포함한 [[PDSCH]] 스케줄링 없는 [[DCI]] 수신 시 [[ACK]](값 1)를 생성하고, 복호화 실패 시 [[NACK]](값 0)를 생성한다.
- [[SPS]] 관련 동작: [[SPS]] PDSCH 릴리즈와 [[SPS]] PDSCH 수신이 동일한 [[Slot]]에서 발생하고 동일한 [[PUCCH]]에 다중화되는 경우, [[UE]]는 [[SPS]] PDSCH 수신에 대한 [[HARQ_ACK]]를 생성하지 않고 릴리즈에 대한 비트만 생성한다.
- [[SCell_Dormancy_Management]]: [[DCI_Format_1_1]] 또는 [[DCI_Format_1_3]]을 통해 [[SCell]] 휴면을 지시받은 경우, [[UE]]는 [[ACK]]에 해당하는 [[HARQ_ACK]] 비트를 생성한다.
- [[One-shot_HARQ_ACK_feedback]]: pdsch-HARQ-ACK-OneShotFeedback이 설정된 [[UE]]가 [[DCI]] 내의 One-shot HARQ-ACK 요청 필드를 감지하면, [[Type-3_HARQ_ACK_codebook]]을 생성하여 보고한다.

## 인과 관계
- [[HARQ_ACK_Codebook_Determination]] depends_on [[PDSCH_Reception_Procedure]] (PDSCH 수신 결과에 따른 ACK/NACK 생성)
- [[HARQ_ACK_Codebook_Determination]] depends_on [[PDSCH_SPS_Procedure]] (SPS PDSCH 수신 및 릴리즈에 대한 피드백 생성)
- [[HARQ_ACK_Codebook_Determination]] triggers [[HARQ_ACK_Reporting]] (생성된 코드북의 상위 계층 보고)
- [[HARQ_ACK_Codebook_Determination]] depends_on [[UCI_Multiplexing]] (생성된 코드북의 PUCCH/PUSCH 다중화)
- [[HARQ_ACK_Codebook_Determination]] depends_on [[PDSCH_CBG_Transmission]] (CBG 기반 피드백 비트 수 결정)

## 관련 개념
- [[HARQ_ACK_Reporting]] (affects)
- [[PDSCH_SPS_Procedure]] (depends_on)
- [[UCI_Multiplexing]] (depends_on)
- [[PDSCH_CBG_Transmission]] (depends_on)
- [[PUCCH_Priority_Handling]] (affects)

## 스펙 근거
- TS 38.213 §9.1: HARQ-ACK 코드북 결정 절차 및 우선순위 인덱스 기반 구성
- TS 38.213 §9.1.3: SCell 휴면 및 SPS PDSCH 릴리즈 관련 HARQ-ACK 비트 생성
- TS 38.213 §9.1.4: Type-3 HARQ-ACK 코드북 및 One-shot 피드백 동작

## 소스
- TS 38.213 §9.1