# PRS_Reception_Procedure

## 정의
DL PRS(Downlink Positioning Reference Signal) 수신 절차는 UE가 네트워크로부터 설정된 위치 측정용 참조 신호를 수신하고, 이를 기반으로 RSTD(Reference Signal Time Difference), RSRP(Reference Signal Received Power), RSRPP(Reference Signal Received Power per Path), 및 UE Rx-Tx 시간 차이를 측정하여 보고하는 일련의 과정을 의미한다.

## 요약
UE는 상위 계층 파라미터인 NR-DL-PRS-ResourceSet 및 NR-DL-PRS-Resource를 통해 DL PRS 자원을 설정받는다. UE는 설정된 측정 갭(Measurement Gap) 또는 DL PRS 처리 윈도우(Processing Window) 내에서 DL PRS를 수신하며, 측정 품질 지표와 함께 위치 관련 정보를 네트워크에 보고한다. 또한, QCL(Quasi Co-Location) 정보를 활용하여 수신 빔포밍 및 측정 정확도를 최적화한다.

## 상세 설명
DL PRS 수신 절차는 다음과 같은 계층적 구조와 동작을 포함한다.

1. 자원 구성:
   - DL PRS는 NR-DL-PRS-PositioningFrequencyLayer 내에 하나 이상의 DL PRS 자원 세트로 구성된다.
   - 각 자원 세트는 K≥1개의 DL PRS 자원을 포함하며, 동일한 주파수 계층 내의 자원들은 동일한 dl-PRS-SubcarrierSpacing, dl-PRS-CyclicPrefix, dl-PRS-PointA, dl-PRS-CombSizeN, dl-PRS-ResourceBandwidth 및 dl-PRS-StartPRB를 공유한다.
   - 각 자원은 dl-PRS-SequenceID를 통해 의사 난수 생성기를 초기화하며, dl-PRS-CombSizeN-AndReOffset을 통해 주파수 도메인 시작 위치를 결정한다.

2. 측정 및 보고:
   - UE는 DL RSTD, DL PRS-RSRP, DL PRS-RSRPP, UE Rx-Tx 시간 차이를 측정한다.
   - 측정 품질을 위해 timingQualityValue 및 timingQualityResolution을 포함하는 NR-TimingQuality를 보고할 수 있다.
   - LoS/NLoS 지시자를 통해 측정 신호의 가시선 여부를 보고하며, 이는 0에서 1 사이의 소프트 값 또는 하드 값으로 표현된다.

3. 측정 갭 및 처리 윈도우:
   - UE는 활성 DL BWP 외부의 신호를 측정하기 위해 측정 갭을 요청하거나, DL-PPW-PreConfig를 통해 설정된 처리 윈도우 내에서 DL PRS를 수신한다.
   - DL PRS 처리 윈도우 내에서 DL PRS와 다른 DL 신호 간의 우선순위가 충돌할 경우, 설정된 우선순위(st1, st2, st3)에 따라 수신 여부를 결정한다.

4. QCL 및 TEG(Timing Error Group) 관리:
   - DL PRS는 다른 DL PRS 또는 SS/PBCH Block과 QCL 'typeD' 또는 'typeC' 관계를 가질 수 있다.
   - UE는 Rx TEG 및 RxTx TEG를 사용하여 측정값의 시간 오차를 그룹화하고, 이를 통해 측정 보고의 신뢰성을 높인다.

## 인과 관계
- [[PRS_Generation]] depends_on [[PRS_Reception_Procedure]] (PRS 생성 파라미터가 수신 절차의 설정값으로 사용됨)
- [[PDCCH_Monitoring_Capability]] affects [[PRS_Reception_Procedure]] (PDCCH 모니터링과 DL PRS 수신 간의 우선순위 및 자원 충돌 관리)
- [[Bandwidth_Part_Operation]] affects [[PRS_Reception_Procedure]] (BWP 내/외부에서의 PRS 측정 가능 여부 결정)

## 관련 개념
- [[PRS_Generation]] (implements)
- [[PDSCH_Reception_Procedure]] (similar_to)
- [[Synchronization_Procedures]] (depends_on)
- [[Timing_Advance_Adjustment]] (affects)

## 스펙 근거
- TS 38.214 §5.1.6.5: DL PRS 자원 구성, 주파수 계층 정의, 측정 보고 및 처리 윈도우 동작 규정
- TS 37.355: DL PRS 관련 상위 계층 파라미터 및 UE 위치 측정 능력 정의
- TS 38.211 §7.4.1.7: DL PRS 시퀀스 생성 및 자원 매핑 규칙
- TS 38.133: 측정 갭 및 DL PRS 우선순위 처리 규정

## 소스
- 3GPP TS 38.214 v17.9.0 (Release 17)
- 3GPP TS 38.211 v17.9.0 (Release 17)
- 3GPP TS 37.355 v17.9.0 (Release 17)
- 3GPP TS 38.133 v17.9.0 (Release 17)