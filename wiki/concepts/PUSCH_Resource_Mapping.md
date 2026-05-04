# PUSCH_Resource_Mapping

## 정의
[[PUSCH]] Resource Mapping은 상위 계층에서 생성된 복소 심볼들을 가상 자원 블록(Virtual Resource Blocks, VRB)에 매핑하고, 이를 다시 물리 자원 블록(Physical Resource Blocks, PRB)으로 변환하여 전송하는 5G NR의 물리 계층 절차를 의미합니다.

## 요약
PUSCH 전송을 위한 자원 매핑은 크게 가상 자원 블록으로의 매핑과 물리 자원 블록으로의 매핑 단계로 나뉩니다. 이는 기본적으로 [[Basic PUSCH transmission]]을 지원하며, [[SR]], [[HARQ-ACK]], [[CSI]]의 다중화 및 [[PUSCH]] 내 피기백(piggyback) 전송을 포함합니다. 또한, [[Multi-TRP PUSCH repetition]] (Type A/B, codebook/non-codebook based), [[Configured Grant]] 기반의 [[Multi-PUSCHs]], 그리고 [[RAR UL grant]] 및 [[TC-RNTI]] 기반의 [[Repetition of PUSCH transmission]] 등 다양한 전송 시나리오를 지원합니다.

## 상세 설명
PUSCH 자원 매핑은 TS 38.211 규격에 따라 다음의 단계를 거칩니다.

1. **가상 자원 블록 매핑 (Mapping to virtual resource blocks):**
   - 전송될 복소 심볼들은 먼저 가상 자원 블록에 매핑됩니다. 이 과정에서 심볼들은 시간 및 주파수 도메인의 자원 요소(Resource Elements)에 배치됩니다.
   - [[PUSCH]] 전송은 [[Slot]] 내에서 수행되며, 데이터 심볼은 [[DMRS_Generation_Mapping]] 및 [[PTRS_Generation_Mapping]]에 의해 점유되지 않은 자원 요소에 할당됩니다.

2. **물리 자원 블록으로의 매핑 (Mapping from virtual to physical resource blocks):**
   - 가상 자원 블록은 물리 자원 블록으로 매핑됩니다. 이 과정은 주파수 도메인에서의 자원 할당 방식(Type 1 또는 Type 2)에 따라 결정됩니다.
   - [[PUSCH_Frequency_Hopping]]이 설정된 경우, 주파수 도메인 자원 할당은 홉(hop) 단위로 변경될 수 있습니다.

3. **특수 전송 시나리오:**
   - [[RAR UL grant]]를 통해 스케줄링된 PUSCH는 [[TC-RNTI]]로 스크램블된 DCI format 0_0에 의해 제어되며, 특정 반복(repetition) 규칙을 따릅니다.
   - [[Multi-PUSCHs for Configured Grant]]는 다수의 PUSCH 전송을 단일 설정으로 처리하여 오버헤드를 줄입니다.
   - [[SR/HARQ-ACK/CSI multiplexing]]은 동일한 슬롯 내에서 발생할 경우, [[PUCCH]] 또는 [[PUSCH]]를 통해 효율적으로 다중화되어 전송됩니다.

## 인과 관계
- [[PUSCH_Layer_Mapping]] (depends_on)
- [[PUSCH_Precoding]] (depends_on)
- [[PUSCH_Frequency_Hopping]] (affects)
- [[PUSCH_Transmission_Procedures]] (triggers)
- [[Slot]] (part_of)
- [[DMRS_Generation_Mapping]] (affects)
- [[PTRS_Generation_Mapping]] (affects)

## 관련 개념
- [[Basic PUSCH transmission]] (part_of)
- [[Multi-TRP PUSCH repetition]] (part_of)
- [[Configured Grant]] (part_of)
- [[RAR UL grant]] (part_of)
- [[SR/HARQ-ACK/CSI multiplexing]] (part_of)
- [[Physical_Resource_Grid]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.1.6: Mapping to virtual resource blocks
- TS 38.211 §6.3.1.7: Mapping from virtual to physical resource blocks
- TS 38.822: UE Feature Priority (2-12, 4-19, 4-19a, 4-19b, 23-3-1, 23-3-1-1, 23-3-1-2, 23-3-1-3, 30-6, 50-1, 55-4d)

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)
- 3GPP TS 38.822 (UE Feature Priority)

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/PUSCH_DMRS_Transmission.md
- entities/PUSCH.md