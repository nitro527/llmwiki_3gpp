# PUCCH_DMRS_Generation

## 정의
[[PUCCH]] 전송 시 채널 추정을 위해 사용되는 [[DMRS]] 시퀀스를 생성하는 절차로, 각 [[PUCCH_Format]]의 특성에 따라 시퀀스 구성 방식이 정의됩니다.

## 요약
[[PUCCH]] 포맷 1, 2, 3, 4는 각각의 구조적 특성에 따라 서로 다른 [[DMRS]] 생성 방식을 따릅니다. 포맷 1은 순환 이동(cyclic shift) 기반의 시퀀스를 사용하며, 포맷 2는 [[QPSK]] 기반의 시퀀스를, 포맷 3과 4는 [[DFT]] 기반의 시퀀스를 생성하여 채널 추정의 정확도를 확보합니다.

## 상세 설명

### PUCCH Format 1
TS 38.211 §6.4.1.3.1에 따라, [[PUCCH]] 포맷 1의 [[DMRS]] 시퀀스 $r_{l,n_s}(m)$은 다음과 같이 생성됩니다.
- 시퀀스는 기본 시퀀스 $r_{u,v}^{(\alpha, \delta)}(n)$에 기반하며, 여기서 $\alpha$는 순환 이동 값을 나타냅니다.
- 시간 도메인에서의 직교 커버 코드(OCC)와 결합되어 다중 사용자 다중화가 가능합니다.
- 심볼 인덱스 $l$과 슬롯 인덱스 $n_s$에 따라 시퀀스가 결정됩니다.

### PUCCH Format 2
TS 38.211 §6.4.1.3.2에 따라, [[PUCCH]] 포맷 2의 [[DMRS]] 시퀀스는 다음과 같이 생성됩니다.
- [[DMRS]]는 [[QPSK]] 변조를 사용하여 생성된 시퀀스 $r(m)$을 기반으로 합니다.
- 시퀀스 길이는 할당된 [[PRB]] 수에 비례하며, 의사 난수 생성기(pseudo-random sequence generator)를 통해 초기화됩니다.
- 스크램블링 식별자 $n_{ID}$와 슬롯 내 심볼 위치가 시퀀스 생성의 주요 파라미터로 사용됩니다.

### PUCCH Format 3 및 4
TS 38.211 §6.4.1.3.3에 따라, [[PUCCH]] 포맷 3과 4의 [[DMRS]] 시퀀스는 다음과 같이 생성됩니다.
- 포맷 3은 [[DFT]] 기반의 시퀀스를 사용하며, 포맷 4는 낮은 PAPR 특성을 유지하기 위한 특정 시퀀스 생성 규칙을 따릅니다.
- 시퀀스 $r_{l,n_s}(m)$은 기본 시퀀스에 순환 이동 $\alpha$가 적용된 형태로 생성됩니다.
- 포맷 4의 경우, 특정 사용자 간의 직교성을 보장하기 위해 추가적인 OCC가 적용될 수 있습니다.

## 인과 관계
- [[PUCCH_DMRS_Mapping]] depends_on [[PUCCH_DMRS_Generation]] (생성된 시퀀스를 자원 요소에 매핑)
- [[PUCCH_Format_Processing]] triggers [[PUCCH_DMRS_Generation]] (포맷별 DMRS 생성 절차 호출)

## 관련 개념
- [[PUCCH]] (part_of)
- [[DMRS]] (part_of)
- [[PUCCH_Format_Processing]] (depends_on)
- [[PUCCH_DMRS_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §6.4.1.3.1 (PUCCH format 1 DMRS)
- TS 38.211 §6.4.1.3.2 (PUCCH format 2 DMRS)
- TS 38.211 §6.4.1.3.3 (PUCCH formats 3 and 4 DMRS)

## 소스
- 3GPP TS 38.211 V16.9.0, "NR; Physical channels and modulation"