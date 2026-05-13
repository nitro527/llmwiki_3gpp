# PDCCH_Monitoring_Capability

## 정의
[[PDCCH]] 모니터링 능력은 [[UE]]가 활성화된 하향링크 [[Bandwidth_Part_Operation]] 내에서 특정 시간 단위(슬롯, 스팬, 또는 슬롯 그룹) 동안 동시에 수신 및 복호화할 수 있는 최대 [[PDCCH]] 후보(candidates) 수와 비중첩 [[CCE]](Control Channel Elements) 수에 대한 제약 조건을 의미한다.

## 요약
[[UE]]는 [[CORESET_Configuration]] 및 [[PDCCH_Search_Space_Configuration]]에 따라 [[PDCCH]]를 모니터링하며, 상위 계층 파라미터인 monitoringCapabilityConfig 설정에 따라 슬롯 단위(Rel-15), 스팬 단위(Rel-16), 또는 슬롯 그룹 단위(Rel-17)로 모니터링 능력을 제한받는다. [[Carrier_Aggregation]] 및 [[Dual_Connectivity_Power_Sharing]] 환경에서는 다중 서빙 셀에 대한 총 모니터링 능력이 정의되며, 특정 조건에서는 [[SS_PBCH_Block_Generation]] 또는 [[LTE]] CRS와의 자원 중첩 시 모니터링 의무가 면제될 수 있다.

## 상세 설명
[[UE]]의 [[PDCCH]] 모니터링 능력은 TS 38.213 §10에 따라 다음과 같이 결정된다.

1. 모니터링 단위 설정:
   - r15monitoringcapability: 슬롯 단위로 최대 [[PDCCH]] 후보 및 비중첩 [[CCE]] 수 제한.
   - r16monitoringcapability: 스팬(span) 단위로 제한. 스팬은 슬롯 내 연속적인 심볼 집합이며, [[UE]]는 스팬 간 최소 시간 간격(T_span)을 준수해야 한다.
   - r17monitoringcapability: 슬롯 그룹 단위로 제한.

2. 스팬 기반 모니터링:
   - [[UE]]는 (2, 2), (4, 3), (7, 3)과 같은 스팬 조합을 지원할 수 있다.
   - 스팬은 [[PDCCH]] 모니터링 기회가 시작되는 첫 심볼부터 마지막 심볼까지로 정의된다.
   - 다중 조합 지원 시, [[UE]]는 설정된 검색 공간에 따라 가장 큰 최대 [[PDCCH]] 후보 및 [[CCE]] 수를 제공하는 조합을 선택한다.

3. 슬롯 그룹 기반 모니터링:
   - SCS 설정에 따라 N_slot개의 연속적인 슬롯 그룹 내에서 모니터링 능력을 산출한다.
   - 그룹은 비중첩이며, 서브프레임 경계에서 시작한다.

4. 모니터링 제외 조건:
   - [[SS_PBCH_Block_Generation]] 자원과 [[PDCCH]] 후보 자원이 중첩되는 경우.
   - [[CORESET_Configuration]]의 TCI 상태가 유효하지 않은 경우.
   - [[LTE]] CRS와 중첩되는 경우(pdcch-CandidateReceptionWithCRSOverlap 설정 여부에 따름).
   - DCI format 2_0에 의해 가용하지 않은 RB 세트로 지시된 경우.

5. [[Carrier_Aggregation]] 및 [[Dual_Connectivity_Power_Sharing]] 환경:
   - 다중 셀 구성 시 pdcch-BlindDetectionCA 등의 파라미터를 통해 총 모니터링 능력을 보고하며, MCG와 SCG 간의 자원 분배를 수행한다.

## 인과 관계
- [[PDCCH]] depends_on [[PDCCH_Monitoring_Capability]] (모니터링 가능한 후보 수 및 CCE 수 제한)
- [[PDCCH_Search_Space_Configuration]] affects [[PDCCH_Monitoring_Capability]] (검색 공간 설정에 따른 모니터링 부하 결정)
- [[CORESET_Configuration]] affects [[PDCCH_Monitoring_Capability]] (CORESET 내 자원 할당이 모니터링 능력에 영향)
- [[Carrier_Aggregation]] affects [[PDCCH_Monitoring_Capability]] (다중 셀 구성 시 총 모니터링 능력 산출)

## 관련 개념
- [[PDCCH]] (implements)
- [[CORESET_Configuration]] (affects)
- [[PDCCH_Search_Space_Configuration]] (affects)
- [[Carrier_Aggregation]] (affects)
- [[Bandwidth_Part_Operation]] (part_of)

## 스펙 근거
- TS 38.213 §10: UE procedure for receiving control information
- TS 38.213 §10.1: PDCCH monitoring capability definitions and constraints
- TS 38.306: UE radio access capabilities (pdcch-BlindDetectionCA, etc.)

## 소스
- 3GPP TS 38.213 v18.0.0 §10