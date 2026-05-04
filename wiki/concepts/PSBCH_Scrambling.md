# PSBCH_Scrambling

## 정의
[[PSBCH]] (Physical Sidelink Broadcast Channel) 전송을 위해 인코딩된 비트 시퀀스에 대해 물리 계층에서 수행하는 스크램블링 절차를 의미합니다.

## 요약
[[PSBCH]] 데이터의 보안 및 간섭 완화를 위해 비트 단위의 스크램블링을 수행합니다. 이 과정은 [[Sidelink]] 통신에서 필수적인 절차이며, 특정 UE Feature와 관련된 보고 절차와는 독립적으로 동작합니다. 본 페이지와 관련된 UE Feature로 Connection Establishment Failure Reporting (20-15)이 있으며, 이는 항상 지원되어야 하는 필수 기능입니다.

## 상세 설명
[[PSBCH]] 전송을 위한 비트 시퀀스 $b(0), b(1), \dots, b(M_{bit}-1)$은 스크램블링 과정을 거쳐 스크램블된 비트 시퀀스 $\tilde{b}(0), \tilde{b}(1), \dots, \tilde{b}(M_{bit}-1)$로 변환됩니다.

스크램블링 연산은 다음과 같이 정의됩니다:
$\tilde{b}(i) = (b(i) + c(i)) \mod 2$

여기서 $c(i)$는 [[Sequence_Generation]]을 통해 생성된 의사 난수 시퀀스(pseudo-random sequence)입니다. 이 시퀀스는 골드 시퀀스(Gold sequence)를 기반으로 하며, 초기값(initialization value)에 의해 결정됩니다.

## 인과 관계
- [[PSBCH_Modulation]] (depends_on): 스크램블링된 비트 시퀀스는 이후 변조 과정을 거쳐 심볼로 매핑됩니다.
- [[Sequence_Generation]] (depends_on): 스크램블링에 사용되는 시퀀스 $c(i)$를 생성하기 위해 호출됩니다.

## 관련 개념
- [[PSBCH]] (part_of)
- [[Sidelink]] (part_of)
- [[Sequence_Generation]] (depends_on)

## 스펙 근거
- TS 38.211 §8.3.3.1에 따르면, [[PSBCH]] 전송을 위한 비트 시퀀스는 스크램블링 과정을 거쳐야 하며, 해당 연산은 모듈로 2 덧셈을 통해 수행됩니다.

## 소스
- 3GPP TS 38.211 V17.0.0 (Release 17), "Physical channels and modulation", Section 8.3.3.1