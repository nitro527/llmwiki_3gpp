# Type0_PDCCH_Monitoring

## 정의
Type0-PDCCH CSS set 모니터링은 [[UE]]가 셀 탐색 과정에서 [[MIB]]를 통해 획득한 정보를 바탕으로, 시스템 정보 블록(SIB1)을 수신하기 위한 [[PDCCH]] 제어 채널을 주기적으로 감시하는 절차를 의미한다.

## 요약
[[UE]]는 [[MIB]] 내의 `pdcch-ConfigSIB1` 파라미터를 사용하여 [[CORESET]] 및 [[Search_Space_Configuration]] 정보를 결정한다. 이는 [[SS_PBCH_Block_Generation]]과 연동되어 특정 시간 및 주파수 자원에서 [[PDCCH]]를 모니터링하도록 하며, 공유 스펙 환경 여부와 주파수 대역(FR1, FR2-1, FR2-2, FR2-NTN)에 따라 서로 다른 테이블을 적용하여 자원 위치와 오프셋을 계산한다.

## 상세 설명
[[UE]]는 셀 탐색 중 [[MIB]]에서 `controlResourceSetZero`와 `searchSpaceZero`를 확인하여 [[CORESET]]의 자원 블록(RB) 수와 심볼 길이를 결정한다.

1. **CORESET 및 모니터링 오케이션 결정**:
   - [[TS_38_213]] §13에 따라 FR1, FR2-1, FR2-NTN 및 공유 스펙 환경에서의 [[CORESET]] 설정은 테이블 13-0부터 13-10A를 참조한다.
   - [[PDCCH]] 모니터링 오케이션은 `searchSpaceZero`를 통해 테이블 13-11부터 13-15A를 기반으로 결정된다.

2. **주파수 오프셋 계산**:
   - 공유 스펙 환경이 아닌 경우와 FR2-2에서는 [[CORESET]]의 가장 작은 RB 인덱스와 [[SS_PBCH_Block_Generation]]의 첫 번째 RB와 겹치는 공통 RB의 가장 작은 인덱스 사이의 오프셋을 계산한다.
   - 공유 스펙 환경(FR1)에서는 [[SS_PBCH_Block_Generation]]의 주파수 위치가 동기화 래스터(Synchronization Raster)의 GSCN과 일치하는지 여부에 따라 오프셋 결정 방식이 달라진다.

3. **다중화 패턴 및 슬롯 모니터링**:
   - 멀티플렉싱 패턴 1의 경우, [[UE]]는 일반적으로 두 개의 슬롯에 걸쳐 [[PDCCH]]를 모니터링한다. 이때 슬롯 인덱스는 [[SS_PBCH_Block_Generation]] 인덱스와 [[CORESET]]의 부반송파 간격(SCS)을 고려하여 결정된다.
   - 멀티플렉싱 패턴 2와 3의 경우, [[SS_PBCH_Block_Generation]]의 주기와 동일한 주기로 하나의 슬롯에서 모니터링을 수행한다.

4. **실패 시 동작**:
   - [[UE]]가 특정 [[SS_PBCH_Block_Generation]]에서 [[CORESET]]을 찾지 못할 경우, 테이블 13-16 및 13-17에 정의된 GSCN 오프셋을 사용하여 인접한 다른 [[SS_PBCH_Block_Generation]]을 탐색할 수 있다.

## 인과 관계
- [[MIB]] depends_on [[Synchronization_Procedures]] (셀 탐색을 통한 MIB 획득 전제)
- [[Type0_PDCCH_Monitoring]] depends_on [[CORESET_Configuration]] (CORESET 파라미터 설정 필요)
- [[Type0_PDCCH_Monitoring]] depends_on [[PDCCH_Search_Space_Configuration]] (Search Space 파라미터 설정 필요)
- [[Type0_PDCCH_Monitoring]] affects [[PDCCH_Monitoring_Capability]] (모니터링 오케이션에 따른 자원 점유)

## 관련 개념
- [[MIB]] (part_of)
- [[CORESET]] (part_of)
- [[SS_PBCH_Block_Generation]] (depends_on)
- [[PDCCH]] (implements)
- [[Synchronization_Procedures]] (depends_on)

## 스펙 근거
- TS 38.213 §13: UE procedure for monitoring Type0-PDCCH CSS sets
- TS 38.211 §6.3.1: CORESET 및 자원 매핑 관련 규정
- TS 38.101-1: SS/PBCH 블록 위치 및 동기화 래스터 관련 규정

## 소스
- 3GPP TS 38.213 (v18.0.0)
- 3GPP TS 38.211 (v18.0.0)
- 3GPP TS 38.101-1 (v18.0.0)