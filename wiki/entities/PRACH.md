# PRACH

## 정의
[[PRACH]]는 5G NR 시스템에서 [[UE]]가 네트워크에 초기 접속하거나, 동기화 상태를 재설정하기 위해 사용하는 상향링크 물리 채널입니다.

## 요약
[[PRACH]]는 랜덤 액세스 절차의 핵심 요소로, [[UE]]가 네트워크와 통신을 시작하기 위해 전송하는 프리앰블 시퀀스를 전달합니다. 이 채널은 [[Basic initial access channels and procedures]]를 통해 항상 지원되며, 다양한 환경(NTN, Wideband 등)에 대응하기 위한 선택적 기능들을 포함합니다.

## 상세 설명
[[PRACH]] 전송은 [[TS 38.211 §6.3.3]]에 정의된 절차를 따릅니다.

1. [[PRACH_Sequence_Generation]]: [[UE]]는 상위 계층에서 설정된 파라미터에 따라 Zadoff-Chu 시퀀스 기반의 프리앰블을 생성합니다.
2. [[PRACH_Resource_Mapping]]: 생성된 시퀀스는 시간 및 주파수 영역의 특정 자원에 매핑됩니다. 이때 [[PRACH]]의 포맷에 따라 서브캐리어 간격과 심볼 구조가 결정됩니다.
3. 전력 제어: [[PRACH_Power_Control]]을 통해 전송 전력이 결정되며, 이는 초기 접속 성공률과 셀 내 간섭에 직접적인 영향을 미칩니다.

## 인과 관계
- [[PRACH_Sequence_Generation]] (part_of) [[PRACH]]
- [[PRACH_Resource_Mapping]] (part_of) [[PRACH]]
- [[PRACH_Power_Control]] (affects) [[PRACH]]
- [[RACH_Procedure_L1]] (triggers) [[PRACH]]
- [[Basic initial access channels and procedures]] (depends_on) [[PRACH]]

## 관련 개념
- [[Basic initial access channels and procedures]] (part_of)
- [[Wideband PRACH]] (similar_to)
- [[RA-SDT in NTN]] (similar_to)
- [[MT-SDT]] (similar_to)
- [[MT-SDT for NTN]] (similar_to)
- [[Parallel PRACH and SRS/PUCCH/PUSCH transmissions across CCs in inter-band CA]] (similar_to)
- [[UL channel access for semi-static channel access mode]] (similar_to)
- [[SSB-based RRM for semi-static channel access mode]] (similar_to)
- [[SSB-based RLM for dynamic channel access mode]] (similar_to)
- [[SSB-based RLM for semi-static channel access mode]] (similar_to)
- [[SSB-based BFD/CBD for dynamic channel access mode]] (similar_to)
- [[SSB-based BFD/CBD for semi-static channel access mode]] (similar_to)
- [[Link_Recovery_Procedures]] (affects)
- [[OFDM_Baseband_Signal_Generation]] (affects)
- [[PUSCH_MsgA_Transmission]] (affects)
- [[RACH_Procedure_DCI_Trigger]] (affects)
- [[SRS_Collision_Handling]] (affects)
- [[Slot_Format_Configuration]] (affects)
- [[Uplink_Power_Control]] (affects)
- [[Uplink_Power_Prioritization]] (affects)

## 스펙 근거
- TS 38.211 §6.3.3.1에 따르면 [[PRACH]] 시퀀스 생성 방식이 규정되어 있습니다.
- TS 38.211 §6.3.3.2에 따르면 [[PRACH]]의 물리 자원 매핑 방식이 규정되어 있습니다.

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/Link_Recovery_Procedures.md
- concepts/OFDM_Baseband_Signal_Generation.md
- concepts/PRACH_Power_Control.md
- concepts/PRACH_Resource_Mapping.md
- concepts/PRACH_Sequence_Generation.md
- concepts/PUSCH_MsgA_Transmission.md
- concepts/RACH_Procedure_DCI_Trigger.md
- concepts/RACH_Procedure_L1.md
- concepts/SRS_Collision_Handling.md
- concepts/Slot_Format_Configuration.md
- concepts/Uplink_Power_Control.md
- concepts/Uplink_Power_Prioritization.md
- entities/PRACH.md