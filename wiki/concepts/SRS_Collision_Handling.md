# SRS_Collision_Handling

## 정의
[[SRS]]와 다른 상향링크 채널 또는 신호([[PUCCH]], [[PUSCH]], [[PRACH]], [[MsgA]]) 간에 시간 자원이 중첩되어 동시 전송이 불가능할 때, [[UE]]가 우선순위에 따라 특정 전송을 수행하거나 드롭(drop)하는 절차를 의미합니다.

## 요약
[[SRS]] 전송은 [[UE]]의 능력(capability) 및 설정된 전력 제어 파라미터에 따라 다른 채널과의 동시 전송 여부가 결정됩니다. 충돌 발생 시, [[UE]]는 상위 계층 설정 및 물리 계층 우선순위 규칙에 따라 [[SRS]]를 드롭하거나, 전송 전력을 조정하거나, 혹은 다중 채널을 동시에 전송합니다.

## 상세 설명
[[SRS]] 충돌 처리는 주로 [[UE]]의 상향링크 전송 능력과 관련이 있습니다.

1. **필수(항상) 및 필수(cap) 기능**:
   - [[Uplink_Power_Control]] (8-3)은 모든 [[UE]]가 준수해야 하는 기본 동작으로, [[SRS]]와 타 채널 간 전력 분배 및 우선순위 결정의 근간이 됩니다.
   - [[Active_spatial_relations]] (2-60)은 [[SRS]] 전송 시 사용되는 빔포밍 및 공간적 설정이 타 채널과 충돌할 경우, 이를 어떻게 처리할지에 대한 제약 조건을 제공합니다.

2. **선택적 기능**:
   - [[Parallel_PRACH_and_SRS_PUCCH_PUSCH_transmissions_across_CCs_in_inter_band_CA]] (4-26) 및 [[Parallel_MsgA_and_SRS_PUCCH_PUSCH_transmissions_across_CCs_in_inter_band_CA]] (9-3) 등은 서로 다른 대역 간(inter-band) CA 환경에서 [[SRS]]와 [[PRACH]] 또는 [[MsgA]]의 동시 전송 가능 여부를 정의합니다.
   - [[Parallel_SRS_and_PUCCH_PUSCH_transmission_across_CCs_in_inter_band_CA]] (4-25)는 [[SRS]]와 [[PUCCH]]/[[PUSCH]]의 동시 전송을 지원하기 위한 능력 기반 규칙을 포함합니다.
   - [[Simultaneous_transmission_of_SRS_on_an_SUL_non_SUL_carrier_and_PUSCH_PUCCH_SRS_on_the_other_UL_carrier_in_the_same_cell]] (6-19)은 [[Supplemental_uplink]] (6-16) 환경에서 동일 셀 내 타 캐리어와의 동시 전송을 다룹니다.
   - [[Enable_configured_UL_transmissions_when_SFI_field_in_DCI_2_0_is_configured_but_DCI_2_0_is_not_detected]] (10-25)는 동적 슬롯 포맷 표시가 없을 경우의 기본 동작을 규정합니다.

3. **주파수 호핑 및 캐리어 스위칭**:
   - [[SRS_frequency_hopping_procedure]]는 [[SRS]] 전송 시 자원 할당의 유연성을 제공하며, 충돌 시 주파수 도메인에서의 회피 전략을 결정하는 요소가 됩니다.
   - [[SRS_carrier_switching]]은 캐리어 간 스위칭이 필요한 경우의 타이밍과 충돌 처리 우선순위를 결정합니다.

## 인과 관계
- [[Uplink_Power_Control]] (depends_on) [[SRS_Collision_Handling]]
- [[SRS_carrier_switching]] (triggers) [[SRS_Collision_Handling]]
- [[Active_spatial_relations]] (affects) [[SRS_Collision_Handling]]

## 관련 개념
- [[SRS]] (part_of)
- [[PUCCH]] (similar_to)
- [[PUSCH]] (similar_to)
- [[PRACH]] (similar_to)
- [[PUSCH_MsgA_Transmission]] (similar_to)

## 스펙 근거
- TS 38.214 §6.2.1.1: [[UE]] [[SRS]] 주파수 호핑 절차 정의
- TS 38.214 §6.2.1.3: 컴포넌트 캐리어 간 [[UE]] 사운딩 절차 및 충돌 처리 관련 규정
- TS 38.822: 관련 [[UE]] 기능(Feature) 우선순위 및 능력 정의

## 소스
- 3GPP TS 38.214 (Release 16/17/18)
- 3GPP TS 38.822 (UE Feature List)