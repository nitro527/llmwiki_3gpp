# PRS_Measurement_Procedure

## 정의
DL PRS(Downlink Positioning Reference Signal) 측정 및 보고 절차는 UE가 네트워크로부터 수신한 PRS 자원을 기반으로 위치 측정을 수행하고, 이를 상위 계층 파라미터를 통해 보고하는 일련의 과정을 의미한다.

## 요약
UE는 RRC_CONNECTED 상태에서 설정된 측정 갭(Measurement Gap) 내에서 DL PRS를 측정한다. 주요 기능으로는 수신기 주파수 호핑(Receiver Frequency Hopping), 반송파 위상 측정(Carrier Phase Positioning), 그리고 대역폭 집성(Bandwidth Aggregation)을 통한 다중 주파수 계층 간의 측정 결합이 포함된다.

## 상세 설명
DL PRS 측정 절차는 TS 38.214 §5.1.6.5에 정의된 다음 메커니즘을 따른다.

1. 수신기 주파수 호핑 (Receiver Frequency Hopping):
Reduced Capability UE는 nr-DL-PRS-RxHoppingRequest를 통해 수신기 주파수 호핑을 설정받을 수 있다. 이는 요청된 대역폭이 UE의 최대 대역폭을 초과할 때 사용된다. UE는 단일 측정 갭 인스턴스 내에서 모든 홉을 수신하며, 단일 홉 또는 다중 홉 기반의 측정을 보고할 수 있다.

2. 반송파 위상 측정 (Carrier Phase Positioning):
UE는 DL RSTD(Reference Signal Time Difference)와 함께 DL RSCPD(Reference Signal Carrier Phase Difference)를, UE Rx-Tx 시간 차이 측정과 함께 DL RSCP(Reference Signal Carrier Phase)를 보고할 수 있다. 이 측정값들은 단일 DL PRS 포지셔닝 주파수 계층 내에서 수행되어야 하며, 측정 갭 내에서 획득된다. 측정 품질은 NR-PhaseQuality를 통해 보고되며, LoS/NLoS 지시자가 포함될 수 있다.

3. 대역폭 집성 (Bandwidth Aggregation):
UE는 nr-DL-PRS-AggregationInfo를 통해 서로 다른 DL PRS 포지셔닝 주파수 계층 간의 자원 집합을 연결(Linkage)받는다. 연결된 자원 집합은 동일한 QCL(Quasi-Co-Location) 정보, 주기성, 심볼 수 등을 공유해야 한다. UE는 최대 4개의 집성된 DL RSTD 또는 UE Rx-Tx 시간 차이 측정을 보고할 수 있으며, 이는 2~3개의 주파수 계층에 걸쳐 수행된다.

## 인과 관계
- [[PRS_Generation]] depends_on [[PRS_Measurement_Procedure]] (측정 대상 신호 생성)
- [[PRS_Measurement_Procedure]] implements [[Carrier_Aggregation]] (다중 주파수 계층 간 측정 결합)
- [[PRS_Measurement_Procedure]] affects [[SRS_Positioning_Procedure]] (Multi-RTT 측정 시 상호 연관)

## 관련 개념
- [[PRS_Generation]] (implements)
- [[Carrier_Aggregation]] (implements)
- [[SRS_Positioning_Procedure]] (affects)

## 스펙 근거
- TS 38.214 §5.1.6.5.1 (PRS receiver frequency hopping)
- TS 38.214 §5.1.6.5.2 (PRS for carrier phase positioning)
- TS 38.214 §5.1.6.5.3 (PRS bandwidth aggregation for positioning measurements)

## 소스
- 3GPP TS 38.214 V17.9.0 (2023-12) Physical layer procedures for data