# PUCCH_Resource_Determination

## 정의
[[PUCCH]] 자원 결정은 [[UE]]가 상위 계층으로부터 설정받은 자원 집합 내에서, 전송해야 할 [[UCI]]의 종류, 우선순위, 그리고 [[HARQ-ACK]] 코드북 크기 등에 따라 실제 전송에 사용할 자원을 선택하는 절차를 의미한다.

## 요약
[[PUCCH]] 자원 결정은 [[UCI]]의 우선순위와 다중화 요구사항에 따라 수행된다. [[UE]]는 [[HARQ-ACK]], [[SR]], [[CSI]]를 단일 또는 다중 [[PUCCH]] 자원에 매핑하며, 필요 시 [[PUSCH]]로 피기백(piggyback)하거나 우선순위가 낮은 정보를 생략하는 절차를 거친다.

## 상세 설명
[[PUCCH]] 자원 결정 절차는 다음과 같은 단계로 구성된다.

1. **자원 집합 선택**: [[UE]]는 전송할 [[UCI]] 비트 수와 [[PUCCH]] 포맷에 따라 [[PUCCH_Resource_Sets]]에서 적절한 자원 집합을 결정한다.
2. **우선순위 기반 결정**: 서로 다른 우선순위를 가진 [[UCI]]가 충돌할 경우, [[UCI_Reporting_Different_Priorities]] 절차에 따라 높은 우선순위의 정보를 우선적으로 전송한다.
3. **다중화 절차**:
   - [[HARQ-ACK]], [[SR]], [[CSI]]가 동일한 슬롯 내에서 전송되어야 할 경우, [[UCI_Multiplexing_PUCCH]]를 통해 단일 [[PUCCH]] 자원으로 결합된다.
   - 특정 조건(예: 동일한 시작 심볼) 하에서 다중화가 수행되며, [[UE]]의 능력(Capability)에 따라 다중화 횟수나 방식이 제한될 수 있다.
4. **[[SPS]] HARQ-ACK 지연**: [[SPS_HARQ_Deferral]] 절차에 따라 [[TDD]] 충돌 등의 상황에서 [[HARQ-ACK]] 전송이 지연될 수 있다.
5. **[[PUSCH]] 피기백**: [[PUCCH]] 자원이 부족하거나 [[PUSCH]]와 전송 시점이 겹치는 경우, [[UCI_Multiplexing_PUSCH]]를 통해 [[PUSCH]] 상에서 [[UCI]]를 전송한다.

## 인과 관계
- [[UCI_Multiplexing_PUCCH]] (depends_on) [[PUCCH_Resource_Determination]]
- [[UCI_Reporting_Different_Priorities]] (affects) [[PUCCH_Resource_Determination]]
- [[PUCCH_Resource_Sets]] (part_of) [[PUCCH_Resource_Determination]]
- [[SPS_HARQ_Deferral]] (triggers) [[PUCCH_Resource_Determination]]

## 관련 개념
- [[PUCCH]] (part_of)
- [[HARQ-ACK]] (depends_on)
- [[SR]] (depends_on)
- [[CSI]] (depends_on)
- [[PUSCH]] (similar_to)

## 스펙 근거
- TS 38.213 §9.2에 따르면 [[PUCCH]]를 통한 [[UCI]] 보고 절차가 정의된다.
- TS 38.213 §9.2.1은 [[PUCCH_Resource_Sets]] 구성을 명시한다.
- TS 38.213 §9.2.5.0~9.2.5.4는 [[UCI]] 다중화, 우선순위 처리 및 [[SPS]] 지연 절차를 규정한다.
- TS 38.822의 Feature 4-19, 4-19a, 4-19b, 4-19c, 4-28, 10-35, 10-35a, 10-35b, 10-35c, 10-36, 11-3g, 25-1은 [[UE]]의 [[PUCCH]]/[[PUSCH]] 다중화 능력 및 [[SPS]] 지연 관련 기능을 정의한다.

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18)
- 3GPP TS 38.822 (UE Features)