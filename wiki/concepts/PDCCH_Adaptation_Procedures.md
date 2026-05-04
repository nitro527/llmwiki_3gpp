# PDCCH_Adaptation_Procedures

## 정의
[[PDCCH]] 모니터링 적응 절차는 [[UE]]가 전력 소모를 최적화하고 네트워크 효율성을 높이기 위해 [[SCell]]의 휴면 상태(dormancy)를 관리하거나, [[Search_space]] 세트 그룹을 동적으로 전환하고, 특정 조건에서 [[PDCCH]] 모니터링을 건너뛰는(skipping) 일련의 L1 제어 절차를 의미한다.

## 요약
본 절차는 [[TS_38.213]]에 정의된 메커니즘으로, [[DCI]]를 통해 [[SCell]]의 활성/휴면 상태를 제어하거나, [[Search_space]] 세트 그룹 스위칭을 수행하여 [[UE]]의 [[PDCCH]] 모니터링 부하를 조절한다. 또한, 페이징 조기 표시(early indication of paging) 및 [[TRS]] 자원 지시와 같은 부가적인 적응 기능을 포함한다.

## 상세 설명
[[PDCCH]] 모니터링 적응은 크게 세 가지 영역으로 구분된다.

1. **[[SCell]] Dormancy 관리**: [[UE]]는 [[DCI_format_1_1]] 또는 [[DCI_format_0_1]] 등을 통해 특정 [[SCell]]에 대한 휴면(dormant) 상태를 지시받을 수 있다. 휴면 상태의 [[SCell]]은 [[PDCCH]] 모니터링을 수행하지 않으며, 이를 통해 전력 소모를 절감한다. [[DCI_format_0_3]]/[[DCI_format_1_3]]을 통한 지시도 지원된다.
2. **[[Search_space]] 세트 그룹 스위칭**: 네트워크는 [[UE]]에게 다수의 [[Search_space]] 세트 그룹을 설정할 수 있으며, [[DCI]]를 통해 현재 활성화된 그룹을 동적으로 전환한다. 이는 트래픽 부하에 따라 [[PDCCH]] 모니터링 빈도를 조절하는 핵심 수단이다.
3. **[[PDCCH]] 모니터링 스킵**: 특정 조건 하에서 [[UE]]는 설정된 [[Search_space]]에 대한 모니터링을 일시적으로 중단한다. 이는 불필요한 블라인드 디코딩을 방지하여 [[UE]]의 배터리 수명을 연장한다.
4. **부가 기능**: 페이징 조기 표시를 통해 [[UE]]가 페이징 메시지 수신 여부를 사전에 인지하여 불필요한 웨이크업을 방지하며, [[TRS]] 자원 지시를 통해 채널 추정 성능을 최적화한다.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) [[PDCCH]] 모니터링 적응 절차
- [[PDCCH]] 모니터링 적응 절차 (affects) [[UE]] 전력 소모 및 [[PDCCH]] 블라인드 디코딩 횟수
- [[SCell_Activation_Deactivation_Timing]] (depends_on) [[SCell]] dormancy 상태

## 관련 개념
- [[PDCCH_Monitoring_Procedures]] (part_of)
- [[DCI_Formats_Processing]] (depends_on)
- [[SCell_Activation_Deactivation_Timing]] (affects)
- [[Bandwidth_Part_Operation]] (depends_on)

## 스펙 근거
- [[TS_38.213]] §10.3: [[SCell]] dormancy 및 비-휴면 동작 정의
- [[TS_38.213]] §10.4: [[Search_space]] 세트 그룹 스위칭 및 모니터링 스킵 절차
- [[TS_38.213]] §10.4A: 페이징 조기 표시를 위한 [[PDCCH]] 모니터링
- [[TS_38.213]] §10.4B: [[TRS]] 자원 지시 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"