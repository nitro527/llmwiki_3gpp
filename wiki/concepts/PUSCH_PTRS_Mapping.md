# PUSCH_PTRS_Mapping

## 정의
[[PUSCH]] 전송 시 위상 잡음 보상을 위해 사용되는 [[PTRS]] 심볼을 물리 자원 그리드 상의 특정 부반송파 및 심볼 위치에 배치하는 절차를 의미한다.

## 요약
[[PUSCH_PTRS_Mapping]]은 [[DMRS]] 포트와의 연관성을 기반으로 수행되며, [[PUSCH_Transform_Precoding]] 활성화 여부에 따라 매핑 방식이 결정된다. 주파수 도메인에서는 특정 부반송파 간격으로, 시간 도메인에서는 [[DMRS]] 심볼 위치를 기준으로 매핑이 이루어진다.

## 상세 설명
[[PUSCH]]를 위한 [[PTRS]] 매핑은 TS 38.211 §6.4.1.2.2에 정의된 절차를 따른다.

1. 매핑 기본 원칙
- [[PTRS]]는 [[PUSCH]]가 할당된 자원 블록 내에서 특정 부반송파(subcarrier)에 매핑된다.
- [[PTRS]] 안테나 포트는 [[DMRS]] 포트와 연관되어 있으며, 상위 계층 파라미터에 의해 설정된 [[DMRS]] 포트 인덱스 중 하나와 매핑된다.

2. [[PUSCH_Transform_Precoding]] 비활성 시 (CP-OFDM)
- 주파수 도메인 매핑: [[PTRS]]는 설정된 주파수 밀도에 따라 특정 부반송파에 매핑된다. 매핑되는 부반송파 인덱스는 [[PUSCH]] 할당 대역폭 내에서 결정된다.
- 시간 도메인 매핑: [[PTRS]]는 [[DMRS]] 심볼 위치를 기준으로 오프셋을 적용하여 배치된다. 이는 위상 잡음 추적을 위해 [[DMRS]]와 인접한 심볼에 배치되는 것을 원칙으로 한다.

3. [[PUSCH_Transform_Precoding]] 활성 시 (DFT-s-OFDM)
- [[PTRS]]는 [[PUSCH]] 심볼 내에서 특정 부반송파 그룹에 매핑된다.
- 변환 프리코딩이 활성화된 경우, [[PTRS]]는 시간 도메인에서 [[DMRS]]와 동일한 심볼 위치에 매핑되거나, 특정 규칙에 따라 분산 배치된다.

4. 안테나 포트 매핑
- [[PTRS]] 포트의 수는 [[DMRS]] 포트의 수와 랭크(rank) 정보에 따라 결정된다.
- 다중 [[PTRS]] 포트가 설정된 경우, 각 포트는 서로 다른 [[DMRS]] 포트 그룹과 연관되어 직교성을 유지한다.

## 인과 관계
- [[PUSCH_PTRS_Generation]] depends_on [[PUSCH_PTRS_Mapping]] (생성된 시퀀스를 물리 자원에 배치)
- [[PUSCH_Transform_Precoding]] affects [[PUSCH_PTRS_Mapping]] (변환 프리코딩 활성 여부에 따른 매핑 규칙 변경)
- [[DMRS]] depends_on [[PUSCH_PTRS_Mapping]] (PTRS 매핑 시 DMRS 위치 참조)

## 관련 개념
- [[PUSCH]] (part_of)
- [[PTRS]] (part_of)
- [[DMRS]] (depends_on)
- [[PUSCH_Transform_Precoding]] (affects)

## 스펙 근거
- TS 38.211 §6.4.1.2.2: PUSCH를 위한 PTRS의 물리 자원 매핑 규칙 및 DMRS와의 연관성 정의

## 소스
- 3GPP TS 38.211 V18.0.0, "NR; Physical channels and modulation"