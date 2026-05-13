# Sequence_Generation

## 정의
5G NR 물리 계층에서 신호의 스크램블링, 참조 신호 생성, 그리고 변조 심볼 매핑 등에 사용되는 의사 난수 시퀀스(Pseudo-random sequence) 및 저-PAPR(Peak-to-Average Power Ratio) 시퀀스 생성 절차를 의미한다.

## 요약
5G NR은 채널의 무작위성을 확보하고 간섭을 제어하기 위해 Gold 시퀀스를 기본으로 사용하며, 특정 채널 및 신호의 특성에 따라 저-PAPR 시퀀스(Type 1, Type 2)를 생성하여 사용한다. 모든 시퀀스 생성은 TS 38.211 §5.2에 정의된 수학적 모델을 따른다.

## 상세 설명
### Gold 시퀀스 생성
Gold 시퀀스는 두 개의 m-시퀀스(Maximum length sequence)의 합으로 생성된다. 시퀀스 $c(n)$은 다음과 같이 정의된다.
- $c(n) = (x_1(n + N_C) + x_2(n + N_C)) \mod 2$
- $x_1(n + 31) = (x_1(n + 3) + x_1(n)) \mod 2$
- $x_2(n + 31) = (x_2(n + 3) + x_2(n + 2) + x_2(n + 1) + x_2(n)) \mod 2$
여기서 $N_C = 1600$이며, 초기값은 각 채널의 설정 파라미터에 따라 결정된다.

### 저-PAPR 시퀀스 생성
저-PAPR 시퀀스는 주로 상향링크 참조 신호에서 사용되며, 크게 두 가지 타입으로 나뉜다.
1. 저-PAPR 시퀀스 Type 1: Zadoff-Chu 시퀀스를 기반으로 하며, 특정 순환 시프트(Cyclic shift)를 적용하여 생성한다.
2. 저-PAPR 시퀀스 Type 2: QPSK 시퀀스를 기반으로 하며, 특정 시퀀스 그룹 및 시퀀스 번호에 따라 생성된다.

## 인과 관계
- [[DMRS_Sequence_Generation]] depends_on [[Sequence_Generation]] (참조 신호 시퀀스 생성 시 Gold 시퀀스 및 저-PAPR 시퀀스 알고리즘 사용)
- [[PUSCH_Scrambling]] depends_on [[Sequence_Generation]] (데이터 스크램블링을 위한 Gold 시퀀스 생성)
- [[PUCCH_Sequence_Generation]] depends_on [[Sequence_Generation]] (제어 채널 시퀀스 생성 시 저-PAPR 시퀀스 사용)
- [[SRS_Generation]] depends_on [[Sequence_Generation]] (사운딩 참조 신호 생성 시 저-PAPR 시퀀스 사용)

## 관련 개념
- [[DMRS_Sequence_Generation]] (implements)
- [[PUSCH_Scrambling]] (implements)
- [[PUCCH_Sequence_Generation]] (implements)
- [[SRS_Generation]] (implements)

## 스펙 근거
- TS 38.211 §5.2.1: Gold 시퀀스 생성 절차 정의
- TS 38.211 §5.2.2: 저-PAPR 시퀀스 Type 1 생성 절차 정의
- TS 38.211 §5.2.3: 저-PAPR 시퀀스 Type 2 생성 절차 정의

## 소스
- 3GPP TS 38.211 V17.0.0, "Physical channels and modulation"