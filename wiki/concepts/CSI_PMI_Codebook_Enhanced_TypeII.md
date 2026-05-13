# CSI_PMI_Codebook_Enhanced_TypeII

## 정의
Enhanced Type II 코드북은 3GPP Rel-16에서 도입된 고해상도 CSI 피드백 메커니즘으로, 다중 안테나 포트 환경에서 서브밴드 단위의 프리코딩 행렬을 정밀하게 보고하기 위해 설계된 코드북 구조입니다.

## 요약
Enhanced Type II 코드북은 높은 주파수 선택적 채널 환경에서 더 정밀한 프리코딩 행렬을 생성하기 위해 서브밴드별 계수 보고를 지원합니다. 이는 상위 계층 파라미터인 codebookType이 'typeII-r16'으로 설정된 경우 사용되며, paramCombination-r16을 통해 코드북 파라미터 조합을 결정합니다. 서브밴드별로 하나 또는 두 개의 프리코딩 행렬을 보고함으로써 채널 상태 정보를 최적화합니다.

## 상세 설명
Enhanced Type II 코드북은 4, 8, 12, 16, 24, 32개의 안테나 포트를 지원하며, 다음과 같은 핵심 파라미터와 절차를 통해 동작합니다.

1. 코드북 파라미터 설정:
   - n1-n2-codebookSubsetRestriction-r16을 통해 N1, N2 값을 구성합니다.
   - paramCombination-r16을 통해 코드북 파라미터 조합을 매핑하며, 특정 안테나 포트 수 및 RI 제한 조건에 따라 일부 조합은 사용이 제한됩니다.

2. 서브밴드 보고 메커니즘:
   - numberOfPMI-SubbandsPerCQI-Subband 파라미터에 의해 제어됩니다.
   - M=1인 경우, 각 서브밴드마다 하나의 프리코딩 행렬을 보고합니다.
   - M=2인 경우, BWP 내의 서브밴드 위치에 따라 프리코딩 행렬 보고 개수가 달라집니다. 첫 번째 또는 마지막 서브밴드가 아닌 경우, 서브밴드의 앞부분 PRB와 뒷부분 PRB에 대해 각각 하나씩, 총 두 개의 프리코딩 행렬을 보고합니다.

3. 프리코딩 행렬 구성:
   - 프리코딩 행렬은 L개의 레이어에 대해 벡터 그룹 인덱스 및 계수(진폭, 위상)를 통해 결정됩니다.
   - 진폭 계수(amplitude coefficient)는 비트맵을 통해 보고 여부가 결정되며, 가장 강한 계수(strongest coefficient)를 기준으로 인덱스가 재매핑됩니다.
   - 진폭 및 위상 계수는 테이블 5.2.2.2.5-2 및 5.2.2.2.5-3에 정의된 매핑 규칙을 따릅니다.

4. 제약 조건:
   - typeII-RI-Restriction-r16에 따라 RI 보고가 제한됩니다.
   - amplitudeSubsetRestriction-r16이 지원되지 않는 경우, 특정 진폭 제한 파라미터 설정이 허용되지 않습니다.

## 인과 관계
- [[CSI_Reporting_Procedure]] depends_on [[CSI_PMI_Codebook_Enhanced_TypeII]] (CSI 보고 시 코드북 기반 PMI 계산 수행)
- [[CSI_PMI_Codebook_Enhanced_TypeII]] depends_on [[CSI_RS_Generation]] (CSI-RS 포트 구성을 통한 코드북 파라미터 결정)

## 관련 개념
- [[CSI_Reporting_Procedure]] (depends_on)
- [[CSI_RS_Generation]] (depends_on)
- [[CSI_PMI_Codebook_TypeI]] (similar_to)

## 스펙 근거
- TS 38.214 §5.2.2.2.5에 따르면, Enhanced Type II 코드북은 4~32개의 안테나 포트를 지원하며 codebookType이 'typeII-r16'으로 설정되어야 합니다.
- TS 38.214 §5.2.2.2.5의 Table 5.2.2.2.5-1은 코드북 파라미터 조합을 정의합니다.
- TS 38.214 §5.2.2.2.5에 따르면, 서브밴드별 프리코딩 행렬 보고 개수는 numberOfPMI-SubbandsPerCQI-Subband 파라미터에 의해 결정됩니다.

## 소스
- 3GPP TS 38.214 v16.9.0, "NR; Physical layer procedures for data" §5.2.2.2.5