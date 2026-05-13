# PDCCH_DMRS_Generation

## 정의
[[PDCCH]] 복조를 위해 사용되는 복조 참조 신호(Demodulation Reference Signal, DMRS)의 시퀀스 생성 및 물리 자원 매핑 절차를 의미합니다.

## 요약
[[PDCCH]] DMRS는 [[CORESET]] 내에서 채널 추정을 위해 사용되는 참조 신호입니다. 시퀀스는 의사 난수 생성기(pseudo-random sequence)를 통해 생성되며, 상위 계층 파라미터에 의해 초기화됩니다. 생성된 시퀀스는 [[CORESET]] 내의 자원 요소(Resource Element, RE)에 매핑되며, 이때 [[CORESET]] 설정 및 프리코딩 입도(precoder granularity)에 따라 매핑 규칙이 결정됩니다.

## 상세 설명
### 시퀀스 생성
[[PDCCH]] DMRS 시퀀스 $r(m)$은 OFDM 심볼 $l$에 대해 정의되며, TS 38.211 §7.4.1.3.1에 따라 의사 난수 시퀀스 $c(i)$를 사용하여 생성됩니다. 의사 난수 생성기는 다음 값으로 초기화됩니다.
$c_{init} = (2^{17}(N_{symb}^{slot}n_{s,f}^{\mu} + l + 1)(2N_{ID}^{n_{SCID}} + 1) + 2N_{ID}^{n_{SCID}} + n_{SCID}) \mod 2^{31}$
여기서 $l$은 슬롯 내 OFDM 심볼 번호, $n_{s,f}^{\mu}$는 프레임 내 슬롯 번호입니다. $N_{ID}^{n_{SCID}}$는 상위 계층 파라미터인 `pdcch-DMRS-ScramblingID`가 제공되는 경우 해당 값을 사용하며, 공통 탐색 공간(Common Search Space)의 경우 별도로 설정된 값을 따르고, 그 외에는 0을 사용합니다.

### 물리 자원 매핑
시퀀스 $r(m)$은 TS 38.211 §7.4.1.3.2에 따라 RE $(k, l)$에 매핑됩니다. 매핑 조건은 다음과 같습니다.
- `precoderGranularity`가 `sameAsREG-bundle`인 경우: UE가 복호화를 시도하는 [[PDCCH]]를 구성하는 REG(Resource Element Group) 내에 위치해야 합니다.
- `precoderGranularity`가 `allContiguousRBs`인 경우: UE가 복호화를 시도하는 [[CORESET]] 내의 연속적인 자원 블록(Resource Block) 집합 내의 모든 REG에 매핑됩니다.

기준점(Reference point)은 [[CORESET]]이 [[PBCH]] 또는 `controlResourceSetZero`에 의해 설정된 경우 해당 [[CORESET]]의 가장 낮은 번호 자원 블록의 서브캐리어 0이며, 그 외의 경우에는 공통 자원 블록 0의 서브캐리어 0입니다. 안테나 포트는 $p=2000$으로 고정됩니다.

## 인과 관계
- [[PDCCH_DMRS_Generation]] depends_on [[CORESET_Configuration]] (CORESET 설정에 따른 자원 매핑 범위 결정)
- [[PDCCH_DMRS_Generation]] affects [[PDCCH]] (채널 추정을 통한 복호화 수행)

## 관련 개념
- [[PDCCH]] (affects)
- [[CORESET_Configuration]] (depends_on)
- [[DMRS]] (part_of)

## 스펙 근거
- TS 38.211 §7.4.1.3.1 (Sequence generation)
- TS 38.211 §7.4.1.3.2 (Mapping to physical resources)

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03) Physical channels and modulation