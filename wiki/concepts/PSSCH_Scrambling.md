# PSSCH_Scrambling

## 정의
[[PSSCH]] 전송을 위해 채널 코딩된 비트 블록을 변조 이전에 의사 난수 시퀀스(pseudo-random sequence)와 XOR 연산하여 무작위화하는 물리 계층 절차를 의미한다.

## 요약
[[PSSCH]] 데이터는 변조 전 스크램블링 과정을 거치며, 이때 사용되는 스크램블링 시퀀스는 [[PSCCH]]의 [[CRC]] 값을 기반으로 초기화된다. 이는 사이드링크 통신에서 데이터의 신뢰성을 높이고 간섭을 완화하기 위한 필수적인 단계이다.

## 상세 설명
[[PSSCH]]의 단일 코드워드에 대해, [[Channel_Coding]]을 거친 비트 블록 $b(0), b(1), \dots, b(M_{bit}-1)$은 변조 이전에 스크램블링된다. 스크램블링된 비트 $\tilde{b}(i)$는 다음 의사 코드를 통해 생성된다.

- $i = 0, 1, \dots, M_{bit}-1$에 대해:
  - 만약 $b(i)$가 [[SCI]] 플레이스홀더 비트인 경우: $\tilde{b}(i) = b(i)$
  - 그 외의 경우: $\tilde{b}(i) = (b(i) + c(i)) \mod 2$

여기서 $c(i)$는 [[Sequence_Generation]]에서 정의된 골드 시퀀스(Gold sequence)이다. 스크램블링 시퀀스 생성기는 다음과 같이 초기화된다.

1. $q=0$인 경우:
   - 초기화 값 $c_{init} = n_{ID}^{PSSCH} \cdot 2^{15} + M_{ID}$
   - 여기서 $M_{ID}$는 해당 [[PSSCH]]와 연관된 [[PSCCH]]의 [[CRC]] 값을 10진수로 변환한 값이다.
2. $q=1$인 경우:
   - 초기화 값 $c_{init} = (1 - q) \cdot 2^{14} + n_{ID}^{PSSCH} \cdot 2^{15} + M_{ID}$
   - 동일하게 $M_{ID}$는 [[PSCCH]]의 [[CRC]] 값을 사용한다.

이 절차는 [[PSSCH]] 데이터가 전송되기 전 물리 계층에서 수행되는 필수적인 데이터 처리 과정이다.

## 인과 관계
- [[PSSCH_Scrambling]] depends_on [[PSCCH]] (스크램블링 시퀀스 초기화를 위한 CRC 값 참조)
- [[PSSCH_Scrambling]] depends_on [[Sequence_Generation]] (스크램블링에 사용되는 의사 난수 시퀀스 생성)
- [[PSSCH_Scrambling]] affects [[PSSCH_Modulation]] (스크램블링된 비트가 변조기로 입력됨)

## 관련 개념
- [[PSSCH]] (part_of)
- [[PSCCH]] (depends_on)
- [[CRC_Calculation]] (depends_on)
- [[Sequence_Generation]] (depends_on)
- [[PSSCH_Modulation]] (affects)

## 스펙 근거
- TS 38.211 §8.3.1.1에 따르면, [[PSSCH]]의 단일 코드워드에 대한 스크램블링 절차와 [[PSCCH]] [[CRC]]를 이용한 초기화 방식이 정의되어 있다.

## 소스
- 3GPP TS 38.211 V17.9.0, "Physical channels and modulation"