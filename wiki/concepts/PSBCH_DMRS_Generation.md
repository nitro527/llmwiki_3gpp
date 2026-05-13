# PSBCH_DMRS_Generation

## 정의
[[PSBCH]] 전송 시 채널 추정을 위해 사용되는 복조 참조 신호(Demodulation Reference Signal, DMRS) 시퀀스를 생성하는 절차를 의미한다.

## 요약
[[PSBCH]] DMRS 시퀀스는 [[S-SS/PSBCH_Block_Generation]] 과정의 일부로 생성되며, 의사 난수 시퀀스(Pseudo-random sequence) 생성기를 기반으로 한다. 각 [[S-SS/PSBCH_Block_Generation]] 오케이션(occasion) 시작 시점에 시퀀스 생성기가 초기화되어 고유한 참조 신호를 생성한다.

## 상세 설명
[[PSBCH]] DMRS 시퀀스 $r(m)$은 다음과 같이 정의된다.

$r(m) = \frac{1}{\sqrt{2}}(1 - 2c(2m)) + j\frac{1}{\sqrt{2}}(1 - 2c(2m+1))$

여기서 $c(i)$는 [[Sequence_Generation]]의 5.2절에 정의된 의사 난수 시퀀스이다. 

스크램블링 시퀀스 생성기는 각 [[S-SS/PSBCH_Block_Generation]] 오케이션이 시작될 때마다 초기화된다. 이때 사용되는 초기화 값 $c_{init}$은 해당 [[S-SS/PSBCH_Block_Generation]]의 식별자 및 관련 파라미터에 의해 결정된다. 생성된 시퀀스는 [[PSBCH]]가 매핑되는 자원 요소(Resource Element)에 할당되어 수신단에서 채널 추정 및 복조를 수행하는 데 사용된다.

## 인과 관계
- [[PSBCH_DMRS_Generation]] depends_on [[Sequence_Generation]] (의사 난수 시퀀스 생성 알고리즘 참조)
- [[PSBCH_DMRS_Generation]] part_of [[S-SS/PSBCH_Block_Generation]] (S-SS/PSBCH 블록 구성의 필수 요소)

## 관련 개념
- [[PSBCH]] (part_of)
- [[S-SS/PSBCH_Block_Generation]] (part_of)
- [[Sequence_Generation]] (depends_on)

## 스펙 근거
- TS 38.211 §8.4.1.4.1에 따르면, S-SS/PSBCH 블록을 위한 참조 신호 시퀀스는 5.2절에 정의된 의사 난수 시퀀스를 사용하여 생성된다.
- TS 38.211 §8.4.1.4.1에 따르면, 스크램블링 시퀀스 생성기는 각 S-SS/PSBCH 블록 오케이션의 시작 시점에 초기화된다.

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03) Physical channels and modulation