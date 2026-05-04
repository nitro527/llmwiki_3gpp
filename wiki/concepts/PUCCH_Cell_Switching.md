# PUCCH_Cell_Switching

## 정의
[[PUCCH_Cell_Switching]]은 [[UE]]가 특정 [[PUCCH]] 그룹에 대해 설정된 복수의 셀 중, 실제 [[PUCCH]] 전송을 수행할 셀을 동적 또는 반정적으로 변경하는 절차를 의미합니다.

## 요약
[[PUCCH_Cell_Switching]]은 상위 계층 시그널링 또는 [[DCI]]를 통해 [[PUCCH]] 전송 셀을 전환함으로써 [[UL]] 자원 활용 효율을 높이고 간섭을 제어합니다. 이 기능은 [[UE]]의 능력(Capability)에 따라 단일 또는 두 개의 [[PUCCH]] 그룹에 대해 적용 가능하며, [[SRS]] 캐리어 스위칭 및 [[BWP]] 적응 등과 연계되어 동작합니다.

## 상세 설명
[[PUCCH_Cell_Switching]]은 [[TS 38.213]] §9.A에 정의된 절차에 따라 다음과 같은 메커니즘으로 수행됩니다.

1. 설정 및 활성화: [[UE]]는 상위 계층 파라미터를 통해 [[PUCCH]] 전송이 가능한 셀들의 집합을 할당받습니다.
2. 스위칭 방식:
   - 반정적(Semi-static) 스위칭: 상위 계층 시그널링에 의해 결정된 규칙에 따라 [[PUCCH]] 전송 셀이 변경됩니다.
   - 동적(Dynamic) 스위칭: [[DCI]] 내의 필드를 통해 [[PUCCH]] 전송 셀을 실시간으로 지시받습니다. 이는 동일한 길이 또는 서로 다른 길이의 중첩된 [[PUCCH]] 슬롯/서브슬롯 환경에서 적용됩니다.
3. 그룹 관리: [[UE]]는 단일 [[PUCCH]] 그룹 또는 두 개의 [[PUCCH]] 그룹에 대해 독립적으로 스위칭을 수행할 수 있습니다.
4. 연동 동작: [[PUCCH_Cell_Switching]] 수행 시 [[SRS]] 캐리어 스위칭, [[BWP]] 적응, 다중 셀 간의 [[Joint_search_space_group_switching]] 등과 조화를 이루어야 합니다.

## 인과 관계
- [[PUCCH_Cell_Switching]] depends_on [[UE]]의 능력(Capability)에 따른 기능 지원 여부
- [[PUCCH_Cell_Switching]] triggers [[PUCCH]] 전송 경로의 변경 및 관련 [[Uplink_Power_Control]] 파라미터 재설정
- [[PUCCH_Cell_Switching]] affects [[PUCCH_Resource_Determination]] 및 [[UCI_Multiplexing_PUCCH]] 수행 시점

## 관련 개념
- [[PUCCH]] (part_of)
- [[DCI]] (triggers)
- [[SRS_Carrier_Switching]] (similar_to)
- [[Bandwidth_Part_Operation]] (affects)
- [[Uplink_Power_Control]] (affects)

## 스펙 근거
- TS 38.213 §9.A: [[PUCCH]] 셀 스위칭 절차 및 동작 정의
- TS 38.822: 관련 [[UE]] 기능(Feature) 25-9, 25-9a, 25-10, 25-10a, 25-10b, 25-10c, 2-56, 4-27, 6-4, 6-19, 9-3, 10-9c 정의

## 소스
- 3GPP TS 38.213 Release 18 (i80)
- 3GPP TS 38.822 (UE Feature list)