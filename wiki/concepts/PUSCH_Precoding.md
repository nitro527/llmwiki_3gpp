# PUSCH_Precoding

## 정의
[[PUSCH]] 전송을 위해 레이어 매핑된 심볼 벡터에 프리코딩 행렬을 적용하여 안테나 포트로 매핑하는 물리 계층 절차를 의미합니다.

## 요약
[[PUSCH]] 프리코딩은 전송 방식에 따라 코드북 기반(codebook-based)과 비코드북 기반(non-codebook-based)으로 구분됩니다. 코드북 기반 전송 시, [[DCI]]를 통해 전달된 [[SRI]]와 [[TPMI]]를 사용하여 프리코딩 행렬을 결정하며, 이는 안테나 포트 수와 레이어 수에 따라 정의된 테이블을 따릅니다. 비코드북 기반 전송의 경우 프리코딩 행렬은 단위 행렬(identity matrix)로 설정됩니다.

## 상세 설명
[[PUSCH]] 프리코딩은 벡터 블록 $z(i)$에 대해 프리코딩 행렬 $W$를 적용하여 $y(i)$를 생성하는 과정입니다.

$y(i) = W z(i)$

여기서 $i = 0, 1, \dots, M_{symb}^{ap}-1$이며, $M_{symb}^{ap}$는 안테나 포트당 심볼 수입니다.

1. 비코드북 기반 전송:
   - 프리코딩 행렬 $W$는 단위 행렬로 설정됩니다.

2. 코드북 기반 전송:
   - 안테나 포트 수에 따라 프리코딩 행렬 $W$가 결정됩니다.
   - 단일 안테나 포트, 단일 레이어 전송 시 $W = [1]$입니다.
   - 2개 또는 4개의 안테나 포트 사용 시, TS 38.211 Table 6.3.1.5-1 ~ 6.3.1.5-7에 정의된 행렬을 사용합니다.
   - 8개의 안테나 포트 사용 시, TS 38.211 Table 6.3.1.5-8의 포트 매핑 함수와 중간 프리코딩 행렬(intermediate precoding matrix) $W_i$를 조합하여 결정합니다.
   - [[TPMI]] 인덱스는 [[DCI]] 포맷 0_1, 0_2, 0_3 또는 상위 계층 파라미터에 의해 결정됩니다.
   - 상위 계층 파라미터 txConfig가 설정되지 않은 경우, $W$는 단위 행렬로 간주됩니다.

3. 코드북 서브셋 및 제약:
   - 코드북 서브셋은 상위 계층 파라미터 codebookSubset 또는 codebookSubsetDCI-0-2에 의해 제한될 수 있습니다.
   - ul-FullPowerTransmission 설정에 따라 fullpowerMode1 또는 fullpowerMode2가 적용되며, 이는 사용 가능한 코드북 및 SRS 리소스 구성에 영향을 미칩니다.

## 인과 관계
- [[PUSCH_Layer_Mapping]] depends_on [[PUSCH_Precoding]] (레이어 매핑된 심볼에 프리코딩 적용)
- [[DCI_Field_Mapping]] triggers [[PUSCH_Precoding]] (DCI 내 SRI/TPMI 필드가 프리코딩 행렬 결정)
- [[SRS_Generation]] affects [[PUSCH_Precoding]] (SRS 리소스와 연계된 SRI가 프리코더 선택의 기준이 됨)

## 관련 개념
- [[PUSCH]] (implements)
- [[SRI]] (affects)
- [[TPMI]] (affects)
- [[DCI]] (triggers)
- [[SRS]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.1.5: 프리코딩 행렬 정의 및 적용 절차
- TS 38.212 §7.3.1.1.3: DCI 포맷 0_2 내 프리코딩 정보 필드 구성
- TS 38.214 §6.1.1.1: 코드북 기반 UL 전송 절차 및 SRI/TPMI 매핑

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03)
- 3GPP TS 38.212 V17.9.0 (2024-03)
- 3GPP TS 38.214 V17.9.0 (2024-03)