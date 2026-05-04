# PUSCH

## 정의
[[PUSCH]]는 5G NR에서 상향링크 사용자 데이터를 전송하기 위해 사용되는 물리 채널입니다. [[UL-SCH]]로부터 전달된 전송 블록을 물리 계층에서 처리하여 기지국으로 전송하는 역할을 수행합니다.

## 요약
[[PUSCH]]는 데이터 전송을 위한 채널로, [[HARQ]] 프로세스를 지원하며 [[UCI]]를 피기백(piggyback)하여 전송할 수 있습니다. 주요 절차로는 [[PUSCH_Scrambling]], [[PUSCH_Modulation]], [[PUSCH_Layer_Mapping]], [[PUSCH_Transform_Precoding]], [[PUSCH_Precoding]] 및 [[PUSCH_Resource_Mapping]]이 포함됩니다. 또한, [[PUSCH_Power_Control]]을 통해 전송 전력을 제어하며, [[PUSCH_Preparation_Time]] 내에 전송 준비를 완료해야 합니다.

## 상세 설명
[[PUSCH]] 전송 과정은 다음과 같은 단계로 구성됩니다:

1. **상위 계층 데이터 처리**: [[UL-SCH]] 데이터는 [[Transport_Block_CRC_Attachment]]를 거쳐 [[LDPC_Base_Graph_Selection]], [[Code_Block_Segmentation_and_Code_Block_CRC_Attachment]], [[Channel_Coding_of_UL_SCH]], [[Rate_Matching]], [[Code_Block_Concatenation]] 과정을 수행합니다.
2. **데이터 및 제어 정보 다중화**: [[UCI_Multiplexing_PUSCH]]를 통해 [[HARQ-ACK]], [[CSI]], [[SR]] 등이 [[PUSCH]]에 다중화될 수 있습니다.
3. **물리 계층 처리**: 
   - [[PUSCH_Scrambling]]: 비트 수준의 스크램블링을 수행합니다.
   - [[PUSCH_Modulation]]: [[Modulation_Mapper]]를 통해 심볼을 생성합니다.
   - [[PUSCH_Layer_Mapping]]: 심볼을 하나 이상의 레이어로 매핑합니다.
   - [[PUSCH_Transform_Precoding]]: 필요 시 DFT 기반의 변환 프리코딩을 적용합니다.
   - [[PUSCH_Precoding]]: 안테나 포트로 심볼을 매핑합니다.
   - [[PUSCH_Resource_Mapping]]: [[Physical_Resource_Grid]] 내의 가상 및 물리 자원에 매핑합니다.

**UE Feature 지원**:
- [[HARQ-ACK_Codebook_Determination]] 및 [[HARQ-ACK_Spatial_Bundling]]을 지원합니다.
- [[UCI_Multiplexing_PUSCH]]를 통해 [[HARQ-ACK]], [[CSI]], [[SR]]을 [[PUSCH]]에 다중화하며, 특히 [[HARQ-ACK_Multiplexing_on_PUSCH_with_different_PUCCH_PUSCH_starting_OFDM_symbols]] 기능을 지원합니다.
- [[UL_Intra-UE_Multiplexing_Prioritization]]을 통해 우선순위가 다른 채널 간의 충돌을 관리합니다.
- [[Supplemental_Uplink]] 및 [[Uplink_Switching_Procedures]]를 지원합니다.

## 인과 관계
- [[PUSCH_Transmission_Procedures]] depends_on [[DCI_Formats_Processing]] (전송 파라미터 결정)
- [[PUSCH_Resource_Allocation]] affects [[PUSCH_Resource_Mapping]]
- [[PUSCH_Power_Control]] affects [[PUSCH_Transmission_Procedures]]
- [[UCI_Multiplexing_PUSCH]] triggers [[UCI_Rate_Matching]]
- [[PUSCH_Preparation_Time]] depends_on [[Frame_Structure_Numerology]]
- [[CSI_Reporting_Procedures]] (affects) [[PUSCH]]
- [[DAPS_Handover_Procedures]] (affects) [[PUSCH]]
- [[DMRS_Bundling_Procedures]] (affects) [[PUSCH]]
- [[L1_L2_Triggered_Mobility]] (affects) [[PUSCH]]
- [[PDCCH_Monitoring_Procedures]] (affects) [[PUSCH]]
- [[PDCCH_Validation_Procedures]] (affects) [[PUSCH]]
- [[PTRS_Generation_Mapping]] (affects) [[PUSCH]]
- [[PUCCH_Resource_Determination]] (affects) [[PUSCH]]
- [[PUSCH_Codebook_Based_Transmission]] (affects) [[PUSCH]]
- [[PUSCH_Configured_Grant_Transmission]] (affects) [[PUSCH]]
- [[PUSCH_DCI_Field_Processing]] (affects) [[PUSCH]]
- [[PUSCH_DMRS_Transmission]] (affects) [[PUSCH]]
- [[PUSCH_Frequency_Hopping]] (affects) [[PUSCH]]
- [[PUSCH_HARQ_Feedback]] (affects) [[PUSCH]]
- [[PUSCH_MsgA_Transmission]] (affects) [[PUSCH]]
- [[PUSCH_PTRS_Transmission]] (affects) [[PUSCH]]
- [[PUSCH_Repetition_Procedures]] (affects) [[PUSCH]]
- [[PUSCH_Transmission_Parameters]] (affects) [[PUSCH]]
- [[Power_Headroom_Report]] (affects) [[PUSCH]]
- [[RACH_Procedure_L1]] (affects) [[PUSCH]]
- [[SRS_Carrier_Switching]] (affects) [[PUSCH]]
- [[SRS_Collision_Handling]] (affects) [[PUSCH]]
- [[SRS_Generation_Mapping]] (affects) [[PUSCH]]
- [[SR_Reporting_Procedure]] (affects) [[PUSCH]]
- [[Scheduling_Offset_Restriction]] (affects) [[PUSCH]]
- [[Sidelink_HARQ_Reporting]] (affects) [[PUSCH]]
- [[Slot_Format_Configuration]] (affects) [[PUSCH]]
- [[UCI_Bit_Sequence_Generation]] (affects) [[PUSCH]]
- [[UCI_PUCCH_Multiplexing]] (affects) [[PUSCH]]
- [[UCI_Reporting_Different_Priorities]] (affects) [[PUSCH]]
- [[UTO_UCI_Reporting]] (affects) [[PUSCH]]
- [[Uplink_Power_Control]] (affects) [[PUSCH]]
- [[Uplink_Power_Prioritization]] (affects) [[PUSCH]]

## 관련 개념
- [[UL-SCH]] (part_of)
- [[PUSCH_Scrambling]] (part_of)
- [[PUSCH_Modulation]] (part_of)
- [[PUSCH_Layer_Mapping]] (part_of)
- [[PUSCH_Transform_Precoding]] (part_of)
- [[PUSCH_Precoding]] (part_of)
- [[PUSCH_Resource_Mapping]] (part_of)
- [[PUSCH_Power_Control]] (affects)
- [[UCI_Multiplexing_PUSCH]] (part_of)
- [[PUSCH_Preparation_Time]] (depends_on)
- [[HARQ]] (part_of)

## 스펙 근거
- TS 38.211 §6.3.1: [[PUSCH]] 물리 계층 처리 절차 정의
- TS 38.212 §6.2: [[UL-SCH]] 채널 코딩 및 다중화 절차
- TS 38.213 §7.1: [[PUSCH]] 전송을 위한 UE 동작 및 전력 제어
- TS 38.214 §6.1: [[PUSCH]] 전송 절차, 자원 할당 및 전송 방식
- TS 38.214 §6.4: [[PUSCH_Preparation_Time]] 정의

## 소스
- 3GPP TS 38.211 v19.0.0 (2024-03)
- 3GPP TS 38.212 v18.0.0 (2024-03)
- 3GPP TS 38.213 v18.0.0 (2024-03)
- 3GPP TS 38.214 v19.0.0 (2024-03)

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/CSI_Reporting_Procedures.md
- concepts/DAPS_Handover_Procedures.md
- concepts/DMRS_Bundling_Procedures.md
- concepts/Frame_Structure_Numerology.md
- concepts/HARQ_ACK_Codebook_Determination.md
- concepts/Half_Duplex_UE_Operation.md
- concepts/L1_L2_Triggered_Mobility.md
- concepts/Modulation_Mapper.md
- concepts/PDCCH_Monitoring_Procedures.md
- concepts/PDCCH_Resource_Mapping.md
- concepts/PDCCH_Validation_Procedures.md
- concepts/PTRS_Generation_Mapping.md
- concepts/PUCCH_Resource_Determination.md
- concepts/PUSCH_Codebook_Based_Transmission.md
- concepts/PUSCH_Configured_Grant_Transmission.md
- concepts/PUSCH_DCI_Field_Processing.md
- concepts/PUSCH_DMRS_Transmission.md
- concepts/PUSCH_Frequency_Hopping.md
- concepts/PUSCH_HARQ_Feedback.md
- concepts/PUSCH_Layer_Mapping.md
- concepts/PUSCH_Modulation.md
- concepts/PUSCH_MsgA_Transmission.md
- concepts/PUSCH_PTRS_Transmission.md
- concepts/PUSCH_Power_Control.md
- concepts/PUSCH_Precoding.md
- concepts/PUSCH_Preparation_Time.md
- concepts/PUSCH_Repetition_Procedures.md
- concepts/PUSCH_Resource_Allocation.md
- concepts/PUSCH_Resource_Mapping.md
- concepts/PUSCH_Scrambling.md
- concepts/PUSCH_Transform_Precoding.md
- concepts/PUSCH_Transmission_Parameters.md
- concepts/PUSCH_Transmission_Procedures.md
- concepts/Power_Headroom_Report.md
- concepts/RACH_Procedure_L1.md
- concepts/SRS_Carrier_Switching.md
- concepts/SRS_Collision_Handling.md
- concepts/SRS_Generation_Mapping.md
- concepts/SR_Reporting_Procedure.md
- concepts/Scheduling_Offset_Restriction.md
- concepts/Sidelink_HARQ_Reporting.md
- concepts/Slot_Format_Configuration.md
- concepts/UCI_Bit_Sequence_Generation.md
- concepts/UCI_Multiplexing_PUSCH.md
- concepts/UCI_PUCCH_Multiplexing.md
- concepts/UCI_Rate_Matching.md
- concepts/UCI_Reporting_Different_Priorities.md
- concepts/UTO_UCI_Reporting.md
- concepts/Uplink_Power_Control.md
- concepts/Uplink_Power_Prioritization.md
- concepts/Uplink_Switching_Procedures.md
- entities/DMRS.md
- entities/PDCCH.md
- entities/PT_RS.md
- entities/PUSCH.md
- entities/Reference_Signals.md
- entities/SRS.md