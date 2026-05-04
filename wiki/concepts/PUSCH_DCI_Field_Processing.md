# PUSCH_DCI_Field_Processing

## 정의
[[PUSCH]]_DCI_Field_Processing은 [[PDCCH]]를 통해 전달되는 [[DCI]] format 0_3의 각 필드를 해석하여 [[UE]]가 상향링크 데이터 전송을 수행하기 위한 파라미터를 결정하는 절차를 의미한다.

## 요약
DCI format 0_3은 고도로 최적화된 [[PUSCH]] 스케줄링을 위해 설계되었으며, [[SRI]], [[TPMI]], 안테나 포트, [[SRS]] 요청, 전력 제어 등 다양한 제어 정보를 포함한다. 본 절차는 TS 38.212 §7.3.1.1.4에 정의된 필드들을 기반으로 물리 계층 파라미터를 설정한다.

## 상세 설명
DCI format 0_3은 [[PUSCH]] 전송을 스케줄링하기 위해 사용되며, 다음과 같은 주요 필드 처리를 포함한다.

*   [[SRI]] (Sounding Reference Signal Resource Indicator): 상향링크 전송에 사용할 공간적 관계(Spatial Relation)를 결정하기 위해 사용된다.
*   [[TPMI]] (Transmitted Precoding Matrix Indicator): 코드북 기반 전송 시 사용할 프리코딩 행렬을 지시한다.
*   안테나 포트(Antenna Ports): [[DMRS]] 전송을 위한 포트 구성 및 레이어 수를 결정한다.
*   [[SRS]] 요청(SRS Request): 비주기적 [[SRS]] 전송을 트리거한다.
*   전력 제어(TPC Command): [[PUSCH_Power_Control]]을 위한 폐루프 전력 조정 값을 제공한다.
*   [[Configurable_Type-1A_fields_for_DCI_format_0_3/1_3]]: 특정 필드의 비트 폭이나 구성을 RRC 설정을 통해 유연하게 변경할 수 있다.

또한, 다음의 UE 기능들이 본 처리 과정에 영향을 미친다.
*   [[Active_spatial_relations]] (2-60): 필수 기능으로, SRI를 통해 지시된 공간적 설정을 활성화한다.
*   [[UL_intra-UE_multiplexing/prioritization_of_overlapping_channel/signals_with_two_priority_levels_in_physical_layer]] (12-1): 우선순위가 다른 채널 간의 충돌 발생 시 처리 방식을 결정한다.
*   [[Second_TPC_field_for_Multi-TRP_PUSCH_repetition]] (23-3-1b): 다중 TRP 환경에서 개별적인 전력 제어를 수행한다.
*   [[UL_cancelation_scheme_for_self-carrier]] (11-7) 및 [[UL_cancelation_scheme_for_cross-carrier]] (11-7a): 스케줄링된 PUSCH의 취소 여부를 판단한다.
*   [[Enable_configured_UL_transmissions_when_SFI_field_in_DCI_2_0_is_configured_but_DCI_2_0_is_not_detected]] (10-25): SFI 미검출 시의 동작을 정의한다.
*   [[Advanced_UE_capability_for_larger_number_of_unicast_UL_DCI]] (49-3y): 더 많은 DCI 수용을 위한 확장 기능을 제공한다.
*   [[DL_priority_indication_in_DCI_with_mixed_DCI_formats]] (11-4b) 및 [[UL_priority_indication_in_DCI_with_mixed_DCI_formats]] (12-1a): 우선순위 지시자를 처리한다.
*   [[Cross_Slot_Scheduling]] (19-2): 스케줄링된 슬롯과 전송 슬롯 간의 오프셋을 처리한다.
*   [[For_type_1_CSS_with_dedicated_RRC_configuration,_type_3_CSS,_and_UE-SS,_monitoring_occasion_can_be_any_OFDM_symbol(s)_of_a_slot_for_Case_2_with_a_DCI_gap_and_constrained_timeline_for_SRS_for_CB_PUSCH]] (22-8c): 모니터링 오케이션의 유연성을 제공한다.

## 인과 관계
*   [[DCI]] 수신 (triggers) [[PUSCH]]_DCI_Field_Processing
*   [[PUSCH]]_DCI_Field_Processing (affects) [[PUSCH_Transmission_Parameters]]
*   [[PUSCH]]_DCI_Field_Processing (depends_on) [[Active_spatial_relations]]

## 관련 개념
*   [[DCI_Formats_Processing]] (part_of)
*   [[PUSCH_Transmission_Parameters]] (depends_on)
*   [[PUSCH_Power_Control]] (affects)
*   [[SRS_Generation_Mapping]] (affects)

## 스펙 근거
*   TS 38.212 §7.3.1.1.1: DCI format 0_0 정의
*   TS 38.212 §7.3.1.1.2: DCI format 0_1 정의
*   TS 38.212 §7.3.1.1.3: DCI format 0_2 정의
*   TS 38.212 §7.3.1.1.4: DCI format 0_3 정의

## 소스
*   3GPP TS 38.212 V18.0.0 (2024-03) "NR; Multiplexing and channel coding"