# PUCCH_Power_Control

## 정의
[[PUCCH]] 전송 시 [[UE]]가 상향링크 채널의 신뢰성을 보장하면서도 간섭을 최소화하기 위해 송신 전력을 결정하는 물리 계층 절차.

## 요약
[[PUCCH]] 전송 전력은 기지국이 설정한 목표 수신 전력, 경로 손실(Pathloss), [[PUCCH]] 포맷에 따른 오프셋, 그리고 [[TPC]] 커맨드에 의한 폐루프(Closed-loop) 조정 값을 합산하여 결정된다. 다중 [[TRP]] 환경이나 다중 공간 관계(Spatial relation) 설정 시, 각 경로에 최적화된 전력 제어 파라미터 세트를 독립적으로 적용할 수 있다.

## 상세 설명
[[UE]]는 [[PUCCH]] 전송 시점 $i$와 서빙 셀 $c$, 활성 상향링크 [[BWP]] $b$에 대해 다음과 같이 전력을 결정한다.

1. 기본 전력 공식:
   $P_{PUCCH,b,c}(i, q_u, q_d, l) = \min \{ P_{CMAX,f,c}(i), P_{O,PUCCH,b,c}(q_u) + 10\log_{10}(2^{\mu} \cdot M_{RB,b,c}^{PUCCH}(i)) + PL_{b,c}(q_d) + \Delta_{F,PUCCH}(F) + \Delta_{TF,b,c}(i) + g_{b,c}(i, l) \} [dBm]$

2. 주요 파라미터:
   - $P_{CMAX,f,c}(i)$: [[UE]]가 설정한 최대 출력 전력.
   - $P_{O,PUCCH,b,c}(q_u)$: 상위 계층에서 제공하는 목표 수신 전력 파라미터. [[PUCCH_Spatial_Setting]]과 연계되어 결정된다.
   - $PL_{b,c}(q_d)$: 하향링크 경로 손실 추정치. [[Pathloss_Estimation]] 절차를 통해 계산되며, 참조 신호(RS) 인덱스 $q_d$를 사용한다.
   - $\Delta_{F,PUCCH}(F)$: [[PUCCH]] 포맷 $F$에 따른 전력 오프셋.
   - $\Delta_{TF,b,c}(i)$: [[UCI]] 비트 수와 자원 요소(RE) 수에 기반한 전력 조정 값.
   - $g_{b,c}(i, l)$: [[TPC]] 커맨드에 의해 누적되는 폐루프 전력 조정 상태.

3. 다중 전력 제어:
   - [[UE]]가 다중 공간 관계 정보나 다중 전력 제어 파라미터 세트를 설정받은 경우, [[MAC]] CE 활성화 명령을 통해 특정 세트를 선택하여 적용한다.
   - 다중 [[TRP]] 환경에서 [[PUCCH]] 반복 전송 시, 각 TCI 상태에 대응하는 전력을 개별적으로 계산할 수 있다.
   - [[TPC]] 커맨드는 [[DCI]] 포맷 1_0, 1_1, 1_2 또는 [[DCI]] 포맷 2_2를 통해 수신하며, 누적된 값은 $g_{b,c}(i, l)$에 반영된다.

## 인과 관계
- [[PUCCH]] depends_on [[PUCCH_Power_Control]] (전송 전력 결정 필수)
- [[Pathloss_Estimation]] affects [[PUCCH_Power_Control]] (경로 손실 값 제공)
- [[PUCCH_Spatial_Setting]] affects [[PUCCH_Power_Control]] (공간 관계에 따른 파라미터 매핑)
- [[TPC]] triggers [[PUCCH_Power_Control]] (폐루프 전력 조정값 갱신)
- [[PUCCH_Repetition]] depends_on [[PUCCH_Power_Control]] (반복 전송 시 전력 제어 적용)

## 관련 개념
- [[PUCCH]] (part_of)
- [[Pathloss_Estimation]] (affects)
- [[PUCCH_Spatial_Setting]] (affects)
- [[TPC]] (triggers)
- [[PUCCH_Repetition]] (depends_on)

## 스펙 근거
- TS 38.213 §7.2.1: [[PUCCH]] 전송 전력 결정 공식 및 파라미터 정의
- TS 38.213 §7.2.1: [[TPC]] 커맨드 적용 및 누적 상태 관리
- TS 38.213 §7.2.1: 다중 공간 관계 및 다중 전력 제어 파라미터 세트 활성화 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"