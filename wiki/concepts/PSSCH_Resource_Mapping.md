# PSSCH_Resource_Mapping

## 정의
[[PSSCH]] 자원 매핑은 복소수 심볼 블록을 할당된 가상 자원 블록(Virtual Resource Block, VRB) 내의 자원 요소(Resource Element, RE)에 배치하고, 이를 물리 자원 블록(Physical Resource Block, PRB)으로 변환하는 물리 계층 절차를 의미한다.

## 요약
[[PSSCH]] 자원 매핑은 2단계 과정으로 수행된다. 첫 번째 단계에서는 2nd-stage [[SCI]]를 위한 복소수 심볼을 매핑하고, 두 번째 단계에서는 나머지 데이터 심볼을 매핑한다. 매핑 시 [[DMRS]], [[PTRS]], [[PSCCH]], [[SL_PRS]] 등 예약된 자원을 제외하며, 첫 번째 OFDM 심볼의 자원 요소는 직전 OFDM 심볼에 복제된다. VRB에서 PRB로의 매핑은 비인터리빙(non-interleaved) 방식을 따른다.

## 상세 설명
[[PSSCH]] 전송을 위해 사용되는 각 안테나 포트에 대해, 복소수 심볼 블록은 전송 전력 규정을 준수하기 위해 진폭 스케일링 계수와 곱해진 후 할당된 VRB 내의 RE에 매핑된다.

매핑 절차는 다음과 같이 2단계로 진행된다:

1. 2nd-stage [[SCI]] 매핑:
   - 할당된 VRB 내에서 주파수 인덱스($k$)를 먼저 증가시키고, 그 다음 시간 인덱스($l$)를 증가시키는 순서로 매핑한다.
   - 시작점은 연관된 [[DMRS]]를 포함하는 첫 번째 [[PSSCH]] 심볼부터이다.
   - 매핑 대상 RE는 [[DMRS]], [[PTRS]], 또는 [[PSCCH]] 전송에 사용되지 않는 RE여야 한다.

2. 데이터 심볼 매핑:
   - 2nd-stage [[SCI]]에 해당하지 않는 복소수 변조 심볼을 매핑한다.
   - 주파수 인덱스($k$)를 먼저 증가시키고, 그 다음 시간 인덱스($l$)를 증가시키는 순서로 매핑한다.
   - 시작 위치는 TS 38.214에 정의된 규정을 따른다.
   - 매핑 대상 RE는 1단계에서 2nd-stage [[SCI]]에 사용된 RE, [[SL_PRS]] 전송에 사용되는 RE, 그리고 [[DMRS]], [[PTRS]], [[CSI_RS]], [[PSCCH]] 전송에 사용되는 RE를 제외해야 한다.

첫 번째 OFDM 심볼에 매핑된 [[PSSCH]] 자원 요소(해당 심볼 내의 [[DMRS]], [[PTRS]], [[CSI_RS]] 포함)는 해당 심볼 바로 앞의 OFDM 심볼에 복제되어야 한다.

VRB-to-PRB 매핑은 비인터리빙 방식을 사용하며, VRB 인덱스 $n_{VRB}$는 동일한 인덱스의 PRB $n_{PRB} = n_{VRB}$에 매핑된다.

## 인과 관계
- [[PSSCH_Resource_Mapping]] depends_on [[PSSCH_DMRS_Mapping]] (DMRS 위치 제외 필요)
- [[PSSCH_Resource_Mapping]] depends_on [[PSSCH_PTRS_Mapping]] (PTRS 위치 제외 필요)
- [[PSSCH_Resource_Mapping]] depends_on [[PSCCH_Resource_Mapping]] (PSCCH 위치 제외 필요)
- [[PSSCH_Resource_Mapping]] depends_on [[SL_PRS_Resource_Selection]] (SL PRS 위치 제외 필요)

## 관련 개념
- [[PSSCH]] (part_of)
- [[SCI]] (affects)
- [[DMRS]] (affects)
- [[PTRS]] (affects)
- [[PSCCH]] (affects)
- [[SL_PRS]] (affects)

## 스펙 근거
- TS 38.211 §8.3.1.5 (Mapping to virtual resource blocks)
- TS 38.211 §8.3.1.6 (Mapping from virtual to physical resource blocks)

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03)