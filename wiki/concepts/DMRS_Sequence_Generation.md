# DMRS_Sequence_Generation

## 정의
[[PUSCH]] 전송을 위한 [[DMRS]] 시퀀스 생성 절차로, [[PUSCH_Transform_Precoding]] 활성화 여부에 따라 서로 다른 생성 알고리즘과 파라미터 초기화 방식을 적용하는 물리 계층 프로세스이다.

## 요약
[[PUSCH]] DMRS 시퀀스는 [[PUSCH_Transform_Precoding]]이 비활성화된 경우 의사 난수 시퀀스(pseudo-random sequence) 기반으로 생성되며, 활성화된 경우 기본 시퀀스(base sequence)와 시퀀스 그룹 호핑(sequence group hopping)을 결합하여 생성된다. 각 경우에 따라 상위 계층 파라미터와 [[DCI]] 필드를 통해 초기화 값이 결정된다.

## 상세 설명

### Transform precoding 비활성화 시 시퀀스 생성
TS 38.211 §6.4.1.1.1.1에 따라, [[PUSCH_Transform_Precoding]]이 비활성화된 경우 DMRS 시퀀스 $r(n)$은 다음과 같이 생성된다.
$r(n) = \frac{1}{\sqrt{2}}(1-2c(2n)) + j\frac{1}{\sqrt{2}}(1-2c(2n+1))$
여기서 $c(n)$은 TS 38.211 §5.2.1에 정의된 의사 난수 시퀀스이며, 초기화 값 $c_{init}$는 다음과 같이 결정된다.
$c_{init} = (2^{17}(N_{symb}^{slot}n_{s,f}^{\mu} + l + 1)(2N_{ID}^{n_{SCID}} + 1) + 2N_{ID}^{n_{SCID}} + n_{SCID}) \mod 2^{31}$
- $l$: 슬롯 내 OFDM 심볼 번호
- $n_{s,f}^{\mu}$: 프레임 내 슬롯 번호
- $N_{ID}^{n_{SCID}}$ 및 $n_{SCID}$: 상위 계층 파라미터(scramblingID0, scramblingID1) 및 DCI 내 DMRS 초기화 필드에 의해 결정됨

### Transform precoding 활성화 시 시퀀스 생성
TS 38.211 §6.4.1.1.1.2에 따라, [[PUSCH_Transform_Precoding]]이 활성화된 경우 DMRS 시퀀스는 기본 시퀀스 $r_{u,v}^{(\alpha, \delta)}(n)$을 기반으로 생성된다.
- $\pi/2$-BPSK 변조가 사용되는 경우, 시퀀스 그룹 $u$와 시퀀스 번호 $v$는 상위 계층 파라미터 및 호핑 모드에 따라 결정된다.
- 그룹 호핑(group hopping) 또는 시퀀스 호핑(sequence hopping)이 활성화된 경우, TS 38.211 §5.2.1의 의사 난수 시퀀스를 사용하여 매 라디오 프레임 시작 시점에서 초기화된다.
- $n_{SCID}$와 유사하게, $\pi/2$-BPSK 변조 시에는 pi2BPSK-ScramblingID0/1 파라미터가 시퀀스 생성의 초기화에 사용된다.

## 인과 관계
- [[PUSCH_Transform_Precoding]] affects [[DMRS_Sequence_Generation]] (변환 프리코딩 활성 여부에 따른 시퀀스 생성 알고리즘 분기)
- [[DMRS_Sequence_Generation]] implements [[DMRS]] (DMRS 물리적 신호 생성의 핵심 절차)
- [[DCI_Field_Mapping]] depends_on [[DMRS_Sequence_Generation]] (DCI 내 DMRS 관련 필드가 시퀀스 초기화 값 결정에 사용됨)

## 관련 개념
- [[PUSCH]] (part_of)
- [[DMRS]] (part_of)
- [[PUSCH_Transform_Precoding]] (affects)
- [[DCI]] (depends_on)

## 스펙 근거
- TS 38.211 §6.4.1.1.1.1 (Sequence generation when transform precoding is disabled)
- TS 38.211 §6.4.1.1.1.2 (Sequence generation when transform precoding is enabled)
- TS 38.211 §5.2.1 (Pseudo-random sequence generation)

## 소스
- 3GPP TS 38.211 V17.9.0 (Release 17) Physical channels and modulation