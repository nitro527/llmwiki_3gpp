# PDSCH_Scrambling

## 정의
[[PDSCH]] 데이터 채널의 전송을 위해 전송되는 비트 시퀀스에 대해 물리 계층에서 수행하는 비트 단위의 스크램블링 절차를 의미합니다.

## 요약
[[PDSCH]]의 각 [[Codeword]]는 전송 전 스크램블링 과정을 거칩니다. 이 과정은 데이터의 무작위성을 높여 간섭을 완화하고, 특정 [[RNTI]] 및 [[Identity]] 값을 기반으로 초기화된 시퀀스를 사용하여 수신 측에서 올바른 데이터를 복원할 수 있도록 합니다.

## 상세 설명
[[PDSCH]] 스크램블링은 전송되는 각 [[Codeword]] $q$에 대해 수행됩니다. 입력 비트 시퀀스 $b^{(q)}(0), \dots, b^{(q)}(M_{bit}^{(q)}-1)$는 스크램블링 시퀀스 $v^{(q)}(i)$와 연산되어 출력 비트 시퀀스 $\tilde{b}^{(q)}(0), \dots, \tilde{b}^{(q)}(M_{bit}^{(q)}-1)$를 생성합니다.

스크램블링 연산은 다음과 같습니다:
$\tilde{b}^{(q)}(i) = (b^{(q)}(i) + v^{(q)}(i)) \mod 2$

여기서 스크램블링 시퀀스 $v^{(q)}(i)$는 [[Gold sequence]]를 기반으로 생성되며, 초기값은 다음 파라미터들에 의해 결정됩니다:
- $n_{RNTI}$: 해당 [[PDSCH]] 전송을 스케줄링하는 [[DCI]]에 포함된 [[RNTI]] 값
- $q$: [[Codeword]] 인덱스 (0 또는 1)
- $N_{ID}$: 상위 계층에서 설정된 [[Identity]] 값

## 인과 관계
- [[PDSCH_Transmission_Parameters]] (depends_on): 스크램블링에 필요한 [[RNTI]] 및 [[Identity]] 파라미터를 결정합니다.
- [[Modulation_Mapper]] (affects): 스크램블링된 비트 시퀀스를 입력받아 변조 심볼을 생성합니다.

## 관련 개념
- [[PDSCH]] (part_of)
- [[Codeword]] (part_of)
- [[RNTI]] (depends_on)
- [[Gold sequence]] (similar_to)

## 스펙 근거
- TS 38.211 §7.3.1.1에 따르면, [[PDSCH]]의 각 [[Codeword]] $q$에 대해 스크램블링이 수행되며, 초기화 시퀀스는 $n_{RNTI}$, $q$, $N_{ID}$에 의해 결정됩니다.

## 소스
- 3GPP TS 38.211 V17.x.x (Release 17) §7.3.1.1