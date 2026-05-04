# PSCCH_Modulation

## 정의
[[PSCCH]]의 데이터 심볼을 생성하기 위해 스크램블링된 비트 시퀀스를 복소수 심볼로 변환하는 물리 계층 절차를 의미합니다.

## 요약
[[PSCCH]] 변조는 QPSK 방식을 사용하며, 입력된 비트 시퀀스를 [[Modulation_Mapper]]를 통해 복소수 심볼로 매핑합니다. 이는 [[Sidelink]] 통신에서 제어 정보를 전송하기 위한 필수 과정입니다.

## 상세 설명
TS 38.211 §8.3.2.2에 따라 [[PSCCH]]의 변조 과정은 다음과 같이 수행됩니다.

1. 입력: [[PSCCH_Scrambling]] 과정을 거친 비트 시퀀스 $b(0), \dots, b(M_{bit}-1)$이 입력됩니다.
2. 변조 방식: [[PSCCH]]는 QPSK(Quadrature Phase Shift Keying) 변조 방식을 사용합니다.
3. 매핑: 입력된 비트 시퀀스는 [[Modulation_Mapper]]를 통해 복소수 심볼 $d(0), \dots, d(M_{symb}-1)$로 변환됩니다. 여기서 $M_{symb} = M_{bit}/2$입니다.
4. QPSK 매핑 규칙: 각 2비트 쌍 $(b(2i), b(2i+1))$은 다음 식에 따라 복소수 심볼 $d(i)$로 매핑됩니다.
   $d(i) = \frac{1}{\sqrt{2}}((1-2b(2i)) + j(1-2b(2i+1)))$

## 인과 관계
- [[PSCCH_Scrambling]] (triggers) [[PSCCH_Modulation]]
- [[PSCCH_Modulation]] (affects) [[PSCCH_Resource_Mapping]]

## 관련 개념
- [[PSCCH]] (part_of)
- [[Modulation_Mapper]] (depends_on)
- [[Sidelink]] (part_of)
- [[QPSK]] (similar_to)

## 스펙 근거
- TS 38.211 §8.3.2.2: PSCCH 변조를 위한 QPSK 매핑 방식 및 수식 정의

## 소스
- 3GPP TS 38.211 V17.0.0 (2022-03), "Physical channels and modulation"