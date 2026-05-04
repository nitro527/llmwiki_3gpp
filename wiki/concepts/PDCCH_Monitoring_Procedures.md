# PDCCH_Monitoring_Procedures

## 정의
[[PDCCH]] Monitoring Procedures는 [[UE]]가 하향링크 제어 정보를 수신하기 위해 특정 시간 및 주파수 자원 내에서 [[PDCCH]]를 탐색하고 복호화하는 일련의 절차를 의미합니다.

## 요약
[[UE]]는 상위 계층 시그널링을 통해 설정된 [[Search_Space]] 내에서 [[PDCCH]]를 모니터링합니다. 이 과정에서 [[Slot]] 내의 시간적 제약(Span), [[SS_PBCH_Block]] 및 [[LTE_CRS]]와의 자원 충돌 회피, 그리고 [[DCI_Formats_Processing]]을 통한 스케줄링 정보 획득이 수행됩니다.

## 상세 설명
[[PDCCH]] 모니터링은 [[Search_Space]] 세트 그룹을 기반으로 수행되며, [[UE]]는 설정된 모니터링 주기와 오프셋에 따라 [[PDCCH]] 후보군을 검사합니다.

- **PDCCH Monitoring Capability**: [[UE]]는 [[Slot]] 내에서 모니터링할 수 있는 [[OFDM]] 심볼의 수와 위치에 따라 제한을 가집니다. 이는 [[Span]] 기반으로 관리되며, 특정 [[UE]]는 [[Slot]] 내 임의의 3개 연속 [[OFDM]] 심볼 내에서 모니터링을 수행하거나, [[Span_Gap]]을 포함한 유연한 모니터링을 지원합니다.
- **Search Space Configuration**: [[Search_Space]]는 [[CORESET]]과 연계되어 설정되며, [[UE]]가 특정 [[DCI]] 포맷을 탐색해야 하는 시간/주파수 자원을 정의합니다.
- **Resource Collision Handling**: [[PDCCH]] 모니터링 자원이 [[SS_PBCH_Block]]이나 [[LTE_CRS]]와 겹치는 경우, [[UE]]는 스펙에 정의된 우선순위 규칙에 따라 해당 자원에서의 [[PDCCH]] 수신을 생략하거나 조정합니다.
- **Monitoring Indication**: [[UE]]는 [[PDCCH]] 모니터링 표시(Indication)를 통해 특정 [[SCell]]에 대한 모니터링 활성화/비활성화 또는 휴면(Dormancy) 상태로의 전환을 수행합니다.

## 인과 관계
- [[Search_Space]] (depends_on) [[CORESET]]
- [[PDCCH]] 모니터링 (affects) [[PDSCH]] 수신 및 [[PUSCH]] 전송
- [[SS_PBCH_Block]] (triggers) [[PDCCH]] 모니터링 자원 회피 절차
- [[DCI_Formats_Processing]] (depends_on) [[PDCCH]] 모니터링 성공

## 관련 개념
- [[PDCCH]] (part_of)
- [[CORESET]] (part_of)
- [[Search_Space]] (part_of)
- [[Slot]] (part_of)
- [[SS_PBCH_Block]] (affects)
- [[DCI_Formats_Processing]] (depends_on)

## 스펙 근거
- TS 38.213 §10에 따르면 [[UE]]는 [[PDCCH]] 수신을 위한 제어 정보 결정 절차를 수행해야 합니다.
- TS 38.213 §10.1에 따르면 [[PDCCH]] 모니터링을 위한 [[Search_Space]] 세트 구성 및 [[Self_Carrier_Scheduling]]과 [[Cross_Carrier_Scheduling]] 절차가 정의됩니다.
- TS 38.213 §10.3에 따르면 [[SCell]]에 대한 [[PDCCH]] 모니터링 표시 및 휴면 상태 동작이 규정됩니다.
- TS 38.213 §10.4에 따르면 [[Search_Space]] 세트 그룹 전환 및 모니터링 건너뛰기(Skipping) 절차가 명시됩니다.

## 소스
- 3GPP TS 38.213 (Release 18) §10, §10.1, §10.2, §10.3, §10.4, §10.5