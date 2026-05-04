# Power_Headroom_Report

## 정의
[[Power_Headroom_Report]] (PHR)은 [[UE]]가 현재 설정된 최대 전송 전력과 실제 전송에 사용되는 전력 간의 차이를 [[gNB]]에 보고하는 메커니즘입니다. 이를 통해 [[gNB]]는 [[Uplink_Power_Control]]을 최적화하고 스케줄링 결정을 내립니다.

## 요약
[[Power_Headroom_Report]]는 크게 Type 1, Type 2, Type 3로 구분됩니다. 
- Type 1: [[PUSCH]] 전송에 대한 전력 여유 보고
- Type 2: [[PUSCH]]와 [[PUCCH]]가 동시에 전송되는 경우의 전력 여유 보고
- Type 3: [[SRS]] 전송에 대한 전력 여유 보고
본 기능은 [[Connection_Establishment_Failure_Reporting]] 및 [[Radio_Link_Failure_Reporting]]과 같은 네트워크 안정성 관련 보고 절차와 밀접하게 연관되어 있으며, [[PHR_enhancement_for_dynamic_waveform_switching]] (54-3a) 등 다양한 [[UE]] 기능과 결합하여 동작합니다.

## 상세 설명
[[Power_Headroom_Report]]는 TS 38.213 §7.7에 따라 정의됩니다.

### Type 1 PHR
[[PUSCH]] 전송이 발생하는 경우, [[UE]]는 다음 식을 기반으로 Type 1 PH를 계산합니다.
PH_type1,c(i, j, qd, l) = P_CMAX,f,c(i) - {P_O_PUSCH,c(j) + 10log10(2^mu * M_RB,c^PUSCH(i)) + alpha_c(j) * PL_c(qd) + delta_TF,c(i) + f_c(i, l)}
여기서 P_CMAX,f,c(i)는 설정된 최대 전송 전력이며, 나머지 항들은 [[PUSCH_Power_Control]] 파라미터입니다.

### Type 2 PHR
[[PUSCH]]와 [[PUCCH]]가 동시에 전송될 때, [[UE]]는 두 채널의 전력 합계를 고려하여 Type 2 PH를 계산합니다. 이는 [[PUCCH_Power_Control]]과 [[PUSCH_Power_Control]]의 결합된 전력 제어 상태를 반영합니다.

### Type 3 PHR
[[SRS]] 전송에 대해 계산되며, [[SRS_Power_Control]] 파라미터를 기반으로 산출됩니다.

## 인과 관계
- [[Uplink_Power_Control]] (affects) [[Power_Headroom_Report]]
- [[Power_Headroom_Report]] (triggers) [[gNB]]의 스케줄링 및 전력 할당 조정
- [[PHR_enhancement_for_dynamic_waveform_switching]] (depends_on) [[Power_Headroom_Report]]
- [[Connection_Establishment_Failure_Reporting]] (part_of) [[UE]] 보고 절차
- [[Radio_Link_Failure_Reporting]] (part_of) [[UE]] 보고 절차

## 관련 개념
- [[PUSCH_Power_Control]] (affects)
- [[PUCCH_Power_Control]] (affects)
- [[SRS_Power_Control]] (affects)
- [[Connection_Establishment_Failure_Reporting]] (part_of)
- [[Radio_Link_Failure_Reporting]] (part_of)
- [[PHR_enhancement_for_dynamic_waveform_switching]] (depends_on)
- [[Support_of_open_loop_SL_power_control_and_RSRP_report]] (depends_on)
- [[DRX_Adaptation]] (depends_on)
- [[UE_assistance_information]] (depends_on)
- [[RACH_reporting]] (depends_on)
- [[Measurement_reporting_Speed_information_upon_network_request]] (depends_on)
- [[Support_of_UL_PDCP_Packet_Average_Delay_measurement]] (depends_on)
- [[Mobility_history_information_storage]] (depends_on)
- [[Cross_RAT_RLF_Report]] (depends_on)
- [[Radio_Link_Failure_Report_for_inter_RAT_MRO_EUTRA]] (depends_on)

## 스펙 근거
- TS 38.213 §7.7: Power headroom report 일반 정의
- TS 38.213 §7.7.1: Type 1 PH report 계산식 및 절차
- TS 38.213 §7.7.2: Type 2 PH report 계산식 및 절차
- TS 38.213 §7.7.3: Type 3 PH report 계산식 및 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"