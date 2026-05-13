# SCI_Format_Mapping

## 정의
SCI_Format_Mapping은 Sidelink 제어 정보(SCI)를 구성하는 각 필드들을 정보 비트(information bits) 시퀀스에 할당하는 규칙 및 절차를 의미한다.

## 요약
NR Sidelink 통신에서 1st-stage SCI와 2nd-stage SCI는 정의된 필드 순서에 따라 정보 비트로 매핑된다. 각 필드는 기술된 순서대로 낮은 차수의 비트에서 높은 차수의 비트로 배치되며, 개별 필드 내에서는 최상위 비트(MSB)가 해당 필드의 가장 낮은 차수 비트에 매핑되는 방식을 따른다.

## 상세 설명
SCI 포맷 매핑은 1st-stage SCI와 2nd-stage SCI 각각에 대해 다음과 같은 원칙으로 수행된다.

1. 필드 순서 매핑: 각 SCI 포맷 내에 정의된 필드들은 기술된 순서대로 정보 비트에 매핑된다. 첫 번째로 기술된 필드가 가장 낮은 차수의 정보 비트에 할당되며, 이후의 필드들은 순차적으로 더 높은 차수의 정보 비트에 할당된다.
2. 필드 내 비트 매핑: 각 필드 내부의 비트들은 최상위 비트(MSB)가 해당 필드에 할당된 정보 비트 중 가장 낮은 차수의 비트에 매핑된다. 예를 들어, 첫 번째 필드의 MSB는 전체 정보 비트 시퀀스의 가장 낮은 차수 비트에 매핑된다.

이러한 매핑 절차는 1st-stage SCI의 경우 정보 비트 $a_0$부터 $a_{A-1}$까지, 2nd-stage SCI의 경우 정보 비트 $b_0$부터 $b_{B-1}$까지 적용된다.

## 인과 관계
- [[PSCCH]] (depends_on) 1st-stage SCI 포맷의 정보 비트 매핑 결과가 물리 채널에 전송됨
- [[PSSCH]] (depends_on) 2nd-stage SCI 포맷의 정보 비트 매핑 결과가 물리 채널에 전송됨

## 관련 개념
- [[PSCCH]] (implements)
- [[PSSCH]] (implements)
- [[Channel_Coding]] (depends_on)

## 스펙 근거
- TS 38.212 §8.3.1에 따르면 1st-stage SCI 포맷의 필드 매핑 규칙이 정의됨
- TS 38.212 §8.4.1에 따르면 2nd-stage SCI 포맷의 필드 매핑 규칙이 정의됨

## 소스
- 3GPP TS 38.212 V18.0.0 (2023-12) "Multiplexing and channel coding"