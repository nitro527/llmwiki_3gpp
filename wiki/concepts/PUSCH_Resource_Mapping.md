# PUSCH_Resource_Mapping

## 정의
[[PUSCH]] 자원 매핑은 상위 계층에서 할당된 가상 자원 블록(VRB, Virtual Resource Block)을 물리적 자원 블록(PRB, Physical Resource Block)으로 변환하고, 최종적으로 시간-주파수 영역의 자원 요소(RE, Resource Element)에 복소 심볼을 배치하는 절차를 의미한다.

## 요약
[[PUSCH]] 전송을 위해 UE는 할당된 VRB 내에서 [[DMRS]], [[PTRS]] 및 타 UE를 위한 자원을 제외한 유효한 RE에 데이터를 매핑한다. VRB에서 PRB로의 매핑은 비인터리브(non-interleaved) 방식을 따르며, MsgA를 통한 2-step RACH 절차 시에는 별도의 자원 구성 파라미터에 따라 PUSCH Occasion(PO)이 결정된다.

## 상세 설명
### VRB에서 RE로의 매핑
TS 38.211 §6.3.1.6에 따라, 각 안테나 포트의 복소 심볼 블록은 전송 전력 제어에 따라 진폭 스케일링된 후 할당된 VRB 내의 유효한 RE에 매핑된다. 매핑 순서는 다음과 같다.
1. 할당된 VRB 내의 주파수 인덱스 $k$가 증가하는 순서로 매핑한다. 이때 $k$는 할당된 최하위 VRB의 첫 번째 부반송파를 기준으로 한다.
2. 주파수 인덱스 매핑 완료 후, 시간 인덱스 $l$이 증가하는 순서로 매핑을 진행한다.
3. 매핑 대상 RE는 [[DMRS]], [[PTRS]] 또는 다른 co-scheduled UE를 위해 예약된 RE를 제외한 자원이어야 한다.

### VRB에서 PRB로의 매핑
TS 38.211 §6.3.1.7에 따라, VRB는 비인터리브 방식으로 PRB에 매핑된다.
- 일반적인 경우: VRB $i$는 PRB $i$에 매핑된다.
- 예외: RAR UL grant 또는 TC-RNTI로 스크램블된 DCI format 0_0에 의해 스케줄링된 경우, 초기 UL BWP 내의 자원 할당에 대해서는 특정 오프셋이 적용된 매핑이 수행된다.

### MsgA PUSCH 자원 구성 (Type-2 RACH)
TS 38.213 §8.1A에 따라, 2-step RACH 절차에서의 PUSCH 전송은 다음과 같이 결정된다.
- PO(PUSCH Occasion)는 주파수 및 시간 자원으로 정의되며, [[DMRS]] 자원과 연관된다.
- UE는 msgA-PUSCH-Config를 통해 주파수 시작점, 인터레이스 수, PRB 수 등을 결정한다.
- PO의 유효성은 PRACH Occasion과의 시간/주파수 중첩 여부 및 TDD UL-DL 설정에 따른 UL 심볼 여부에 의해 판단된다.
- 주파수 호핑이 설정된 경우, msgA-HoppingBits를 사용하여 두 번째 홉의 주파수 오프셋을 결정하며, guardPeriodMsgA-PUSCH 설정에 따라 홉 간 시간 분리가 발생할 수 있다.

## 인과 관계
- [[PUSCH]] depends_on [[PUSCH_Resource_Mapping]] (데이터 전송을 위한 물리적 자원 위치 결정)
- [[DMRS_Resource_Mapping]] affects [[PUSCH_Resource_Mapping]] (DMRS가 점유한 RE는 PUSCH 데이터 매핑에서 제외)
- [[PUSCH_Frequency_Hopping]] affects [[PUSCH_Resource_Mapping]] (호핑 설정에 따른 주파수 자원 위치 변경)
- [[PRACH]] triggers [[PUSCH_Resource_Mapping]] (2-step RACH 절차에서 PRACH 이후 PUSCH 전송 시)

## 관련 개념
- [[PUSCH]] (part_of)
- [[DMRS]] (affects)
- [[PRACH]] (triggers)
- [[PUSCH_Frequency_Hopping]] (affects)

## 스펙 근거
- TS 38.211 §6.3.1.6 (VRB to RE mapping)
- TS 38.211 §6.3.1.7 (VRB to PRB mapping)
- TS 38.213 §8.1A (Type-2 RACH PUSCH mapping)

## 소스
- 3GPP TS 38.211 V18.0.0 (2023-12)
- 3GPP TS 38.213 V18.0.0 (2023-12)