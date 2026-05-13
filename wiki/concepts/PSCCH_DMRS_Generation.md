# PSCCH_DMRS_Generation

## 정의
[[PSCCH]] 전송을 위한 복조 참조 신호(Demodulation Reference Signal, [[DMRS]]) 시퀀스를 생성하는 절차를 의미합니다.

## 요약
[[PSCCH]] DMRS 시퀀스는 의사 난수 시퀀스(pseudo-random sequence)를 기반으로 생성되며, 슬롯 내의 OFDM 심볼 번호, 슬롯 번호, 그리고 상위 계층에서 설정된 스크램블링 식별자(Scrambling ID)를 초기값으로 사용하여 결정됩니다.

## 상세 설명
[[PSCCH]] DMRS 시퀀스 $r(m)$은 다음 식에 따라 생성됩니다.

$r(m) = \frac{1}{\sqrt{2}}(1 - 2c(2m)) + j\frac{1}{\sqrt{2}}(1 - 2c(2m+1))$

여기서 $c(i)$는 [[Sequence_Generation]]에서 정의된 의사 난수 시퀀스입니다. 이 시퀀스 생성기는 다음과 같은 초기값 $c_{init}$으로 초기화됩니다.

$c_{init} = (2^{17}(N_{symb}^{slot}n_{s,f}^{\mu} + l + 1)(2N_{ID}^{SL} + 1) + 2N_{ID}^{SL}) \mod 2^{31}$

이 식에서 사용되는 파라미터는 다음과 같습니다.
- $l$: 슬롯 내의 OFDM 심볼 번호
- $n_{s,f}^{\mu}$: 프레임 내의 슬롯 번호
- $N_{ID}^{SL}$: 상위 계층 파라미터인 sl-DMRS-ScrambleID에 의해 주어지며, 리소스 풀이 전용 SL PRS 리소스 풀인 경우 sl-DMRS-ScrambleID-DedicatedSL-PRS-RP에 의해 주어짐

## 인과 관계
- [[PSCCH_DMRS_Generation]] depends_on [[Sequence_Generation]] (의사 난수 시퀀스 생성 알고리즘 사용)
- [[PSCCH_DMRS_Generation]] affects [[PSCCH_DMRS_Mapping]] (생성된 시퀀스를 물리적 리소스에 매핑)

## 관련 개념
- [[PSCCH]] (part_of)
- [[DMRS]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[PSCCH_DMRS_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §8.4.1.3.1에 따르면, PSCCH DMRS 시퀀스는 의사 난수 시퀀스 생성기를 통해 생성되며, 슬롯 내 심볼 번호, 슬롯 번호, 그리고 상위 계층 파라미터인 sl-DMRS-ScrambleID 또는 sl-DMRS-ScrambleID-DedicatedSL-PRS-RP를 사용하여 초기화됩니다.

## 소스
- 3GPP TS 38.211 V17.9.0 (Release 17) §8.4.1.3.1