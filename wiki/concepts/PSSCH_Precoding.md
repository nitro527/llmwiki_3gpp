# PSSCH_Precoding

## 정의
[[PSSCH]] (Physical Sidelink Shared Channel) 프리코딩은 [[Sidelink]] 전송을 위해 [[Layer_Mapping]]을 거친 심볼들을 안테나 포트로 매핑하기 전, 공간적 다중화 및 전송 품질 향상을 위해 수행되는 신호 처리 절차를 의미합니다.

## 요약
[[PSSCH]] 프리코딩은 [[Layer_Mapping]] 이후의 복소수 심볼 벡터에 대해 프리코딩 행렬을 적용하여 안테나 포트별 신호를 생성합니다. 이 과정은 [[Sidelink]] 전송의 공간적 특성을 결정하며, [[TS_38_211]] 규격에 따라 정의됩니다.

## 상세 설명
[[PSSCH]] 프리코딩은 다음과 같은 단계로 수행됩니다.

1. 입력: [[PSSCH_Layer_Mapping]]을 통해 생성된 복소수 심볼 블록 $x(i) = [x^{(0)}(i) \dots x^{(\nu-1)}(i)]^T$가 입력됩니다. 여기서 $\nu$는 전송 레이어의 수입니다.
2. 프리코딩 적용: 프리코딩 행렬 $P(i)$를 입력 벡터에 곱하여 안테나 포트별 신호 $y(i) = [y^{(0)}(i) \dots y^{(P-1)}(i)]^T$를 생성합니다.
3. 수식: $y(i) = P(i)x(i)$
   - $P(i)$는 안테나 포트 수 $P$와 레이어 수 $\nu$에 의해 결정되는 행렬입니다.
   - [[Sidelink]] 전송에서 프리코딩은 주로 단일 안테나 포트 전송을 기본으로 하거나, 특정 조건에서 다중 안테나 전송을 지원합니다.

## 인과 관계
- [[PSSCH_Layer_Mapping]] (depends_on)
- [[PSSCH_Resource_Mapping]] (affects)

## 관련 개념
- [[PSSCH]] (part_of)
- [[Sidelink]] (part_of)
- [[PSSCH_Layer_Mapping]] (depends_on)

## 스펙 근거
- [[TS_38_211]] §8.3.1.4에 따르면, [[PSSCH]] 전송을 위한 프리코딩은 레이어 매핑된 신호에 대해 안테나 포트 매핑을 수행하는 과정으로 정의됩니다.

## 소스
- 3GPP TS 38.211 V17.4.0, "Physical channels and modulation", Section 8.3.1.4