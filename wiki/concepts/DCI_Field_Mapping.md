# DCI_Field_Mapping

## 정의
[[DCI_Field_Mapping]]은 [[PDCCH]]를 통해 전송되는 [[DCI]] 포맷 내의 각 제어 정보 필드들이 정보 비트(information bits)로 매핑되는 규칙 및 절차를 의미한다.

## 요약
[[DCI]] 포맷은 정의된 필드 순서에 따라 정보 비트에 매핑되며, 각 필드의 최상위 비트(MSB)는 해당 필드의 가장 낮은 차수 정보 비트에 매핑된다. 페이로드 크기가 12비트 미만인 경우, 12비트가 될 때까지 0으로 패딩(zero-padding)을 수행한다.

## 상세 설명
TS 38.212 §7.3.1에 따라 [[DCI]] 포맷의 필드 매핑은 다음과 같은 원칙을 따른다.

1. 필드 순서: 각 필드는 기술된 순서대로 정보 비트에 매핑된다. 첫 번째 필드는 가장 낮은 차수의 정보 비트에 매핑되며, 이후 필드들은 순차적으로 더 높은 차수의 정보 비트에 매핑된다.
2. 비트 정렬: 각 필드의 최상위 비트(MSB)는 해당 필드에 할당된 정보 비트 중 가장 낮은 차수의 비트에 매핑된다.
3. 제로 패딩: [[DCI]] 포맷의 총 정보 비트 수가 12비트 미만인 경우, 페이로드 크기가 12비트가 될 때까지 0을 추가한다.
4. 크기 결정: [[DCI]] 포맷의 크기는 활성 [[Bandwidth_Part]] 설정에 따라 결정되며, 필요 시 [[DCI_Size_Alignment]] 절차를 통해 조정된다.
5. 특수 포맷 처리: [[DCI]] 포맷 0_3 및 1_3의 경우, 상위 계층 파라미터인 `scheduledCellComboListDCI-0-3` 또는 `scheduledCellComboListDCI-1-3` 설정에 따라 결정되며, 설정되지 않은 경우 `scheduledCellListDCI-0-3` 또는 `scheduledCellListDCI-1-3`을 참조하여 크기를 산출한다.
6. HARQ 코드북: [[HARQ_ACK_Codebook_Determination]] 과정에서 `pdsch-HARQ-ACK-CodebookList-r16` 또는 `pdsch-HARQ-ACK-CodebookListMulticast-r17`이 설정된 경우, 해당 리스트의 엔트리를 사용하여 필드 구성을 결정한다.

## 인과 관계
- [[DCI_Field_Mapping]] depends_on [[DCI_Size_Alignment]] (DCI 페이로드 크기 조정 시 필수)
- [[DCI_Field_Mapping]] affects [[PDCCH]] (DCI 비트 구성이 PDCCH 페이로드로 전송됨)
- [[DCI_Field_Mapping]] depends_on [[Bandwidth_Part_Operation]] (DCI 크기 결정의 기준이 됨)

## 관련 개념
- [[DCI_Size_Alignment]] (depends_on)
- [[PDCCH]] (affects)
- [[Bandwidth_Part_Operation]] (depends_on)
- [[HARQ_ACK_Codebook_Determination]] (depends_on)

## 스펙 근거
- TS 38.212 §7.3.1: DCI formats 및 필드 매핑 규칙 정의
- TS 38.212 §7.3.1.0: DCI 크기 조정 절차

## 소스
- 3GPP TS 38.212 V18.0.0 (2023-12) "Multiplexing and channel coding"