# PRACH_Sequence_Generation

## 정의
[[PRACH]] 프리앰블 시퀀스 생성은 [[UE]]가 [[RACH_Procedure_L1]]을 수행할 때 기지국과의 초기 접속 또는 상향링크 동기화를 위해 사용하는 물리 계층의 랜덤 액세스 프리앰블 신호를 생성하는 절차를 의미합니다.

## 요약
[[PRACH]] 프리앰블 시퀀스는 자자노프(Zadoff-Chu) 시퀀스를 기반으로 생성됩니다. 이 과정은 [[UE]]의 [[Basic_MAC_procedures]] 및 [[Basic_power_control_operation]]과 밀접하게 연관되어 있으며, 특정 셀 설정에 따라 시퀀스 순환 이동(Cyclic Shift)이 적용됩니다. 또한, [[Wideband_PRACH]] 및 [[Wideband_PRACH_for_120_kHz_in_FR2-2]]와 같은 고도화된 기능 환경에서도 동일한 기본 생성 원리가 적용됩니다.

## 상세 설명
TS 38.211 §6.3.3.1에 따르면, [[PRACH]] 프리앰블 시퀀스는 다음과 같은 단계로 생성됩니다.

1. **시퀀스 기반 생성**: 프리앰블 시퀀스는 자자노프 시퀀스(Zadoff-Chu sequence)를 기반으로 정의됩니다.
2. **순환 이동(Cyclic Shift)**: 생성된 기본 시퀀스에 대해 상위 계층에서 설정된 순환 이동 값이 적용됩니다. 이는 동일한 프리앰블 자원 내에서 서로 다른 [[UE]]를 구분하거나, 셀 반경에 따른 지연 확산을 고려하기 위함입니다.
3. **매핑**: 생성된 시퀀스는 [[PRACH_Resource_Mapping]] 절차를 통해 물리적 자원 그리드에 매핑됩니다.

본 절차는 [[Parallel_PRACH_and_SRS_PUCCH_PUSCH_transmissions_across_CCs_in_inter-band_CA]]와 같은 복합적인 상향링크 전송 환경에서도 [[Basic_power_control_operation]]에 의해 제어되는 전송 전력을 바탕으로 수행됩니다.

## 인과 관계
- [[RACH_Procedure_L1]] (triggers) [[PRACH_Sequence_Generation]]
- [[PRACH_Sequence_Generation]] (affects) [[PRACH_Resource_Mapping]]
- [[Basic_power_control_operation]] (affects) [[PRACH_Sequence_Generation]]
- [[Basic_MAC_procedures]] (depends_on) [[PRACH_Sequence_Generation]]

## 관련 개념
- [[PRACH]] (part_of)
- [[RACH_Procedure_L1]] (depends_on)
- [[PRACH_Resource_Mapping]] (depends_on)
- [[Basic_power_control_operation]] (part_of)
- [[Basic_MAC_procedures]] (part_of)

## 스펙 근거
- TS 38.211 §6.3.3.1: PRACH 프리앰블 시퀀스 생성 및 자자노프 시퀀스 정의에 관한 기술 규격.

## 소스
- 3GPP TS 38.211 V17.x.x (Release 17), "Physical channels and modulation"