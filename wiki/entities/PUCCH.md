# PUCCH

## 정의
[[PUCCH]]는 5G NR에서 상향링크 제어 정보인 [[UCI]]를 전송하기 위해 정의된 물리 채널입니다.

## 요약
[[PUCCH]]는 [[HARQ-ACK]], [[SR]], [[CSI]]를 기지국으로 전달하는 역할을 수행합니다. 전송되는 정보량과 시간/주파수 자원 점유 방식에 따라 5가지 포맷(Format 0 ~ 4)으로 구분되며, 각 포맷은 고유한 [[Sequence Generation]], [[Modulation]], [[Mapping to physical resources]] 절차를 가집니다.

## 상세 설명
[[PUCCH]]는 전송되는 정보의 양과 심볼 길이에 따라 다음과 같이 구성됩니다.

*   [[PUCCH]] Format 0: 1~2개의 심볼을 사용하며, 짧은 페이로드(최대 2비트)를 위한 시퀀스 기반 전송 방식입니다.
*   [[PUCCH]] Format 1: 4~14개의 심볼을 사용하며, 짧은 페이로드(최대 2비트)를 위한 시퀀스 변조 방식입니다.
*   [[PUCCH]] Format 2: 1~2개의 심볼을 사용하며, 2비트 이상의 페이로드를 위한 [[Scrambling]], [[Modulation]] 기반 전송 방식입니다.
*   [[PUCCH]] Format 3 및 4: 4~14개의 심볼을 사용하며, 많은 양의 [[UCI]]를 전송하기 위해 [[Block-wise spreading]] 및 [[Transform precoding]]을 지원합니다.

[[UCI]]는 전송 전 [[Channel Coding of UCI]] 및 [[Rate Matching]] 과정을 거치며, 필요에 따라 [[UCI Multiplexing PUCCH]]를 통해 단일 [[PUCCH]] 자원으로 다중화됩니다. 또한, [[PUCCH Power Control]]을 통해 상향링크 전송 전력을 제어합니다.

## 인과 관계
*   [[UCI Bit Sequence Generation]] (triggers) [[UCI Channel Coding]]
*   [[UCI Channel Coding]] (triggers) [[UCI Rate Matching]]
*   [[UCI Rate Matching]] (triggers) [[UCI Multiplexing PUCCH]]
*   [[PUCCH Format Processing]] (depends_on) [[PUCCH]]
*   [[PUCCH]] (affects) [[PUCCH Power Control]]

## 관련 개념
- [[UCI]] (part_of)
- [[HARQ-ACK]] (part_of)
- [[SR]] (part_of)
- [[CSI]] (part_of)
- [[PUCCH Format Processing]] (depends_on)
- [[PUCCH Power Control]] (affects)
- [[UCI Multiplexing PUCCH]] (depends_on)
- [[CSI_Reporting_Procedures]] (affects)
- [[DAPS_Handover_Procedures]] (affects)
- [[DMRS_Bundling_Procedures]] (affects)
- [[HARQ_ACK_Codebook_Determination]] (affects)
- [[Half_Duplex_UE_Operation]] (affects)
- [[IAB_Timing_Control]] (affects)
- [[PDSCH_DCI_Field_Processing]] (affects)
- [[PUCCH_Cell_Switching]] (affects)
- [[PUCCH_Repetition]] (affects)
- [[PUCCH_Resource_Determination]] (affects)
- [[PUCCH_Resource_Sets]] (affects)
- [[PUCCH_Sequence_Hopping]] (affects)
- [[PUCCH_Spatial_Setting]] (affects)
- [[PUSCH_Frequency_Hopping]] (affects)
- [[PUSCH_HARQ_Feedback]] (affects)
- [[PUSCH_Modulation]] (affects)
- [[PUSCH_Resource_Mapping]] (affects)
- [[Power_Headroom_Report]] (affects)
- [[RACH_Procedure_L1]] (affects)
- [[RedCap_UE_Procedures]] (affects)
- [[SCell_Activation_Deactivation_Timing]] (affects)
- [[SPS_HARQ_Deferral]] (affects)
- [[SRS_Carrier_Switching]] (affects)
- [[SRS_Collision_Handling]] (affects)
- [[SR_Reporting_Procedure]] (affects)
- [[Sidelink_HARQ_Reporting]] (affects)
- [[Slot_Format_Configuration]] (affects)
- [[UCI_Bit_Sequence_Generation]] (affects)
- [[UCI_PUCCH_Multiplexing]] (affects)
- [[UCI_Processing_PUCCH]] (affects)
- [[UCI_Rate_Matching]] (affects)
- [[UCI_Reporting_Different_Priorities]] (affects)
- [[UTO_UCI_Reporting]] (affects)
- [[Uplink_Power_Control]] (affects)
- [[Uplink_Power_Prioritization]] (affects)
- [[Uplink_Switching_Procedures]] (affects)
- [[Reference_Signals]] (affects)

## 스펙 근거
*   TS 38.211 §6.3.2: [[PUCCH]]의 일반적인 구조, 시퀀스 생성, 포맷별 자원 매핑 규정.
*   TS 38.212 §6.3.1: [[UCI]] 비트 생성, 채널 코딩, 레이트 매칭 및 다중화 절차.
*   TS 38.822: UE Feature 4-1(기본), 4-2~4-7(포맷별 지원), 4-12(공간 번들링), 4-13(SR 설정), 4-19/4-19a/4-19b(다중화 관련) 등 필수 및 선택 기능 정의.

## 소스
*   3GPP TS 38.211 V16.9.0 (2022-03)
*   3GPP TS 38.212 V16.8.0 (2022-03)
*   3GPP TS 38.822 V16.0.0 (2020-07)

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/CSI_Reporting_Procedures.md
- concepts/DAPS_Handover_Procedures.md
- concepts/DMRS_Bundling_Procedures.md
- concepts/HARQ_ACK_Codebook_Determination.md
- concepts/Half_Duplex_UE_Operation.md
- concepts/IAB_Timing_Control.md
- concepts/PDSCH_DCI_Field_Processing.md
- concepts/PUCCH_Cell_Switching.md
- concepts/PUCCH_Format_Processing.md
- concepts/PUCCH_Power_Control.md
- concepts/PUCCH_Repetition.md
- concepts/PUCCH_Resource_Determination.md
- concepts/PUCCH_Resource_Sets.md
- concepts/PUCCH_Sequence_Hopping.md
- concepts/PUCCH_Spatial_Setting.md
- concepts/PUSCH_Frequency_Hopping.md
- concepts/PUSCH_HARQ_Feedback.md
- concepts/PUSCH_Modulation.md
- concepts/PUSCH_Resource_Mapping.md
- concepts/Power_Headroom_Report.md
- concepts/RACH_Procedure_L1.md
- concepts/RedCap_UE_Procedures.md
- concepts/SCell_Activation_Deactivation_Timing.md
- concepts/SPS_HARQ_Deferral.md
- concepts/SRS_Carrier_Switching.md
- concepts/SRS_Collision_Handling.md
- concepts/SR_Reporting_Procedure.md
- concepts/Sidelink_HARQ_Reporting.md
- concepts/Slot_Format_Configuration.md
- concepts/UCI_Bit_Sequence_Generation.md
- concepts/UCI_Multiplexing_PUCCH.md
- concepts/UCI_PUCCH_Multiplexing.md
- concepts/UCI_Processing_PUCCH.md
- concepts/UCI_Rate_Matching.md
- concepts/UCI_Reporting_Different_Priorities.md
- concepts/UTO_UCI_Reporting.md
- concepts/Uplink_Power_Control.md
- concepts/Uplink_Power_Prioritization.md
- concepts/Uplink_Switching_Procedures.md
- entities/PUCCH.md
- entities/Reference_Signals.md