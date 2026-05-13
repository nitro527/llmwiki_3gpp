# PBCH_DMRS_Generation

## 정의
[[PBCH]]의 복조를 위해 사용되는 [[DMRS]] 시퀀스를 생성하고, 이를 [[SS_PBCH_Block_Generation]] 내의 특정 자원 요소에 매핑하는 절차를 의미합니다.

## 요약
[[PBCH]] [[DMRS]]는 [[SS_PBCH_Block_Generation]] 내에서 채널 추정을 위해 사용됩니다. 시퀀스는 [[SS_PBCH_Block_Generation]]의 인덱스와 반-프레임 정보를 기반으로 초기화되며, 정의된 시간 및 주파수 자원 요소에 매핑됩니다.

## 상세 설명
[[PBCH]] [[DMRS]] 시퀀스 생성 및 매핑은 TS 38.211 §7.4.1.4.1 및 §7.4.3.1.3에 따라 수행됩니다.

### 시퀀스 생성
[[DMRS]] 시퀀스는 [[Sequence_Generation]]에서 정의된 의사 난수 시퀀스를 기반으로 생성됩니다. 스크램블링 시퀀스 생성기는 각 [[SS_PBCH_Block_Generation]] 발생 시점에 다음 값으로 초기화됩니다.

- $c_{init} = 2^{11}(\bar{i}_{SSB} + 1) + 2^6(\bar{v} + 1) + \bar{i}_{SSB}$
- 여기서 $\bar{i}_{SSB}$는 [[SS_PBCH_Block_Generation]] 인덱스의 하위 비트이며, $\bar{v}$는 반-프레임 번호 및 인덱스 관련 정보입니다.
- 구체적으로, $L_{max}=4$인 경우 $\bar{i}_{SSB}$는 인덱스의 하위 2비트이며, $L_{max}=8$ 또는 $64$인 경우 하위 3비트를 사용합니다.

### 자원 매핑
[[PBCH]] 및 [[DMRS]] 심볼은 [[SS_PBCH_Block_Generation]] 내에서 전력 할당 계수 $\beta_{PBCH}$ 및 $\beta_{DMRS}$에 의해 스케일링됩니다.

- [[DMRS]]는 [[SS_PBCH_Block_Generation]] 내의 특정 자원 요소($k, l$)에 매핑됩니다.
- 매핑 순서는 주파수 인덱스 $k$가 증가하는 순서대로, 그 다음 시간 인덱스 $l$이 증가하는 순서대로 진행됩니다.
- [[PBCH]] 데이터 심볼은 [[DMRS]]가 점유하지 않은 나머지 자원 요소에 동일한 순서로 매핑됩니다.
- 구체적인 주파수 및 시간 인덱스 위치는 TS 38.211의 Table 7.4.3.1-1에 정의된 값을 따릅니다.

## 인과 관계
- [[PBCH_DMRS_Generation]] depends_on [[SS_PBCH_Block_Generation]] (SSB 인덱스 및 반-프레임 정보 사용)
- [[PBCH_DMRS_Generation]] implements [[DMRS_Sequence_Generation]] (PBCH 전용 DMRS 시퀀스 생성 로직 구현)
- [[PBCH_DMRS_Generation]] affects [[PBCH]] (채널 추정을 통한 복조 성능 결정)

## 관련 개념
- [[SS_PBCH_Block_Generation]] (part_of)
- [[DMRS_Sequence_Generation]] (implements)
- [[PBCH]] (affects)
- [[Sequence_Generation]] (depends_on)

## 스펙 근거
- TS 38.211 §7.4.1.4.1 (Sequence generation)
- TS 38.211 §7.4.3.1.3 (Mapping of PBCH and DM-RS within an SS/PBCH block)

## 소스
- 3GPP TS 38.211 V16.9.0 (Release 16)