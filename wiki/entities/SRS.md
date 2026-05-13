# SRS

## 정의
Sounding Reference Signal(SRS)은 기지국(gNB)이 상향링크 채널 상태 정보를 획득하거나, 단말(UE)의 위치를 측정하기 위해 사용하는 상향링크 참조 신호이다.

## 요약
SRS는 상향링크 채널 품질 측정, 빔 관리, 코드북 기반 또는 비코드북 기반 프리코딩을 위한 채널 상태 정보(CSI) 획득, 그리고 위치 측정(Positioning)을 위해 사용된다. 단말은 상위 계층 시그널링을 통해 설정된 자원 구성에 따라 주기적(Periodic), 반주기적(Semi-persistent), 또는 비주기적(Aperiodic)으로 SRS를 전송한다.

## 상세 설명
TS 38.214 §6.2에 따라 SRS의 주요 동작은 다음과 같다.

1. 자원 구성 및 전송:
   - 단말은 상위 계층 파라미터 SRS-ResourceSet 및 SRS-Resource를 통해 SRS 전송을 위한 시간 및 주파수 자원을 할당받는다.
   - SRS는 슬롯 내 임의의 OFDM 심볼에서 시작할 수 있도록 설정될 수 있다.
   - 위치 측정을 위한 SRS(SRS-Pos)는 별도의 자원 구성을 통해 지원되며, 비주기적 및 반주기적 SRS 자원 모두를 지원한다.

2. 전력 제어:
   - SRS 전송 전력은 상향링크 전력 제어 메커니즘을 따른다.
   - 위치 측정을 위한 SRS의 경우, 서빙 셀의 PRS(Positioning Reference Signal) 또는 인접 셀의 SSB(Synchronization Signal Block) 및 PRS를 기반으로 한 개방 루프 전력 제어(OLPC)가 적용된다.
   - 경로 손실(PathLoss) 추정치는 서빙 셀별로 유지되거나, 모든 셀에 걸쳐 통합적으로 관리될 수 있다.

3. 시퀀스 및 매핑:
   - SRS는 [[SRS_Generation]]을 통해 생성된 시퀀스를 기반으로 하며, [[SRS_Mapping]]을 통해 물리 자원에 매핑된다.

## 인과 관계
- [[SRS_Generation]] depends_on [[SRS]] (SRS 시퀀스 생성의 기반)
- [[SRS_Mapping]] depends_on [[SRS]] (SRS 자원 매핑의 대상)
- [[SRS_Power_Control]] depends_on [[SRS]] (SRS 전송 전력 제어 수행)
- [[SRS_Spatial_Relation]] depends_on [[SRS]] (SRS 빔포밍 및 공간적 설정)
- [[SRS_Switching]] depends_on [[SRS]] (안테나 스위칭을 통한 SRS 전송)
- [[SRS_Positioning_Procedure]] depends_on [[SRS]] (위치 측정을 위한 SRS 활용)
- [[SRS_CLI_Measurement]] depends_on [[SRS]] (교차 링크 간섭 측정을 위한 SRS 활용)

## 관련 개념
- [[SRS_Generation]] (implements)
- [[SRS_Mapping]] (implements)
- [[SRS_Power_Control]] (affects)
- [[SRS_Spatial_Relation]] (affects)
- [[SRS_Switching]] (affects)
- [[SRS_Positioning_Procedure]] (implements)
- [[SRS_CLI_Measurement]] (implements)

## 스펙 근거
- TS 38.214 §6.2: UE reference signal (RS) procedure
- TS 38.211 §6.4.1: Sounding reference signal

## 소스
- 3GPP TS 38.214 V19.0.0 (2024-03)
- 3GPP TS 38.211 V19.0.0 (2024-03)