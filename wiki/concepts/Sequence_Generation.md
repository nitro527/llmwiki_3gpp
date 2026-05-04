# Sequence_Generation

## 정의
[[Sequence_Generation]]은 5G NR 시스템에서 물리 채널 및 신호의 전송을 위해 사용되는 의사 난수(Pseudo-random) 시퀀스 및 낮은 PAPR(Peak-to-Average Power Ratio) 특성을 갖는 시퀀스를 생성하는 절차를 의미한다.

## 요약
5G NR PHY 계층은 데이터의 [[Scrambling]]이나 [[Reference_Signals]] 생성 등을 위해 두 가지 주요 시퀀스 생성 방식을 사용한다. 첫째는 Gold 시퀀스 기반의 의사 난수 시퀀스 생성이며, 둘째는 전송 신호의 PAPR을 낮추기 위한 Low-PAPR 시퀀스 생성이다. Low-PAPR 시퀀스는 시퀀스 길이에 따라 Type 1과 Type 2로 구분되어 정의된다.

## 상세 설명
### Pseudo-random sequence generation
TS 38.211 §5.2.1에 정의된 의사 난수 시퀀스는 길이 31의 Gold 시퀀스를 기반으로 생성된다. 출력 시퀀스 $c(n)$은 두 개의 m-시퀀스 $x_1(n)$과 $x_2(n)$의 모듈로-2 합으로 정의되며, 초기값(initialization)에 따라 다양한 채널의 특성에 맞게 생성된다.

### Low-PAPR sequence generation type 1
TS 38.211 §5.2.2에 정의된 Type 1 시퀀스는 주로 [[DMRS]]와 같은 참조 신호에 사용된다.
- Base sequences of length 36 or larger: 시퀀스 길이에 따라 특정 순환 시프트(cyclic shift)와 위상 회전이 적용된 Zadoff-Chu 시퀀스 기반의 생성 방식을 따른다.
- Base sequences of length less than 36: 길이가 36 미만인 경우, 미리 정의된 시퀀스 테이블을 기반으로 생성된다.

### Low-PAPR sequence generation type 2
TS 38.211 §5.2.3에 정의된 Type 2 시퀀스는 특정 조건 하에서 사용되는 낮은 PAPR 특성을 가진 시퀀스이다.
- Sequences of length 30 or larger: 특정 생성 규칙에 따라 시퀀스가 결정된다.
- Sequences of length less than 30: 짧은 길이에 최적화된 별도의 생성 규칙을 따른다.

## 인과 관계
- [[Scrambling]] (depends_on) [[Sequence_Generation]]
- [[Reference_Signals]] (depends_on) [[Sequence_Generation]]
- [[DMRS_Generation_Mapping]] (depends_on) [[Sequence_Generation]]
- [[PRACH_Sequence_Generation]] (depends_on) [[Sequence_Generation]]

## 관련 개념
- [[Scrambling]] (affects)
- [[DMRS]] (depends_on)
- [[Reference_Signals]] (part_of)
- [[OFDM_Baseband_Signal_Generation]] (depends_on)

## 스펙 근거
- TS 38.211 §5.2.1: Pseudo-random sequence generation 절차 정의
- TS 38.211 §5.2.2: Low-PAPR sequence generation type 1 정의
- TS 38.211 §5.2.3: Low-PAPR sequence generation type 2 정의

## 소스
- 3GPP TS 38.211 V17.x.x (Release 17) Physical channels and modulation