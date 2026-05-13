# Paging_Early_Indication

## 정의
[[Paging_Early_Indication]]은 [[RRC_IDLE]] 또는 [[RRC_INACTIVE]] 상태에 있는 [[UE]]가 [[Paging_Occasion]]을 모니터링하기 전, [[DCI_Format_2_7]]을 통해 페이징 발생 여부를 미리 확인하거나 [[TRS]] 자원의 가용성을 판단하는 절차를 의미한다.

## 요약
[[UE]]는 네트워크로부터 설정된 [[PDCCH]] 모니터링 기회를 통해 [[DCI_Format_2_7]]을 수신한다. 이 DCI는 특정 [[Paging_Occasion]]에 대한 페이징 존재 여부를 지시하는 페이징 지시 필드와, [[TRS]] 자원 세트의 가용성을 알리는 [[TRS]] 가용성 지시 필드를 포함할 수 있다. 이를 통해 [[UE]]는 불필요한 [[PDCCH]] 모니터링을 생략하여 전력을 절감할 수 있다.

## 상세 설명
[[UE]]는 [[RRC]] 시그널링을 통해 [[Paging_Early_Indication]]을 위한 파라미터를 제공받는다.

1. [[DCI_Format_2_7]] 모니터링 설정:
   - [[pei-SearchSpace]]: [[DCI_Format_2_7]]을 모니터링하기 위한 [[Type2A-PDCCH_CSS_set]] 설정.
   - [[pei-FrameOffset]]: 프레임 시작점부터 첫 번째 [[Paging_Frame]]까지의 오프셋.
   - [[firstPDCCH-MonitoringOccasionOfPEI-O]]: 프레임 시작점부터 첫 번째 [[PDCCH]] 모니터링 기회까지의 심볼 오프셋.
   - [[payloadSizeDCI-2-7]]: [[DCI_Format_2_7]]의 페이로드 크기.
   - [[subgroupsNumPerPO]]: [[Paging_Occasion]] 당 서브그룹 수.
   - [[po-NumPerPEI]]: [[DCI_Format_2_7]]과 연관된 [[Paging_Occasion]]의 수.

2. 페이징 지시 절차:
   - [[DCI_Format_2_7]] 내 페이징 지시 필드는 서브그룹별 비트를 포함한다.
   - 특정 서브그룹 인덱스에 대해 값이 '1'이면 [[UE]]는 해당 [[Paging_Occasion]]을 모니터링해야 하며, '0'이면 모니터링을 생략할 수 있다.

3. [[TRS]] 가용성 지시 절차:
   - [[trs-ResourceSetConfig]] 또는 [[trs-ResourceSetConfig-r18]]이 설정된 경우, [[DCI_Format_2_7]] 또는 [[P-RNTI]]로 스크램블된 [[DCI_Format_1_0]]에 [[TRS]] 가용성 지시 필드가 포함된다.
   - 비트맵의 각 비트는 [[TRS]] 자원 세트 그룹과 연관된다.
   - 값이 '1'이면 해당 [[TRS]] 자원 세트가 유효함을 나타내며, '0'은 현재 상태 유지(변경 없음)를 의미한다.
   - 유효 기간은 [[validityDuration]] 파라미터에 의해 결정되며, 기본값은 2이다.

## 인과 관계
- [[DCI_Format_2_7]] depends_on [[PDCCH_Monitoring_Procedures]] (페이징 조기 지시 수신을 위한 전제 조건)
- [[Paging_Early_Indication]] affects [[PDCCH_Monitoring_Procedures]] (페이징 모니터링 여부 결정에 따른 동작 제어)
- [[TRS]] depends_on [[Paging_Early_Indication]] (TRS 자원 가용성 지시를 통한 TRS 수신 여부 결정)

## 관련 개념
- [[PDCCH]] (implements)
- [[DCI_Format_2_7]] (implements)
- [[Paging_Occasion]] (affects)
- [[TRS]] (affects)
- [[P-RNTI]] (depends_on)
- [[RRC_IDLE]] (depends_on)
- [[RRC_INACTIVE]] (depends_on)

## 스펙 근거
- TS 38.213 §10.4A: [[DCI_Format_2_7]]을 이용한 페이징 조기 지시 절차 정의
- TS 38.213 §10.4B: [[TRS]] 자원 가용성 지시 절차 정의

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)