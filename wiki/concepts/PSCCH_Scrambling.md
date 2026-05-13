# PSCCH_Scrambling

## 정의
[[PSCCH]] 전송을 위해 물리 계층에서 수행되는 비트 단위의 스크램블링 절차를 의미하며, 변조 이전에 데이터의 무작위화를 통해 간섭을 완화하고 신호의 통계적 특성을 개선하는 과정입니다.

## 요약
[[PSCCH]]를 통해 전송되는 비트 블록은 변조 과정에 앞서 스크램블링 시퀀스와의 비트 단위 XOR 연산을 통해 스크램블링됩니다. 이 과정은 전송되는 비트의 신뢰성을 높이고 물리 채널의 특성을 최적화하기 위해 필수적으로 수행됩니다.

## 상세 설명
[[PSCCH]] 전송을 위한 비트 블록 $b(0), b(1), \dots, b(M_{bit}-1)$은 변조 이전에 스크램블링 과정을 거칩니다. 여기서 $M_{bit}$는 해당 물리 채널을 통해 전송되는 총 비트 수를 나타냅니다.

스크램블링된 비트 블록 $\tilde{b}(0), \tilde{b}(1), \dots, \tilde{b}(M_{bit}-1)$은 다음 식에 의해 생성됩니다.
$\tilde{b}(i) = (b(i) + c(i)) \mod 2$

위 식에서 $c(i)$는 [[Sequence_Generation]]의 5.2.1절에 정의된 스크램블링 시퀀스를 의미합니다. 스크램블링 시퀀스 생성기는 TS 38.211 §8.3.2.1에 명시된 초기화 값에 따라 설정되며, 이 초기화 값은 해당 물리 채널의 전송 파라미터와 연동됩니다.

## 인과 관계
- [[PSCCH_Scrambling]] depends_on [[Sequence_Generation]] (스크램블링 시퀀스 생성 알고리즘 사용)
- [[PSCCH_Transmission_Procedure]] triggers [[PSCCH_Scrambling]] (PSCCH 전송 시 변조 전 필수 수행)

## 관련 개념
- [[PSCCH]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[PSCCH_Transmission_Procedure]] (triggers)

## 스펙 근거
- TS 38.211 §8.3.2.1: PSCCH 스크램블링 절차 및 수식 정의

## 소스
- 3GPP TS 38.211 V16.9.0, "NR; Physical channels and modulation"