# DAPS_Handover_Procedures

## 정의
[[DAPS_Handover_Procedures]]는 [[UE]]가 소스 셀(Source Cell)과 타겟 셀(Target Cell)에 동시에 연결된 상태를 유지하며 핸드오버를 수행하는 절차를 의미합니다. 이는 핸드오버 중 데이터 중단 시간을 최소화하기 위해 도입되었습니다.

## 요약
[[DAPS_Handover_Procedures]]는 [[UE]]가 핸드오버 명령을 수신한 후, 소스 셀과의 연결을 유지하면서 타겟 셀로의 랜덤 액세스 절차를 수행하는 메커니즘입니다. 이 과정에서 [[UE]]는 두 셀 그룹에 대해 독립적인 [[Uplink_Power_Control]]을 수행하며, 전송 충돌을 방지하기 위한 우선순위 규칙을 따릅니다.

## 상세 설명
[[DAPS_Handover_Procedures]]가 설정된 경우, [[UE]]는 다음과 같은 동작을 수행합니다:

1. **필수 기능 지원**: 
   - [[Basic_initial_access_channels_and_procedures]] (1-1)를 항상 지원해야 합니다.
   - [[TCI_states_for_PDSCH]] (2-4) 및 [[Additional_active_TCI_state_for_PDCCH]] (2-4a)와 같은 필수 기능이 적용됩니다.
   - 선택적으로 [[RLF_for_DAPS_HO]] (37-2), [[Simultaneous_UL_transmission_for_DAPS_handover_for_intra_frequency]] (5-5) 등을 지원할 수 있습니다.

2. **전력 제어**:
   - 소스 셀 그룹과 타겟 셀 그룹에 대해 각각 독립적인 [[Uplink_Power_Control]] 파라미터가 설정됩니다.
   - [[UE]]는 각 셀 그룹의 전송 전력을 합산하여 최대 전송 전력($P_{CMAX}$)을 초과하지 않도록 제어합니다.

3. **전송 충돌 회피**:
   - 두 셀 그룹에서 동시에 [[PUSCH]] 또는 [[PUCCH]] 전송이 발생할 경우, [[Uplink_Power_Prioritization]] 규칙에 따라 전송 우선순위가 결정됩니다.
   - 타겟 셀로의 랜덤 액세스 절차와 소스 셀로의 데이터 전송이 충돌할 경우, 특정 우선순위 로직에 따라 전송이 제한되거나 조정됩니다.

## 인과 관계
- [[DAPS_Handover_Procedures]] (depends_on) [[Uplink_Power_Control]]
- [[DAPS_Handover_Procedures]] (triggers) [[RACH_Procedure_L1]]
- [[DAPS_Handover_Procedures]] (affects) [[Uplink_Power_Prioritization]]

## 관련 개념
- [[Uplink_Power_Control]] (depends_on)
- [[RACH_Procedure_L1]] (part_of)
- [[Uplink_Power_Prioritization]] (affects)
- [[Dual_Connectivity_Power_Control]] (similar_to)

## 스펙 근거
- TS 38.213 §15에 따르면, DAPS 핸드오버 시 [[UE]]는 소스 셀과 타겟 셀 각각에 대해 독립적인 전력 제어 루프를 유지하며, 두 셀 그룹 간의 전송 전력 합계가 [[UE]]의 최대 전력 제한을 초과하지 않도록 관리해야 합니다.

## 소스
- 3GPP TS 38.213 Release 18, "Physical layer procedures for control"