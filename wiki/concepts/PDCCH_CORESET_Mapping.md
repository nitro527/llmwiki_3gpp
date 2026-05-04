# PDCCH_CORESET_Mapping

## 정의
[[PDCCH]] [[CORESET]] 매핑은 [[Physical_Resource_Grid]] 내에서 [[Control_channel_element]] (CCE)가 시간 및 주파수 자원에 할당되는 방식과, 이를 제어하기 위한 설정 파라미터 및 [[Reference_Signals]]와의 관계를 정의하는 절차입니다.

## 요약
[[CORESET]]은 [[PDCCH]]가 전송될 수 있는 시간-주파수 자원 영역을 정의하며, [[CCE]] 단위로 구성됩니다. 다중 [[TRP]] 환경에서의 [[Multi-DCI]] 기반 동작을 위해 [[coresetPoolIndex]]가 사용되며, 이는 [[DM-RS]] 스크램블링 초기화 및 [[QCL]] 가정과 밀접하게 연관됩니다.

## 상세 설명
[[CORESET]]은 1개에서 3개의 [[OFDM_Baseband_Signal_Generation]] 심볼로 구성되며, 주파수 도메인에서는 6개의 [[Resource_Block]] 단위로 할당됩니다.

1. **CCE 구성**: [[CORESET]] 내의 자원은 [[CCE]]로 분할되며, 각 [[CCE]]는 6개의 [[Resource_Element_Group]] (REG)로 구성됩니다. 하나의 [[REG]]는 하나의 [[OFDM]] 심볼 내의 하나의 [[Resource_Block]]에 해당합니다.
2. **coresetPoolIndex**: [[Multi-DCI]] 기반 [[Multi-TRP]] 동작을 지원하기 위해 각 [[CORESET]]에는 [[coresetPoolIndex]]가 설정될 수 있습니다. 값이 설정되지 않은 경우 기본값 0으로 간주합니다.
3. **DM-RS 스크램블링**: [[PDCCH]] [[DM-RS]]의 스크램블링 시퀀스 초기화는 [[CORESET]] 설정에 포함된 파라미터와 [[coresetPoolIndex]]를 참조하여 결정됩니다.
4. **QCL 가정**: [[PDCCH]] 수신을 위해 [[UE]]는 [[CORESET]]에 설정된 [[Transmission_Configuration_Indicator]] (TCI) 상태를 통해 [[QCL]] 정보를 획득합니다. [[Multi-DCI]] 환경에서는 서로 다른 [[TRP]]로부터의 [[PDCCH]]를 구분하기 위해 서로 다른 [[QCL]] 가정이 적용될 수 있습니다.

## 인과 관계
- [[CORESET]] 설정 (triggers) [[CCE]] 매핑
- [[coresetPoolIndex]] (affects) [[DM-RS]] 스크램블링 초기화
- [[TCI_State]] (depends_on) [[QCL]] 가정
- [[Multi-DCI]] 기반 [[Multi-TRP]] (triggers) [[coresetPoolIndex]] 설정

## 관련 개념
- [[PDCCH]] (part_of)
- [[CORESET]] (part_of)
- [[CCE]] (part_of)
- [[DM-RS]] (depends_on)
- [[QCL]] (depends_on)
- [[Multi-TRP]] (affects)

## 스펙 근거
- TS 38.211 §7.3.2.1: [[CCE]]의 정의 및 [[REG]] 구성에 관한 규정
- TS 38.211 §7.3.2.2: [[CORESET]]의 시간-주파수 자원 할당 및 설정 파라미터
- TS 38.213 §10.1: [[UE]]의 [[PDCCH]] 모니터링 및 [[CORESET]] 기반 자원 할당 절차
- TS 38.213 §10.1.1: 셀 간 스케줄링 및 [[CORESET]] 매핑 관련 절차

## 소스
- 3GPP TS 38.211 V19.0.0 (2024-03)
- 3GPP TS 38.213 V18.0.0 (2024-03)