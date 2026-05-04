# UCI_Multiplexing_PUSCH

## 정의
[[UCI_Multiplexing_PUSCH]]는 [[UE]]가 [[PUSCH]] 전송 시점에 [[HARQ-ACK]], [[CSI]], [[SR]]과 같은 [[Uplink_Control_Information]]을 데이터와 함께 다중화하여 전송하는 절차를 의미합니다.

## 요약
[[UCI_Multiplexing_PUSCH]]는 상향링크 자원의 효율성을 높이기 위해 [[PUSCH]] 전송 자원 내에 [[UCI]]를 피기백(piggyback)하여 전송하는 메커니즘입니다. TS 38.822에 정의된 다양한 [[UE]] 기능(feature)에 따라 [[HARQ-ACK]], [[CSI]], [[SR]]의 다중화가 지원되며, 우선순위가 다른 [[UCI]] 간의 처리 절차를 포함합니다.

## 상세 설명
[[UCI_Multiplexing_PUSCH]]의 주요 절차는 다음과 같습니다.

1. [[UCI_Bit_Sequence_Generation]]: [[HARQ-ACK]], [[CSI]], [[CG-UCI]], [[UTO-UCI]] 등의 비트 시퀀스를 생성합니다.
2. [[UCI_Channel_Coding]]: 생성된 [[UCI]] 비트들은 [[Polar_code]] 또는 소형 블록 길이용 채널 코딩 기법을 사용하여 부호화됩니다.
3. [[UCI_Rate_Matching]]: 부호화된 [[UCI]] 비트들은 [[PUSCH]] 자원에 매핑되기 위해 [[UCI_Rate_Matching]] 과정을 거칩니다.
4. [[UCI_Multiplexing_PUSCH]] 매핑: 부호화된 [[UCI]] 비트들은 [[PUSCH]]의 데이터 심볼과 다중화되어 물리 자원에 매핑됩니다.
5. 우선순위 처리: 서로 다른 우선순위 인덱스를 가진 [[UCI]]가 존재할 경우, TS 38.212 §6.3.2.7에 따라 우선순위가 높은 [[UCI]]가 우선적으로 처리됩니다.

## 인과 관계
- [[UCI_Bit_Sequence_Generation]] (depends_on) [[UCI_Multiplexing_PUSCH]]
- [[UCI_Channel_Coding]] (depends_on) [[UCI_Multiplexing_PUSCH]]
- [[UCI_Rate_Matching]] (depends_on) [[UCI_Multiplexing_PUSCH]]
- [[PUSCH]] (part_of) [[UCI_Multiplexing_PUSCH]]

## 관련 개념
- [[HARQ_ACK_Codebook_Determination]] (depends_on)
- [[UCI_Reporting_Different_Priorities]] (affects)
- [[PUSCH_Transmission_Procedures]] (part_of)
- [[UCI_Bit_Sequence_Generation]] (part_of)
- [[UCI_Channel_Coding]] (part_of)
- [[UCI_Rate_Matching]] (part_of)

## 스펙 근거
- TS 38.212 §6.3.2: [[UCI]] on [[PUSCH]] 전송 절차 및 비트 시퀀스 생성, 채널 코딩, 다중화 규정
- TS 38.212 §6.3.2.7: 서로 다른 우선순위 인덱스를 가진 [[UCI]]의 [[PUSCH]] 다중화
- TS 38.213 §9.3: [[PUSCH]] 상의 [[UCI]] 보고 절차
- TS 38.822: 4-19, 4-19a, 4-19b, 4-19c, 4-28, 10-35, 10-35a, 10-35b, 10-35c, 10-36, 11-3g, 25-16 등 [[UE]] 기능 요구사항

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03)
- 3GPP TS 38.213 V18.0.0 (2024-03)
- 3GPP TS 38.822 V18.0.0 (2024-03)