# Synchronization_Signal_Generation

## 정의
[[Synchronization_Signal_Generation]]은 [[NR]] 시스템에서 [[UE]]가 하향링크 동기를 획득하고, [[Physical_layer_cell_identity]]를 식별하기 위해 사용하는 [[PSS]] 및 [[SSS]]의 시퀀스 생성 및 물리 자원 매핑 절차를 의미합니다.

## 요약
[[Synchronization_Signal_Generation]]은 [[SS_PBCH_Block]]의 핵심 구성 요소인 [[PSS]]와 [[SSS]]를 생성하여 시간-주파수 자원에 매핑합니다. [[PSS]]는 3개의 [[Physical_layer_cell_identity]] 그룹 내 식별자를 제공하며, [[SSS]]는 336개의 [[Physical_layer_cell_identity]] 그룹 식별자를 제공하여 총 1008개의 고유한 [[Physical_layer_cell_identity]]를 구성합니다.

## 상세 설명
### Physical-layer cell identities
[[Physical_layer_cell_identity]]는 $N_{ID}^{(1)} \in \{0, 1, \dots, 335\}$와 $N_{ID}^{(2)} \in \{0, 1, 2\}$의 조합으로 정의되며, 전체 식별자는 $N_{ID}^{cell} = 3N_{ID}^{(1)} + N_{ID}^{(2)}$로 계산됩니다.

### Primary synchronization signal (PSS)
[[PSS]] 시퀀스는 [[m-sequence]]를 기반으로 생성됩니다. 시퀀스 생성은 $N_{ID}^{(2)}$에 따라 결정되며, 생성된 시퀀스는 [[SS_PBCH_Block]] 내의 특정 주파수 자원에 매핑됩니다.

### Secondary synchronization signal (SSS)
[[SSS]] 시퀀스는 2개의 [[m-sequence]]의 조합(Gold sequence 기반)으로 생성됩니다. 시퀀스 생성은 $N_{ID}^{(1)}$과 $N_{ID}^{(2)}$에 의해 결정되며, [[PSS]]와 마찬가지로 [[SS_PBCH_Block]] 내의 정의된 자원 요소에 매핑됩니다.

## 인과 관계
- [[Physical_layer_cell_identity]] (depends_on) [[PSS]]
- [[Physical_layer_cell_identity]] (depends_on) [[SSS]]
- [[SS_PBCH_Block]] (part_of) [[PSS]]
- [[SS_PBCH_Block]] (part_of) [[SSS]]

## 관련 개념
- [[SS_PBCH_Block]] (part_of)
- [[Sequence_Generation]] (similar_to)
- [[Physical_Resource_Grid]] (depends_on)

## 스펙 근거
- TS 38.211 §7.4.2.1에 따르면 [[Physical_layer_cell_identity]]는 $N_{ID}^{(1)}$과 $N_{ID}^{(2)}$의 조합으로 정의됩니다.
- TS 38.211 §7.4.2.2.1 및 §7.4.2.2.2에 따르면 [[PSS]] 시퀀스 생성 및 자원 매핑 절차가 정의됩니다.
- TS 38.211 §7.4.2.3.1 및 §7.4.2.3.2에 따르면 [[SSS]] 시퀀스 생성 및 자원 매핑 절차가 정의됩니다.

## 소스
- 3GPP TS 38.211 V17.x.x (Release 17), "Physical channels and modulation"