# Dual Connectivity Power Control

## 정의
[[Dual Connectivity]] 환경에서 [[UE]]가 서로 다른 셀 그룹(Master Cell Group 및 Secondary Cell Group)에 동시에 전송할 때, 전체 전송 전력을 규정된 한계치 내에서 효율적으로 분배하고 제어하는 절차를 의미합니다.

## 요약
[[Dual Connectivity]] 구성 시 [[UE]]는 각 셀 그룹별로 할당된 전송 전력 한계 내에서 동작해야 합니다. TS 38.213 §7.6에 따라 [[EN-DC]], [[NE-DC]], [[NR-DC]] 각 시나리오별로 전력 공유 및 우선순위 결정 메커니즘이 정의되어 있으며, 이를 통해 [[UE]]의 최대 전송 전력 제한을 준수합니다.

## 상세 설명
[[Dual Connectivity]] 환경에서의 전력 제어는 다음과 같은 원칙을 따릅니다.

- [[EN-DC]] (E-UTRA-NR Dual Connectivity): [[UE]]는 E-UTRA 셀 그룹과 NR 셀 그룹 간의 전력 공유를 수행합니다. TS 38.213 §7.6.1에 따라, [[UE]]는 상위 계층에서 설정된 파라미터와 각 RAT(Radio Access Technology)의 전력 요구사항을 고려하여 전력을 배분합니다.
- [[NE-DC]] (NR-E-UTRA Dual Connectivity): NR이 마스터, E-UTRA가 세컨더리인 경우로, TS 38.213 §7.6.1A에 정의된 절차에 따라 전력을 제어합니다.
- [[NR-DC]] (NR-NR Dual Connectivity): 두 개의 NR 셀 그룹(MCG와 SCG) 간의 전력 제어를 수행합니다. TS 38.213 §7.6.2에 따라, [[UE]]는 각 셀 그룹의 전력 한계 내에서 [[Uplink Power Control]]을 수행하며, 필요 시 전력 우선순위 규칙에 따라 전송 전력을 조정합니다.

## 인과 관계
- [[Uplink Power Control]] (affects) [[Dual Connectivity Power Control]]
- [[Dual Connectivity]] (triggers) [[Dual Connectivity Power Control]]
- [[Uplink Power Prioritization]] (depends_on) [[Dual Connectivity Power Control]]

## 관련 개념
- [[Uplink Power Control]] (depends_on)
- [[Dual Connectivity]] (part_of)
- [[Uplink Power Prioritization]] (affects)

## 스펙 근거
- TS 38.213 §7.6: Dual connectivity 전력 제어 일반 요구사항
- TS 38.213 §7.6.1: EN-DC 환경의 전력 공유 절차
- TS 38.213 §7.6.1A: NE-DC 환경의 전력 공유 절차
- TS 38.213 §7.6.2: NR-DC 환경의 전력 공유 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"