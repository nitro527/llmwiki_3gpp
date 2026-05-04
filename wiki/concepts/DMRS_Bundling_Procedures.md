# DMRS_Bundling_Procedures

## 정의
[[DMRS]] 번들링 절차는 [[PUSCH]] 또는 [[PUCCH]] 전송 시, 연속적이거나 비연속적인 다수의 전송 구간에 걸쳐 [[Reference_Signals]]의 위상 연속성(Phase Continuity) 및 전력 일관성(Power Consistency)을 유지하여 채널 추정 성능을 향상시키기 위한 절차를 의미한다.

## 요약
[[DMRS]] 번들링은 UE가 시간 도메인 윈도우(Time Domain Window, TDW) 내에서 전송되는 신호들에 대해 일관된 채널 상태를 가정할 수 있도록 지원한다. 이를 위해 Nominal TDW와 Actual TDW를 결정하며, 해당 윈도우 내에서 UE는 위상과 전력의 일관성을 보장해야 한다. 본 기능은 특정 [[UE_Feature_Priority]]를 만족하는 단말에 의해 지원된다.

## 상세 설명
[[DMRS]] 번들링 절차는 다음과 같은 핵심 요소로 구성된다.

1. **UE Feature 지원**: 
   - [필수(cap)] [[HARQ_ACK_Codebook_Determination]]을 위한 [[PUCCH]] 또는 [[PUSCH]]의 공간적 번들링(Spatial Bundling).
   - [필수(cap)] [[PUCCH_Spatial_Setting]]을 위한 활성 공간 관계(Active Spatial Relations).
   - [필수(cap)] SR/[[HARQ_ACK]]/[[CSI_Reporting_Procedures]] 다중화 절차.
   - [선택] 최대 [[DMRS]] 번들링 지속 시간, [[PUCCH_Repetition]]을 위한 번들링, 향상된 인터 슬롯 주파수 호핑, 비연속적 전송(Non-back-to-back)을 위한 번들링, NGSO 시나리오에서의 NTN [[PUSCH]] 번들링, [[PUCCH]]를 통한 반-영구적 빔 보고 및 [[CSI_Reporting_Procedures]] 보고.

2. **TDW 결정**: 
   - Nominal TDW: 상위 계층 파라미터에 의해 설정된 시간 범위로, 번들링이 적용될 수 있는 이론적 최대 범위를 정의한다.
   - Actual TDW: 실제 전송되는 [[PUSCH]] 또는 [[PUCCH]] 자원들이 시간적으로 연속적이거나, 특정 조건을 만족하여 번들링이 가능한 실제 구간을 의미한다.

3. **위상 및 전력 일관성**: 
   - 번들링 윈도우 내에서 UE는 전송되는 [[DMRS]]의 위상과 전력을 일정하게 유지해야 한다. 이를 통해 기지국(gNB)은 다수의 슬롯에 걸쳐 수신된 [[DMRS]]를 결합하여 채널 추정의 정확도를 높일 수 있다.

## 인과 관계
- [[DMRS]] 번들링 절차는 [[PUSCH_Transmission_Procedures]] 및 [[PUCCH_Repetition]]의 성능을 향상시킨다.
- [[PUCCH_Spatial_Setting]] 및 [[Active_Spatial_Relations]]의 설정은 번들링 가능 여부를 결정하는 주요 요인이다.
- [[DMRS]] 번들링은 [[Channel_Estimation]]의 정확도를 높여 결과적으로 [[HARQ_ACK_Codebook_Determination]]의 신뢰성을 높인다.

## 관련 개념
- [[DMRS]] (part_of)
- [[PUSCH]] (affects)
- [[PUCCH]] (affects)
- [[PUCCH_Repetition]] (depends_on)
- [[Channel_Estimation]] (triggers)
- [[HARQ_ACK_Codebook_Determination]] (depends_on)

## 스펙 근거
- TS 38.214 §6.1.7에 따르면, UE는 상위 계층 파라미터에 기반하여 [[DMRS]] 번들링을 위한 시간 도메인 윈도우를 결정한다.
- TS 38.822에 명시된 [[UE_Feature_Priority]] 항목(4-12, 30-4, 30-4d, 30-4f, 30-4h, 44-2, 2-23, 2-32a, 2-60, 4-19, 4-19a, 4-19b)은 본 절차의 구현 및 지원 범위를 정의한다.

## 소스
- 3GPP TS 38.214 "Physical layer procedures for data"
- 3GPP TS 38.822 "UE features"