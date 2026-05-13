# DCI_Size_Alignment

## 정의
[[DCI_Size_Alignment]]는 [[PDCCH]]를 통해 전송되는 서로 다른 [[DCI_Formats]] 간의 페이로드 크기를 일치시키기 위해 수행되는 패딩(padding) 또는 절단(truncation) 절차를 의미한다.

## 요약
[[PDCCH]] 모니터링 시 [[UE]]가 복호화해야 하는 [[DCI_Formats]]의 크기가 서로 다를 경우, 블라인드 디코딩 복잡도를 줄이기 위해 특정 규칙에 따라 비트를 추가하거나 제거하여 크기를 정렬한다. 이 과정은 [[Common_Search_Space]]와 [[UE_Specific_Search_Space]]에서 단계별로 수행되며, 최종적으로 셀당 설정된 DCI 크기 개수 제한을 준수해야 한다.

## 상세 설명
[[DCI_Size_Alignment]]는 TS 38.212 §7.3.1.0에 정의된 단계별 절차를 따른다.

### 단계별 절차
- **Step 0**: [[Common_Search_Space]] 내의 [[DCI_Format_0_0]]과 [[DCI_Format_1_0]] 간의 크기를 정렬한다. [[DCI_Format_0_0]]이 [[DCI_Format_1_0]]보다 작으면 제로 패딩을 추가하고, 크면 [[Frequency_Domain_Resource_Assignment]] 필드의 상위 비트를 절단한다.
- **Step 1**: [[UE_Specific_Search_Space]] 내의 [[DCI_Format_0_0]]과 [[DCI_Format_1_0]] 간의 크기를 정렬한다. [[Supplementary_Uplink]] 설정 시 SUL과 non-SUL 간의 [[DCI_Format_0_0]] 크기를 맞추며, 이후 [[DCI_Format_1_0]]과의 크기 비교를 통해 패딩을 수행한다.
- **Step 2**: [[DCI_Format_0_1]] 및 [[DCI_Format_1_1]]에 대해 수행한다. SUL 설정 시 [[DCI_Format_0_1]] 간 크기를 맞추고, 다른 [[Search_Space]]의 [[DCI_Format_0_0]]/[[DCI_Format_1_0]]과 크기가 같으면 1비트의 제로 패딩을 추가한다.
- **Step 2A/2B**: [[DCI_Format_0_2]], [[DCI_Format_1_2]], [[DCI_Format_0_3]], [[DCI_Format_1_3]]에 대해 SUL 설정 시 크기 정렬을 수행한다.
- **Step 3~4D**: 설정된 DCI 크기 개수 제한(셀당 최대 4개, C-RNTI 기준 최대 3개)을 만족할 때까지 반복하며, 필요 시 패딩을 제거하거나 추가적인 정렬을 수행한다.

### 제한 사항
모든 정렬 절차 후에도 다음 조건 중 하나라도 발생하면 해당 설정은 유효하지 않은 것으로 간주한다.
- 셀당 설정된 DCI 크기 개수가 4개를 초과하는 경우
- C-RNTI로 설정된 DCI 크기 개수가 3개를 초과하는 경우
- 서로 다른 [[Search_Space]] 간에 특정 [[DCI_Formats]]의 크기가 동일하여 [[PDCCH]] 후보군이 겹치는 경우(예: [[DCI_Format_0_0]]과 [[DCI_Format_0_1]] 등)

## 인과 관계
- [[DCI_Size_Alignment]] depends_on [[PDCCH_Search_Space_Configuration]] (검색 공간 설정에 따른 DCI 크기 결정)
- [[DCI_Size_Alignment]] affects [[PDCCH_Validation]] (정렬된 DCI 크기를 기반으로 유효성 검사 수행)
- [[DCI_Size_Alignment]] implements [[DCI_Formats]] (DCI 포맷 간 크기 일치 메커니즘 구현)

## 관련 개념
- [[PDCCH]] (affects)
- [[DCI_Formats]] (affects)
- [[Search_Space]] (depends_on)
- [[PDCCH_Validation]] (depends_on)
- [[Bandwidth_Part_Operation]] (depends_on)

## 스펙 근거
- TS 38.212 §7.3.1.0: DCI size alignment 절차 및 단계별 규칙 정의
- TS 38.213 §10.1: DCI 크기 카운팅 및 제한 사항 정의

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03) "Multiplexing and channel coding"