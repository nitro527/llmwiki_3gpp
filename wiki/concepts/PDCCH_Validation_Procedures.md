# PDCCH Validation Procedures

## 정의
[[PDCCH]] Validation Procedures는 [[UE]]가 수신한 [[DCI]]가 [[DL]] [[SPS]], [[UL]] Grant Type 2, 또는 [[Sidelink]] Configured Grant Type 2를 활성화하거나 해제하기 위한 유효한 제어 정보인지 확인하는 절차를 의미합니다.

## 요약
본 절차는 특정 [[DCI Format]] 내의 필드 값들을 검사하여 해당 DCI가 설정된 자원 할당을 활성화 또는 해제하는지 판단합니다. 이 과정은 [[RRC]]에 의해 설정된 파라미터와 DCI 내의 특정 필드 조합을 기반으로 수행됩니다.

## 상세 설명
UE는 수신된 DCI가 다음의 조건들을 만족할 때 해당 DCI를 유효한 것으로 간주합니다.

### DL SPS 및 UL Grant Type 2 검증
TS 38.213 §10.2에 따라, UE는 다음의 조건을 검사합니다.
- DCI 내의 CRC가 [[C-RNTI]], [[CS-RNTI]], 또는 [[MCS-C-RNTI]]로 스크램블링되어야 합니다.
- DCI 내의 특정 필드(예: HARQ process number, Redundancy version, MCS 등)가 사전에 정의된 값과 일치해야 합니다.
- 만약 DCI가 SPS 활성화를 지시하는 경우, 해당 DCI는 특정 자원 할당 정보를 포함하며, UE는 이를 기반으로 주기적인 자원 할당을 수행합니다.
- DCI가 SPS 해제를 지시하는 경우, 모든 HARQ process number와 특정 필드들이 해제 명령을 나타내는 값으로 설정되어야 합니다.

### SL Configured Grant Type 2 검증
TS 38.213 §10.2A에 따라, SL Configured Grant Type 2에 대한 검증은 다음을 포함합니다.
- DCI 내의 CRC가 [[SL-CS-RNTI]]로 스크램블링되어야 합니다.
- DCI 내의 필드들이 SL 자원 할당을 활성화하거나 해제하기 위한 특정 비트 패턴을 만족해야 합니다.

## 인과 관계
- [[PDCCH]] 수신 (triggers) [[PDCCH Validation Procedures]]
- [[PDCCH Validation Procedures]] (affects) [[SPS]] 활성화/해제
- [[PDCCH Validation Procedures]] (affects) [[PUSCH]] Configured Grant Type 2 활성화/해제
- [[PDCCH Validation Procedures]] (affects) [[Sidelink]] Configured Grant Type 2 활성화/해제

## 관련 개념
- [[DCI]] (depends_on)
- [[SPS]] (depends_on)
- [[PUSCH]] (depends_on)
- [[Sidelink]] (depends_on)
- [[RRC]] (depends_on)

## 스펙 근거
- TS 38.213 §10.2: PDCCH validation for DL SPS and UL grant Type 2
- TS 38.213 §10.2A: PDCCH validation for SL configured grant Type 2

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)