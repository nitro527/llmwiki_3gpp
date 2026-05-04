# SRS

## 정의
[[SRS]] (Sounding Reference Signal)는 [[UE]]가 상향링크 채널 품질을 측정하고, [[gNB]]가 이를 기반으로 상향링크 스케줄링, 빔포밍, 전력 제어 등을 수행할 수 있도록 지원하는 상향링크 참조 신호입니다.

## 요약
[[SRS]]는 [[gNB]]의 요청에 따라 [[UE]]가 전송하는 신호로, 주파수 선택적 스케줄링 및 채널 상태 정보 획득을 위해 사용됩니다. 본 페이지는 [[TS 38.213]] §7.3에 정의된 [[UE]] 동작을 중심으로 기술합니다.

## 상세 설명
[[SRS]] 전송은 [[gNB]]로부터의 상위 계층 시그널링 또는 [[DCI]]를 통해 트리거됩니다. [[UE]]는 설정된 [[SRS]] 자원 세트 내에서 자원을 선택하여 전송하며, 주요 동작은 다음과 같습니다.

- [[SRS]] 전송 시점 및 자원 설정: [[gNB]]는 [[SRS-ResourceSet]] 및 [[SRS-Resource]]를 통해 시간/주파수 자원, 시퀀스 정보, 콤(comb) 구조 등을 설정합니다.
- [[UE]] 동작: [[UE]]는 설정된 자원에 따라 [[SRS]]를 생성하고 전송합니다. 이때 [[SRS]] 전송은 [[PUSCH]] 전송이나 다른 상향링크 채널과의 우선순위 규칙에 따라 결정됩니다.
- [[CLI]] 측정: [[UE]]는 [[CLI]] (Cross-Link Interference) 측정을 위해 [[SRS]] 자원을 활용할 수 있으며, 이는 [[RSSI]] 측정 등을 포함합니다.
- [[SRS-RSRP]] 측정: [[UE]]는 특정 [[SRS]] 자원을 기반으로 [[RSRP]]를 측정하여 보고할 수 있습니다.

## 인과 관계
- [[SRS]] (triggers) [[gNB]]의 상향링크 스케줄링 결정
- [[SRS]] (depends_on) [[UE]]의 상향링크 전력 제어 설정
- [[SRS]] (affects) [[PUSCH]] 프리코딩 및 빔포밍 가중치 계산

## 관련 개념
- [[SRS_Generation_Mapping]] (part_of)
- [[SRS_Power_Control]] (depends_on)
- [[SRS_Collision_Handling]] (triggers)
- [[SRS_Carrier_Switching]] (similar_to)
- [[PUSCH]] (affects)

## 스펙 근거
- [[TS 38.213]] §7.3: [[SRS]] 전송을 위한 [[UE]] 동작 및 트리거링 메커니즘 정의
- Feature 17-4: Simultaneous reception of DL signals/channels and SRS-RSRP measurement resource
- Feature 16-1c: Default spatial relation
- Feature 16-1e: Pathloss reference RS activation via MAC CE
- Feature 17-2: SRS-RSRP measurement
- Feature 17-3: Simultaneous reception of DL signals/channels and CLI-RSSI measurement resource
- Feature 23-1-1m: Indication/configuration of R17 TCI states for SRS
- Feature 23-3-1, 23-3-1-1, 23-3-1-2, 23-3-1-3: Multi-TRP [[PUSCH]] repetition 관련 [[SRS]] 설정
- Feature 23-8-6, 23-8-11: Partial frequency sounding of [[SRS]]

## 소스
- 3GPP TS 38.213 v18.0.0 (2024-03) "NR; Physical layer procedures for control"
- 3GPP TS 38.822 v17.0.0 (2022-03) "NR; Study on enhancements for CLI"