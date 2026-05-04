# PDCCH_Resource_Mapping

## 정의
[[PDCCH]] 물리 자원 매핑은 [[CCE]] 단위로 구성된 제어 채널 자원을 실제 시간-주파수 자원인 [[REG]] 및 [[CORESET]] 내의 물리적 자원으로 변환하는 절차를 의미합니다.

## 요약
[[PDCCH]]는 [[CORESET]] 내에서 [[CCE]] 인덱싱을 통해 정의되며, [[REG]] 번들링 및 인터리빙 과정을 거쳐 물리적 자원에 매핑됩니다. 본 절차는 [[Self-carrier_scheduling]] 및 [[Cross-carrier_scheduling]] 환경을 지원하며, [[UE]]의 [[PDCCH]] 모니터링 능력에 따라 자원 할당이 결정됩니다.

## 상세 설명
[[PDCCH]]의 물리 자원 매핑은 다음과 같은 단계로 수행됩니다.

1. **CCE-to-REG 매핑**: [[PDCCH]]는 하나 이상의 [[CCE]]로 구성되며, 각 [[CCE]]는 6개의 [[REG]]로 이루어집니다. [[REG]]는 하나의 [[OFDM_symbol]] 내의 하나의 [[PRB]]를 점유합니다.
2. **REG 번들링**: 주파수 다이버시티를 얻기 위해 [[REG]]들은 번들로 묶여 [[CORESET]] 내에 분산됩니다.
3. **인터리빙**: [[CORESET]] 설정에 따라 [[REG]]들은 인터리빙되거나 비인터리빙 방식으로 매핑됩니다. 인터리빙 방식은 [[CORESET]] 내에서 [[CCE]]가 주파수 도메인 상에 분산되도록 하여 간섭을 완화합니다.
4. **다중 서빙 셀 환경**: [[Cross-carrier_scheduling]]이 설정된 경우, [[PDCCH]]는 다른 서빙 셀의 [[DCI]]를 스케줄링할 수 있습니다. 이때 [[CIF]] 필드가 [[DCI]]에 포함되어 대상 셀을 식별합니다.

## 인과 관계
- [[PDCCH_CORESET_Mapping]] (depends_on): [[CORESET]] 설정이 선행되어야 [[PDCCH]] 자원 매핑이 가능함.
- [[DCI_Formats_Processing]] (affects): [[DCI]] 크기에 따라 필요한 [[CCE]] 집합 수준(Aggregation Level)이 결정됨.
- [[Bandwidth_Part_Operation]] (part_of): [[PDCCH]] 모니터링은 활성화된 [[BWP]] 내에서 수행됨.

## 관련 개념
- [[PDCCH]] (part_of)
- [[CORESET]] (part_of)
- [[CCE]] (part_of)
- [[REG]] (part_of)
- [[DCI]] (affects)
- [[Self-carrier_scheduling]] (similar_to)
- [[Cross-carrier_scheduling]] (similar_to)

## 스펙 근거
- [[PDCCH]] 자원 매핑 절차는 TS 38.211 §7.3.2.5에 규정되어 있습니다.
- [[UE]]의 [[PDCCH]] 모니터링 및 자원 할당 절차는 TS 38.213 §10.1에 정의되어 있습니다.
- [[Self-carrier_scheduling]] 및 [[Cross-carrier_scheduling]]에 관한 상세 사항은 TS 38.213 §10.1.1을 따릅니다.
- [필수(항상)] 2-12: [[PUSCH]] 전송 관련 기본 절차 준수.
- [필수(cap)] 2-31: [[Beam_failure_recovery]] 절차 지원.
- [필수(cap)] 2-33a: [[PDSCH]] RE-mapping 패턴 지원.
- [선택] 11-2: Rel-16 [[PDCCH]] 모니터링 능력.
- [선택] 11-2a, 11-2c, 11-2d, 11-2e: [[DL_CA]] 및 [[NR-DC]] 환경에서의 [[CCE]]/[[BD]] 스케일링 및 캐리어 수 지원.

## 소스
- 3GPP TS 38.211 V16.9.0, "Physical channels and modulation"
- 3GPP TS 38.213 V16.9.0, "Physical layer procedures for control"
- 3GPP TS 38.822, "UE radio access capabilities"