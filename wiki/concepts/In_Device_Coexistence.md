# In_Device_Coexistence

## 정의
[[In_Device_Coexistence]]는 동일한 [[UE]] 내에 탑재된 서로 다른 무선 통신 기술(예: E-UTRA, NR, ISM 대역 등)이 인접한 주파수 대역을 사용할 때 발생하는 간섭을 관리하고 완화하기 위한 기술적 절차를 의미합니다.

## 요약
[[In_Device_Coexistence]]는 단일 [[UE]] 내에서 다중 RAT(Radio Access Technology)가 동시에 동작할 때 발생하는 대역 내 또는 대역 간 간섭 문제를 해결하기 위해 설계되었습니다. 특히 [[TS 38.822]]에 정의된 다양한 [[UE]] 기능들을 통해 네트워크와 협력하여 간섭을 회피하거나 완화합니다. 이와 관련하여 [[Connection_Establishment_Failure_Reporting]]은 필수적으로 지원되어야 하며, 그 외 [[Short_term_time_scale_TDM_for_in_device_coexistence]] 및 [[IDC]]와 같은 선택적 기능들이 상황에 따라 활용됩니다.

## 상세 설명
[[In_Device_Coexistence]] 메커니즘은 [[UE]]가 내부적으로 겪는 간섭 상황을 네트워크에 보고하고, 네트워크가 이를 바탕으로 자원 할당을 조정하거나 [[UE]]가 자체적으로 TDM(Time Division Multiplexing) 기반의 스케줄링을 수행하도록 유도합니다.

- **필수 기능**: [[Connection_Establishment_Failure_Reporting]]은 [[UE]]가 네트워크 연결 과정에서 겪는 실패 정보를 보고하여, 공존 문제로 인한 연결 실패를 네트워크가 인지할 수 있도록 합니다.
- **선택 기능**:
    - [[Short_term_time_scale_TDM_for_in_device_coexistence]]: 짧은 시간 단위로 자원을 분할하여 간섭을 회피합니다.
    - [[IDC]]: 전반적인 공존 관리 기능을 수행합니다.
    - [[RACH_reporting]], [[Immediate_Measurement_WLAN_measurement]], [[Logged_Measurement_Bluetooth_measurement]], [[Measurement_reporting_Speed_information_upon_network_request]], [[Support_of_GNSS_or_A_GNSS_to_provide_location_information_with_SON_and_MDT_related_measurement]], [[Support_of_UL_PDCP_Packet_Average_Delay_measurement]], [[Mobility_history_information_storage]], [[Cross_RAT_RLF_Report]], [[Radio_Link_Failure_Report_for_inter_RAT_MRO_EUTRA]]: 간섭 환경 분석 및 네트워크 최적화를 위한 보조 기능들입니다.

## 인과 관계
- [[In_Device_Coexistence]] (triggers) [[Connection_Establishment_Failure_Reporting]]
- [[In_Device_Coexistence]] (depends_on) [[Short_term_time_scale_TDM_for_in_device_coexistence]]
- [[In_Device_Coexistence]] (affects) [[Uplink_Power_Control]]

## 관련 개념
- [[Connection_Establishment_Failure_Reporting]] (part_of)
- [[Short_term_time_scale_TDM_for_in_device_coexistence]] (part_of)
- [[IDC]] (part_of)
- [[Uplink_Power_Control]] (affects)

## 스펙 근거
- TS 38.213 §16.7에 따르면, [[UE]]는 [[In_Device_Coexistence]] 및 동일 채널 공존을 위한 동작을 수행하며, 이는 네트워크의 설정과 [[UE]]의 보고 기능을 기반으로 합니다.
- TS 38.822에 명시된 [[UE]] 기능 목록에 따라 [[Connection_Establishment_Failure_Reporting]]은 필수적으로 구현되어야 합니다.

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"
- 3GPP TS 38.822 "Study on UE radio transmission and reception capabilities"