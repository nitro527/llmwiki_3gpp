# PUSCH_DMRS_Transmission

## 정의
[[PUSCH]] 전송 시 채널 추정 및 복조를 위해 사용하는 [[DMRS]]의 생성, 매핑 및 전송 절차를 의미합니다.

## 요약
[[PUSCH]] [[DMRS]]는 [[DCI]]를 통해 할당된 자원 내에서 전송되며, [[UE]]의 능력(Capability)에 따라 공간 관계 설정 및 다중 포트 지원 여부가 결정됩니다. 본 절차는 [[DMRS]] 포트 할당, [[CDM]] 그룹 구성, 그리고 [[PT-RS]]와의 연관성을 포함합니다.

## 상세 설명
[[TS 38.214]] §6.2.2에 따르면, [[PUSCH]] [[DMRS]] 전송 절차는 다음과 같은 핵심 요소로 구성됩니다.

* [[DMRS]] 포트 할당: [[DCI]] 포맷을 통해 전송되는 정보에 따라 [[DMRS]] 포트가 결정됩니다. 이는 [[PUSCH]] 전송을 위한 레이어 수와 연관됩니다.
* [[CDM]] 그룹: [[DMRS]]는 직교성을 유지하기 위해 [[CDM]] 그룹으로 나뉘며, 동일한 [[CDM]] 그룹 내의 포트들은 시간/주파수 자원을 공유합니다.
* 공간 관계: [[UE]]는 [[Active_spatial_relations]] (Capability 2-60)을 지원해야 하며, 이를 통해 [[PUSCH]] 전송 시의 빔포밍 및 공간적 특성을 결정합니다.
* [[PT-RS]] 연관: [[PUSCH]] [[DMRS]] 포트는 [[PT-RS]] 포트와 연관될 수 있습니다. Rel.18에서 강화된 [[DMRS]] 포트를 사용하는 경우, 랭크(Rank) 1-4 및 5-8에 대해 1포트 또는 2포트 [[PT-RS]] 구성이 가능합니다 (Capability 40-4-6g, 40-4-6h, 40-4-6i, 40-4-6j).
* 전송 방식: [[Single-DCI_based_STx2P_SDM_scheme_for_PUSCH]] (Capability 40-6-1, 40-6-1-1, 40-6-1a)를 지원하여 코드북 기반 및 비코드북 기반 전송에서 효율적인 다중 안테나 전송을 수행합니다.

## 인과 관계
* [[DCI_Formats_Processing]] (triggers) [[PUSCH_DMRS_Transmission]]
* [[PUSCH_DMRS_Transmission]] (affects) [[PUSCH_Resource_Mapping]]
* [[PUSCH_DMRS_Transmission]] (depends_on) [[DMRS_Generation_Mapping]]
* [[PUSCH_DMRS_Transmission]] (affects) [[PTRS_Generation_Mapping]]

## 관련 개념
* [[PUSCH]] (part_of)
* [[DMRS]] (part_of)
* [[PT-RS]] (similar_to)
* [[DCI_Formats_Processing]] (depends_on)

## 스펙 근거
* [[TS 38.214]] §6.2.2: [[UE]] [[DMRS]] 전송 절차 정의
* [[TS 38.822]]: [[UE]] Feature Priority 및 관련 Capability 정의

## 소스
* 3GPP TS 38.214 V19.0.0 (Release 19)
* 3GPP TS 38.822 V18.0.0 (Release 18)