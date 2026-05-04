# Bandwidth Part Operation

## 정의
[[Bandwidth_Part_Operation]]은 5G NR 시스템에서 UE가 전체 시스템 대역폭 내의 일부 주파수 자원만을 사용하여 통신할 수 있도록 하는 동적 자원 관리 메커니즘을 의미합니다.

## 요약
UE는 RRC 설정을 통해 하나 이상의 [[Bandwidth_Part]] (BWP)를 구성받으며, 특정 시점에는 하나의 DL BWP와 하나의 UL BWP만이 활성화되어 동작합니다. BWP 전환은 [[DCI]]를 통한 명시적 지시나 BWP inactivity timer를 통한 암시적 방식으로 수행됩니다.

## 상세 설명
TS 38.213 §12에 명시된 BWP 동작의 핵심 요소는 다음과 같습니다.

- UE Feature 지원:
  - 2-50: Basic TRS (항상 지원)
  - 2-60: Active spatial relations (항상 지원)
  - 6-1: Basic BWP operation with restriction (항상 지원)
  - 6-1a: BWP operation without restriction on BW of BWP(s) (선택)
  - 6-2: Type A BWP adaptation with same numerology (선택)
  - 6-3: Type B BWP adaptation with same numerology (선택)
  - 6-4: BWP adaptation with different numerologies (선택)
  - 16-2a: Multi-DCI based multi-TRP (선택)
  - 40-1-7: Unified TCI with joint DL/UL TCI update for multi-DCI based multi-TRP (선택)
  - 40-1-9: Unified TCI with separate DL/UL TCI update for multi-DCI based multi-TRP (선택)
  - 5-1a: UE specific RRC configure UL/DL assignment (선택)
  - 6-5: Basic DL NR-NR CA operation (선택)

- BWP 구성 및 활성화:
  - 서빙 셀당 최대 4개의 DL BWP와 4개의 UL BWP가 RRC를 통해 구성될 수 있습니다.
  - 초기 활성 BWP는 RRC 설정에 의해 결정되며, 이후 [[PDCCH]]를 통해 수신된 DCI 내의 BWP indicator 필드에 의해 전환됩니다.

- BWP Inactivity Timer:
  - 네트워크는 bwp-InactivityTimer를 설정할 수 있으며, 해당 타이머가 만료되면 UE는 미리 정의된 Default BWP로 전환합니다.
  - 타이머는 활성 BWP가 Default BWP가 아닌 경우에 동작하며, 새로운 DCI 수신 시 타이머가 재시작됩니다.

- DCI 기반 변경:
  - DCI format 1_1 또는 1_2를 통해 DL BWP를, DCI format 0_1 또는 0_2를 통해 UL BWP를 동적으로 변경할 수 있습니다.

## 인과 관계
- [[PDCCH]] (triggers) [[Bandwidth_Part_Operation]] : DCI 내 BWP indicator 필드를 통해 BWP 전환을 유발함
- [[RRC]] (depends_on) [[Bandwidth_Part_Operation]] : BWP 구성 정보 및 타이머 값을 설정함
- [[Frame_Structure_Numerology]] (part_of) [[Bandwidth_Part_Operation]] : 각 BWP는 특정 numerology를 가질 수 있음

## 관련 개념
- [[Bandwidth_Part]] (part_of)
- [[DCI]] (affects)
- [[PDCCH]] (affects)
- [[RRC]] (depends_on)

## 스펙 근거
- TS 38.213 §12: Bandwidth part operation에 대한 전반적인 절차 및 타이머 관리 규정
- TS 38.822: UE Feature Priority 관련 요구사항 명시

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03), "NR; Physical layer procedures for control"
- 3GPP TS 38.822 V18.0.0 (2024-03), "NR; User Equipment (UE) radio access capabilities"