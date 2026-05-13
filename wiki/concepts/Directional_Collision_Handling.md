# Directional_Collision_Handling

## 정의
[[Directional_Collision_Handling]]은 다중 서빙 셀 환경에서 TDD(Time Division Duplex) 설정에 따른 상향링크(UL) 및 하향링크(DL) 심볼 간의 충돌을 해결하기 위해, 특정 우선순위 규칙에 따라 전송 또는 수신 동작을 결정하는 절차를 의미한다.

## 요약
본 기능은 다중 셀 환경에서 서로 다른 셀 간의 TDD 설정이 충돌할 때, UE가 반이중(Half-duplex) 동작을 수행해야 하는 경우 전송/수신 우선순위를 결정한다. 특히 [[SRS]] 스위칭과 연계된 동작 및 다중 셀 간의 방향성 충돌을 해결하기 위해 참조 셀(Reference Cell)을 설정하고, 상위 계층 설정 및 DCI 기반의 동적 스케줄링 간의 충돌을 방지하는 메커니즘을 제공한다.

## 상세 설명
TS 38.213 §11.1에 따라, 다중 셀 환경에서 directionalCollisionHandling-r16이 활성화된 경우 UE는 다음과 같은 절차를 수행한다.

1. 참조 셀 결정: UE는 활성 셀 중 가장 작은 셀 인덱스를 가진 셀을 참조 셀로 결정한다. 이때 simultaneousRxTxInterBandCA 능력에 따라 대역별 또는 전체 셀 중 하나를 선택한다.
2. 심볼 방향성 판단: 
   - tdd-UL-DL-ConfigurationCommon 또는 tdd-UL-DL-ConfigurationDedicated에 의해 명시된 방향을 따른다.
   - 유연한(Flexible) 심볼의 경우, 상위 계층에 의해 [[SRS]], [[PUCCH]], [[PUSCH]], [[PRACH]]가 설정되면 UL로, [[PDCCH]], [[PDSCH]], [[CSI_RS]]가 설정되면 DL로 간주한다.
3. 충돌 해결 규칙:
   - 참조 셀과 다른 셀 간의 방향이 상충할 경우, 참조 셀의 설정을 우선하거나 특정 조건에서 유연하게 동작한다.
   - 동일 대역 내에서는 참조 셀의 방향이 우선시되며, 다른 대역인 경우 DCI에 의한 동적 스케줄링이 상위 계층 설정보다 우선할 수 있다.
   - UE는 참조 셀의 UL/DL 설정과 다른 셀의 DCI 스케줄링이 충돌하지 않도록 보장해야 한다.

또한, TS 38.214 §6.2.1.3에 따라 [[SRS]] 스위칭이 포함된 경우, UE는 먼저 SRS 관련 우선순위/드롭 규칙을 적용한 후, 본 절차를 적용한다.

## 인과 관계
- [[SRS_Switching]] depends_on [[Directional_Collision_Handling]] (SRS 스위칭 시 충돌 해결 절차 선행)
- [[Slot_Format_Configuration]] affects [[Directional_Collision_Handling]] (슬롯 포맷 설정이 충돌 판단의 기준이 됨)
- [[Carrier_Aggregation]] triggers [[Directional_Collision_Handling]] (다중 셀 환경에서 TDD 충돌 발생 시 동작)

## 관련 개념
- [[Slot_Format_Configuration]] (affects)
- [[SRS_Switching]] (depends_on)
- [[Carrier_Aggregation]] (triggers)
- [[PDCCH]] (affects)
- [[PUSCH]] (affects)
- [[PUCCH]] (affects)
- [[SRS]] (affects)

## 스펙 근거
- TS 38.213 §11.1: Slot configuration 및 다중 셀 방향성 충돌 해결 절차
- TS 38.214 §6.2.1.3: SRS 스위칭 시 우선순위 및 충돌 해결 규칙

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18)
- 3GPP TS 38.214 v19.0.0 (Release 19)