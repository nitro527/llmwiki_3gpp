# Sidelink_Prioritization

## 정의
[[Sidelink_Prioritization]]은 [[UE]]가 [[Uplink]] 전송과 [[Sidelink]] 전송이 시간적으로 중첩되거나, [[Downlink]] 수신과 [[Sidelink]] 수신이 중첩될 때, 물리 계층에서 우선순위를 결정하고 전력 제어를 수행하여 충돌을 해결하는 절차를 의미합니다.

## 요약
[[UE]]는 상향링크와 사이드링크 간의 동시 전송 또는 수신이 요구될 때, 각 채널 및 신호에 할당된 우선순위 값을 비교합니다. 우선순위가 낮은 전송은 드롭(drop)되거나 전력이 제한되며, 특정 조건에서는 [[Power_Headroom_Report]] 및 전력 공유 메커니즘을 통해 자원을 효율적으로 분배합니다.

## 상세 설명
TS 38.213 §16.2.4에 따라 [[UE]]는 다음과 같은 우선순위 기반 동작을 수행합니다.

1. 전송 우선순위 결정:
   - [[UE]]는 [[Uplink]] 전송(예: [[PUSCH]], [[PUCCH]], [[SRS]], [[PRACH]])과 [[Sidelink]] 전송(예: [[PSSCH]], [[PSCCH]], [[PSFCH]])이 중첩될 때, 각 채널의 우선순위 인덱스를 비교합니다.
   - 우선순위가 낮은 채널은 해당 심볼 구간에서 전송이 취소되거나 전력이 0으로 설정됩니다.
   - [[Sidelink]] 전송의 경우, [[SCI]]를 통해 전달된 우선순위 필드 값이 기준이 됩니다.

2. 전력 제어 및 공유:
   - 동시 전송 시 총 전송 전력이 [[UE]]의 최대 전송 전력을 초과하는 경우, 우선순위가 높은 채널에 전력을 우선 할당합니다.
   - [[Sidelink]] 전송이 [[Uplink]] 전송과 동일한 캐리어 또는 다른 캐리어에서 발생할 때, [[Transmission_Power_Prioritization]] 절차를 통해 전력 스케일링이 적용됩니다.

3. 수신 우선순위 결정:
   - [[Downlink]] 수신과 [[Sidelink]] 수신이 중첩되는 경우, [[UE]]는 구현 방식에 따라 수신 우선순위를 결정하며, 일반적으로 [[PDCCH]]를 통해 스케줄링된 [[Downlink]] 데이터 수신이 우선시됩니다.

## 인과 관계
- [[Sidelink_Prioritization]] depends_on [[Sidelink_Transmission_Procedure]] (우선순위 결정 대상 전송 절차)
- [[Sidelink_Prioritization]] affects [[Transmission_Power_Prioritization]] (전력 할당 우선순위 제어)
- [[Sidelink_Prioritization]] depends_on [[Sidelink_Resource_Configuration]] (우선순위 파라미터 설정)

## 관련 개념
- [[Transmission_Power_Prioritization]] (affects)
- [[Sidelink_Transmission_Procedure]] (depends_on)
- [[Sidelink_Resource_Configuration]] (depends_on)
- [[Uplink_Tx_Switching]] (affects)

## 스펙 근거
- TS 38.213 §16.2.4: Prioritization of transmissions/receptions 절차 정의
- TS 38.213 §16.2.4.1: Sidelink와 Uplink 간의 전송 우선순위 규칙 명시
- TS 38.213 §16.2.4.2: Sidelink와 Downlink 간의 수신 우선순위 규칙 명시

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"