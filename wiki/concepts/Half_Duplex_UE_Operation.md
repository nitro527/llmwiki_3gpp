# Half_Duplex_UE_Operation

## 정의
[[Half_Duplex_UE_Operation]]은 페어드 스펙트럼(Paired Spectrum) 환경에서 동작하는 [[UE]]가 하향링크(DL) 수신과 상향링크(UL) 전송을 동시에 수행할 수 없는 물리적 제약을 극복하기 위해, 시간 자원을 분할하여 충돌을 회피하는 동작 절차를 의미한다.

## 요약
[[Half_Duplex_UE_Operation]]은 [[UE]]가 동일한 주파수 대역 내에서 DL과 UL을 동시에 처리할 수 없는 하드웨어적 한계를 고려하여, [[PDCCH]], [[PDSCH]], [[PUSCH]], [[PUCCH]] 등의 물리 채널 간의 시간적 충돌을 방지하는 메커니즘이다. 이는 특히 [[RedCap_UE_Procedures]]와 같은 특정 단말 유형이나 TDD/FDD 동작 모드에서 필수적으로 요구되는 기능이다.

## 상세 설명
[[Half_Duplex_UE_Operation]]은 다음과 같은 핵심 기능 및 동작을 포함한다.

*   **기본 스케줄링 및 HARQ 동작**: [[Basic_scheduling/HARQ_operation]]은 모든 [[Half_Duplex_UE_Operation]]의 근간이 되며, DL 수신과 UL 전송이 겹치지 않도록 스케줄링 타이밍을 제어한다.
*   **PDSCH 매핑 타입 A**: [[PDSCH_mapping_type_A_with_less_than_7_OFDM_symbols]] 기능을 통해 짧은 시간 내에 DL 수신을 완료함으로써 UL 전송과의 충돌 가능성을 줄인다.
*   **추가적인 동작 모드**:
    *   [[Half-duplex_UE_behaviour_in_TDD_CA_for_same_SCS]]: TDD 반송파 집성 환경에서 동일한 부반송파 간격(SCS)을 사용할 때의 충돌 회피.
    *   [[Half-duplex_FDD_operation_type_A_for_RedCap_UE]]: FDD 환경에서 [[RedCap_UE]]가 하프 듀플렉스 방식으로 동작할 때의 절차.
    *   [[UE_specific_RRC_configure_UL/DL_assignment]]: RRC 설정을 통해 명시적으로 UL/DL 할당을 제어.
    *   [[More_than_one_DL/UL_switch_point_in_a_slot]]: 슬롯 내에서 다수의 스위칭 지점을 허용하여 유연한 자원 활용.
    *   [[RA_Type_0_for_PUSCH]], [[Dynamic_switching_between_RA_Type_0_and_RA_Type_1_for_PDSCH]], [[Dynamic_switching_between_RA_Type_0_and_RA_Type_1_for_PUSCH]]: 자원 할당 방식의 동적 변경을 통한 효율적 스케줄링.
    *   [[UE_PDSCH_processing_capability_#2]], [[UE_PDSCH_processing_capability_#2_with_scheduling_limitation_for_30kHz-SCS]], [[UE_PUSCH_processing_capability_#2]]: 향상된 처리 능력을 활용하여 스케줄링 제약을 완화.

## 인과 관계
- [[Basic_scheduling/HARQ_operation]] (depends_on) [[Half_Duplex_UE_Operation]]
- [[PDSCH_mapping_type_A_with_less_than_7_OFDM_symbols]] (depends_on) [[Half_Duplex_UE_Operation]]
- [[Half_Duplex_UE_Operation]] (affects) [[PUSCH_Transmission_Procedures]]
- [[Half_Duplex_UE_Operation]] (affects) [[PDSCH_Reception_Procedures]]

## 관련 개념
- [[Basic_scheduling/HARQ_operation]] (part_of)
- [[PDSCH_mapping_type_A_with_less_than_7_OFDM_symbols]] (part_of)
- [[RedCap_UE_Procedures]] (similar_to)
- [[TDD_CA]] (depends_on)

## 스펙 근거
TS 38.213 §17.2에 따르면, 페어드 스펙트럼에서 동작하는 하프 듀플렉스 [[UE]]는 DL 수신과 UL 전송이 시간적으로 겹치지 않도록 보장해야 하며, 이를 위해 상위 계층 설정 및 DCI 기반의 스케줄링 제한을 따른다.

## 소스
- 3GPP TS 38.213 v18.0.0 "Physical layer procedures for control" §17.2