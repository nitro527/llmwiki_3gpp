# PDCCH

## 정의
[[PDCCH]]는 하향링크 제어 정보인 [[DCI]]를 전송하기 위한 물리 채널로, 기지국이 단말에게 자원 할당, 전력 제어, 슬롯 포맷 정보 등을 전달하는 핵심 제어 채널이다.

## 요약
[[PDCCH]]는 단말이 특정 [[CORESET]] 내에서 [[DCI]]를 수신하기 위해 블라인드 디코딩을 수행하는 채널이다. 단말은 상위 계층 설정에 따라 [[PDCCH_Monitoring_Capability]]를 기반으로 슬롯, 스팬(span), 또는 슬롯 그룹 단위로 모니터링을 수행하며, [[PDCCH_Search_Space_Configuration]]에 정의된 후보군을 디코딩한다.

## 상세 설명
[[PDCCH]]는 [[DCI]]를 전송하며, 이를 위해 정보 요소 다중화, [[CRC_Calculation]], 채널 코딩, [[Rate_Matching]] 과정을 거친다. TS 38.211 §7.3.2에 따라 [[PDCCH]]는 하나 이상의 [[CORESET]] 내에서 전송된다.

단말은 활성화된 하향링크 [[Bandwidth_Part_Operation]] 상에서 설정된 검색 공간 집합에 따라 [[PDCCH]] 후보를 모니터링한다. 모니터링 과정에서 단말은 다음의 제약 사항을 고려한다:
- 추가적인 활성 [[TCI_State_Management]]가 설정된 경우 이를 PDCCH 수신에 적용한다.
- [[PDCCH_Monitoring_Capability]]에 따라 슬롯당, 스팬당, 또는 슬롯 그룹당 최대 [[PDCCH]] 후보 수 및 비중첩 [[CCE]] 수를 준수해야 한다.
- 특정 [[SS_PBCH_Block_Generation]] 자원과 [[PDCCH]] 후보가 겹치는 경우, TS 38.213 §10에 명시된 조건에 따라 모니터링 생략 여부를 결정한다.
- [[LTE_CRS]]와의 자원 중첩이 발생하는 경우, 단말의 설정에 따라 모니터링 여부가 결정된다.
- [[DCI_Field_Mapping]]을 통해 전달되는 가용 RB 세트 지시자가 있는 경우, 해당 자원을 제외하고 모니터링을 수행한다.

다중 셀 환경(Carrier Aggregation)이나 [[Dual_Connectivity_Power_Sharing]] 환경에서는 단말의 블라인드 디코딩 능력(pdcch-BlindDetectionCA 등)에 따라 모니터링 가능한 최대 후보 수가 제한된다.

## 인과 관계
- [[PDCCH]] depends_on [[CORESET_Configuration]] (PDCCH가 전송되는 자원 영역 정의)
- [[PDCCH]] depends_on [[PDCCH_Search_Space_Configuration]] (모니터링할 후보군 및 주기 정의)
- [[PDCCH]] depends_on [[PDCCH_Monitoring_Capability]] (단말의 최대 모니터링 능력 제한)
- [[PDCCH]] triggers [[PDSCH_Reception_Procedure]] (DCI를 통한 하향링크 자원 할당)
- [[PDCCH]] triggers [[PUSCH_Transmission_Procedure]] (DCI를 통한 상향링크 자원 할당)
- [[PDCCH]] implements [[DCI_Field_Mapping]] (제어 정보의 비트 필드 구성)

## 관련 개념
- [[CORESET_Configuration]] (depends_on)
- [[PDCCH_Search_Space_Configuration]] (depends_on)
- [[PDCCH_Monitoring_Capability]] (depends_on)
- [[DCI_Field_Mapping]] (implements)
- [[PDCCH_Scrambling]] (part_of)
- [[PDCCH_Resource_Mapping]] (part_of)
- [[PDCCH_DMRS_Generation]] (part_of)

## 스펙 근거
- TS 38.211 §7.3.2: Physical downlink control channel (PDCCH) 물리적 특성 정의
- TS 38.212 §7.3: Downlink control information 코딩 절차
- TS 38.213 §10: UE procedure for receiving control information 모니터링 절차 및 능력 제한

## 소스
- 3GPP TS 38.211 (Physical channels and modulation)
- 3GPP TS 38.212 (Multiplexing and channel coding)
- 3GPP TS 38.213 (Physical layer procedures for control)