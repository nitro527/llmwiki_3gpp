# CSI_PMI_Codebook_TypeI

## 정의
Type I CSI(Channel State Information) PMI(Precoding Matrix Indicator) 코드북은 5G NR에서 기지국이 빔포밍을 수행할 때 UE가 채널 상태를 기반으로 최적의 프리코더를 선택하여 보고하도록 설계된 코드북 체계입니다. 이는 Single-Panel 및 Multi-Panel 구성으로 나뉩니다.

## 요약
Type I 코드북은 낮은 오버헤드로 채널 정보를 피드백하기 위해 설계되었습니다. Single-Panel은 단일 안테나 어레이를 사용하는 일반적인 환경에 적합하며, Multi-Panel은 여러 개의 안테나 패널을 사용하는 환경에서 공간적 다이버시티를 활용하기 위해 사용됩니다. UE는 상위 계층 파라미터 설정을 통해 코드북 타입을 선택하고, RI(Rank Indicator), PMI, CQI(Channel Quality Indicator)를 포함한 CSI를 보고합니다.

## 상세 설명

### Type I Single-Panel Codebook
2개의 안테나 포트(3000, 3001)를 사용하는 경우, PMI는 코드북 인덱스에 직접 매핑됩니다. 4개에서 32개 사이의 안테나 포트를 사용하는 경우, PMI는 RI 값에 따라 3개 또는 4개의 코드북 인덱스($i_1, i_2, i_3, i_4$) 조합으로 구성됩니다.

- 코드북 인덱스 조합: RI가 1~2인 경우 $i_1, i_2, i_3$를 사용하며, RI가 3~4인 경우 $i_1, i_2, i_3, i_4$를 사용합니다.
- 파라미터 설정: $N_1, N_2$는 상위 계층 파라미터 `n1-n2`를 통해 설정되며, 이는 안테나 포트 수에 따른 코드북 구성을 결정합니다. $N_2=1$인 경우 UE는 $i_2$를 보고하지 않습니다.
- 코드북 서브셋 제한: `twoTX-CodebookSubsetRestriction` 또는 `typeI-SinglePanel-codebookSubsetRestriction-i2`와 같은 비트맵 파라미터를 통해 특정 프리코더의 보고를 제한할 수 있습니다.
- RI 제한: `typeI-SinglePanel-ri-Restriction`을 통해 특정 랭크에 대한 보고를 제한합니다.

### Type I Multi-Panel Codebook
8, 16, 32개의 안테나 포트를 사용하는 환경에서 다중 패널을 지원합니다.

- 파라미터 설정: $N_g, N_1, N_2$는 상위 계층 파라미터 `ng-n1-n2`를 통해 설정됩니다.
- 코드북 모드: `codebookMode`는 '1' 또는 '2'로 설정되며, 이는 프리코더 벡터 구성 방식에 영향을 미칩니다.
- 프리코더 구성: PMI는 코드북 인덱스 $i_1, i_2$로 구성되며, $i_1$은 패널 간 위상 및 빔 정보를 포함합니다.
- RI 제한: `ri-Restriction` 비트맵을 통해 특정 랭크의 보고를 제한합니다.

## 인과 관계
- [[CSI_RS_Generation]] depends_on [[CSI_PMI_Codebook_TypeI]] (CSI-RS 포트 기반 코드북 구성)
- [[CSI_Reporting_Procedure]] triggers [[CSI_PMI_Codebook_TypeI]] (CSI 보고 시 코드북 기반 PMI 계산)

## 관련 개념
- [[CSI_RS_Generation]] (depends_on)
- [[CSI_Reporting_Procedure]] (affects)
- [[CSI_PMI_Codebook_TypeII]] (similar_to)

## 스펙 근거
- TS 38.214 §5.2.2.2.1 (Type I Single-Panel Codebook 정의 및 파라미터)
- TS 38.214 §5.2.2.2.2 (Type I Multi-Panel Codebook 정의 및 파라미터)

## 소스
- 3GPP TS 38.214 v16.9.0 (Release 16)