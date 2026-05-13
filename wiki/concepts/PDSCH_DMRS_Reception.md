# PDSCH_DMRS_Reception

## 정의
[[PDSCH]] 수신을 위해 필요한 복조용 참조 신호인 [[DMRS]]를 단말이 수신하고, 이를 기반으로 채널 추정 및 데이터 복조를 수행하는 절차를 의미한다.

## 요약
[[PDSCH_DMRS_Reception]]은 [[PDCCH]]를 통해 전달된 [[DCI]] 포맷에 따라 [[DMRS]] 설정 파라미터를 적용하여 수행된다. 단말은 상위 계층 설정 및 [[DCI]] 필드를 통해 [[DMRS]] 타입, 포트 할당, CDM 그룹 정보, 그리고 [[QCL]] 가정을 획득하며, 이를 바탕으로 채널 추정 및 데이터 복조를 위한 참조 신호 처리를 수행한다.

## 상세 설명
[[PDSCH_DMRS_Reception]] 절차는 [[PDCCH]]의 [[DCI]] 포맷에 따라 다음과 같이 구분된다.

1. 기본 수신 절차
- [[DCI]] 포맷 1_0, 4_0, 4_1로 스케줄링된 경우 또는 상위 계층 설정이 완료되기 전에는, 단말은 [[DMRS]]가 포함된 심볼을 제외하고 [[PDSCH]]가 존재하지 않는다고 가정한다. 단, 2심볼 할당의 [[PDSCH]] 매핑 타입 B는 예외로 한다. 이 경우 [[DMRS]] 포트 1000을 사용하는 타입 1 [[DMRS]]가 전송된다고 가정한다.
- [[DCI]] 포맷 1_1, 1_3 또는 4_2(멀티캐스트)의 경우, 상위 계층 파라미터인 [[DMRS]] 타입(dmrs-Type, dmrs-TypeEnh) 및 최대 전면 로드 [[DMRS]] 심볼 수(maxLength)를 사용하여 수신한다.
- maxLength가 'len1'인 경우, 단일 심볼 [[DMRS]]가 스케줄링되며, 추가 [[DMRS]] 위치(dmrs-AdditionalPosition)는 'pos0'~'pos3'까지 설정 가능하다.
- maxLength가 'len2'인 경우, 단일 및 이중 심볼 [[DMRS]]가 모두 가능하며, 추가 [[DMRS]] 위치는 'pos0' 또는 'pos1'로 설정된다.

2. 안테나 포트 및 CDM 그룹 관리
- [[DMRS]] 설정 타입 1, 2 및 향상된(enhanced) 타입 1, 2에 따라 [[DCI]]의 안테나 포트 필드를 해석한다.
- 단말은 할당된 안테나 포트가 속한 CDM 그룹 내의 나머지 직교 안테나 포트들이 다른 단말을 위한 [[PDSCH]] 전송에 사용되지 않음을 가정할 수 있다.
- [[DCI]] 포맷 1_1 수신 시, TS 38.212의 테이블에 정의된 CDM 그룹 인덱스를 통해 해당 그룹이 데이터 전송에 사용되지 않는 [[DMRS]] 자원임을 식별한다.

3. [[QCL]] 가정 및 특수 케이스
- [[DMRS]]와 동일한 PCI를 가진 [[SS_PBCH_Block_Generation]]이 동일 심볼에서 수신될 경우, 단말은 'QCL-TypeD' 관계를 가정할 수 있다.
- 두 개의 TCI 상태가 지시된 경우, 각 TCI 상태는 할당된 안테나 포트의 CDM 그룹과 매핑된다.
- [[PDCCH_Config]] 내에 서로 다른 CORESETPoolIndex가 설정된 경우, 단말은 다중 [[PDCCH]]에 의한 중첩 [[PDSCH]] 수신을 수행할 수 있으며, 이때 [[DMRS]] 설정의 일관성을 유지해야 한다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_DMRS_Reception]] (데이터 복조를 위한 채널 추정 전제)
- [[DCI_Field_Mapping]] affects [[PDSCH_DMRS_Reception]] (안테나 포트 및 TCI 상태 지시)
- [[DMRS_Resource_Mapping]] implements [[PDSCH_DMRS_Reception]] (물리적 자원 위치 결정)
- [[PDSCH_TCI_State_Management]] affects [[PDSCH_DMRS_Reception]] (QCL 가정 및 빔 설정)

## 관련 개념
- [[DMRS]] (part_of)
- [[PDSCH]] (part_of)
- [[DCI]] (affects)
- [[QCL]] (depends_on)
- [[SS_PBCH_Block_Generation]] (affects)

## 스펙 근거
- TS 38.214 §5.1.6.2: [[DMRS]] 수신 절차 및 파라미터 적용 규칙
- TS 38.211 §7.4.1.1: [[DMRS]] 시퀀스 생성 및 자원 매핑
- TS 38.212 §7.3.1.2: [[DCI]] 내 안테나 포트 필드 해석 및 테이블 정의

## 소스
- 3GPP TS 38.214 V17.9.0 (2024-03)
- 3GPP TS 38.211 V17.9.0 (2024-03)
- 3GPP TS 38.212 V17.9.0 (2024-03)