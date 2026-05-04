# PUCCH_Spatial_Setting

## 정의
[[PUCCH]] Spatial Setting은 [[UE]]가 [[PUCCH]] 전송 시 사용할 공간 필터(Spatial domain filter)를 결정하고, 이를 [[gNB]]와 정렬하기 위한 설정 절차를 의미합니다. 이는 [[Beam_correspondence]]를 기반으로 하며, 상위 계층 시그널링 및 [[MAC_CE]]를 통해 동적으로 제어됩니다.

## 요약
[[PUCCH]] 전송을 위한 공간 관계(Spatial relation)는 [[PUCCH-SpatialRelationInfo]]를 통해 설정됩니다. [[UE]]는 [[MAC_CE]]를 통해 특정 [[PUCCH]] 자원에 대한 공간 관계를 활성화하거나 업데이트할 수 있으며, 이는 [[HARQ_ACK]] 전송 등 [[UCI]] 전송의 빔 방향을 결정하는 핵심 요소입니다.

## 상세 설명
[[PUCCH]] 전송 시 [[UE]]는 설정된 공간 관계 정보를 사용하여 송신 빔을 형성합니다. 주요 메커니즘은 다음과 같습니다.

1. **Spatial Relation 설정**: [[RRC]] 시그널링을 통해 [[PUCCH-SpatialRelationInfo]]가 구성되며, 이는 [[SS_PBCH_Block]], [[CSI_RS]], 또는 [[SRS]]와 같은 참조 신호를 기반으로 공간 필터를 정의합니다.
2. **MAC CE 기반 업데이트**: [[TS_38_213]] §9.2.2에 따라, [[UE]]는 [[MAC_CE]]를 수신하여 특정 [[PUCCH]] 자원 세트 내의 자원에 대해 활성화된 공간 관계를 지시받을 수 있습니다. 이는 [[PUCCH_Spatial_Setting]]의 동적 변경을 가능하게 합니다.
3. **Beam Correspondence**: [[UE]]는 [[Beam_correspondence]] 능력을 활용하여 하향링크 참조 신호(예: [[CSI_RS]])를 통해 획득한 공간 정보를 상향링크 [[PUCCH]] 전송에 적용합니다.
4. **추가적인 공간 관계**: [[PUCCH]] 전송의 유연성을 위해 다중 공간 관계 설정이 지원되며, 이는 [[Active_spatial_relations]] 및 [[Additional_active_spatial_relation_for_PUCCH]] 기능을 통해 구현됩니다.

## 인과 관계
- [[PUCCH_Resource_Sets]] (depends_on): [[PUCCH]] 자원 설정 내에 공간 관계 정보가 포함됨
- [[MAC_CE]] (triggers): [[PUCCH]] 자원에 대한 공간 관계 활성화 및 변경을 유발함
- [[Beam_correspondence]] (depends_on): 하향링크 빔 정보를 상향링크 빔으로 변환하는 능력에 의존함
- [[HARQ_ACK_spatial_bundling_for_PUCCH_or_PUSCH_per_PUCCH_group]] (affects): 공간적 빔 설정에 따라 [[HARQ_ACK]] 번들링 방식이 영향을 받을 수 있음

## 관련 개념
- [[PUCCH]] (part_of)
- [[Beam_correspondence]] (depends_on)
- [[MAC_CE]] (triggers)
- [[RRC]] (part_of)
- [[CSI_RS]] (depends_on)
- [[SS_PBCH_Block]] (depends_on)
- [[SRS]] (depends_on)

## 스펙 근거
- [[TS_38_213]] §9.2.2: [[PUCCH]] 자원 및 공간 관계 설정에 관한 절차 정의
- [[TS_38_822]]: [[Active_spatial_relations]], [[Beam_correspondence]], [[PUCCH_spatialrelationinfo_indication_by_a_MAC_CE_per_PUCCH_resource]] 등 관련 기능 명시

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)
- 3GPP TS 38.822 V17.0.0 (2022-03)