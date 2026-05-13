# Beam_Correspondence

## 정의
Beam_Correspondence는 UE가 하향링크(DL) 측정(예: SSB 또는 CSI-RS)을 통해 획득한 공간 도메인 필터 정보를 상향링크(UL) 전송(예: SRS 또는 PUCCH/PUSCH)에 동일하게 적용할 수 있는 능력을 의미한다.

## 요약
Beam_Correspondence는 기지국이 UE의 상향링크 빔을 직접 제어하지 않고도, UE가 스스로 최적의 상향링크 빔을 결정하도록 유도하는 메커니즘이다. 이를 지원하는 UE는 DL 수신 빔과 UL 송신 빔 간의 상호 관계를 활용하여 빔 관리 오버헤드를 줄이고 효율적인 빔 포밍을 수행한다.

## 상세 설명
Beam_Correspondence는 UE의 구현 능력에 따라 지원 여부가 결정되며, 기지국은 UE의 보고를 통해 해당 능력을 인지한다.

1. 빔 측정 및 선택: UE는 [[SS_PBCH_Block_Generation]] 또는 [[CSI_RS_Generation]]을 통해 수신된 신호를 측정하여 최적의 DL 빔을 식별한다.
2. 공간 도메인 필터 결정: Beam_Correspondence가 지원되는 경우, UE는 식별된 DL 빔의 공간 도메인 필터(Spatial Domain Filter)를 상향링크 전송을 위한 공간 관계(Spatial Relation) 설정에 재사용한다.
3. 상향링크 적용: UE는 [[SRS_Spatial_Relation]]을 설정할 때, DL 참조 신호(SSB 또는 CSI-RS)를 참조하여 상향링크 송신 빔을 결정한다.
4. 빔 보고: UE는 주기적, 비주기적 또는 반영구적 빔 보고를 통해 기지국에 최적의 빔 정보를 전달하며, 이는 [[CSI_Reporting_Procedure]]의 일부로 수행된다.
5. 빔 스위칭: 기지국은 TCI 상태 변경이나 빔 스위칭 명령을 통해 UE의 빔을 동적으로 제어할 수 있으며, UE는 이를 수신하여 빔을 업데이트한다.

## 인과 관계
- [[SRS_Spatial_Relation]] depends_on [[Beam_Correspondence]] (상향링크 빔 결정 시 빔 대응 능력 활용)
- [[CSI_Reporting_Procedure]] depends_on [[Beam_Correspondence]] (빔 보고 시 최적 빔 정보의 정확도 보장)
- [[PDSCH_TCI_State_Management]] depends_on [[Beam_Correspondence]] (DL 빔 정보와 UL 빔 정보 간의 정렬)

## 관련 개념
- [[SS_PBCH_Block_Generation]] (affects)
- [[CSI_RS_Generation]] (affects)
- [[SRS_Spatial_Relation]] (implements)
- [[CSI_Reporting_Procedure]] (implements)
- [[PDSCH_TCI_State_Management]] (affects)

## 스펙 근거
- TS 38.214 §5.1.6.1에 따르면, CSI-RS 자원은 L1-RSRP 및 L1-SINR 계산을 위해 사용되며, 이는 빔 관리 및 빔 대응을 위한 기초 데이터를 제공한다.
- TS 38.214 §5.1.6.1에서 언급된 TCI 상태 및 QCL(Quasi Co-Location) 가정은 UE가 수신 빔을 결정하는 핵심 근거가 된다.
- TS 38.822에 정의된 빔 관련 기능들은 UE의 빔 대응 능력과 결합하여 상향링크 전송 효율을 최적화한다.

## 소스
- 3GPP TS 38.214 V16.9.0 (2022-03) "NR; Physical layer procedures for data"
- 3GPP TS 38.822 "Study on beam management for NR"