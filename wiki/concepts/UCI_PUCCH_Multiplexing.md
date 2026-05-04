# UCI_PUCCH_Multiplexing

## 정의
[[UCI_PUCCH_Multiplexing]]은 인코딩된 [[UCI]] 비트들을 물리적 자원인 [[PUCCH]]에 매핑하고 다중화하는 절차를 의미합니다.

## 요약
[[UCI]] 정보(예: [[HARQ_ACK_Codebook_Determination]], [[SR_Reporting_Procedure]], [[CSI_Reporting_Procedures]])는 [[UCI_Channel_Coding]]을 거쳐 인코딩된 후, [[PUCCH]] 포맷에 따라 물리 자원에 할당됩니다. 이 과정에서 다중화된 비트들은 특정 규칙에 따라 [[PUCCH]]의 심볼 및 부반송파에 배치됩니다.

## 상세 설명
[[UCI]] 비트가 [[PUCCH]]를 통해 전송될 때, 각 [[PUCCH_Format_Processing]]에 따라 다음과 같은 절차를 따릅니다.

1. **비트 연결 및 다중화**: [[UCI_Channel_Coding]]을 통해 생성된 비트들은 [[PUCCH]] 자원의 용량에 맞게 연결 및 다중화됩니다.
2. **물리 자원 매핑**: 인코딩된 비트들은 [[PUCCH]]의 할당된 심볼과 부반송파 위치에 매핑됩니다. 이때 [[PUCCH]] 포맷에 따라 [[DMRS_Generation_Mapping]]과 함께 전송됩니다.
3. **UE 기능 지원**:
    * [필수(cap)] 4-19: 동일한 시작 심볼을 가진 [[SR]], [[HARQ_ACK]], [[CSI]]의 슬롯 내 다중화.
    * [필수(cap)] 4-28: 서로 다른 [[PUCCH]]/[[PUSCH]] 시작 심볼을 가진 [[PUSCH]] 상의 [[HARQ_ACK]] 다중화.
    * [선택] 4-19a: 서로 다른 시작 심볼을 가진 [[SR]]/[[HARQ_ACK]]의 슬롯 내 다중화.
    * [선택] 4-19b: 슬롯 내 다중화가 1회 이상 발생하는 경우(동일/상이한 시작 심볼).
    * [선택] 4-19c: 서로 다른 시작 심볼을 가진 [[SR]]/[[HARQ_ACK]]/[[CSI]]의 슬롯 내 다중화.
    * [선택] 4-27: 제어 채널 다중화를 위한 중첩된 채널 그룹이 1개 이상인 경우.
    * [선택] 10-24: [[CG_UCI_Multiplexing_with_HARQ_ACK]] 지원.
    * [선택] 10-35, 10-35a, 10-35b, 10-35c, 10-36: 비면허 대역(unlicensed spectrum)에서의 상기 다중화 기능 지원.

## 인과 관계
- [[UCI_Channel_Coding]] (depends_on) [[UCI_PUCCH_Multiplexing]]
- [[PUCCH_Format_Processing]] (affects) [[UCI_PUCCH_Multiplexing]]
- [[UCI_PUCCH_Multiplexing]] (triggers) [[PUCCH]] 전송

## 관련 개념
- [[UCI]] (part_of)
- [[PUCCH]] (part_of)
- [[UCI_Channel_Coding]] (depends_on)
- [[PUCCH_Format_Processing]] (depends_on)

## 스펙 근거
- TS 38.212 §6.3.1.5에 따르면, 코드 블록 연결(Code block concatenation) 절차가 수행됩니다.
- TS 38.212 §6.3.1.6에 따르면, 인코딩된 [[UCI]] 비트들을 [[PUCCH]]로 다중화하는 규칙이 정의됩니다.

## 소스
- 3GPP TS 38.212 V18.0.0 (2023-12)
- 3GPP TS 38.822 (UE Feature List)