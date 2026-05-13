# PDCCH_Scrambling

## 정의
[[PDCCH]] 전송을 위해 변조 전 단계에서 비트 블록에 스크램블링 시퀀스를 적용하여 데이터의 무작위성을 부여하는 물리 계층 절차를 의미한다.

## 요약
[[PDCCH]]를 통해 전송되는 비트 블록은 변조 이전에 스크램블링 과정을 거친다. 스크램블링 시퀀스는 [[Sequence_Generation]]에서 정의된 방식에 따라 생성되며, 초기화 값은 [[PDCCH]]의 검색 공간 유형 및 상위 계층 파라미터 설정에 따라 결정된다.

## 상세 설명
[[PDCCH]]의 비트 블록 $b(0), \dots, b(M_{bit}-1)$은 변조 이전에 스크램블링되어 스크램블링된 비트 블록 $\tilde{b}(0), \dots, \tilde{b}(M_{bit}-1)$을 생성한다. 여기서 $M_{bit}$는 물리 채널을 통해 전송되는 비트 수이다.

스크램블링 연산은 다음과 같다:
$\tilde{b}(i) = (b(i) + c(i)) \mod 2$

스크램블링 시퀀스 $c(i)$는 [[Sequence_Generation]]의 5.2.1절에 정의된 방식에 따라 생성된다. 스크램블링 시퀀스 생성기는 다음 값으로 초기화된다:
$c_{init} = n_{RNTI} \cdot 2^{16} + n_{ID}$

여기서 $n_{ID}$는 다음과 같이 결정된다:
- UE-specific search space의 경우: 상위 계층 파라미터 pdcch-DMRS-ScramblingID가 설정되어 있다면 해당 값을 사용하고, 그렇지 않으면 0을 사용한다.
- G-RNTI, G-CS-RNTI, MCCH-RNTI, Multicast-MCCH-RNTI로 CRC가 스크램블된 Common search space의 경우: 공통 MBS 주파수 자원에 pdcch-DMRS-ScramblingID가 설정되어 있다면 해당 값을 사용하고, 그렇지 않으면 0을 사용한다.
- 그 외의 경우: 0을 사용한다.

또한 $n_{RNTI}$는 다음과 같이 결정된다:
- UE-specific search space에서 pdcch-DMRS-ScramblingID가 설정된 경우: C-RNTI를 사용한다.
- 그 외의 경우: 0을 사용한다.

## 인과 관계
- [[PDCCH_Scrambling]] depends_on [[Sequence_Generation]] (스크램블링 시퀀스 생성 알고리즘 참조)
- [[PDCCH_Scrambling]] affects [[Modulation_Mapper]] (스크램블링된 비트가 변조기로 입력됨)

## 관련 개념
- [[PDCCH]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[Modulation_Mapper]] (affects)

## 스펙 근거
- TS 38.211 §7.3.2.3에 따르면 PDCCH 비트 스크램블링 절차 및 초기화 파라미터 $n_{ID}$, $n_{RNTI}$ 결정 방식이 정의되어 있다.

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03) Physical channels and modulation