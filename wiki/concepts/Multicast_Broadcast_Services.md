# Multicast Broadcast Services

## 정의
[[Multicast_Broadcast_Services]] (MBS)는 5G NR 시스템에서 다수의 [[UE]]에게 동일한 데이터를 효율적으로 전송하기 위한 그룹 통신 기술을 의미하며, [[PDCCH]]를 통한 제어 정보 수신 및 [[PDSCH]]를 통한 데이터 수신, 그리고 이에 대한 [[HARQ]]-ACK 보고 절차를 포함합니다.

## 요약
MBS는 G-RNTI 또는 G-CS-RNTI를 사용하여 그룹 공통 제어 및 데이터 전송을 수행합니다. [[UE]]는 설정된 피드백 모드에 따라 [[HARQ]]-ACK를 보고하며, 이는 동적 스케줄링 또는 [[SPS]] 기반으로 동작합니다. 관련 기능은 [[UE]]의 능력(Capability)에 따라 지원 여부가 결정됩니다.

## 상세 설명
MBS는 다음과 같은 핵심 메커니즘을 통해 동작합니다.

*   **UE Feature Priority**:
    *   [필수(항상)]: 33-1 (Broadcast)
    *   [필수(항상)]: 33-2 (Dynamic scheduling for multicast for PCell), 33-2h (Dynamic scheduling for multicast for SCell)
    *   [필수(항상)]: 33-5-1 (SPS group-common PDSCH for multicast on PCell), 33-5-3 (One SPS group-common PDSCH configuration for multicast for Scell)
    *   [선택]: 33-5-1a, 33-5-1b, 33-5-1f, 33-5-1g (SPS 기반 피드백 활성화/비활성화 및 모드 설정)
    *   [선택]: 33-2b (동적 스케줄링 피드백 활성화/비활성화)
    *   [선택]: 33-3-3a, 33-3-5 (유니캐스트 및 멀티캐스트 HARQ-ACK 코드북 다중화)

*   **수신 절차**: [[UE]]는 G-RNTI로 스크램블된 [[PDCCH]]를 모니터링하여 그룹 공통 [[PDSCH]] 할당 정보를 획득합니다.
*   **HARQ-ACK 보고**: 
    *   ACK/NACK 기반 피드백 또는 NACK-only 기반 피드백 모드가 설정될 수 있습니다.
    *   [[RRC]] 설정 또는 [[DCI]]를 통해 피드백 활성화 여부가 제어됩니다.
    *   유니캐스트와 멀티캐스트 [[HARQ]]-ACK가 동일한 우선순위를 가질 경우, 코드북 타입에 따라 다중화되어 보고됩니다.

## 인과 관계
*   [[PDCCH]] 수신 (triggers) [[PDSCH]] 수신
*   [[PDSCH]] 수신 (triggers) [[HARQ]]-ACK 보고
*   [[UE]] Capability (affects) MBS 피드백 모드 지원

## 관련 개념
- [[PDCCH]] (depends_on)
- [[PDSCH]] (depends_on)
- [[HARQ]] (part_of)
- [[SPS]] (similar_to)
- [[RRC]] (affects)

## 스펙 근거
TS 38.213 §18에 따르면, MBS를 위한 그룹 공통 [[PDSCH]] 수신 및 [[HARQ]]-ACK 피드백 절차는 다음과 같이 정의됩니다.
*   §18.1: G-RNTI 및 G-CS-RNTI를 이용한 [[PDCCH]] 모니터링 및 [[PDSCH]] 수신 절차
*   §18.2: 멀티캐스트를 위한 [[HARQ]]-ACK 보고 모드(ACK/NACK 기반 및 NACK-only 기반) 설정
*   §18.3: 유니캐스트 및 멀티캐스트 [[HARQ]]-ACK 코드북 생성 및 다중화 규칙

## 소스
- 3GPP TS 38.213 v18.0.0, "NR; Physical layer procedures for control"