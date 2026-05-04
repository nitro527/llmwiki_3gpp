# UCI_Rate_Matching

## 정의
[[UCI_Rate_Matching]]은 [[UCI]] 비트가 채널 코딩을 거친 후, 전송될 물리 채널의 가용 자원 크기에 맞춰 비트 시퀀스의 길이를 조정하는 절차를 의미합니다.

## 요약
[[UCI]]는 사용되는 채널 코딩 방식([[Polar_code]] 또는 small block length [[Channel_Coding]])과 우선순위 인덱스에 따라 서로 다른 레이트 매칭 알고리즘을 적용합니다. 이 과정은 [[PUCCH]] 또는 [[PUSCH]]를 통해 전송되는 [[UCI]]의 최종 비트 수를 결정하며, 물리 계층 자원 매핑의 핵심 단계입니다.

## 상세 설명
[[UCI_Rate_Matching]]은 크게 인코딩 방식과 우선순위 인덱스에 따라 네 가지 경로로 구분됩니다.

1. [[Polar_code]]를 사용하는 경우:
   - 일반적인 [[UCI]] 전송 시 TS 38.212 §6.3.1.4.1에 따라 레이트 매칭을 수행합니다.
   - 서로 다른 우선순위 인덱스를 가진 [[UCI]]가 존재할 경우, TS 38.212 §6.3.1.4.3에 정의된 절차에 따라 우선순위별로 레이트 매칭을 수행합니다.

2. Small block length [[Channel_Coding]]을 사용하는 경우:
   - 일반적인 [[UCI]] 전송 시 TS 38.212 §6.3.1.4.2에 따라 레이트 매칭을 수행합니다.
   - 서로 다른 우선순위 인덱스를 가진 [[UCI]]가 존재할 경우, TS 38.212 §6.3.1.4.4에 정의된 절차에 따라 레이트 매칭을 수행합니다.

이 절차는 가용 자원 요소(RE)의 수와 [[UCI]]의 코드 레이트를 고려하여 출력 시퀀스 길이를 결정하며, 최종적으로 [[Modulation_Mapper]]로 전달될 비트 스트림을 생성합니다.

## 인과 관계
- [[UCI_Channel_Coding]] (triggers) [[UCI_Rate_Matching]]
- [[UCI_Rate_Matching]] (affects) [[Modulation_Mapper]]
- [[PUCCH_Resource_Sets]] (depends_on) [[UCI_Rate_Matching]]

## 관련 개념
- [[UCI]] (part_of)
- [[Polar_code]] (similar_to)
- [[Channel_Coding]] (part_of)
- [[PUCCH]] (depends_on)
- [[PUSCH]] (depends_on)

## 스펙 근거
- TS 38.212 §6.3.1.4.1: [[UCI]] encoded by [[Polar_code]] 레이트 매칭 규정
- TS 38.212 §6.3.1.4.2: [[UCI]] encoded by channel coding of small block lengths 레이트 매칭 규정
- TS 38.212 §6.3.1.4.3: [[UCI]] with different priority indexes encoded by [[Polar_code]] 레이트 매칭 규정
- TS 38.212 §6.3.1.4.4: [[UCI]] with different priority indexes encoded by channel coding of small block lengths 레이트 매칭 규정

## 소스
- 3GPP TS 38.212 V18.0.0, "Multiplexing and channel coding"