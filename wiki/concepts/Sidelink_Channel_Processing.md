# Sidelink_Channel_Processing

## 정의
[[Sidelink_Channel_Processing]]은 [[Sidelink]] 통신 환경에서 [[PSBCH]], [[PSSCH]], [[PSCCH]]를 통해 전송되는 데이터 및 제어 정보를 물리 계층에서 처리하는 일련의 절차를 의미합니다.

## 요약
[[Sidelink]] 채널 처리는 [[SCI]]를 통한 제어 정보 전송과 [[PSSCH]]를 통한 데이터 전송으로 구분됩니다. [[PSCCH]]는 1st-stage [[SCI]]를 전달하며, [[PSSCH]]는 2nd-stage [[SCI]]와 데이터를 다중화하여 전송합니다. 각 채널은 [[CRC]] 부착, 채널 코딩, [[Rate_Matching]] 과정을 거쳐 물리 자원에 매핑됩니다.

## 상세 설명
[[Sidelink]] 채널 처리는 다음과 같은 주요 단계를 포함합니다.

1. [[PSCCH]] 처리:
   - 1st-stage [[SCI]] ([[SCI_format_1_A]], [[SCI_format_1_B]])를 생성합니다.
   - [[CRC]]를 부착하고 채널 코딩을 수행한 후 [[Rate_Matching]]을 거쳐 [[PSCCH]] 자원에 매핑합니다.

2. [[PSSCH]] 처리:
   - 2nd-stage [[SCI]] ([[SCI_format_2_A]], [[SCI_format_2_B]], [[SCI_format_2_C]], [[SCI_format_2_D]])를 생성합니다.
   - 데이터와 2nd-stage [[SCI]]를 다중화합니다.
   - [[CRC]] 부착, 채널 코딩, [[Rate_Matching]]을 수행합니다.
   - 최종적으로 코딩된 2nd-stage [[SCI]] 비트와 데이터를 [[PSSCH]] 물리 자원에 매핑합니다.

3. [[PSBCH]] 처리:
   - [[Sidelink]] 방송 정보를 위한 채널 처리 절차를 수행합니다.

## 인과 관계
- [[SCI]] 생성 (triggers) [[PSCCH]] 및 [[PSSCH]] 처리
- [[Channel_Coding]] (affects) [[Rate_Matching]]
- [[Multiplexing]] (part_of) [[PSSCH]] 처리

## 관련 개념
- [[PSCCH]] (part_of)
- [[PSSCH]] (part_of)
- [[PSBCH]] (part_of)
- [[SCI]] (depends_on)
- [[CRC]] (depends_on)
- [[Channel_Coding_General]] (depends_on)
- [[Rate_Matching]] (depends_on)

## 스펙 근거
- TS 38.212 §8.1: [[PSBCH]] 채널 처리 절차 정의
- TS 38.212 §8.2: [[PSSCH]] 데이터 및 제어 정보 다중화 정의
- TS 38.212 §8.3: [[PSCCH]]를 통한 1st-stage [[SCI]] 포맷, [[CRC]], 채널 코딩 및 [[Rate_Matching]] 정의
- TS 38.212 §8.4: [[PSSCH]]를 통한 2nd-stage [[SCI]] 포맷, [[CRC]], 채널 코딩, [[Rate_Matching]] 및 다중화 정의

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03) "NR; Multiplexing and channel coding"