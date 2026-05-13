# PRACH_Power_Control

## 정의
[[PRACH]] 전송 시 [[UE]]가 적용해야 할 상향링크 전송 전력을 결정하는 절차로, 경로 손실(Pathloss) 보상 및 타겟 수신 전력 설정을 통해 기지국에서의 성공적인 프리앰블 검출을 보장하는 메커니즘.

## 요약
[[UE]]는 TS 38.213 §7.4에 따라 [[PRACH]] 전송 전력을 결정하며, 이는 설정된 최대 출력 전력, 상위 계층에서 제공하는 타겟 수신 전력, 그리고 [[DL_RS]]를 기반으로 계산된 경로 손실의 합으로 정의된다. 전송 실패 시 전력 램핑(Power Ramping)을 수행하며, 특정 조건에서 전력 램핑 카운터를 일시 중지하거나 전송 전력을 조정한다.

## 상세 설명
[[UE]]는 활성 상향링크 [[BWP]]에서 [[PRACH]] 전송 전력 $P_{PRACH,b,f,c}(i)$ [dBm]을 다음과 같이 결정한다.

$P_{PRACH,b,f,c}(i) = \min \{ P_{CMAX,f,c}(i), P_{O\_PREAMBLE,b,f,c} + PL_{b,f,c}(i) \}$

- $P_{CMAX,f,c}(i)$: 캐리어 $f$, 셀 $c$의 전송 기회 $i$에 대한 [[UE]] 설정 최대 출력 전력.
- $P_{O\_PREAMBLE,b,f,c}$: 상위 계층에서 제공하는 PREAMBLE_RECEIVED_TARGET_POWER.
- $PL_{b,f,c}(i)$: 활성 하향링크 [[BWP]]의 [[DL_RS]]를 기반으로 계산된 경로 손실(referenceSignalPower - higher layer filtered RSRP).

경로 손실 계산을 위한 [[referenceSignalPower]]는 다음과 같이 결정된다.
1. [[PDCCH]] order에 의한 응답이 아니거나, 경합 기반(Contention-based) [[RACH]] 절차인 경우, 또는 링크 복구 절차와 관련된 경우 [[SS_PBCH_Block_Generation]]의 ss-PBCH-BlockPower를 사용한다.
2. [[PDCCH]] order에 의한 비경합 기반(Contention-free) [[RACH]] 절차인 경우, [[PDCCH]] order의 [[DM_RS]]와 준-동일 위치(Quasi-collocated) 관계에 있는 [[DL_RS]] 또는 지시된 [[SS_PBCH_Block_Generation]]의 전력을 사용한다.
3. 주기적 [[CSI_RS]]가 설정된 경우, ss-PBCH-BlockPower에 powerControlOffsetSS를 적용하여 계산한다.

전력 램핑 카운터 관리:
- [[Random_Access_Response]]를 수신하지 못한 경우, 상위 계층 절차에 따라 다음 [[PRACH]] 전송 전력을 결정한다.
- 공간 도메인 전송 필터 변경, 전력 할당 문제(PUSCH/PUCCH/SRS와의 충돌), 또는 슬롯 포맷 결정 등으로 인해 [[PRACH]] 전송을 수행하지 못하거나 감소된 전력으로 전송하는 경우, 물리 계층은 상위 계층에 전력 램핑 카운터 일시 중지를 통지할 수 있다.

## 인과 관계
- [[PRACH]] depends_on [[PRACH_Power_Control]] (전송 전력 결정 필수)
- [[Random_Access_Response]] depends_on [[PRACH_Power_Control]] (전력 램핑 카운터 관리 연동)
- [[Pathloss_Estimation]] depends_on [[PRACH_Power_Control]] (경로 손실 계산값 사용)
- [[Transmission_Power_Prioritization]] affects [[PRACH_Power_Control]] (전력 할당에 따른 전송 제한 및 램핑 카운터 제어)

## 관련 개념
- [[PRACH]] (part_of)
- [[Random_Access_Response]] (depends_on)
- [[Pathloss_Estimation]] (depends_on)
- [[Transmission_Power_Prioritization]] (affects)

## 스펙 근거
- TS 38.213 §7.4: [[PRACH]] 전송 전력 결정 공식 및 파라미터 정의
- TS 38.213 §7.4: [[PDCCH]] order 및 링크 복구 시 [[referenceSignalPower]] 결정 규칙
- TS 38.213 §7.4: 전력 램핑 카운터 일시 중지 조건 및 물리 계층 통지 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"