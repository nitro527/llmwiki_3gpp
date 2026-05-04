# SRS_Carrier_Switching

## 정의
[[SRS]] Carrier Switching은 [[UE]]가 서로 다른 [[Component_Carrier]] 간에 상향링크 전송 경로를 전환하여 [[Sounding_Reference_Signal]]을 전송하는 절차를 의미합니다.

## 요약
본 기능은 [[UE]]가 다중 캐리어 환경에서 특정 [[Component_Carrier]]로 RF 자원을 리튜닝하여 [[SRS]]를 전송할 수 있게 합니다. 이 과정에서 발생하는 RF 리튜닝 시간 동안의 데이터 전송 중단 관리 및 캐리어 간 전송 충돌 시의 우선순위 규칙이 정의됩니다.

## 상세 설명
[[SRS]] Carrier Switching은 [[UE]]의 능력에 따라 지원 여부가 결정됩니다. 주요 메커니즘은 다음과 같습니다.

- **RF 리튜닝**: [[UE]]가 소스 캐리어에서 타겟 캐리어로 전송 경로를 변경할 때 필요한 시간(RF retuning time)을 확보해야 합니다.
- **전송 우선순위**: [[SRS]] 전송과 [[PUSCH]] 또는 [[PUCCH]] 전송이 충돌하거나, 리튜닝 시간으로 인해 데이터 전송이 불가능한 경우, 스펙에 정의된 우선순위 규칙에 따라 상향링크 전송이 일시 중단되거나 조정됩니다.
- **UE 능력**: [[SRS_Tx_switch]] (2-55)는 필수 능력으로 요구되며, 그 외 [[SRS_carrier_switch]] (2-56), [[Application_of_DL_interruptions_due_to_UL_Tx_switching_between_two_uplink_carriers]] (7-2) 등 다수의 선택적 기능이 존재합니다.

## 인과 관계
- [[SRS_Tx_switch]] (depends_on) [[SRS_Carrier_Switching]]
- [[SRS_Carrier_Switching]] (triggers) [[Uplink_Switching_Procedures]]
- [[SRS_Carrier_Switching]] (affects) [[PUSCH_Transmission_Procedures]]

## 관련 개념
- [[SRS]] (part_of)
- [[Component_Carrier]] (part_of)
- [[Uplink_Switching_Procedures]] (similar_to)
- [[PUSCH]] (affects)

## 스펙 근거
- TS 38.214 §6.2.1.3에 따르면, [[UE]]는 상위 계층 파라미터에 의해 설정된 경우 서로 다른 [[Component_Carrier]] 간에 [[SRS]] 전송을 위한 스위칭을 수행할 수 있습니다.
- TS 38.214 §6.2.1.3은 [[SRS]] 전송을 위해 필요한 RF 리튜닝 시간과 이로 인해 발생하는 상향링크 전송의 일시 중단 조건 및 우선순위 규칙을 명시합니다.

## 소스
- 3GPP TS 38.214 V17.9.0, "NR; Physical layer procedures for data"
- 3GPP TS 38.822, "NR; User Equipment (UE) radio transmission and reception"