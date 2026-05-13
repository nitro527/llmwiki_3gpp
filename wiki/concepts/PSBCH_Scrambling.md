# PSBCH_Scrambling

## 정의
[[PSBCH]] 전송을 위해 채널 코딩된 비트 블록을 변조 이전에 의사 난수 시퀀스를 사용하여 비트 단위로 XOR 연산하여 무작위화하는 물리 계층 절차를 의미한다.

## 요약
[[PSBCH]]를 통해 전송되는 비트 블록은 변조 과정에 진입하기 전 스크램블링 과정을 거친다. 이 과정은 [[Sequence_Generation]]에서 정의된 스크램블링 시퀀스를 사용하여 수행되며, 각 S-SS/PSBCH 블록의 시작 시점에서 시퀀스 생성기를 초기화함으로써 데이터의 보안성과 신뢰성을 확보한다.

## 상세 설명
[[PSBCH]]를 통해 전송되는 비트 블록 $b(0), b(1), \dots, b(M_{bit}-1)$은 변조 이전에 스크램블링 과정을 거쳐 스크램블된 비트 블록 $\tilde{b}(0), \tilde{b}(1), \dots, \tilde{b}(M_{bit}-1)$로 변환된다. 여기서 $M_{bit}$는 [[PSBCH]]를 통해 전송되는 총 비트 수를 나타낸다.

스크램블링 연산은 다음 식을 따른다.
$\tilde{b}(i) = (b(i) + c(i)) \mod 2$

위 식에서 $c(i)$는 [[Sequence_Generation]]의 절차에 따라 생성된 스크램블링 시퀀스이다. 스크램블링 시퀀스 생성기는 각 S-SS/PSBCH 블록이 시작될 때마다 초기화된다.

## 인과 관계
- [[PSBCH]] depends_on [[PSBCH_Scrambling]] (변조 전 비트 무작위화 수행)
- [[PSBCH_Scrambling]] depends_on [[Sequence_Generation]] (스크램블링 시퀀스 생성 알고리즘 참조)

## 관련 개념
- [[PSBCH]] (part_of)
- [[Sequence_Generation]] (depends_on)

## 스펙 근거
TS 38.211 §8.3.3.1에 따르면, [[PSBCH]] 전송 비트 블록은 변조 이전에 스크램블링되어야 하며, 스크램블링 시퀀스 $c(i)$는 §5.2.1에 정의된 방식을 따르고 각 S-SS/PSBCH 블록 시작 시점에 초기화된다.

## 소스
- TS 38.211 §8.3.3.1