# PUSCH_PTRS_Generation

## 정의
[[PUSCH]] 전송 시 위상 잡음(Phase Noise) 보상을 위해 사용되는 [[PTRS]]의 시퀀스 생성 절차를 의미하며, [[Transform_Precoding]] 활성화 여부에 따라 서로 다른 생성 방식을 적용한다.

## 요약
[[PUSCH]]를 위한 [[PTRS]] 시퀀스는 [[DMRS]]와 유사하게 의사 난수(Pseudo-random) 시퀀스를 기반으로 생성된다. [[Transform_Precoding]]이 비활성화된 경우와 활성화된 경우에 따라 시퀀스 매핑 및 생성 파라미터가 결정되며, 이는 수신단에서 위상 추적을 수행하기 위한 기준 신호로 활용된다.

## 상세 설명
[[PUSCH]] [[PTRS]] 시퀀스 $r_{l,k}(m)$은 다음과 같은 절차를 통해 생성된다.

1. 기본 시퀀스 생성:
   [[PTRS]] 시퀀스는 다음 식에 의해 정의된다.
   $r_{l,k}(m) = r_{l,m}(m)$
   여기서 $l$은 [[OFDM]] 심볼 인덱스, $k$는 서브캐리어 인덱스이다.

2. [[Transform_Precoding]] 비활성화 시:
   [[Transform_Precoding]]이 비활성화된 경우, 시퀀스는 [[DMRS]] 시퀀스 생성과 동일한 골드 시퀀스(Gold sequence)를 기반으로 생성된다.
   $r_{l,m}(m) = \frac{1}{\sqrt{2}}((1-2c(2m)) + j(1-2c(2m+1)))$
   이때, 의사 난수 시퀀스 $c(i)$는 [[DMRS]] 설정에 따라 초기화되며, 슬롯 내의 심볼 인덱스 $l$과 [[RNTI]], [[Scrambling_ID]] 등에 의해 결정된다.

3. [[Transform_Precoding]] 활성화 시:
   [[Transform_Precoding]]이 활성화된 경우, [[PTRS]]는 [[DFT]] 확산 이전에 생성되며, 시퀀스 생성은 다음과 같은 파라미터를 따른다.
   - 시퀀스 $r_{l,m}(m)$은 [[DMRS]] 시퀀스 생성 방식과 동일한 구조를 가지나, [[Transform_Precoding]]이 적용된 [[PUSCH]]의 특성에 맞춰 매핑된다.
   - 시퀀스 생성 시 사용되는 초기값 $c_{init}$은 상위 계층 파라미터 및 [[DMRS]] 포트 정보에 의해 결정된다.

## 인과 관계
- [[PUSCH_PTRS_Generation]] depends_on [[DMRS_Sequence_Generation]] (시퀀스 생성 알고리즘 및 초기값 공유)
- [[PUSCH_PTRS_Generation]] affects [[PUSCH_PTRS_Mapping]] (생성된 시퀀스를 물리 자원에 배치)
- [[PUSCH_Transform_Precoding]] affects [[PUSCH_PTRS_Generation]] (변환 프리코딩 활성화 여부에 따른 시퀀스 생성 방식 결정)

## 관련 개념
- [[PUSCH]] (part_of)
- [[PTRS]] (implements)
- [[DMRS_Sequence_Generation]] (depends_on)
- [[Transform_Precoding]] (affects)
- [[PUSCH_PTRS_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §6.4.1.2.1: PUSCH PTRS 시퀀스 생성 공식 및 파라미터 정의

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03) "Physical channels and modulation"