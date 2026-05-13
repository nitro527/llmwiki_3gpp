# SL_PRS_Generation

## 정의
SL PRS(Sidelink Positioning Reference Signal)는 사이드링크 환경에서 UE 간의 위치 측정을 위해 전송되는 참조 신호이며, 해당 신호의 전송 전력 결정 및 자원 구성 절차를 의미한다.

## 요약
SL PRS는 공유 자원 풀 또는 전용 자원 풀을 통해 전송되며, 각 풀의 설정에 따라 전송 전력 파라미터와 경로 손실 보상 방식이 결정된다. 전송 전력은 CBR(Channel Busy Ratio) 측정값, 우선순위 레벨, 그리고 상위 계층에서 제공하는 전력 제어 파라미터에 의해 계산된다.

## 상세 설명
SL PRS 전송 전력은 TS 38.213 §16.2.3A에 따라 결정된다.

1. 전송 전력 결정 공식:
   UE는 SL PRS 전송 기회(transmission occasion)에 대해 다음 식을 사용하여 전력을 결정한다.
   P_SL_PRS = min{P_CMAX, P_O + alpha * PL + delta_TF} [dBm]
   - P_CMAX: TS 38.101-1에 정의된 최대 전송 전력
   - P_O: 자원 풀 유형에 따라 결정되는 기준 전력
   - alpha: 경로 손실 보상 계수
   - PL: 경로 손실(Pathloss) 추정값
   - delta_TF: 전송 포맷에 따른 보정값

2. 자원 풀 유형별 파라미터:
   - 공유 자원 풀(Shared SL PRS resource pool):
     - P_O는 dl-P0-PSSCH-PSCCH 또는 dl-P0-PSSCH-PSCCH-r17 값을 사용한다.
     - alpha는 dl-Alpha-PSSCH-PSCCH 값을 사용하며, 미제공 시 1을 적용한다.
     - 최대 전송 전력은 우선순위와 CBR 범위에 기반한 sl-MaxTxPower를 따른다.
   - 전용 자원 풀(Dedicated SL PRS resource pool):
     - P_O는 dl-P0-SL-PRS 값을 사용한다.
     - alpha는 dl-Alpha-SL-PRS 값을 사용하며, 미제공 시 1을 적용한다.
     - 최대 전송 전력은 우선순위와 CBR 범위에 기반한 sl-PRS-MaxTx-Power를 따른다.

3. 경로 손실(PL) 추정:
   - 활성 SL BWP가 서빙 셀에 있는 경우, TS 38.213 §7.1.1의 절차를 따르되, DCI format 0_0 모니터링 여부에 따라 PUSCH 전력 결정에 사용되는 RS 자원을 참조한다.

4. 전송 포맷 보정(delta_TF):
   - 유니캐스트(Unicast) 전송이고 수신 UE로부터 특정 정보가 보고된 경우, 별도의 보정값을 적용한다. 그렇지 않은 경우 0 [dBm]을 적용한다.

5. 필터링:
   - 전력 결정에 사용되는 PSSCH 또는 SL PRS 전송 전력 및 RSRP는 상위 계층에서 제공하는 sl-FilterCoefficient를 사용하여 필터링된다.

## 인과 관계
- [[Sidelink_Power_Control]] depends_on [[SL_PRS_Generation]] (SL PRS 전송 전력 제어 로직 포함)
- [[SL_PRS_Resource_Selection]] depends_on [[SL_PRS_Generation]] (자원 선택 시 전력 제약 고려)
- [[Sidelink_Congestion_Control]] affects [[SL_PRS_Generation]] (CBR 측정값에 따른 전송 전력 제한)
- [[Pathloss_Estimation]] depends_on [[SL_PRS_Generation]] (경로 손실 추정값 활용)

## 관련 개념
- [[Sidelink_Power_Control]] (depends_on)
- [[SL_PRS_Resource_Selection]] (depends_on)
- [[Sidelink_Congestion_Control]] (affects)
- [[Pathloss_Estimation]] (depends_on)

## 스펙 근거
- TS 38.213 §16.2.3A: SL PRS 전송 전력 결정 절차 및 파라미터 정의
- TS 38.214 §6: 혼잡 제어 처리 시간 관련 참조
- TS 38.101-1: P_CMAX 정의 참조
- TS 38.215: RSRP 정의 참조

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"