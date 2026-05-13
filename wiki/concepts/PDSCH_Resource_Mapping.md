# PDSCH_Resource_Mapping

## 정의
[[PDSCH]] 물리 자원 매핑은 상위 계층에서 생성된 복소수 심볼 블록을 가용 가능한 물리 자원 요소(RE, Resource Element)에 순차적으로 배치하고, 가상 자원 블록(VRB, Virtual Resource Block)을 물리 자원 블록(PRB, Physical Resource Block)으로 변환하는 일련의 과정을 의미합니다.

## 요약
[[PDSCH]] 전송을 위해 할당된 자원 중 [[SS_PBCH_Block_Generation]], [[DMRS]], [[CSI_RS_Generation]], [[PUSCH_PTRS_Mapping]] 등 예약된 자원을 제외한 가용 RE에 심볼을 매핑합니다. VRB에서 PRB로의 매핑은 비인터리브(non-interleaved) 또는 인터리브(interleaved) 방식을 따르며, 특정 DCI 포맷 및 검색 공간(Search Space)에 따라 매핑 규칙이 결정됩니다.

## 상세 설명
### 자원 요소 매핑 절차
[[PDSCH]] 심볼은 할당된 VRB 내에서 다음 기준을 만족하는 RE에 순차적으로 매핑됩니다.
- 할당된 VRB 내에 존재할 것
- [[PDSCH_Resource_Allocation]]에 따라 가용하다고 선언된 PRB일 것
- [[DMRS]] 전송에 사용되지 않을 것
- [[CSI_RS_Generation]] 중 비제로 전력(NZP) CSI-RS(단, TRS-ResourceSet으로 설정되지 않은 경우)에 사용되지 않을 것
- [[PUSCH_PTRS_Mapping]]에 정의된 PT-RS에 사용되지 않을 것
- 기타 예약된 자원으로 선언되지 않았을 것

매핑 순서는 할당된 VRB 내에서 부반송파 인덱스($k$)를 먼저 증가시키고, 그 다음 OFDM 심볼 인덱스($l$)를 증가시키는 순서로 진행됩니다.

### VRB-to-PRB 매핑
- 비인터리브 매핑: VRB $i$는 PRB $i$에 매핑됩니다. 단, 공통 검색 공간(Common Search Space)에서 DCI format 1_0으로 스케줄링된 경우, CORESET의 시작 PRB 인덱스를 기준으로 오프셋이 적용됩니다.
- 인터리브 매핑: 자원 블록 번들(Resource Block Bundle) 단위로 분할하여 매핑합니다. 번들 크기는 상위 계층 파라미터(vrb-ToPRB-Interleaver 등)에 의해 결정되며, 주파수 도메인 프리코딩의 일관성을 유지하기 위해 동일 번들 내에서는 동일한 프리코딩이 적용된다고 가정합니다.

### 자원 가용성 제약
- [[SS_PBCH_Block_Generation]]이 포함된 PRB와 겹치는 경우, 해당 심볼에서는 PDSCH 전송이 불가능한 것으로 간주합니다.
- [[PDSCH_DMRS_Generation]] RE와 가용하지 않은 RE가 겹치는 설정은 허용되지 않습니다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_Resource_Mapping]] (물리 자원 매핑 수행)
- [[PDSCH_Resource_Mapping]] depends_on [[PDSCH_Resource_Allocation]] (가용 자원 범위 결정)
- [[PDSCH_Resource_Mapping]] affects [[DMRS]] (DMRS 위치 제외)
- [[PDSCH_Resource_Mapping]] affects [[CSI_RS_Generation]] (CSI-RS 위치 제외)
- [[PDSCH_Resource_Mapping]] affects [[SS_PBCH_Block_Generation]] (SSB 위치 제외)

## 관련 개념
- [[PDSCH]] (part_of)
- [[PDSCH_Resource_Allocation]] (depends_on)
- [[DMRS]] (affects)
- [[CSI_RS_Generation]] (affects)
- [[SS_PBCH_Block_Generation]] (affects)
- [[PDCCH]] (depends_on)

## 스펙 근거
- TS 38.211 §7.3.1.5: PDSCH의 가상 자원 블록 매핑 및 RE 가용성 기준
- TS 38.211 §7.3.1.6: VRB-to-PRB 매핑 방식 및 번들링 규칙
- TS 38.214 §5.1.4: PDSCH 자원 매핑 및 SS/PBCH 블록 간섭 회피

## 소스
- 3GPP TS 38.211 V17.9.0
- 3GPP TS 38.214 V17.9.0