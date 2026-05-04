# PDCCH

## 정의
[[PDCCH]]는 [[5G NR]] 시스템에서 [[DCI]]를 전송하기 위해 사용되는 물리 채널로, [[PDSCH]] 및 [[PUSCH]]의 스케줄링 정보, [[Slot]] 포맷 표시, [[TPC]] 명령 등을 전달합니다.

## 요약
[[PDCCH]]는 [[CORESET]] 내의 [[CCE]] 집합을 통해 전송되며, [[UE]]는 설정된 [[Search_Space]] 내에서 블라인드 디코딩을 수행하여 제어 정보를 획득합니다. Rel-16 이후 도입된 향상된 모니터링 능력과 [[TCI]] 상태 관리 기능을 통해 유연한 빔 관리 및 자원 효율성을 제공합니다.

## 상세 설명
[[PDCCH]]의 전송 및 수신 절차는 다음과 같은 핵심 요소로 구성됩니다.

*   **[[CORESET]] 및 [[CCE]]**: [[PDCCH]]는 [[CORESET]] 내에서 [[CCE]] 단위로 리소스가 할당됩니다. TS 38.211 §7.3.2.1에 따라 하나의 [[PDCCH]]는 1, 2, 4, 8, 16개의 [[CCE]]로 구성된 [[Aggregation_Level]]을 가집니다.
*   **[[DCI]] 전송**: [[PDCCH]]는 [[DCI]]를 운반하며, 이는 [[CRC]]가 [[RNTI]]로 스크램블링된 형태입니다. TS 38.212 §7.3에 정의된 다양한 [[DCI_Formats_Processing]]을 통해 스케줄링 정보가 전달됩니다.
*   **[[TCI]] 상태 및 [[QCL]]**: [[UE]]는 [[CORESET]]에 대해 하나 이상의 [[TCI]] 상태를 설정받을 수 있습니다. TS 38.213 §10.1에 따라, [[UE]]는 [[QCL]] 가정을 바탕으로 [[PDCCH]]를 수신하며, 이는 빔 관리의 핵심이 됩니다. Rel-16에서는 [[CORESET]]당 다중 [[TCI]] 상태 구성(3-4) 및 추가적인 활성 [[TCI]] 상태(2-4a)가 지원됩니다.
*   **모니터링 능력**: [[UE]]는 [[PDCCH_Monitoring_Procedures]]를 통해 특정 [[Slot]] 내의 OFDM 심볼 구간에서 모니터링을 수행합니다. Rel-16 PDCCH monitoring capability(11-2) 및 3개 심볼 구간 모니터링(3-2) 등을 통해 [[UE]]의 처리 성능에 따른 유연한 스케줄링이 가능합니다.
*   **자원 매핑**: [[PDCCH_Resource_Mapping]]은 [[CORESET]] 내의 [[REG]] 번들링을 기반으로 수행되며, TS 38.211 §7.3.2.5에 따라 물리 자원에 매핑됩니다.

## 인과 관계
*   [[CORESET]] 설정 (depends_on) [[PDCCH_CORESET_Mapping]]
*   [[DCI]] 전송 (triggers) [[PDSCH_Reception_Procedures]] 또는 [[PUSCH_Transmission_Procedures]]
*   [[TCI]] 상태 설정 (affects) [[PDCCH]] 수신 빔 형성
*   [[PDCCH]] 모니터링 능력 (affects) [[PDCCH_Monitoring_Procedures]]의 스케줄링 밀도

## 관련 개념
*   [[CORESET]] (part_of)
*   [[DCI]] (part_of)
*   [[CCE]] (part_of)
*   [[Search_Space]] (depends_on)
*   [[TCI]] (affects)
*   [[QCL]] (depends_on)
*   [[PDCCH_Monitoring_Procedures]] (triggers)

## 스펙 근거
*   TS 38.211 §7.3.2: [[PDCCH]] 물리 채널 구조, [[CCE]], [[CORESET]], 스크램블링 및 자원 매핑 정의.
*   TS 38.212 §7.3: [[DCI]] 포맷, [[CRC]] 부착, 채널 코딩 및 레이트 매칭.
*   TS 38.213 §10: [[UE]]의 [[PDCCH]] 수신 절차, 검색 공간, 모니터링 및 [[PDCCH]] 검증 절차.
*   TS 38.822: Rel-16 PDCCH 모니터링 능력 및 [[TCI]] 상태 관련 [[UE]] 피처 정의.

## 소스
*   3GPP TS 38.211 "Physical channels and modulation"
*   3GPP TS 38.212 "Multiplexing and channel coding"
*   3GPP TS 38.213 "Physical layer procedures for control"
*   3GPP TS 38.822 "UE features"