# Uplink_Power_Control

## 정의
[[Uplink_Power_Control]]은 [[UE]]가 상향링크 채널 및 신호인 [[PUSCH]], [[PUCCH]], [[SRS]], [[PRACH]]를 전송할 때, 기지국에서의 수신 성능을 최적화하고 셀 내 간섭을 최소화하기 위해 전송 전력을 조절하는 L1 제어 절차를 의미합니다.

## 요약
[[Uplink_Power_Control]]은 경로 손실(Pathloss) 추정, 폐루프(Closed-loop) 전력 제어, 그리고 각 채널별 파라미터 설정을 통해 수행됩니다. [[UE]]는 상위 계층에서 설정된 파라미터와 기지국으로부터 수신한 [[DCI]]를 기반으로 전송 전력을 결정하며, 다중 채널 동시 전송 시 전력 제한 상황을 고려한 우선순위 규칙을 따릅니다.

## 상세 설명
[[Uplink_Power_Control]]의 핵심 메커니즘은 다음과 같습니다.

*   **경로 손실 추정**: [[UE]]는 [[SS_PBCH_Block]] 또는 [[CSI_RS]]를 기반으로 하향링크 경로 손실을 측정합니다. 이 값은 상향링크 전송 전력 계산 시 보상값으로 사용됩니다.
*   **전력 제어 파라미터**: 각 채널은 상위 계층 파라미터인 P0(목표 수신 전력)와 Alpha(경로 손실 보상 계수)를 사용하여 기본 전력을 설정합니다.
*   **TCI 상태 기반 조정**: [[UE]]는 [[TCI]] 상태와 연계된 상향링크 전력 제어 설정을 통해, 특정 빔이나 공간적 관계(Spatial relation)에 최적화된 전력 제어를 수행합니다.
*   **전력 제한 및 우선순위**: 여러 채널이 동시에 전송될 때, [[UE]]의 최대 전송 전력을 초과하지 않도록 전력을 재분배하거나 일부 전송을 생략하는 우선순위 규칙이 적용됩니다. 이는 [[Uplink_Power_Prioritization]]을 통해 관리됩니다.
*   **보고 절차**: [[UE]]는 자신의 전력 여유를 기지국에 알리기 위해 [[Power_Headroom_Report]]를 수행합니다.

## 인과 관계
- [[DCI]] (triggers) [[Uplink_Power_Control]]
- [[TCI]] 상태 (affects) [[Uplink_Power_Control]]
- [[Uplink_Power_Control]] (affects) [[PUSCH]], [[PUCCH]], [[SRS]], [[PRACH]] 전송 품질
- [[Uplink_Power_Prioritization]] (depends_on) [[Uplink_Power_Control]]

## 관련 개념
- [[PUSCH_Power_Control]] (part_of)
- [[PUCCH_Power_Control]] (part_of)
- [[SRS_Power_Control]] (part_of)
- [[PRACH_Power_Control]] (part_of)
- [[Power_Headroom_Report]] (similar_to)
- [[Uplink_Power_Prioritization]] (depends_on)
- [[Dual_Connectivity_Power_Control]] (depends_on)

## 스펙 근거
- TS 38.213 §7에 따르면, [[UE]]는 [[PUSCH]], [[PUCCH]], [[SRS]], [[PRACH]] 전송을 위한 전력 제어 절차를 수행해야 합니다.
- TS 38.213 §7.1.1에 따르면, [[PUSCH]] 전송 전력은 경로 손실, 폐루프 전력 제어 값, 그리고 [[DCI]]를 통해 전달된 TPC 명령에 의해 결정됩니다.
- TS 38.213 §7.5에 따르면, 다중 채널 전송 시 전력 제한 상황에서의 우선순위 규칙이 정의됩니다.
- TS 38.213 §7.7에 따르면, [[UE]]는 [[Power_Headroom_Report]]를 통해 기지국에 전력 상태를 보고합니다.

## 소스
- 3GPP TS 38.213 (v18.0.0) §7, §7.1, §7.1.1, §7.2, §7.2.1, §7.3, §7.3.1, §7.4, §7.5, §7.6, §7.7
- 3GPP TS 38.822 (UE Feature List 관련 항목: 8-3, 4-26, 2-60, 4-25, 6-16, 23-1-1h, 39-2, 4-12, 4-19, 4-19a, 4-19b, 4-19c)