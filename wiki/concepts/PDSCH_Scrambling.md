# PDSCH_Scrambling

## 정의
[[PDSCH]] 전송 시 코드워드(codeword) 단위로 비트 수준에서 수행되는 스크램블링 절차를 의미합니다.

## 요약
[[PDSCH]]는 최대 2개의 코드워드를 전송할 수 있으며, 각 코드워드의 비트 블록은 변조(modulation) 이전에 스크램블링 시퀀스와 XOR 연산을 통해 스크램블링됩니다. 스크램블링 시퀀스 생성기는 RNTI 및 상위 계층 파라미터에 의해 초기화됩니다.

## 상세 설명
[[PDSCH]] 전송을 위해 각 코드워드 $q$에 대해 비트 블록 $b^{(q)}(0), \dots, b^{(q)}(M_{bit}^{(q)}-1)$은 다음 식에 따라 스크램블링된 비트 블록 $\tilde{b}^{(q)}(0), \dots, \tilde{b}^{(q)}(M_{bit}^{(q)}-1)$로 변환됩니다.

$\tilde{b}^{(q)}(i) = (b^{(q)}(i) + c^{(q)}(i)) \mod 2$

여기서 $c^{(q)}(i)$는 [[Sequence_Generation]]의 절차에 따라 생성되는 스크램블링 시퀀스입니다. 스크램블링 시퀀스 생성기는 다음 값으로 초기화됩니다.

$c_{init} = n_{RNTI} \cdot 2^{15} + q \cdot 2^{14} + n_{ID}$

- $n_{RNTI}$는 [[PDSCH]] 전송과 관련된 RNTI 값입니다.
- $q$는 코드워드 인덱스입니다.
- $n_{ID}$는 다음과 같이 결정됩니다.
  - C-RNTI, MCS-C-RNTI, CS-RNTI로 스케줄링되고 DCI format 1_0이 아닌 경우: 상위 계층 파라미터 dataScramblingIdentityPDSCH가 설정되어 있다면 해당 값을 사용합니다.
  - 멀티캐스트(G-RNTI, G-CS-RNTI)의 경우: pdsch-ConfigMulticast 내의 dataScramblingIdentityPDSCH를 사용합니다.
  - 브로드캐스트(MCCH-RNTI, G-RNTI)의 경우: pdsch-ConfigMCCH 또는 pdsch-ConfigMTCH 내의 dataScramblingIdentityPDSCH를 사용합니다.
  - CORESETPoolIndex가 0인 CORESET으로 스케줄링된 경우: dataScramblingIdentityPDSCH를 사용합니다.
  - CORESETPoolIndex가 1인 CORESET으로 스케줄링된 경우: dataScramblingIdentityPDSCH2를 사용합니다.
  - 위 조건에 해당하지 않는 경우: $n_{ID} = 0$을 사용합니다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_Scrambling]] (변조 전 비트 스크램블링 필수)
- [[PDSCH_Scrambling]] depends_on [[Sequence_Generation]] (스크램블링 시퀀스 생성)

## 관련 개념
- [[PDSCH]] (part_of)
- [[Sequence_Generation]] (implements)

## 스펙 근거
- TS 38.211 §7.3.1.1: PDSCH 스크램블링 절차 및 초기화 파라미터 정의
- TS 38.214 §5.1: RNTI와 PDSCH 전송의 연관성 정의

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03) §7.3.1.1