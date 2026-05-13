# PDCCH_Search_Space_Configuration

## 정의
PDCCH 검색 공간(Search Space)은 [[UE]]가 [[DCI]]를 검출하기 위해 모니터링해야 하는 [[PDCCH]] 후보(candidate)들의 집합을 정의하는 논리적 단위입니다. 이는 공통 검색 공간(CSS, Common Search Space)과 단말 특정 검색 공간(USS, UE-Specific Search Space)으로 구분됩니다.

## 요약
[[UE]]는 상위 계층 시그널링을 통해 설정된 검색 공간 세트(Search Space Set)를 기반으로 [[CORESET]] 내의 특정 시간-주파수 자원에서 [[PDCCH]]를 모니터링합니다. 각 검색 공간 세트는 [[RNTI]] 유형, [[DCI]] 포맷, 모니터링 주기, 오프셋 및 [[CCE]] 집합 수준(Aggregation Level)에 따라 정의되며, [[TS 38.213]] §10.1에 명시된 절차에 따라 [[PDCCH]] 후보를 결정합니다.

## 상세 설명
검색 공간 세트는 [[CORESET]]과 연관되어 있으며, [[UE]]는 다음의 주요 파라미터를 통해 모니터링 기회(Monitoring Occasion)를 결정합니다.

1. 검색 공간 유형:
   - CSS 세트: 시스템 정보(SI-RNTI), 페이징(P-RNTI), 랜덤 액세스(RA-RNTI, MsgB-RNTI, TC-RNTI), 그룹 공통 제어 정보(SFI-RNTI, INT-RNTI, TPC-RNTI 등) 및 멀티캐스트(G-RNTI, MCCH-RNTI)를 위한 DCI를 수신합니다.
   - USS 세트: 유니캐스트 데이터 스케줄링(C-RNTI, MCS-C-RNTI, CS-RNTI) 및 사이드링크 제어 정보를 위한 DCI를 수신합니다.

2. 모니터링 기회 결정:
   - 모니터링 주기(periodicity)와 오프셋(offset)을 통해 슬롯 단위의 모니터링 기회를 결정합니다.
   - `monitoringSymbolsWithinSlot`을 통해 슬롯 내의 시작 심볼과 [[CORESET]] 지속 시간(duration)을 기반으로 모니터링 심볼을 결정합니다.
   - `monitoringSlotsWithinSlotGroup`이 제공되는 경우, 슬롯 그룹 내의 특정 슬롯에서 모니터링을 수행합니다.

3. CCE 인덱스 계산:
   - 특정 [[CCE]] 집합 수준 $L$에 대한 [[PDCCH]] 후보 $m$의 [[CCE]] 인덱스는 다음 식을 따릅니다:
     $L \cdot \{ (Y_{p, n_{CI}} + \lfloor m \cdot N_{CCE, p} / (L \cdot M_{p, n_{CI}, max}) \rfloor + n_{CI}) \mod \lfloor N_{CCE, p} / L \rfloor \} + i$
     여기서 $Y_{p, n_{CI}}$는 검색 공간 세트 $p$와 [[RNTI]]에 따라 결정되는 값이며, $i = 0, \dots, L-1$입니다.

4. 다중 검색 공간 처리:
   - 동일한 [[RNTI]]로 스크램블된 여러 [[DCI]] 포맷을 모니터링할 때, [[UE]]는 슬롯당 최대 처리 가능한 [[PDCCH]] 후보 수 및 비중첩 [[CCE]] 수 제한을 준수해야 합니다.
   - `searchSpaceLinkingId`가 동일한 검색 공간 세트들은 링크되어 동일한 정보를 가진 [[DCI]]를 검출하기 위해 사용될 수 있습니다.

## 인과 관계
- [[PDCCH_Search_Space_Configuration]] depends_on [[CORESET_Configuration]] (검색 공간은 특정 CORESET 자원 내에서 정의됨)
- [[PDCCH_Search_Space_Configuration]] affects [[PDCCH_Validation]] (설정된 검색 공간 내에서만 DCI 유효성 검사 수행)
- [[PDCCH_Search_Space_Configuration]] depends_on [[PDCCH_Monitoring_Capability]] (UE의 모니터링 능력에 따라 검색 공간 설정 및 후보 수 제한)
- [[PDCCH_Search_Space_Configuration]] triggers [[PDCCH_Resource_Mapping]] (설정된 검색 공간 파라미터에 따라 CCE-to-REG 매핑 수행)

## 관련 개념
- [[CORESET_Configuration]] (depends_on)
- [[PDCCH_Monitoring_Capability]] (depends_on)
- [[PDCCH_Validation]] (affects)
- [[PDCCH_Resource_Mapping]] (triggers)
- [[DCI_Field_Mapping]] (depends_on)

## 스펙 근거
- TS 38.213 §10.1: UE procedure for determining physical downlink control channel assignment
- TS 38.213 §10.1, Table 10.1-1: CCE aggregation levels and maximum number of PDCCH candidates
- TS 38.213 §10.1, Table 10.1-2/2A/2B: Maximum number of monitored PDCCH candidates per slot/span/group of slots

## 소스
- 3GPP TS 38.213 v18.0.0 §10.1