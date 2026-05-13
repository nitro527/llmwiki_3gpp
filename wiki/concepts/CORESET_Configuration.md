# CORESET_Configuration

## 정의
CORESET(Control Resource Set)은 [[PDCCH]]를 수신하기 위해 [[UE]]가 모니터링하는 시간-주파수 자원 영역을 의미하며, 특정 [[BWP]] 내에서 제어 채널의 전송을 위한 자원 블록 집합과 시간 지속 시간을 정의하는 설정 단위이다.

## 요약
CORESET은 [[PDCCH]] 수신을 위한 물리적 자원 할당을 정의하며, [[DMRS]] 스크램블링 초기화, 프리코더 입도(precoder granularity), 시간 도메인 지속 시간, 주파수 도메인 자원 할당, [[TCI]] 상태 등을 포함한다. 다중 [[TRP]] 환경을 지원하기 위해 `coresetPoolIndex`를 통해 CORESET을 그룹화할 수 있다.

## 상세 설명
각 [[DL BWP]] 내에서 [[UE]]는 상위 계층 시그널링을 통해 하나 이상의 CORESET을 설정받는다. CORESET 설정의 주요 파라미터는 다음과 같다.

- **CORESET Index**: `controlResourceSetId`를 통해 식별되며, 0번 인덱스는 초기 접속 시 사용되는 CORESET을 의미한다.
- **coresetPoolIndex**: 다중 [[TRP]] 동작을 위해 사용되며, 값이 제공되지 않거나 모든 CORESET에 동일한 값이 설정된 경우 단일 그룹으로 간주한다. 값이 0과 1로 구분되어 설정되면, 서로 다른 [[TRP]]로부터의 [[PDCCH]] 수신을 독립적으로 관리할 수 있다.
- **Frequency Domain Resources**: `frequencyDomainResources` 비트맵을 통해 6개의 연속적인 [[PRB]] 그룹 단위로 자원을 할당한다.
- **Duration**: `duration` 파라미터는 CORESET이 점유하는 연속적인 OFDM 심볼의 개수(1, 2, 또는 3)를 정의한다.
- **DMRS Scrambling**: `pdcch-DMRS-ScramblingID`를 통해 [[DMRS]] 스크램블링 시퀀스 초기화 값을 설정한다.
- **Precoder Granularity**: `precoderGranularity`는 동일한 [[DMRS]] 프리코더를 가정할 수 있는 REG(Resource Element Group)의 범위를 지정한다.
- **TCI State**: [[PDCCH]] 수신을 위한 [[DMRS]] 안테나 포트의 [[QCL]] 정보를 제공한다. `tci-PresentInDCI` 또는 `tci-PresentDCI-1-2`를 통해 [[DCI]] 내 [[TCI]] 필드 포함 여부를 결정한다.

## 인과 관계
- [[PDCCH_Search_Space_Configuration]] depends_on [[CORESET_Configuration]] (검색 공간은 특정 CORESET과 연동되어야 함)
- [[PDCCH_Scrambling]] depends_on [[CORESET_Configuration]] (DMRS 스크램블링 ID가 CORESET 설정에 포함됨)
- [[PDCCH_Resource_Mapping]] depends_on [[CORESET_Configuration]] (주파수 자원 및 심볼 지속 시간이 CORESET에 의해 결정됨)

## 관련 개념
- [[PDCCH]] (implements)
- [[BWP]] (part_of)
- [[TCI]] (affects)
- [[DMRS]] (affects)
- [[QCL]] (affects)

## 스펙 근거
- TS 38.213 §10.1: CORESET 설정 파라미터 및 [[UE]]의 [[PDCCH]] 모니터링 절차 정의
- TS 38.211 §7.3.2.2: CORESET의 시간-주파수 자원 매핑 및 [[DMRS]] 구조

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"
- 3GPP TS 38.211 V18.0.0 (2024-03) "NR; Physical channels and modulation"