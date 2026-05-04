# PRACH_Power_Control

## 정의
[[PRACH]] 전송 시 [[UE]]가 적용해야 하는 전송 전력 설정 절차를 의미하며, 목표 수신 전력과 경로 손실 보상을 결합하여 산출하는 메커니즘입니다.

## 요약
[[PRACH_Power_Control]]은 [[UE]]가 랜덤 액세스 절차를 수행할 때 기지국에서 요구하는 목표 수신 전력을 만족시키기 위해 경로 손실을 보상하는 방식으로 동작합니다. 이 과정에서 [[UE]]는 상위 계층에서 제공하는 파라미터와 현재 경로 손실 측정값을 사용하여 전송 전력을 결정합니다.

## 상세 설명
[[UE]]는 [[PRACH]] 전송을 위해 다음과 같은 전력 제어 절차를 수행합니다.

1. **전력 산출 공식**: [[UE]]는 특정 [[PRACH]] 전송 기회(RO)에서 전송 전력 $P_{PRACH,b,f,c}(i)$를 결정합니다. 이는 목표 수신 전력인 $P_{O\_PRACH,b,f,c}(i)$와 경로 손실 보상값인 $PL_{b,f,c}(q_d)$의 합으로 구성됩니다.
2. **필수 기능 지원**:
   - [필수(항상)] 8-3: Basic power control operation을 통해 기본적인 전력 제어 루프를 운용합니다.
   - [필수(cap)] 8-8: UL power control with 2 PUSCH closed loops 및 8-9: UL power control with 2 PUCCH closed loops를 지원하여 상향링크 전력 제어의 정밀도를 높입니다.
3. **선택적 기능 지원**:
   - 4-26: Parallel PRACH and SRS/PUCCH/PUSCH transmissions across CCs in inter-band CA를 통해 다중 대역 환경에서의 동시 전송 시 전력 제어를 수행합니다.
   - 11-8: Enhanced UL power control scheme을 통해 향상된 전력 제어 알고리즘을 적용할 수 있습니다.
   - 15-23: Support of open loop SL power control and RSRP report를 통해 사이드링크 전력 제어와의 연동을 지원합니다.
   - 23-3-1b, 23-3-2, 23-3-2b, 23-3-2c, 23-3-2d, 23-3-2e: Multi-TRP 환경에서의 전력 제어 파라미터 업데이트 및 반복 전송을 위한 전력 제어 설정을 지원합니다.

## 인과 관계
- [[RACH_Procedure_L1]] (triggers): [[PRACH]] 전송이 시작될 때 전력 제어 절차가 트리거됩니다.
- [[Uplink_Power_Control]] (part_of): [[PRACH_Power_Control]]은 전체 상향링크 전력 제어 체계의 일부입니다.
- [[PRACH_Resource_Mapping]] (depends_on): 전송 전력은 매핑된 자원과 경로 손실 측정값에 의존합니다.

## 관련 개념
- [[RACH_Procedure_L1]] (triggers)
- [[Uplink_Power_Control]] (part_of)
- [[PRACH_Resource_Mapping]] (depends_on)

## 스펙 근거
- TS 38.213 §7.4에 따르면, [[UE]]는 [[PRACH]] 전송 전력을 결정할 때 상위 계층에서 설정된 목표 수신 전력과 경로 손실 보상 계수를 반영해야 합니다.

## 소스
- 3GPP TS 38.213 v18.0.0, "Physical layer procedures for control"