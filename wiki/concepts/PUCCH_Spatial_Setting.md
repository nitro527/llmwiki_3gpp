# PUCCH_Spatial_Setting

## 정의
PUCCH_Spatial_Setting은 [[PUCCH]] 전송 시 UE가 사용할 공간 도메인 필터(Spatial Domain Filter)를 결정하는 절차를 의미하며, 이는 빔포밍 및 공간적 송신 방향을 제어하기 위한 설정값들의 집합입니다.

## 요약
UE는 상위 계층 시그널링인 PUCCH-SpatialRelationInfo 또는 TCI-State를 통해 PUCCH 전송을 위한 공간적 설정을 제공받습니다. 이를 통해 UE는 특정 참조 신호(SSB, CSI-RS, SRS)와 동일한 공간 도메인 필터를 적용하거나, 지시된 TCI 상태에 따른 빔을 사용하여 PUCCH를 전송합니다.

## 상세 설명
PUCCH 전송을 위한 공간 설정은 다음과 같은 메커니즘을 통해 결정됩니다.

1. 공간 설정 제공 방식:
   - TCI-State 또는 TCI-UL-State가 제공되는 경우, TS 38.214에 정의된 절차에 따라 공간 설정이 결정됩니다.
   - PUCCH-SpatialRelationInfo가 단일 값으로 설정된 경우 해당 설정이 적용됩니다.
   - 다수의 PUCCH-SpatialRelationInfo가 제공되는 경우, TS 38.321의 MAC CE 기반 활성화 절차를 따릅니다. 이 경우 UE는 PDSCH 수신에 대한 HARQ-ACK 정보를 포함하는 PUCCH 전송 슬롯 이후의 첫 번째 슬롯부터 새로운 공간 설정을 적용합니다.

2. 참조 신호 기반 공간 도메인 필터 결정:
   - ssb-Index가 제공되는 경우: 해당 인덱스의 SS/PBCH block 수신 시 사용한 공간 도메인 필터를 동일하게 적용합니다.
   - csi-RS-Index 또는 qcl-Type이 'typeD'로 설정된 csi-rs가 제공되는 경우: 해당 CSI-RS 수신 시 사용한 공간 도메인 필터를 동일하게 적용합니다.
   - srs가 제공되는 경우: 해당 SRS 자원 전송 시 사용한 공간 도메인 필터를 동일하게 적용합니다.

3. TCI 상태 지시:
   - applyIndicatedTCI-State 파라미터가 제공될 경우, 'first', 'second', 또는 'both' 설정에 따라 각각 대응되는 TCI-State 또는 TCI-UL-State의 공간 도메인 필터를 적용합니다.
   - coresetPoolIndex가 설정된 경우, 각 CORESET에 특화된 TCI 상태가 적용됩니다.

4. 기본 공간 설정(Default Spatial Relation):
   - pathlossReferenceRSs가 제공되지 않고, enableDefaultBeamPL-ForPUCCH가 활성화된 경우, UE는 활성 DL BWP 내 가장 낮은 ID를 가진 CORESET의 PDCCH 수신 시 사용한 공간 설정을 PUCCH 전송에 동일하게 적용합니다.

5. 빔 대응(Beam Correspondence):
   - beamCorrespondenceWithoutUL-BeamSweeping 능력을 지원하는 UE는 PUCCH 전송 전 채널 접속 절차 수행 시, 설정된 PUCCH-SpatialRelationInfo 내의 referenceSignal과 연관된 공간 도메인 필터를 사용할 수 있습니다.

## 인과 관계
- [[PUCCH]] depends_on [[PUCCH_Spatial_Setting]] (전송을 위한 빔 및 공간 필터 결정)
- [[PUCCH_Spatial_Setting]] depends_on [[CSI_RS]] (공간 도메인 필터 참조 신호로 사용)
- [[PUCCH_Spatial_Setting]] depends_on [[SRS]] (공간 도메인 필터 참조 신호로 사용)
- [[PUCCH_Spatial_Setting]] depends_on [[SS_PBCH_Block_Generation]] (공간 도메인 필터 참조 신호로 사용)
- [[PUCCH_Spatial_Setting]] depends_on [[PDCCH]] (기본 공간 설정 참조 대상)

## 관련 개념
- [[PUCCH]] (part_of)
- [[TCI_State]] (affects)
- [[Spatial_Relation_Info]] (affects)
- [[Pathloss_Estimation]] (depends_on)
- [[Beam_Correspondence]] (implements)

## 스펙 근거
- TS 38.213 §9.2.2: PUCCH 전송을 위한 공간 설정 및 참조 신호 연동 절차 정의
- TS 38.213 §9.2.2: 기본 공간 설정(Default spatial setting) 조건 및 적용 규칙
- TS 38.213 §9.2.2: 빔 대응 지원 UE의 공간 도메인 필터 결정 절차

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §9.2.2