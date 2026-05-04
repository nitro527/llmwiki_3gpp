# PDSCH_Reception_Preparation_Time

## 정의
[[PDSCH]] 수신 준비 시간은 [[UE]]가 [[PDCCH]]를 통해 [[PDSCH]] 스케줄링 정보를 수신한 시점부터, 해당 [[PDSCH]]의 첫 번째 심볼을 수신하기 위해 필요한 최소한의 처리 시간을 의미합니다. 특히 [[PDCCH]]와 [[PDSCH]]가 서로 다른 [[Frame_Structure_Numerology]]를 가지는 환경에서의 시간 제약 조건을 다룹니다.

## 요약
본 절차는 [[UE]]가 서로 다른 [[Subcarrier_Spacing]]을 가진 [[PDCCH]]와 [[PDSCH]]를 수신할 때, [[PDSCH]] 수신을 준비하기 위해 요구되는 최소 시간인 $N_{pdsch}$를 결정하는 메커니즘을 정의합니다. 이는 [[UE]]의 처리 능력과 [[PDCCH]]/[[PDSCH]] 간의 뉴머롤로지 차이에 따라 결정됩니다.

## 상세 설명
[[TS_38_214]] §5.5에 따르면, [[UE]]가 [[PDCCH]]를 수신한 슬롯과 [[PDSCH]]가 스케줄링된 슬롯의 [[Subcarrier_Spacing]]이 다를 경우, [[PDSCH]] 수신 준비 시간은 다음과 같이 결정됩니다.

1. **기본 요구사항**: [[UE]]는 [[Basic_PDSCH_reception]] 및 [[Basic_scheduling_HARQ_operation]]을 항상 지원해야 하며, [[PDSCH_beam_switching]] 능력 또한 필수적으로 고려해야 합니다.
2. **뉴머롤로지 차이**: [[PDCCH]]의 [[Subcarrier_Spacing]]($\mu_{PDCCH}$)과 [[PDSCH]]의 [[Subcarrier_Spacing]]($\mu_{PDSCH}$)이 다른 경우, [[UE]]는 더 큰 [[Subcarrier_Spacing]]을 기준으로 하는 처리 시간 요구사항을 준수해야 합니다.
3. **선택적 기능 지원**: [[UE]]는 [[Up_to_2_unicast_PDSCHs_per_slot_per_CC_for_different_TBs_for_UE_processing_time_Capability_1]] 등 다중 [[PDSCH]] 수신 능력이나 [[PDSCH_repetitions_over_multiple_slots]], [[Separation_of_two_unicast_PDSCHs_with_a_gap]]과 같은 고급 스케줄링 기능을 지원할 수 있습니다.
4. **타이밍 결정**: [[Non_numerical_PDSCH_to_HARQ_ACK_timing]]이 적용되는 경우를 포함하여, [[UE]]는 스케줄링 [[DCI]]의 마지막 심볼 이후부터 [[PDSCH]]의 첫 번째 심볼까지의 시간이 $N_{pdsch}$ 이상이 되도록 보장해야 합니다.

## 인과 관계
- [[PDCCH_Monitoring_Procedures]] (triggers) [[PDSCH]] 수신 준비 시간 계산
- [[Frame_Structure_Numerology]] (affects) $N_{pdsch}$ 값 결정
- [[PDSCH_Reception_Procedures]] (depends_on) [[PDSCH_Reception_Preparation_Time]]

## 관련 개념
- [[PDSCH]] (part_of)
- [[PDCCH]] (part_of)
- [[Frame_Structure_Numerology]] (affects)
- [[Basic_PDSCH_reception]] (depends_on)
- [[Basic_scheduling_HARQ_operation]] (depends_on)
- [[PDSCH_beam_switching]] (depends_on)
- [[PDSCH_repetitions_over_multiple_slots]] (similar_to)
- [[Non_numerical_PDSCH_to_HARQ_ACK_timing]] (affects)

## 스펙 근거
- [[TS_38_214]] §5.5: [[PDCCH]]와 [[PDSCH]] 간 서로 다른 [[Subcarrier_Spacing]] 환경에서의 [[PDSCH]] 수신 준비 시간 요구사항 정의

## 소스
- 3GPP TS 38.214 V17.9.0, "NR; Physical layer procedures for data"