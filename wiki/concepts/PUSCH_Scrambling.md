# PUSCH_Scrambling

## 정의
[[PUSCH]] 전송 시 변조(Modulation) 이전에 비트 단위의 데이터 보안 및 간섭 완화를 위해 수행되는 비트 레벨 스크램블링(Scrambling) 과정.

## 요약
[[PUSCH]] 전송을 위해 생성된 코드워드(Codeword) 비트들은 의사 난수(Pseudo-random) 시퀀스와 XOR 연산을 통해 스크램블링된다. 이 과정은 [[Sequence_Generation]]에서 정의된 시퀀스 생성기를 사용하며, RNTI(Radio Network Temporary Identifier) 및 상위 계층 파라미터에 의해 초기화된다.

## 상세 설명
[[PUSCH]] 전송을 위한 스크램블링은 TS 38.211 §6.3.1.1에 따라 수행된다.

1. 입력 비트 블록 $b^{(q)}(0), \dots, b^{(q)}(M_{bit}^{(q)}-1)$은 변조 이전에 스크램블링되어 $b^{(q)}(0), \dots, b^{(q)}(M_{bit}^{(q)}-1)$로 변환된다.
2. UCI(Uplink Control Information) placeholder 비트가 포함된 경우, 해당 비트는 스크램블링되지 않고 그대로 전달된다.
3. 스크램블링 시퀀스 $c^{(q)}(i)$는 TS 38.211 §5.2.1에 정의된 Gold 시퀀스를 사용한다.
4. 시퀀스 생성기 초기화 값 $c_{init}$는 다음과 같이 결정된다:
   - $c_{init} = (n_{RNTI} \cdot 2^{15} + q \cdot 2^{14} + n_{ID}) \mod 2^{31}$
   - $n_{ID}$는 상위 계층 파라미터 dataScramblingIdentityPUSCH가 설정되고 RNTI가 C-RNTI, MCS-C-RNTI, SP-CSI-RNTI, 또는 CS-RNTI인 경우 해당 값으로 설정된다. 단, DCI format 0_0가 common search space에서 스케줄링된 경우는 제외된다.
   - Type-2 random access procedure에 의해 트리거된 경우, 상위 계층 파라미터 msgA-DataScramblingIndex가 사용된다.
   - 그 외의 경우 $n_{ID} = 0$으로 설정된다.
5. $n_{RNTI}$는 해당 [[PUSCH]] 전송과 연관된 RNTI 값이며, msgA 전송의 경우 RA-RNTI가 사용된다.

## 인과 관계
- [[PUSCH]] depends_on [[PUSCH_Scrambling]] (변조 전 비트 처리 필수)
- [[PUSCH_Scrambling]] depends_on [[Sequence_Generation]] (스크램블링 시퀀스 생성 기반)
- [[PUSCH_Scrambling]] depends_on [[Random_Access_Response]] (RAR UL grant 기반 초기화 시 RNTI 사용)

## 관련 개념
- [[PUSCH]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[Random_Access_Response]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.1.1: Scrambling 절차 및 초기화 파라미터 정의
- TS 38.211 §5.2.1: 스크램블링 시퀀스 생성기 정의
- TS 38.213 §8.1A: Type-2 random access procedure 관련 정의
- TS 38.213 §8.3: PUSCH 전송 관련 RNTI 매핑
- TS 38.321 §5.1.3A: msgA 프리앰블 인덱스 정의

## 소스
- 3GPP TS 38.211 V18.0.0 (2023-12) Physical channels and modulation