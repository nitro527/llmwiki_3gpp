# SRS_Mapping

## 정의
[[SRS]] 자원 매핑은 상위 계층 파라미터에 의해 구성된 [[SRS]] 자원 세트 내의 자원들을 시간 및 주파수 영역의 물리적 자원 요소(RE)에 할당하고, 시퀀스 생성 및 주파수 호핑을 수행하는 절차를 의미한다.

## 요약
[[SRS]]는 주기적(periodic), 반영구적(semi-persistent), 비주기적(aperiodic) 타입으로 구성되며, TS 38.211 §6.4.1.4.3에 따라 시퀀스 생성, 진폭 스케일링, 그리고 슬롯 내 OFDM 심볼 및 안테나 포트별 RE 매핑이 수행된다. 비주기적 [[SRS]]는 [[DCI]]를 통해 트리거되며, 슬롯 오프셋 및 가용 슬롯 판단 로직을 따른다.

## 상세 설명
[[SRS]] 자원 매핑은 다음과 같은 핵심 파라미터와 절차를 포함한다.

1. 시퀀스 매핑 및 진폭 스케일링:
   [[SRS]] 시퀀스는 각 OFDM 심볼 및 안테나 포트별로 진폭 스케일링 계수와 곱해진 후, TS 38.211 §6.4.1.4.3의 수식에 따라 슬롯 내 RE에 매핑된다. 시퀀스 길이는 상위 계층 파라미터에 의해 결정된 대역폭 설정에 따라 결정된다.

2. 주파수 도메인 위치:
   시작 위치는 상위 계층 파라미터 `StartRBIndex`, `freqDomainShift`, `transmissionComb` 등에 의해 결정된다. 주파수 호핑이 활성화된 경우, 호핑 패턴은 `freqHopping` 파라미터와 `b-hop` 값에 따라 결정되며, 호핑이 비활성화된 경우 주파수 위치 인덱스는 고정된다.

3. 시간 도메인 동작:
   - 주기적/반영구적 [[SRS]]: 상위 계층 파라미터 `periodicityAndOffset-p` 또는 `periodicityAndOffset-sp`에 의해 슬롯 레벨 주기와 오프셋이 결정된다.
   - 비주기적 [[SRS]]: [[DCI]] 포맷 0_1, 0_2, 0_3 등을 통해 트리거된다. 트리거링 시점과 전송 시점 사이의 최소 시간 간격은 [[PUSCH]] 준비 시간 및 스위칭 시간(`Tswitch`)을 고려하여 결정된다. `availableSlotOffsetList`가 설정된 경우, UE는 설정된 슬롯 오프셋 리스트 중 하나를 선택하여 전송한다.

4. 공간 관계(Spatial Relation):
   [[SRS]] 전송을 위한 공간 필터는 `spatialRelationInfo` 또는 `spatialRelationInfoPos`를 통해 참조 신호(SS/PBCH block, CSI-RS, DL PRS 등)와 연동된다. MAC CE를 통한 업데이트가 가능하며, 특정 조건에서는 기본 빔(Default Beam) 설정이 적용된다.

5. 충돌 처리:
   [[SRS]]와 [[PUCCH]] 또는 [[PUSCH]]가 동일 심볼에서 충돌할 경우, 우선순위 규칙에 따라 [[SRS]] 심볼이 드롭되거나 전송이 제한된다. 특히 [[SRS]] 자원 세트 내에서 서로 다른 시간 도메인 동작을 혼용하는 것은 허용되지 않는다.

## 인과 관계
- [[SRS]] depends_on [[Sequence_Generation]] (시퀀스 생성 기반 매핑)
- [[SRS]] affects [[SRS_Power_Control]] (전송 전력 결정)
- [[SRS]] depends_on [[DCI_Field_Mapping]] (비주기적 트리거링)
- [[SRS]] depends_on [[Slot_Format_Configuration]] (가용 슬롯 판단)
- [[SRS]] affects [[PUSCH_Transmission_Procedure]] (충돌 시 자원 드롭)

## 관련 개념
- [[SRS]] (implements)
- [[PUSCH]] (affects)
- [[PUCCH]] (affects)
- [[DCI]] (triggers)
- [[Slot]] (part_of)

## 스펙 근거
- TS 38.211 §6.4.1.4.3: [[SRS]] 자원 매핑, 시퀀스 정의, 주파수 호핑 및 RE 매핑 절차
- TS 38.214 §6.2.1: [[SRS]] 자원 구성, 트리거링, 공간 관계 및 충돌 처리 절차

## 소스
- 3GPP TS 38.211 V16.9.0 (Release 16)
- 3GPP TS 38.214 V16.9.0 (Release 16)