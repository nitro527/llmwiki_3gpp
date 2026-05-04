# UCI_Multiplexing_PUCCH

## 정의
[[UCI_Multiplexing_PUCCH]]는 [[UE]]가 [[Slot]] 내에서 서로 다른 유형의 [[UCI]] ([[HARQ-ACK]], [[SR]], [[CSI]])를 하나의 [[PUCCH]] 자원에 결합하여 전송하거나, 시간적으로 중첩된 자원 간의 우선순위를 결정하여 처리하는 절차를 의미합니다.

## 요약
[[UE]]는 상위 계층 설정에 따라 [[HARQ-ACK]], [[SR]], [[CSI]]를 동일한 [[PUCCH]] 자원 내에서 멀티플렉싱하거나, 우선순위 규칙에 따라 특정 정보를 선택적으로 전송합니다. 이 과정은 [[Slot]] 내의 시작 심볼 위치와 [[UCI]]의 우선순위, 그리고 [[Sidelink]]와 [[Uplink]] 간의 충돌 여부에 따라 결정됩니다.

## 상세 설명
[[UCI_Multiplexing_PUCCH]] 절차는 다음과 같은 핵심 메커니즘을 포함합니다.

1. **우선순위 결정**: [[SL]] [[HARQ-ACK]] 정보와 [[DL]] [[HARQ-ACK]], [[SR]], [[CSI]]가 동일한 [[PUCCH]] 자원에서 충돌할 경우, [[TS 38.213]] §9.2.5.0에 정의된 우선순위 규칙에 따라 처리합니다.
2. **멀티플렉싱 절차**:
   - [[HARQ-ACK]] 또는 [[CSI]]와 [[SR]]이 동일한 [[PUCCH]] 자원에 할당된 경우, [[TS 38.213]] §9.2.5.1에 따라 결합합니다.
   - [[HARQ-ACK]], [[SR]], [[CSI]]가 동시에 보고되어야 할 경우, [[TS 38.213]] §9.2.5.2에 따라 하나의 [[PUCCH]] 자원으로 멀티플렉싱합니다.
3. **우선순위 기반 보고**: 서로 다른 우선순위를 가진 [[UCI]]가 충돌할 경우, [[TS 38.213]] §9.2.5.3에 따라 높은 우선순위의 [[UCI]]를 우선적으로 전송합니다.
4. **SPS PDSCH 지연**: [[SPS]] [[PDSCH]]에 대한 [[HARQ-ACK]] 보고가 다른 [[UCI]]와 충돌하여 전송이 불가능할 경우, [[TS 38.213]] §9.2.5.4에 따라 보고를 지연할 수 있습니다.

## 인과 관계
- [[UCI_Bit_Sequence_Generation]] (depends_on): 멀티플렉싱된 [[UCI]] 비트 시퀀스를 생성하기 위해 선행되어야 합니다.
- [[UCI_Channel_Coding]] (depends_on): 멀티플렉싱된 정보를 채널 코딩하기 위해 필요합니다.
- [[PUCCH_Resource_Determination]] (affects): 멀티플렉싱 결과에 따라 최종적으로 사용할 [[PUCCH]] 자원이 결정됩니다.

## 관련 개념
- [[HARQ-ACK]] (part_of)
- [[SR]] (part_of)
- [[CSI]] (part_of)
- [[PUCCH]] (part_of)
- [[Slot]] (part_of)
- [[Sidelink]] (depends_on)

## 스펙 근거
- [[TS 38.213]] §9.2.5: UE procedure for reporting multiple UCI types
- [[TS 38.213]] §9.2.5.0: UE procedure for prioritization between SL HARQ-ACK information in a PUCCH and DL HARQ-ACK or SR or CSI in a PUCCH
- [[TS 38.213]] §9.2.5.1: UE procedure for multiplexing HARQ-ACK or CSI and SR in a PUCCH
- [[TS 38.213]] §9.2.5.2: UE procedure for multiplexing HARQ-ACK/SR/CSI in a PUCCH
- [[TS 38.213]] §9.2.5.3: UE procedure for reporting UCI of different priorities
- [[TS 38.213]] §9.2.5.4: UE procedure for deferring HARQ-ACK for SPS PDSCH
- [[TS 38.822]] Feature 4-19, 4-19a, 4-19b, 4-19c, 4-2, 4-28, 10-35, 10-35a, 10-35b, 10-35c, 10-36, 11-3g

## 소스
- 3GPP TS 38.213 Release 18 (v18.0.0)