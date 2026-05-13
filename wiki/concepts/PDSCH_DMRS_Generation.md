# PDSCH_DMRS_Generation

## 정의
[[PDSCH]] 전송을 위한 복조 참조 신호(Demodulation Reference Signal, DMRS) 시퀀스를 생성하는 물리 계층 절차.

## 요약
[[PDSCH]] DMRS 시퀀스는 의사 난수(pseudo-random) 시퀀스 생성기를 기반으로 생성되며, 슬롯 내 OFDM 심볼 번호, 슬롯 번호, 상위 계층 파라미터 및 DCI 필드에 의해 초기화된다. 이 시퀀스는 채널 추정을 위해 수신단에서 사용된다.

## 상세 설명
[[PDSCH]] DMRS 시퀀스 $r(m)$은 TS 38.211 §7.4.1.1.1에 따라 다음과 같이 정의된다.

$r(m) = \frac{1}{\sqrt{2}}(1 - 2c(2m)) + j\frac{1}{\sqrt{2}}(1 - 2c(2m + 1))$

여기서 $c(i)$는 TS 38.211 §5.2.1에 정의된 의사 난수 시퀀스이다. 시퀀스 생성기는 다음 값으로 초기화된다.

$c_{init} = (2^{17}(N_{symb}^{slot}n_{s,f}^{\mu} + l + 1)(2N_{ID}^{(n_{SCID})} + 1) + 2N_{ID}^{(n_{SCID})} + n_{SCID}) \mod 2^{31}$

- $l$: 슬롯 내 OFDM 심볼 번호
- $n_{s,f}^{\mu}$: 프레임 내 슬롯 번호
- $N_{ID}^{(n_{SCID})}$: 상위 계층 파라미터 scramblingID0 또는 scramblingID1에 의해 결정됨
- $n_{SCID}$: DMRS 시퀀스 초기화 필드(DCI 내 존재 시) 또는 0으로 설정

상위 계층 파라미터 및 DCI 포맷에 따른 $N_{ID}^{(n_{SCID})}$ 결정 규칙은 다음과 같다.
1. [[PDCCH]] DCI format 1_1, 1_2, 1_3 (C-RNTI, MCS-C-RNTI, CS-RNTI): scramblingID0, scramblingID1 사용
2. [[PDCCH]] DCI format 1_0 (C-RNTI, MCS-C-RNTI, CS-RNTI): scramblingID0 사용
3. [[PDCCH]] DCI format 4_2 (G-RNTI, G-CS-RNTI): pdsch-ConfigMulticast 내 scramblingID0, scramblingID1 사용
4. [[PDCCH]] DCI format 4_1 (G-RNTI, G-CS-RNTI): pdsch-ConfigMulticast 내 scramblingID0 사용
5. MCCH-RNTI 또는 G-RNTI: pdsch-ConfigMCCH 또는 pdsch-ConfigMTCH 내 scramblingID0 사용
6. 기타: $N_{ID}^{(n_{SCID})} = N_{ID}^{cell}$

또한, dmrs-Downlink가 제공되는 경우 $n_{SCID}$는 CDM 그룹 $\lambda$에 따라 추가적인 오프셋을 가질 수 있다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_DMRS_Generation]] (채널 추정을 위한 참조 신호 생성)
- [[PDSCH_DMRS_Generation]] depends_on [[DMRS_Sequence_Generation]] (기본 시퀀스 생성 알고리즘 참조)
- [[PDSCH_DMRS_Generation]] triggers [[PDSCH_DMRS_Reception]] (생성된 시퀀스를 기반으로 수신단에서 채널 추정 수행)

## 관련 개념
- [[PDSCH]] (part_of)
- [[DMRS]] (part_of)
- [[DCI]] (affects)
- [[PDCCH]] (affects)

## 스펙 근거
- TS 38.211 §7.4.1.1.1: Sequence generation
- TS 38.211 §5.2.1: Pseudo-random sequence generation

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03)