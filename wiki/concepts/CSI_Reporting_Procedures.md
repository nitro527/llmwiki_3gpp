# CSI_Reporting_Procedures

## 정의
[[CSI_Reporting_Procedures]]는 [[UE]]가 [[gNB]]로부터 수신한 [[CSI_RS]] 및 [[CSI_IM]]을 측정하여, 채널 상태 정보를 계산하고 이를 [[PUCCH]] 또는 [[PUSCH]]를 통해 네트워크에 보고하는 일련의 절차를 의미합니다.

## 요약
[[CSI]] 프레임워크는 보고 설정([[Reporting_settings]]), 자원 설정([[Resource_settings]]), 보고 구성([[Reporting_configurations]])으로 구성됩니다. [[UE]]는 [[CQI]], [[PMI]], [[RI]] 등을 계산하며, 트리거링 방식에 따라 주기적, 반주기적(Semi-persistent), 비주기적(Aperiodic) 보고를 수행합니다. [[TS_38_214]] §5.2에 명시된 절차에 따라 [[UE]]는 특정 처리 시간 내에 계산을 완료해야 합니다.

## 상세 설명
- **CSI 프레임워크**: [[TS_38_214]] §5.2.1에 따라 [[CSI]] 보고는 보고 설정과 자원 설정의 조합으로 정의됩니다. 보고 설정은 보고할 양(Quantity)과 주기 등을 결정하며, 자원 설정은 측정에 사용될 [[CSI_RS]] 및 [[CSI_IM]] 자원을 정의합니다.
- **보고 구성**: [[L1_RSRP]], [[L1_SINR]], [[TDCP]] 등 다양한 보고 양이 지원됩니다. [[PMI]] 보고를 위해 [[Type_I_Codebook]] 및 [[Type_II_Codebook]] 등 다양한 코드북이 정의되어 있습니다.
- **트리거링**: [[PDCCH]]를 통한 [[DCI]]로 비주기적 [[CSI]] 보고가 트리거되며, [[MAC_CE]]를 통해 반주기적 [[CSI]] 보고가 활성화됩니다.
- **계산 절차**: [[UE]]는 [[CSI_reference_resource]] 정의에 따라 [[CQI]], [[PMI]], [[RI]]를 계산합니다. 이 과정에서 [[NCJT]], [[CJT]], [[Predicted_CSI]] 등에 대한 가정이 적용됩니다.
- **보고 채널**: [[CSI]]는 [[PUCCH]] 또는 [[PUSCH]]를 통해 전송되며, 다수의 보고가 충돌할 경우 [[Priority_rules_for_CSI_reports]]에 따라 처리됩니다.
- **필수 기능**: 
    - [[Active_spatial_relations]] (cap)
    - [[HARQ_ACK_multiplexing_on_PUSCH_with_different_PUCCH_PUSCH_starting_OFDM_symbols]] (cap)
    - [[Basic_PDCP_procedures]] (항상)
    - [[Sidelink_CSI_report]] (cap)
- **선택 기능**: 
    - [[Support_of_cri_RI_CQI_report_without_non_PMI_PortIndication]]
    - [[CSI_reporting_cross_PUCCH_group]]
    - [[Support_of_Rel_16_based_doppler_CSI]]
    - [[Support_of_Rel_17_based_doppler_CSI]]
    - [[HARQ_ACK_multiplexing_on_PUSCH_with_different_PUCCH_PUSCH_starting_OFDM_symbols_for_unlicensed_spectrum]]
    - [[Cross_Slot_Scheduling]]
    - [[CMR_sharing]]
    - [[UE_specific_K_offset]]

## 인과 관계
- [[CSI_RS_Generation_Mapping]] (depends_on): [[CSI]] 보고를 위한 측정 자원을 제공합니다.
- [[CSI_Computation_Timing]] (affects): [[UE]]가 [[CSI]]를 보고하기 위해 필요한 최소 시간을 결정합니다.
- [[UCI_Multiplexing_PUSCH]] (triggers): [[CSI]]가 [[PUSCH]]로 전송될 때 다중화 절차를 유발합니다.
- [[UCI_Processing_PUCCH]] (triggers): [[CSI]]가 [[PUCCH]]로 전송될 때 처리 절차를 유발합니다.

## 관련 개념
- [[CSI_RS]] (part_of)
- [[CSI_IM]] (part_of)
- [[CQI_Calculation_Procedures]] (depends_on)
- [[PMI_Codebook_Procedures]] (depends_on)
- [[CSI_Processing_Criteria]] (affects)

## 스펙 근거
- [[TS_38_214]] §5.2: UE procedure for reporting channel state information (CSI)
- [[TS_38_214]] §5.2.1: Channel state information framework
- [[TS_38_214]] §5.2.2: Channel state information
- [[TS_38_214]] §5.2.3: CSI reporting using PUSCH
- [[TS_38_214]] §5.2.4: CSI reporting using PUCCH
- [[TS_38_214]] §5.2.5: Priority rules for CSI reports
- [[TS_38_214]] §5.4: UE CSI computation time

## 소스
- 3GPP TS 38.214 v19.0.0 (Release 19)