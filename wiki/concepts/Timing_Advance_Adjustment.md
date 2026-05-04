# Timing_Advance_Adjustment

## 정의
[[Timing_Advance_Adjustment]]는 [[UE]]가 상향링크 전송 시 기지국([[gNB]])에서의 수신 타이밍을 정렬하기 위해 전송 시점을 앞당기는 제어 절차를 의미합니다.

## 요약
[[Timing_Advance_Adjustment]]는 [[UE]]가 전송하는 상향링크 신호가 [[gNB]]의 수신 윈도우 내에 도달하도록 전송 타이밍을 조정하는 메커니즘입니다. 이는 [[TS 38.822]]에 정의된 다양한 [[UE]] Feature와 연계되어 동작하며, 특히 [[Connection_Establishment_Failure_Reporting]] (20-15) 및 [[Beam_reporting_timing]] (2-25)과 같은 필수 기능들이 이 타이밍 제어와 밀접하게 관련되어 있습니다.

## 상세 설명
[[Timing_Advance_Adjustment]]는 다음과 같은 절차와 요구사항을 포함합니다.

*   **필수 기능**: [[UE]]는 [[Connection_Establishment_Failure_Reporting]] (20-15)을 항상 지원해야 하며, [[Beam_reporting_timing]] (2-25)을 필수(cap)로 지원해야 합니다.
*   **선택 기능**: 
    *   [[Multi_TRP_operation]] 관련: 40-2-2 (Basic feature for multi-DCI based inter-cell Multi-TRP operation with two TA enhancement)
    *   측정 및 보고 관련: 2-28 (A-CSI-RS beam switching timing), 20-4 (Immediate Measurement – WLAN), 20-5 (Logged Measurement – Bluetooth), 20-10 (GNSS/A-GNSS support), 20-11 (UL PDCP Packet Average Delay), 20-14 (RLF Report for inter-RAT MRO EUTRA)
    *   타이밍 및 전송 강화: 10-14 (Non-numerical PDSCH to HARQ-ACK timing), 20-7 (Case 1 OTA timing alignment), 26-1 (Uplink Time and Frequency pre-compensation and timing relationship enhancements)
*   **동작 원리**: [[gNB]]는 [[UE]]로부터 수신된 상향링크 신호의 도달 시간을 측정하여 타이밍 오차를 계산하고, 이를 보정하기 위한 [[Timing_Advance]] 명령을 [[MAC_CE]] 또는 [[DCI]]를 통해 전달합니다. [[UE]]는 이 명령을 수신한 후, 지정된 오프셋만큼 전송 타이밍을 조정하여 상향링크 신호를 전송합니다.

## 인과 관계
- [[Timing_Advance_Adjustment]] depends_on [[RACH_Procedure_L1]] (초기 타이밍 정렬)
- [[Timing_Advance_Adjustment]] affects [[PUSCH_Transmission_Procedures]] (전송 시점 결정)
- [[Timing_Advance_Adjustment]] affects [[PUCCH_Format_Processing]] (전송 시점 결정)
- [[Timing_Advance_Adjustment]] triggers [[Uplink_Power_Control]] (타이밍 변경에 따른 전력 제어 보정)

## 관련 개념
- [[RACH_Procedure_L1]] (depends_on)
- [[PUSCH_Transmission_Procedures]] (affects)
- [[PUCCH_Format_Processing]] (affects)
- [[Uplink_Power_Control]] (triggers)

## 스펙 근거
- [[TS 38.213]] §4.2에 따르면, [[UE]]는 상향링크 전송 타이밍 조정을 위해 [[gNB]]로부터 수신된 타이밍 어드밴스 명령을 적용해야 합니다.
- [[TS 38.822]]에 명시된 [[UE]] Feature Priority에 따라 20-15(필수), 2-25(필수-cap) 및 기타 선택적 기능들이 [[Timing_Advance_Adjustment]]의 성능 및 동작 범위에 영향을 미칩니다.

## 소스
- 3GPP TS 38.213 v18.0.0, "NR; Physical layer procedures for control"
- 3GPP TS 38.822 v18.0.0, "NR; User Equipment (UE) radio access capabilities"