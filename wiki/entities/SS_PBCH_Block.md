# SS_PBCH_Block

## 정의
[[SS_PBCH_Block]] (Synchronization Signal/Physical Broadcast Channel Block)은 5G NR 시스템에서 [[UE]]가 셀을 탐색하고, 동기를 획득하며, 시스템 정보를 수신하기 위해 사용하는 물리 계층의 기본 단위입니다.

## 요약
[[SS_PBCH_Block]]은 [[PSS]], [[SSS]], [[PBCH]], 그리고 [[DMRS]]로 구성됩니다. [[UE]]는 이 블록을 통해 하향링크 동기화, 셀 ID 식별, 그리고 [[MIB]] 수신을 수행합니다. 본 개체와 관련된 주요 기능으로 [[Radio_Link_Monitoring]], [[SS_SINR]] 측정, [[CSI_RS]] 기반 측정 등이 있으며, [[SCell]] 운용 시 본 블록의 유무에 따른 다양한 지원 기능이 정의되어 있습니다.

## 상세 설명
[[SS_PBCH_Block]]은 시간 및 주파수 영역에서 고정된 구조를 가집니다.
- 시간 영역: 4개의 [[OFDM]] 심볼로 구성되며, 심볼 인덱스에 따라 [[PSS]], [[SSS]], [[PBCH]] 및 [[DMRS]]가 매핑됩니다 (TS 38.211 §7.4.3.1).
- 주파수 영역: 240개의 부반송파를 점유하며, 이는 20개의 [[Resource_Block]]에 해당합니다.
- 구성 요소:
    - [[PSS]]: 초기 동기화 및 셀 ID의 하위 계층 식별을 위해 사용됩니다.
    - [[SSS]]: 셀 ID의 상위 계층 식별 및 프레임 동기화를 위해 사용됩니다.
    - [[PBCH]]: [[MIB]]를 전송하며, 시스템 초기 접속에 필요한 핵심 정보를 포함합니다.
    - [[DMRS]]: [[PBCH]] 복조를 위한 참조 신호로 사용됩니다.

## 인과 관계
- [[Cell_Search]] (triggers) [[SS_PBCH_Block]] 수신
- [[SS_PBCH_Block]] (depends_on) [[Synchronization_Signal_Generation]]
- [[SS_PBCH_Block]] (affects) [[Radio_Link_Monitoring]]
- [[SS_PBCH_Block]] (part_of) [[Frame_Structure_Numerology]]

## 관련 개념
- [[PSS]] (part_of)
- [[SSS]] (part_of)
- [[PBCH]] (part_of)
- [[DMRS]] (part_of)
- [[Cell_Search]] (depends_on)
- [[Radio_Link_Monitoring]] (depends_on)
- [[MIB]] (part_of)

## 스펙 근거
- TS 38.211 §7.4.3: [[SS_PBCH_Block]]의 시간-주파수 구조 및 매핑 규칙 정의
- TS 38.211 §7.4.3.1: [[PSS]], [[SSS]], [[PBCH]], [[DMRS]]의 상세 매핑 위치
- TS 38.211 §7.4.3.2: [[SS_PBCH_Block]]의 시간 위치 결정 방식
- TS 38.213 §4.1: [[Cell_Search]] 절차에서의 [[SS_PBCH_Block]] 활용

## 소스
- 3GPP TS 38.211 v16.9.0 (Release 16)
- 3GPP TS 38.213 v16.8.0 (Release 16)