# UCI_Processing_PUCCH

## 정의
[[UCI_Processing_PUCCH]]는 [[UE]]가 상향링크 제어 정보인 [[UCI]]를 [[PUCCH]]를 통해 전송하기 위해 수행하는 일련의 신호 처리 절차를 의미합니다.

## 요약
[[UCI_Processing_PUCCH]]는 [[HARQ-ACK]], [[SR]], [[CSI]]와 같은 제어 정보를 비트 단위로 생성하고, 채널 코딩, 레이트 매칭 및 멀티플렉싱을 거쳐 최종적으로 [[PUCCH]] 자원에 매핑하는 과정을 포함합니다. 이 과정은 [[UE]]의 능력(Capability) 및 설정된 [[PUCCH]] 포맷에 따라 차등적으로 적용됩니다.

## 상세 설명
[[UCI_Processing_PUCCH]]는 다음과 같은 단계로 구성됩니다.

1. **UCI 비트 시퀀스 생성**: [[HARQ-ACK]], [[SR]], [[CSI]]의 조합에 따라 비트 시퀀스를 생성합니다. 서로 다른 우선순위 인덱스를 가진 [[UCI]]가 결합될 경우 별도의 규칙이 적용됩니다.
2. **코드 블록 분할 및 CRC 부착**: [[UCI]] 데이터의 크기에 따라 [[Polar_code]] 또는 소형 블록 길이 채널 코딩을 위한 분할 및 [[CRC]] 부착이 수행됩니다.
3. **채널 코딩**: [[Polar_code]]를 사용하거나, 정보 비트 수가 적은 경우 소형 블록 길이 채널 코딩을 사용하여 오류 정정 부호를 생성합니다.
4. **레이트 매칭**: 할당된 [[PUCCH]] 자원의 크기에 맞추어 부호화된 비트들을 레이트 매칭합니다. 우선순위 인덱스가 다른 경우에도 각각의 레이트 매칭 규칙을 따릅니다.
5. **코드 블록 연결**: 분할되었던 코드 블록들을 하나의 시퀀스로 연결합니다.
6. **멀티플렉싱**: 최종적으로 부호화된 [[UCI]] 비트들을 [[PUCCH]] 물리 자원에 매핑합니다.

## 인과 관계
- [[UCI_Bit_Sequence_Generation]] (triggers) [[UCI_Processing_PUCCH]]
- [[UCI_Channel_Coding]] (part_of) [[UCI_Processing_PUCCH]]
- [[UCI_Rate_Matching]] (part_of) [[UCI_Processing_PUCCH]]
- [[UCI_PUCCH_Multiplexing]] (part_of) [[UCI_Processing_PUCCH]]

## 관련 개념
- [[HARQ-ACK]] (depends_on)
- [[SR]] (depends_on)
- [[CSI]] (depends_on)
- [[PUCCH]] (part_of)
- [[Polar_code]] (similar_to)

## 스펙 근거
- TS 38.212 §6.3.1.1에 따르면 [[UCI]] 비트 시퀀스 생성 절차는 [[HARQ-ACK]]/[[SR]] 전용, [[CSI]] 전용, 혹은 이들의 조합 및 우선순위 인덱스에 따라 정의됩니다.
- TS 38.212 §6.3.1.2에 따르면 [[UCI]]에 대한 코드 블록 분할 및 [[CRC]] 부착은 [[Polar_code]] 사용 여부에 따라 구분됩니다.
- TS 38.212 §6.3.1.3 및 §6.3.1.4에 따르면 [[UCI]]의 채널 코딩 및 레이트 매칭은 [[Polar_code]] 또는 소형 블록 길이 채널 코딩 방식에 따라 수행됩니다.
- TS 38.212 §6.3.1.6에 따르면 부호화된 [[UCI]] 비트들은 [[PUCCH]]로 멀티플렉싱됩니다.

## 소스
- 3GPP TS 38.212 V18.0.0 (2023-12) §6.3.1