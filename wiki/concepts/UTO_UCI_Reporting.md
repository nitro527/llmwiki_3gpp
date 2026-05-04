# UTO_UCI_Reporting

## 정의
[[UTO_UCI_Reporting]]은 [[UE]]가 [[Configured_Grant_Transmission]]을 통해 할당받은 [[PUSCH]] 자원 중 사용하지 않은 [[Transmission_Occasion]]에 대한 정보를 비트맵 형태로 [[gNB]]에 보고하는 절차를 의미합니다.

## 요약
- [필수(cap)] [[skipUplinkTxCg-r16]] 및 [[skipUplinkTxDynamic-r16]] 기능을 지원하는 [[UE]]는 상향링크 자원 효율성을 위해 사용되지 않은 [[CG-PUSCH]] 자원을 보고할 수 있습니다.
- [선택] [[UCI_indication_of_unused_CG-PUSCH_transmission_occasions]] 기능이 활성화된 경우, [[UE]]는 [[UTO-UCI]]를 생성하여 [[gNB]]에 전송합니다.
- [선택] [[CG-UCI_multiplexing_with_HARQ_ACK]] 기능을 통해 [[HARQ-ACK]] 정보와 함께 다중화될 수 있습니다.

## 상세 설명
[[UTO-UCI]] 보고는 [[UE]]가 [[Configured_Grant_Transmission]]으로 설정된 자원 중 실제 데이터 전송이 발생하지 않은 [[Transmission_Occasion]]을 식별하여 보고하는 메커니즘입니다. 

1. **비트맵 생성**: [[UE]]는 설정된 [[CG-PUSCH]] 자원들에 대해 각 [[Transmission_Occasion]]의 사용 여부를 비트맵으로 구성합니다.
2. **보고 트리거**: [[gNB]]로부터의 요청 또는 [[UE]]의 자율적인 판단에 의해 [[UTO-UCI]]가 생성됩니다.
3. **전송**: 생성된 [[UTO-UCI]]는 [[PUSCH]] 내의 [[UCI_Multiplexing_PUSCH]] 절차를 따르거나, 설정된 경우 [[PUCCH]]를 통해 전송될 수 있습니다.
4. **목적**: 이를 통해 [[gNB]]는 [[UE]]가 사용하지 않은 자원을 다른 [[UE]]에게 재할당하거나, 해당 자원을 효율적으로 관리할 수 있습니다.

## 인과 관계
- [[skipUplinkTxCg-r16]] (depends_on) [[UTO_UCI_Reporting]]
- [[UCI_indication_of_unused_CG-PUSCH_transmission_occasions]] (triggers) [[UTO_UCI_Reporting]]
- [[UTO_UCI_Reporting]] (affects) [[PUSCH_Resource_Allocation]]

## 관련 개념
- [[Configured_Grant_Transmission]] (part_of)
- [[UCI_Multiplexing_PUSCH]] (part_of)
- [[HARQ_ACK_Codebook_Determination]] (similar_to)

## 스펙 근거
- TS 38.213 §9.3.1에 따르면, [[UE]]는 상위 계층 파라미터에 의해 설정된 경우 [[CG-PUSCH]] 자원의 사용 여부를 나타내는 [[UTO-UCI]]를 보고해야 합니다.
- 해당 섹션에서는 [[UTO-UCI]]의 비트맵 구성 및 보고 타이밍에 대한 절차를 규정하고 있습니다.

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §9.3.1