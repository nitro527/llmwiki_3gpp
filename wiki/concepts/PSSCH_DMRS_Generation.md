# PSSCH_DMRS_Generation

## 정의
[[PSSCH]] 전송을 위한 [[DMRS]] 시퀀스를 생성하는 절차로, [[PSCCH]]의 [[CRC]] 값을 기반으로 의사 난수 생성기를 초기화하여 물리 계층 참조 신호를 생성하는 과정이다.

## 요약
[[PSSCH]] [[DMRS]]는 [[TS 38.211]] §8.4.1.1.1에 정의된 수식에 따라 생성된다. 시퀀스 생성기는 슬롯 내의 OFDM 심볼 번호, 슬롯 번호, 그리고 해당 [[PSSCH]]와 연관된 [[PSCCH]]의 [[CRC]] 값을 입력 파라미터로 사용하여 초기화된다.

## 상세 설명
[[PSSCH]] [[DMRS]] 시퀀스 $r(m)$은 다음 수식에 따라 생성된다.

$r(m) = \frac{1}{\sqrt{2}}(1-2c(2m)) + j\frac{1}{\sqrt{2}}(1-2c(2m+1))$

여기서 $c(i)$는 [[TS 38.211]] §5.2.1에 정의된 의사 난수 시퀀스(pseudo-random sequence)이다. 의사 난수 생성기는 다음 값으로 초기화된다.

$c_{init} = (2^{17}(N_{symb}^{slot}n_{s,f}^{\mu} + l + 1)(2N_{ID}^{n_{SCID}} + 1) + 2N_{ID}^{n_{SCID}} + n_{SCID}) \mod 2^{31}$

이때, 초기화 파라미터는 다음과 같이 결정된다.
- $l$: 슬롯 내의 OFDM 심볼 번호
- $n_{s,f}^{\mu}$: 프레임 내의 슬롯 번호
- $N_{ID}^{n_{SCID}}$: [[PSCCH]]와 연관된 [[CRC]]의 10진수 표현값으로, [[TS 38.212]] §7.3.2에 정의된 절차를 따른다.

## 인과 관계
- [[PSCCH]] (depends_on) [[PSSCH_DMRS_Generation]] (PSCCH의 CRC 값이 DMRS 시퀀스 초기화에 사용됨)
- [[PSSCH_DMRS_Generation]] (triggers) [[DMRS_Sequence_Generation]] (DMRS 시퀀스 생성 알고리즘을 구현함)

## 관련 개념
- [[PSCCH]] (depends_on)
- [[DMRS_Sequence_Generation]] (implements)
- [[CRC_Calculation]] (depends_on)

## 스펙 근거
- TS 38.211 §8.4.1.1.1: Sequence generation
- TS 38.212 §7.3.2: CRC calculation for PSCCH

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03) Physical channels and modulation