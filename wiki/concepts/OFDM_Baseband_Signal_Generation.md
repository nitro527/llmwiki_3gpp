# OFDM_Baseband_Signal_Generation

## 정의
[[OFDM_Baseband_Signal_Generation]]은 [[5G_NR]] 시스템에서 물리 채널 및 신호의 복소 심볼을 시간 영역의 기저대역 신호로 변환하는 절차를 의미합니다.

## 요약
- [필수(항상)] CP-OFDM waveform for DL and UL
- [필수(항상)] DFT-S-OFDM waveform for UL
- [필수(항상)] DL modulation scheme
- [필수(항상)] UL modulation scheme
- [선택] 11-9b: F1AP over LTE leg signaling for EN-DC IAB-MT
- [선택] 20-11: Support of UL PDCP Packet Average Delay measurement
- [선택] 26-8: Support of polarization signalling in NR NTN
- [선택] 37-9: Signaling Based Logged MDT Override Protection
- [선택] 37-11: Excess packet delay
- [선택] 40-4-11: Joint configuration of Rel.18 DMRS ports and Rel.18 dynamic switching between DFT-S-OFDM and CP-OFDM for PUSCH
- [선택] 41-2-5: Reporting timestamp with OFDM symbol index associated with RSCP measurement and RSCPD measurement
- [선택] 55-8: SCG Failure Report for CPAC

## 상세 설명
[[OFDM_Baseband_Signal_Generation]]은 크게 일반 채널과 특수 채널(PRACH, RIM-RS)로 구분되어 수행됩니다.

1. 일반 채널 및 신호: [[PRACH]] 및 [[RIM_RS_Generation_Mapping]]을 제외한 모든 채널은 [[Frame_Structure_Numerology]]에 정의된 서브캐리어 간격 및 CP 길이를 기반으로 IFFT를 수행하여 시간 영역 신호를 생성합니다.
2. [[PRACH]]: 랜덤 액세스 프리앰블 전송을 위해 특정 시퀀스 구조와 CP 구성을 따르는 별도의 생성 절차를 가집니다.
3. [[RIM_RS_Generation_Mapping]]: 원격 간섭 관리를 위한 참조 신호 생성 절차를 따릅니다.

## 인과 관계
- [[Frame_Structure_Numerology]] (depends_on) [[OFDM_Baseband_Signal_Generation]]
- [[OFDM_Baseband_Signal_Generation]] (affects) [[Physical_Resource_Grid]]

## 관련 개념
- [[Frame_Structure_Numerology]] (depends_on)
- [[PRACH]] (part_of)
- [[RIM_RS_Generation_Mapping]] (part_of)
- [[Physical_Resource_Grid]] (depends_on)

## 스펙 근거
- TS 38.211 §5.3.1에 따르면, PRACH 및 RIM-RS를 제외한 모든 채널의 OFDM 기저대역 신호 생성은 서브캐리어 매핑 및 IFFT 변환을 통해 수행됩니다.
- TS 38.211 §5.3.2에 따르면, PRACH는 프리앰블 시퀀스 특성에 따른 별도의 시간 영역 신호 생성 규칙을 따릅니다.
- TS 38.211 §5.3.3에 따르면, RIM-RS는 해당 신호의 목적에 맞는 시퀀스 및 매핑 규칙을 적용합니다.

## 소스
- 3GPP TS 38.211 v19.0.0 (Release 19) §5.3