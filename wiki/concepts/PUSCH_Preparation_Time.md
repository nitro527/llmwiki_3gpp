# PUSCH Preparation Time

## 정의
[[PUSCH]] 준비 시간(Preparation procedure time)은 [[UE]]가 [[DCI]]를 수신한 시점부터 해당 [[DCI]]에 의해 스케줄링된 [[PUSCH]] 전송을 시작하기까지 필요한 최소한의 처리 시간을 의미합니다.

## 요약
[[UE]]는 [[PDCCH]]를 통해 수신한 [[DCI]] 정보를 바탕으로 [[PUSCH]] 전송을 준비합니다. 이 과정에서 [[UE]]의 처리 능력(Capability), [[BWP]] 스위칭 여부, [[Timing_Advance_Adjustment]] 등이 고려되며, 특정 조건에서는 다중 [[TB]] 처리를 위한 추가적인 능력이 요구됩니다.

## 상세 설명
[[TS_38_214]] §6.4에 따르면, [[PUSCH]] 준비 시간은 다음과 같은 요소들에 의해 결정됩니다.

- [[UE]] 처리 능력: [[UE]]는 [[Capability_1]] 또는 [[Capability_2]] 중 지원하는 처리 능력에 따라 최소 준비 시간을 산출합니다.
- [[BWP]] 스위칭: [[DCI]]가 [[BWP]] 스위칭을 포함하는 경우, [[UE]]는 스위칭에 필요한 추가 시간을 확보해야 합니다.
- 다중 [[TB]] 처리: [[UE]]는 슬롯당 다중 [[PUSCH]] 전송을 지원하기 위해 다음과 같은 기능을 선택적으로 구현할 수 있습니다.
    - 슬롯당 최대 2개, 4개, 또는 7개의 [[PUSCH]] 전송 지원 ([[Capability_1]] 및 [[Capability_2]] 기반)
    - [[CBG]] 기반 전송 시 슬롯당 최대 2개, 4개, 또는 7개의 유니캐스트 [[PUSCH]] 전송 지원
- [[Timing_Advance_Adjustment]]: [[UE]]는 [[Timing_Advance_Adjustment]]가 적용되는 경우, 이에 따른 타이밍 오프셋을 고려하여 [[PUSCH]] 전송 시점을 결정합니다.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) [[PUSCH]] 준비 절차
- [[Bandwidth_Part_Operation]] (affects) [[PUSCH]] 준비 시간
- [[Timing_Advance_Adjustment]] (affects) [[PUSCH]] 전송 타이밍
- [[UE_Capability]] (depends_on) [[PUSCH]] 준비 시간 산출 방식

## 관련 개념
- [[PUSCH]] (part_of)
- [[DCI]] (depends_on)
- [[BWP]] (affects)
- [[Timing_Advance_Adjustment]] (affects)
- [[CBG]] (affects)

## 스펙 근거
- [[TS_38_214]] §6.4: [[UE]] [[PUSCH]] 준비 절차 시간 및 관련 파라미터 정의

## 소스
- 3GPP TS 38.214 V19.0.0 (2024-03), "NR; Physical layer procedures for data"