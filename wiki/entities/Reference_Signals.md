# Reference Signals

## 정의
[[Reference_Signals]]는 [[5G_NR]] 시스템에서 채널 추정, 복조, 동기화, 위치 측정 및 무선 환경 모니터링을 위해 송신단과 수신단이 사전에 약속한 물리 계층 신호입니다.

## 요약
[[Reference_Signals]]는 상향링크와 하향링크로 구분되며, 데이터 채널의 복조를 위한 [[DMRS]], 위상 잡음 보상을 위한 [[PT_RS]], 채널 상태 정보 측정을 위한 [[CSI_RS]], 상향링크 품질 측정을 위한 [[SRS]], 위치 기반 서비스를 위한 [[PRS]], 그리고 간섭 관리를 위한 [[RIM_RS]] 등으로 구성됩니다.

## 상세 설명
[[5G_NR]]에서 정의된 주요 [[Reference_Signals]]는 다음과 같습니다.

* [[DMRS]] (Demodulation Reference Signal): [[PUSCH]], [[PUCCH]], [[PDSCH]], [[PDCCH]], [[PBCH]]의 복조를 위해 사용됩니다. TS 38.211 §6.4.1 및 §7.4.1에 따라 각 채널의 특성에 맞게 시퀀스 생성 및 자원 매핑이 수행됩니다.
* [[PT_RS]] (Phase-tracking Reference Signal): 고주파 대역에서 발생하는 위상 잡음(Phase Noise)을 추적하고 보상하기 위해 [[PUSCH]] 및 [[PDSCH]]와 함께 전송됩니다.
* [[SRS]] (Sounding Reference Signal): 기지국이 상향링크 채널 상태를 파악하여 스케줄링 및 빔포밍을 최적화할 수 있도록 UE가 전송합니다.
* [[CSI_RS]] (CSI Reference Signal): UE가 하향링크 채널 상태 정보(CSI)를 측정하여 기지국에 보고할 수 있도록 지원합니다.
* [[PRS]] (Positioning Reference Signal): UE의 위치 추정을 위해 하향링크에서 전송되는 신호입니다.
* [[RIM_RS]] (RIM Reference Signal): 원격 간섭 관리(Remote Interference Management)를 위해 사용되는 신호입니다.

## 인과 관계
* [[Reference_Signals]]는 [[Physical_Resource_Grid]] 상의 특정 자원 요소에 매핑되어 전송됩니다.
* [[DMRS]]는 [[PUSCH]] 및 [[PDSCH]]의 복조 성능에 직접적인 영향을 미칩니다.
* [[CSI_RS]]는 [[CSI_Reporting_Procedures]]의 기초 데이터를 제공합니다.
* [[SRS]]는 [[Uplink_Power_Control]] 및 빔 관리 절차를 트리거합니다.

## 관련 개념
- [[DMRS]] (part_of)
- [[PT_RS]] (part_of)
- [[SRS]] (part_of)
- [[CSI_RS]] (part_of)
- [[PRS]] (part_of)
- [[RIM_RS]] (part_of)
- [[Physical_Resource_Grid]] (depends_on)
- [[Channel_Coding_General]] (affects)

## 스펙 근거
- TS 38.211 §6.4: 상향링크 물리 신호 (DMRS, PT-RS, SRS) 정의
- TS 38.211 §7.4: 하향링크 물리 신호 (DMRS, PT-RS, CSI-RS, RIM-RS, PRS, 동기화 신호) 정의
- TS 38.822: 
  - [필수(cap)] 2-60: Active spatial relations
  - [필수(cap)] 2-33: CSI-RS and CSI-IM reception for CSI feedback
  - [선택] 17-4: Simultaneous reception of DL signals/channels and SRS-RSRP measurement resource
  - [선택] 26-9: UE-specific K_offset
  - [선택] 17-3: Simultaneous reception of DL signals/channels and CLI-RSSI measurement resource
  - [선택] 42-8: simultaneousCSI-SubReportsPerCC-r18
  - [선택] 1-8: RLM based on a mix of SS block and CSI-RS signals within active BWP
  - [선택] 2-15a: Association between CSI-RS and SRS
  - [선택] 2-15b: CSI-RS processing framework for SRS
  - [선택] 10-26e: RLM based on a mix of SS block and CSI-RS signals within active BWP for operation with shared spectrum channel access
  - [선택] 10-31: Support of P/SP-CSI-RS reception with CSI-RS-ValidationWith-DCI-r16 configured
  - [선택] 13-9: OLPC for SRS for positioning based on PRS from the serving cell

## 소스
- 3GPP TS 38.211 V17.9.0 (Release 17)
- 3GPP TS 38.822 V18.0.0 (Release 18)