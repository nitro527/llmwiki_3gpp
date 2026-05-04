# Sidelink_DMRS_Generation_Mapping

## 정의
[[Sidelink]] 통신에서 수신단이 채널 추정 및 복조를 수행할 수 있도록 지원하는 [[Reference_Signals]]인 [[DMRS]]의 시퀀스 생성 및 물리 자원 매핑 절차를 의미합니다. 이는 [[PSSCH]], [[PSCCH]], [[PSBCH]] 각각에 대해 정의됩니다.

## 요약
[[Sidelink]] [[DMRS]]는 각 채널의 특성에 따라 [[Sequence_Generation]]을 통해 시퀀스를 생성하고, 정의된 [[Physical_Resource_Grid]] 내의 자원 요소(RE)에 매핑됩니다. 각 채널은 고유한 스크램블링 식별자 및 매핑 규칙을 가지며, 이는 수신단에서의 정확한 채널 추정을 보장합니다.

## 상세 설명
### PSSCH DMRS
[[PSSCH]]를 위한 [[DMRS]]는 TS 38.211 §8.4.1.1에 따라 생성 및 매핑됩니다. 시퀀스 생성 시 상위 계층 파라미터 및 슬롯 내 심볼 위치가 반영되며, 자원 매핑은 [[PSSCH]]가 할당된 주파수 및 시간 자원 내에서 수행됩니다.

### PSCCH DMRS
[[PSCCH]]를 위한 [[DMRS]]는 TS 38.211 §8.4.1.3에 따라 생성 및 매핑됩니다. [[PSCCH]]는 제어 정보를 포함하므로, [[DMRS]]는 제어 채널의 복조 성능을 최적화하기 위해 고정된 위치의 RE에 매핑됩니다.

### PSBCH DMRS
[[PSBCH]]를 위한 [[DMRS]]는 TS 38.211 §8.4.1.4에 따라 생성 및 매핑됩니다. 이는 [[Sidelink]] 동기화 및 초기 접속을 위해 필수적이며, 특정 시퀀스 생성 규칙을 따릅니다.

## 인과 관계
- [[Sequence_Generation]] (depends_on) [[Sidelink_DMRS_Generation_Mapping]]
- [[Sidelink_Resource_Grid]] (affects) [[Sidelink_DMRS_Generation_Mapping]]
- [[Sidelink_DMRS_Generation_Mapping]] (triggers) [[Sidelink_Transmission_Procedures]]

## 관련 개념
- [[PSSCH]] (part_of)
- [[PSCCH]] (part_of)
- [[PSBCH]] (part_of)
- [[DMRS]] (part_of)
- [[Reference_Signals]] (similar_to)

## 스펙 근거
- TS 38.211 §8.4.1.1: [[PSSCH]]를 위한 [[DMRS]] 시퀀스 생성 및 매핑
- TS 38.211 §8.4.1.3: [[PSCCH]]를 위한 [[DMRS]] 시퀀스 생성 및 매핑
- TS 38.211 §8.4.1.4: [[PSBCH]]를 위한 [[DMRS]] 시퀀스 생성 및 매핑

## 소스
- 3GPP TS 38.211 V17.9.0 (Release 17)