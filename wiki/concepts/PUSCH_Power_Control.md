# PUSCH_Power_Control

## 정의
[[PUSCH]] 전송 전력 제어는 기지국이 [[UE]]의 상향링크 전송 전력을 조절하여 셀 내 간섭을 최소화하고, 목표 수신 품질을 유지하기 위해 수행하는 물리 계층 절차입니다.

## 요약
[[PUSCH]] 전력 제어는 개루프(Open-loop) 및 폐루프(Closed-loop) 전력 제어 메커니즘을 결합하여 수행됩니다. [[UE]]는 경로 손실(Pathloss) 추정, 타겟 수신 전력 설정, 그리고 기지국으로부터 수신된 TPC(Transmit Power Control) 명령을 기반으로 최종 전송 전력을 결정합니다. 최신 스펙에서는 [[TCI_State]]와 연동된 전력 제어 파라미터 매핑을 통해 빔 기반의 정밀한 전력 관리를 지원합니다.

## 상세 설명
[[PUSCH]] 전송 전력은 TS 38.213 §7에 정의된 절차에 따라 결정됩니다.

1. 경로 손실 추정: [[UE]]는 서빙 셀당 최대 4개의 경로 손실 추정치를 유지합니다. 경로 손실 참조 신호(RS)는 [[TCI_State]] 또는 [[TCI_UL_State]]와 연동된 `pathlossReferenceRS-Id-r17`을 통해 제공됩니다. MAC CE에 의해 RS 자원이 업데이트될 경우, 특정 슬롯 오프셋 이후부터 새로운 경로 손실 추정치가 적용됩니다.
2. 전력 제어 파라미터: `p0AlphaSetforPUSCH`가 제공되는 경우, 타겟 전력($P_0$)과 알파($\alpha$) 값, 그리고 전력 제어 조정 상태($f_c$)는 해당 [[TCI_State]] 또는 [[TCI_UL_State]]와 연동된 설정값을 따릅니다.
3. 전송 전력 결정: [[UE]]는 설정된 타겟 전력, 경로 손실, 대역폭 보정치, 그리고 누적된 TPC 명령을 합산하여 최종 전송 전력을 계산합니다.
4. 다중 TRP 및 TCI 연동: LTM(L1/L2 Triggered Mobility) 셀 스위치 명령이나 [[TCI_State]] 지시가 있을 경우, 해당 상태에 매핑된 전력 제어 파라미터를 사용하여 전송 전력을 동적으로 조정합니다.
5. PDCCH 모니터링: 두 개의 [[PDCCH]] 후보가 포함된 경우, 모니터링 시점은 두 후보의 모니터링 시점의 합집합으로 정의되며, 전력 제어 관련 명령 수신 시점 결정에 영향을 줍니다.

## 인과 관계
- [[PUSCH]] depends_on [[PUSCH_Power_Control]] (전송 전력 결정 필수)
- [[PUSCH_Power_Control]] depends_on [[Pathloss_Estimation]] (경로 손실 값 참조)
- [[PUSCH_Power_Control]] depends_on [[TCI_State_Management]] (전력 제어 파라미터 매핑)
- [[PUSCH_Power_Control]] triggers [[Transmission_Power_Prioritization]] (전력 제한 시 우선순위 결정)

## 관련 개념
- [[Pathloss_Estimation]] (depends_on)
- [[TCI_State_Management]] (depends_on)
- [[Transmission_Power_Prioritization]] (triggers)
- [[PUSCH]] (part_of)

## 스펙 근거
- TS 38.213 §7: Uplink Power control 절차 전반
- TS 38.213 §7.1.1: PUSCH 전력 제어 파라미터 및 경로 손실 참조 설정
- TS 38.213 §10.1: PDCCH 모니터링 및 수신 시점 정의

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18)