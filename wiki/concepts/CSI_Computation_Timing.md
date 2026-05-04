# CSI_Computation_Timing

## 정의
[[CSI_Computation_Timing]]은 [[DCI]]를 통해 트리거된 [[CSI]] 보고를 수행하기 위해 [[UE]]가 채널 상태 정보를 계산하고 준비하는 데 필요한 최소 처리 시간을 의미합니다.

## 요약
[[UE]]는 [[PDCCH]]를 통해 수신한 [[DCI]] 기반의 [[Aperiodic_CSI]] 보고 요청을 처리하기 위해 특정 시간 제약 조건을 준수해야 합니다. 이 시간은 [[UE]]의 능력(Capability)에 따라 결정되며, [[CSI_RS]] 수신 및 [[CSI]] 계산을 위한 물리 계층 처리 시간을 포함합니다.

## 상세 설명
[[TS_38_214]] §5.4에 따르면, [[UE]]가 [[DCI]]를 수신한 시점부터 해당 [[CSI]] 보고를 위한 [[CSI_RS]] 수신 및 계산을 완료하기까지의 시간은 [[UE]]의 처리 능력에 따라 정의됩니다.

1. **필수 능력 기반 처리**: [[UE]]는 [[Beam_reporting_timing]](2-25) 및 [[Active_spatial_relations]](2-60)과 같은 필수 기능을 지원해야 하며, 이를 통해 [[CSI]] 계산의 유효성을 판단합니다.
2. **처리 시간 산정**: [[UE]]는 [[CSI]] 보고를 트리거하는 [[DCI]]가 포함된 [[Slot]] 이후, [[CSI_RS]] 자원과 [[CSI]] 보고가 수행되는 [[Slot]] 사이의 간격이 [[UE]]의 최소 처리 시간 요구사항을 만족하는지 확인합니다.
3. **선택적 기능 지원**:
   - [[A_CSI_RS_beam_switching_timing]](2-28) 및 [[New_capability_for_beamSwitchTiming_values_of_224_and_336]](14-7)을 통해 더 정밀한 빔 스위칭 타이밍을 지원할 수 있습니다.
   - [[Support_of_P_SP_CSI_RS_reception_with_CSI_RS_ValidationWith_DCI_r16_configured]](10-31) 기능을 통해 [[DCI]] 기반의 [[CSI_RS]] 유효성 검증을 수행합니다.
   - [[Cross_Slot_Scheduling]](19-2), [[Cancellation_of_PUCCH_PUSCH_or_PRACH_with_a_DCI_scheduling_a_PDSCH_or_CSI_RS_or_a_DCI_format_2_0_for_SFI]](22-9), [[Triggering_SRS_only_in_DCI_0_1_0_2]](23-8-2), [[UE_specific_K_offset]](26-9) 등은 [[CSI]] 보고 타이밍 및 자원 할당에 영향을 미치는 선택적 기능들입니다.
   - [[Per_aperiodic_CSI_RS_resource_resource_set_configuration_for_TCI_selection_in_S_DCI_based_MTRP]](40-1-3), [[Per_aperiodic_CSI_RS_resource_resource_set_configuration_for_TCI_selection_in_M_DCI_based_MTRP]](40-1-3a), [[Basic_feature_for_multi_DCI_based_inter_cell_Multi_TRP_operation_with_two_TA_enhancement]](40-2-2)는 [[Multi_TRP]] 환경에서의 [[CSI]] 계산 및 보고 타이밍을 최적화합니다.

## 인과 관계
- [[DCI]] 수신 (triggers) [[CSI]] 계산 및 보고
- [[UE]] 처리 능력 (affects) [[CSI]] 계산 시간
- [[CSI_RS]] 설정 (depends_on) [[CSI]] 계산 유효성

## 관련 개념
- [[CSI_Reporting_Procedures]] (part_of)
- [[CSI_RS]] (depends_on)
- [[DCI]] (triggers)
- [[UE_Capability]] (affects)

## 스펙 근거
- [[TS_38_214]] §5.4: UE CSI computation time 정의 및 요구사항 명시

## 소스
- 3GPP TS 38.214 V19.0.0 (2024-03)