# CSI_PMI_Codebook_TypeII

## 정의
[[CSI_PMI_Codebook_TypeII]]는 [[CSI_RS]]를 기반으로 하는 고해상도 채널 상태 정보(CSI) 보고를 위한 코드북 구조로, 다수의 빔을 결합하여 공간적 해상도를 높이고 서브밴드 단위의 진폭 및 위상 정보를 보고함으로써 하향링크 빔포밍 성능을 최적화하는 기술입니다.

## 요약
이 코드북은 상위 계층 파라미터 codebookType이 'typeII' 또는 'typeII-PortSelection'으로 설정된 경우 사용됩니다. UE는 RI(Rank Indicator)가 2 이하인 경우에만 보고하며, 선택된 빔들에 대한 진폭 및 위상 계수를 서브밴드 단위로 보고하여 기지국이 정밀한 프리코딩을 수행할 수 있도록 지원합니다.

## 상세 설명
### Type II 코드북
TS 38.214 §5.2.2.2.3에 따라, UE는 설정된 CSI-RS 포트 수에 따라 n1-n2-codebookSubsetRestriction을 통해 공간적 기저(spatial basis)를 제한받습니다.
- 프리코더는 RI에 대응하는 코드북 인덱스 $i_1$과 $i_2$로 결정됩니다.
- $i_1$은 빔 결합을 위한 기저 벡터들을 식별하며, $i_2$는 각 빔에 대한 진폭 및 위상 계수를 포함합니다.
- 진폭 계수는 subbandAmplitude 파라미터 설정에 따라 'true'일 경우 전체 해상도로, 'false'일 경우 제한된 해상도로 보고됩니다.
- 가장 강한 계수(strongest coefficient)는 별도로 식별되며, 나머지 계수들은 보고된 진폭 및 위상 정보를 통해 재구성됩니다.

### Type II Port Selection 코드북
TS 38.214 §5.2.2.4에 따라, codebookType이 'typeII-PortSelection'으로 설정된 경우, UE는 특정 안테나 포트를 선택하여 채널을 표현합니다.
- 포트 선택은 인덱스 $i_1$을 통해 수행되며, 선택된 포트들에 대해 Type II와 유사한 방식으로 진폭 및 위상 계수를 보고합니다.
- 이 방식은 특정 안테나 포트 그룹의 물리적 특성을 활용하여 채널을 근사화하는 데 유리합니다.

### 공통 보고 절차
- RI > 2인 경우 보고가 제한됩니다.
- 위상 계수는 phaseAlphabetSize 파라미터에 의해 결정된 크기의 알파벳을 사용합니다.
- 서브밴드 진폭 보고 시, 가장 강한 계수를 제외한 나머지 계수들 중 상위 $M$개의 강한 계수들에 대해 상세 정보를 보고하며, 나머지는 0으로 간주합니다.

## 인과 관계
- [[CSI_Reporting_Procedure]] depends_on [[CSI_PMI_Codebook_TypeII]] (CSI 보고 시 코드북 기반 프리코더 정보 생성)
- [[CSI_RS]] triggers [[CSI_PMI_Codebook_TypeII]] (CSI-RS 측정을 통해 코드북 인덱스 결정)

## 관련 개념
- [[CSI_RS]] (depends_on)
- [[CSI_Reporting_Procedure]] (implements)
- [[CSI_PMI_Codebook_TypeI]] (similar_to)
- [[CSI_PMI_Codebook_Enhanced_TypeII]] (similar_to)

## 스펙 근거
- TS 38.214 §5.2.2.2.3: Type II Codebook 상세 구조 및 계수 보고 절차
- TS 38.214 §5.2.2.2.4: Type II Port Selection Codebook 상세 구조 및 포트 선택 절차

## 소스
- 3GPP TS 38.214 V17.9.0 (Release 17)