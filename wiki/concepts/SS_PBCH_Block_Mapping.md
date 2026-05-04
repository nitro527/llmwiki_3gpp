# SS_PBCH_Block_Mapping

## 정의
[[SS_PBCH_Block_Mapping]]은 5G NR 시스템에서 [[SS_PBCH_Block]]을 구성하는 [[PSS]], [[SSS]], [[PBCH]], 그리고 [[DMRS]]가 시간-주파수 자원 그리드 상에 어떻게 배치되는지를 정의하는 절차입니다.

## 요약
[[SS_PBCH_Block]]은 4개의 [[OFDM]] 심볼과 240개의 부반송파로 구성된 시간-주파수 자원 블록입니다. 이 블록 내에서 각 물리 채널 및 신호는 고정된 위치에 매핑되어 [[UE]]가 초기 접속 및 셀 탐색을 수행할 수 있도록 합니다. 본 절차는 [[TS 38.211]]에 명시된 물리 계층의 핵심 메커니즘으로, [[Basic_initial_access_channels_and_procedures]]를 지원하기 위한 필수 요소입니다.

## 상세 설명
[[SS_PBCH_Block]] 내의 자원 매핑은 다음과 같이 수행됩니다.

1. [[PSS]] (Primary Synchronization Signal):
   - [[SS_PBCH_Block]]의 첫 번째 심볼에 매핑됩니다.
   - 127개의 부반송파를 점유하며, 주파수 도메인에서 특정 오프셋을 가지고 배치됩니다.

2. [[SSS]] (Secondary Synchronization Signal):
   - [[SS_PBCH_Block]]의 세 번째 심볼에 매핑됩니다.
   - 127개의 부반송파를 점유하며, [[PSS]]와 동일한 주파수 오프셋을 가집니다.

3. [[PBCH]] 및 [[DMRS]] (Demodulation Reference Signal):
   - [[PBCH]]는 두 번째 심볼 전체, 네 번째 심볼 전체, 그리고 세 번째 심볼 중 [[SSS]]가 점유하지 않는 영역에 매핑됩니다.
   - [[DMRS]]는 [[PBCH]]의 복조를 위해 [[PBCH]]가 매핑되는 심볼들에 분산되어 배치됩니다.

## 인과 관계
- [[SS_PBCH_Block_Mapping]]은 [[Synchronization_Signal_Generation]]에 의해 생성된 신호를 물리 자원에 배치하는 역할을 수행합니다.
- 본 매핑 절차는 [[UE]]의 [[Basic_initial_access_channels_and_procedures]]를 triggers 합니다.
- [[SS_PBCH_Block]]의 자원 구성은 [[Frame_Structure_Numerology]]에 depends_on 합니다.

## 관련 개념
- [[SS_PBCH_Block]] (part_of)
- [[PSS]] (part_of)
- [[SSS]] (part_of)
- [[PBCH]] (part_of)
- [[DMRS]] (part_of)
- [[Synchronization_Signal_Generation]] (affects)
- [[Basic_initial_access_channels_and_procedures]] (triggers)

## 스펙 근거
- [[TS 38.211]] §7.4.3.1에 따르면, [[SS_PBCH_Block]]은 4개의 [[OFDM]] 심볼과 240개의 부반송파로 구성됩니다.
- [[TS 38.211]] §7.4.3.1.1에 따라 [[PSS]]는 첫 번째 심볼에 매핑됩니다.
- [[TS 38.211]] §7.4.3.1.2에 따라 [[SSS]]는 세 번째 심볼에 매핑됩니다.
- [[TS 38.211]] §7.4.3.1.3에 따라 [[PBCH]] 및 [[DMRS]]는 지정된 심볼 내의 가용 자원에 매핑됩니다.

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03), "Physical channels and modulation"
  - §7.4.3.1 Time-frequency structure of an SS/PBCH block
  - §7.4.3.1.1 Mapping of PSS within an SS/PBCH block
  - §7.4.3.1.2 Mapping of SSS within an SS/PBCH block
  - §7.4.3.1.3 Mapping of PBCH and DM-RS within an SS/PBCH block