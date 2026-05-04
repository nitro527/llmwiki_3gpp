# Scheduling_Offset_Restriction

## 정의
[[Scheduling_Offset_Restriction]]은 [[UE]]가 [[PDCCH]]를 통해 수신한 [[DCI]]에 포함된 스케줄링 정보(예: [[K0]], [[K2]])를 적용할 때, 네트워크가 설정한 최소 스케줄링 오프셋 값([[K0min]], [[K2min]])을 준수하도록 강제하는 물리 계층 메커니즘을 의미합니다.

## 요약
본 기능은 [[UE]]의 처리 능력 및 환경 변화에 따라 [[PDSCH]] 및 [[PUSCH]] 스케줄링의 최소 지연 시간을 동적으로 제어하기 위해 도입되었습니다. [[TS 38.822]]에 정의된 다양한 [[UE]] Feature들이 본 메커니즘과 연관되어 있으며, 특히 [[DCI]] format 0_3/1_3을 통한 동적 변경 기능이 포함됩니다.

## 상세 설명
[[Scheduling_Offset_Restriction]]은 [[UE]]가 스케줄링 명령을 수신한 시점부터 실제 데이터 전송 또는 수신이 시작되기까지의 최소 시간 간격을 제한합니다.

1. **최소 오프셋 설정**: 네트워크는 [[RRC]] 설정을 통해 [[K0min]] 및 [[K2min]] 값을 구성할 수 있습니다. 이는 [[UE]]가 특정 [[BWP]] 또는 [[Cell]] 환경에서 데이터를 처리하기 위해 필요한 최소한의 시간을 보장합니다.
2. **동적 변경**: [[DCI]] format 0_3 또는 1_3을 통해 현재 적용 중인 최소 스케줄링 오프셋 제한을 동적으로 업데이트할 수 있습니다. 이는 트래픽 부하가 급격히 변하거나 [[DRX]] 상태가 변경되는 상황에서 유연한 스케줄링을 가능하게 합니다.
3. **적용 지연**: [[TS 38.214]] §5.3.1에 따라, 새로운 최소 스케줄링 오프셋 제한이 [[DCI]]를 통해 지시된 경우, 해당 변경 사항이 실제 [[UE]] 동작에 반영되기까지는 일정 수준의 적용 지연(Application delay)이 발생합니다.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) [[Scheduling_Offset_Restriction]]의 값 변경
- [[Scheduling_Offset_Restriction]] (affects) [[PDSCH_Reception_Procedures]] 및 [[PUSCH_Transmission_Procedures]]의 타이밍
- [[DRX_Adaptation]] (depends_on) [[Scheduling_Offset_Restriction]]의 동적 조정

## 관련 개념
- [[PDSCH]] (depends_on)
- [[PUSCH]] (depends_on)
- [[DCI_Formats_Processing]] (affects)
- [[DRX_Adaptation]] (depends_on)
- [[Bandwidth_Part_Operation]] (part_of)

## 스펙 근거
- TS 38.214 §5.3.1: Application delay of the minimum scheduling offset restriction에 관한 규정
- TS 38.822: 
    - 19-2: Cross Slot Scheduling
    - 49-10: Dynamic indication of applicable minimum scheduling restriction by DCI format 0_3/1_3
    - 5-1a: UE specific RRC configure UL/DL assignment
    - 11-5: PUSCH repetition Type B
    - 15-7: Transmitting LTE sidelink mode 3 scheduled by NR Uu
    - 19-1: DRX Adaptation
    - 41-12: DRX adaptation for FR2-2
    - 19-1-4: Network controlled small gap (NCSG) performing measurement based on flag deriveSSB-IndexFromCellInter
    - 40-2-2: Basic feature for multi-DCI based inter-cell Multi-TRP operation with two TA enhancement
    - 55-4d: Determining a different PUCCH resource to transmit HARQ-ACK for PDSCH scheduled after UL grant
    - 2-28: A-CSI-RS beam switching timing
    - 3-5a: For type 1 CSS with dedicated RRC configuration, type 3 CSS, and UE-SS, monitoring occasion can be any OFDM symbol(s) of a slot for Case 2 with a DCI gap

## 소스
- 3GPP TS 38.214 v19.0.0, "Physical layer procedures for data"
- 3GPP TS 38.822, "UE features"