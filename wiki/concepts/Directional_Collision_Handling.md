# Directional_Collision_Handling

## 정의
[[Directional_Collision_Handling]]은 다중 서빙 셀 환경에서 서로 다른 상향링크(UL) 및 하향링크(DL) 전송 방향이 시간적으로 중첩될 때, [[UE]]가 전송 우선순위를 결정하고 충돌을 회피하기 위해 수행하는 물리 계층 절차를 의미합니다.

## 요약
본 절차는 [[TS 38.213]]에 정의된 다양한 제어 시그널링을 통해 [[Slot]] 포맷을 구성하고, 전송 방향이 충돌하는 경우 우선순위 규칙에 따라 특정 전송을 취소하거나 조정함으로써 시스템의 안정적인 운용을 보장합니다. 특히 [[Slot_Format_Configuration]] 및 [[Cancellation_indication]] 등을 활용하여 동적인 자원 관리를 수행합니다.

## 상세 설명
[[Directional_Collision_Handling]]은 다음과 같은 메커니즘을 통해 수행됩니다.

1. [[Slot_Format_Configuration]]: [[UE]]는 상위 계층 시그널링 및 [[DCI]]를 통해 각 [[Slot]]의 심볼이 DL, UL, 또는 Flexible로 구성되는지 확인합니다.
2. [[Cancellation_indication]]: 네트워크는 [[INT-RNTI]]를 사용하는 [[PDCCH]]를 통해 특정 자원 영역에서의 전송을 중단하도록 지시할 수 있습니다. 이는 전송 방향 충돌이 예상되는 상황에서 우선순위가 낮은 전송을 즉시 취소하는 데 사용됩니다.
3. [[SRS_switching]]: 서로 다른 주파수 대역이나 셀 간의 [[SRS]] 전송 시 발생하는 스위칭 시간 제약으로 인한 충돌을 관리합니다.
4. [[Adaptation_of_cell_operation]]: 네트워크는 셀 간의 전송 방향 불일치를 해소하기 위해 동적으로 셀 운용 방식을 적응시킵니다.

## 인과 관계
- [[Slot_Format_Configuration]] (affects) [[Directional_Collision_Handling]]
- [[Cancellation_indication]] (affects) [[Directional_Collision_Handling]]
- [[SRS_switching]] (depends_on) [[Directional_Collision_Handling]]
- [[Adaptation_of_cell_operation]] (triggers) [[Directional_Collision_Handling]]

## 관련 개념
- [[Slot_Format_Configuration]] (part_of)
- [[Cancellation_indication]] (part_of)
- [[SRS_switching]] (part_of)
- [[Adaptation_of_cell_operation]] (part_of)
- [[PDCCH]] (depends_on)
- [[UE]] (affects)

## 스펙 근거
- [[TS 38.213]] §11.1에 따르면 [[UE]]는 [[Slot]] 포맷을 결정하기 위한 절차를 수행해야 합니다.
- [[TS 38.213]] §11.2A에 따르면 [[Cancellation_indication]]을 통한 전송 취소 절차가 정의됩니다.
- [[TS 38.213]] §11.4에 따르면 [[SRS]] 스위칭과 관련된 충돌 회피 절차가 명시되어 있습니다.
- [[TS 38.213]] §11.5에 따르면 셀 운용의 적응을 통한 충돌 관리 절차가 기술되어 있습니다.

## 소스
- 3GPP TS 38.213 "NR; Physical layer procedures for control" (Release 18)