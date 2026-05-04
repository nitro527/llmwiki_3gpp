# PDSCH_Resource_Mapping

## 정의
[[PDSCH]] Resource Mapping은 [[Physical_Resource_Grid]] 상에서 변조된 심볼들을 물리적 자원 요소([[RE]])에 매핑하는 과정으로, 안테나 포트 매핑, 가상 자원 블록([[VRB]])에서 물리 자원 블록([[PRB]])으로의 매핑, 그리고 [[RE]] 레벨의 레이트 매칭을 포함하는 절차를 의미합니다.

## 요약
[[PDSCH]] 전송을 위한 자원 매핑은 크게 두 단계로 구분됩니다. 첫째, 안테나 포트 매핑을 통해 레이어 데이터를 안테나 포트에 할당합니다. 둘째, 자원 블록 할당 방식에 따라 [[VRB]]를 [[PRB]]에 매핑합니다. 이 과정에서 [[RE]] 레벨의 입도(granularity)를 고려하여 [[DMRS]], [[PTRS]] 등 제어 신호나 참조 신호가 점유하는 자원을 제외한 나머지 자원에 실제 데이터가 매핑됩니다.

## 상세 설명
1. **안테나 포트 매핑**: [[PDSCH]] 레이어는 TS 38.211 §7.3.1.4에 따라 안테나 포트에 매핑됩니다. 이는 전송되는 레이어의 수와 안테나 포트 구성에 따라 결정됩니다.
2. **VRB-to-PRB 매핑**: TS 38.211 §7.3.1.5 및 §7.3.1.6에 따라 수행됩니다.
   - Non-interleaved 매핑: [[VRB]]가 동일한 인덱스의 [[PRB]]에 직접 매핑됩니다.
   - Interleaved 매핑: [[VRB]]가 주파수 다이버시티를 얻기 위해 특정 규칙에 따라 분산된 [[PRB]]에 매핑됩니다.
3. **RE 레벨 매핑**: TS 38.214 §5.1.4.2에 따라 수행됩니다.
   - 데이터 심볼은 할당된 [[PRB]] 내에서 주파수 우선(frequency-first) 방식으로 매핑됩니다.
   - [[DMRS]], [[CSI_RS]], [[PTRS]] 등 예약된 자원 요소는 건너뛰며, 이를 RE-level rate matching이라 합니다.
   - RB 심볼 레벨 입도(TS 38.214 §5.1.4.1)에서는 할당된 자원 블록 내에서 심볼 단위로 매핑이 이루어집니다.

## 인과 관계
- [[PDSCH_Layer_Mapping]] (depends_on): 안테나 포트 매핑 이전에 레이어 매핑이 선행되어야 합니다.
- [[DMRS_Generation_Mapping]] (affects): [[DMRS]] 위치에 따라 [[PDSCH]] 데이터가 매핑될 [[RE]]가 결정됩니다.
- [[PDSCH_Resource_Allocation]] (triggers): 상위 계층이나 [[DCI]]를 통한 자원 할당 정보가 매핑 절차를 시작합니다.

## 관련 개념
- [[PDSCH]] (part_of)
- [[Physical_Resource_Grid]] (depends_on)
- [[DMRS]] (affects)
- [[VRB]] (part_of)
- [[PRB]] (part_of)

## 스펙 근거
- TS 38.211 §7.3.1.4: Antenna port mapping
- TS 38.211 §7.3.1.5: Mapping to virtual resource blocks
- TS 38.211 §7.3.1.6: Mapping from virtual to physical resource blocks
- TS 38.214 §5.1.4: PDSCH resource mapping
- TS 38.214 §5.1.4.1: PDSCH resource mapping with RB symbol level granularity
- TS 38.214 §5.1.4.2: PDSCH resource mapping with RE level granularity

## 소스
- 3GPP TS 38.211 V17.0.0 (Release 17)
- 3GPP TS 38.214 V17.0.0 (Release 17)