# Uplink_Power_Prioritization

## 정의
[[Uplink_Power_Prioritization]]은 단말([[UE]])이 다수의 상향링크 채널 및 신호([[PUSCH]], [[PUCCH]], [[PRACH]], [[SRS]])를 동시에 전송해야 할 때, 단말의 최대 전송 전력 제한을 초과하지 않도록 각 채널 간의 우선순위를 결정하고 전력을 할당하는 절차를 의미합니다.

## 요약
단말은 상향링크 전송 시 총 전송 전력이 설정된 최대 전력 제한을 넘지 않도록 조정해야 합니다. TS 38.213 §7.5에 따라, 전력 부족 상황 발생 시 우선순위가 낮은 채널부터 전력을 줄이거나 전송을 생략하는 방식으로 우선순위 기반의 전력 제어를 수행합니다.

## 상세 설명
단말은 상향링크 전송 시 다음과 같은 우선순위 규칙 및 기능 지원을 기반으로 동작합니다.

### 필수 기능
- 8-3: Basic power control operation (항상 지원)
- 2-60: Active spatial relations (Capability 기반 지원)

### 선택 기능
- 4-26: Parallel [[PRACH]] and [[SRS]]/[[PUCCH]]/[[PUSCH]] transmissions across CCs in inter-band CA
- 6-16: Supplemental uplink
- 39-2: Parallel PRACH and SRS/PUCCH/PUSCH transmissions across CCs in intra-band non-contiguous CA
- 4-25: Parallel SRS and PUCCH/PUSCH transmission across CCs in inter-band CA
- 6-19: Simultaneous transmission of SRS on an SUL/non-SUL carrier and PUSCH/PUCCH/SRS on the other UL carrier in the same cell
- 9-3: Parallel MsgA and SRS/PUCCH/PUSCH transmissions across CCs in inter-band CA
- 10-25: Enable configured UL transmissions when SFI field in DCI 2_0 is configured but DCI 2_0 is not detected
- 12-1: UL intra-UE multiplexing/prioritization of overlapping channel/signals with two priority levels in physical layer
- 13-9e: PathLoss estimate maintenance per serving cell
- 13-9f: PathLoss estimate maintenance across all cells

단말은 다수의 서빙 셀에서 상향링크 전송이 겹칠 경우, 각 채널의 우선순위를 비교하여 전력 할당을 결정합니다. 전력 제한 상황에서 우선순위가 낮은 채널은 전력이 0으로 조정되거나 전송이 취소될 수 있습니다.

## 인과 관계
- [[Uplink_Power_Control]] (depends_on): 각 채널의 개별 전력 제어 결과가 우선순위 결정의 입력값이 됨.
- [[PUSCH_Power_Control]] (part_of): PUSCH 전력 할당 시 우선순위 규칙이 적용됨.
- [[PUCCH_Power_Control]] (part_of): PUCCH 전력 할당 시 우선순위 규칙이 적용됨.
- [[SRS_Power_Control]] (part_of): SRS 전력 할당 시 우선순위 규칙이 적용됨.
- [[PRACH_Power_Control]] (part_of): PRACH 전력 할당 시 우선순위 규칙이 적용됨.

## 관련 개념
- [[Uplink_Power_Control]] (depends_on)
- [[PUSCH_Power_Control]] (part_of)
- [[PUCCH_Power_Control]] (part_of)
- [[SRS_Power_Control]] (part_of)
- [[PRACH_Power_Control]] (part_of)

## 스펙 근거
- TS 38.213 §7.5: Prioritizations for transmission power reductions에 따르면, 단말은 상향링크 전송 전력이 최대 전력을 초과할 경우 정의된 우선순위 규칙에 따라 전력을 조정해야 함을 명시함.

## 소스
- 3GPP TS 38.213 Release 18.0.0 (i80) §7.5