# PSSCH_Resource_Mapping

## 정의
[[PSSCH]] (Physical Sidelink Shared Channel)의 전송을 위해 상위 계층에서 할당된 자원 내에서, 복소 심볼(complex-valued symbols)을 가상 자원 블록(VRB, Virtual Resource Block)에 매핑하고, 이를 다시 물리 자원 블록(PRB, Physical Resource Block)으로 매핑하는 절차를 의미합니다.

## 요약
[[PSSCH]]의 자원 매핑은 크게 두 단계로 구성됩니다. 첫 번째는 변조된 심볼을 [[PSSCH]] 전송을 위해 할당된 VRB에 순차적으로 매핑하는 과정이며, 두 번째는 이 VRB를 실제 무선 자원인 PRB로 변환하는 과정입니다. 이 과정에서 [[Sidelink]] 통신의 특성에 따라 자원 할당 방식이 결정됩니다.

## 상세 설명
TS 38.211 §8.3.1.5 및 §8.3.1.6에 정의된 [[PSSCH]] 자원 매핑 절차는 다음과 같습니다.

1. **VRB 매핑**: 변조된 심볼은 먼저 VRB 인덱스 순서대로 매핑됩니다. 이때 각 심볼은 [[PSSCH]] 전송에 할당된 자원 요소(RE, Resource Element)에 순차적으로 채워집니다.
2. **VRB-to-PRB 매핑**: VRB는 물리적인 자원인 PRB에 매핑됩니다. [[Sidelink]] 모드 1 및 모드 2 동작에 따라 상위 계층에서 지시된 자원 할당 정보에 기반하여 매핑이 수행됩니다.
3. **제약 사항**: 매핑 과정에서 [[DMRS]] (Demodulation Reference Signal) 및 기타 제어 채널([[PSCCH]])이 점유하는 RE는 제외되며, 해당 RE를 건너뛰고 다음 가용 RE에 심볼을 매핑합니다.

## 인과 관계
- [[PSSCH_Modulation]] (depends_on): 변조된 심볼이 자원 매핑의 입력값으로 사용됩니다.
- [[PSSCH_Layer_Mapping]] (depends_on): 레이어 매핑된 심볼이 VRB 매핑의 대상이 됩니다.
- [[Sidelink_Resource_Grid]] (affects): 매핑 결과가 물리 자원 그리드 상의 위치를 결정합니다.

## 관련 개념
- [[PSSCH]] (part_of)
- [[Sidelink]] (part_of)
- [[DMRS_Generation_Mapping]] (affects)
- [[PSCCH_Resource_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §8.3.1.5: Mapping to virtual resource blocks
- TS 38.211 §8.3.1.6: Mapping from virtual to physical resource blocks

## 소스
- 3GPP TS 38.211 V17.9.0 (Release 17)