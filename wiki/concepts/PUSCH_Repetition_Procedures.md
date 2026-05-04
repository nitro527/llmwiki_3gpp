# PUSCH_Repetition_Procedures

## 정의
[[PUSCH]] 반복 전송 절차는 동일한 [[Transport_Block]] (TB)를 여러 슬롯 또는 슬롯 내 여러 번의 기회에 걸쳐 전송함으로써 상향링크 데이터 전송의 신뢰성을 향상시키는 기법입니다.

## 요약
[[PUSCH]] 반복은 전송 효율과 커버리지 확장을 위해 설계되었으며, 크게 Type A와 Type B로 구분됩니다. 이 절차는 [[DCI]]를 통한 동적 스케줄링 또는 [[PUSCH_Configured_Grant_Transmission]]을 통해 수행됩니다. UE는 [[Active_spatial_relations]]를 유지하며, 다중 슬롯에 걸친 TB 처리 및 리던던시 버전(RV) 시퀀스 적용을 통해 전송을 수행합니다.

## 상세 설명
[[PUSCH]] 반복 절차는 다음과 같은 핵심 메커니즘을 포함합니다.

*   **UE Feature 지원**: 
    *   필수(cap): [[Active_spatial_relations]] (2-60) 지원이 필수적으로 요구됩니다.
    *   선택 사항: 
        *   Type 1/2 configured [[PUSCH]] repetitions over multiple slots (5-14, 5-16, 10-38, 10-39)
        *   TB processing over multi-slot [[PUSCH]] (30-3, 30-3a)
        *   UE processing time Capability 1/2에 따른 슬롯당 최대 [[PUSCH]] 전송 수 (5-12, 5-12a, 5-12b, 5-13d)
*   **Type A/B 구분**: 
    *   Type A: 슬롯 내 심볼 위치가 고정된 반복 전송 방식입니다.
    *   Type B: 슬롯 경계에 구애받지 않고 심볼 단위로 반복 전송을 수행하는 방식입니다.
*   **RV 시퀀스**: 반복 전송 시 각 전송 기회마다 [[HARQ]] 리던던시 버전(RV)이 정의된 시퀀스에 따라 순환적으로 적용되어 채널 코딩 이득을 극대화합니다.
*   **무효 심볼 처리**: [[Slot_Format_Configuration]] 등에 의해 전송이 불가능한 심볼이 포함될 경우, 해당 심볼을 건너뛰거나(omission) 전송을 연기하는 절차가 적용됩니다.
*   **TCI 상태 연동**: 반복 전송 시 [[Active_spatial_relations]] 및 [[TCI_State]]가 유지되거나 설정에 따라 변경될 수 있습니다.

## 인과 관계
*   [[PUSCH_Resource_Allocation]] (depends_on): 시간 도메인 자원 할당 정보가 반복 횟수 및 방식을 결정합니다.
*   [[HARQ_ACK_Codebook_Determination]] (affects): 반복 전송 시의 [[HARQ]] 피드백 타이밍 및 처리 방식에 영향을 줍니다.
*   [[PUSCH_Transmission_Procedures]] (part_of): 전체 상향링크 전송 절차의 일부로 동작합니다.

## 관련 개념
- [[PUSCH]] (part_of)
- [[HARQ]] (affects)
- [[DCI]] (triggers)
- [[Slot_Format_Configuration]] (affects)
- [[Active_spatial_relations]] (depends_on)
- [[PUSCH_Configured_Grant_Transmission]] (similar_to)

## 스펙 근거
- TS 38.214 §6.1.2.1: [[PUSCH]] 시간 도메인 자원 할당 및 반복 전송 파라미터 결정 절차 정의
- TS 38.214 §6.1.2.1.1: 자원 할당 테이블 선택 및 반복 전송 관련 설정 근거

## 소스
- 3GPP TS 38.214 (Release 16/17/18)
- 3GPP TS 38.822 (UE Feature 목록)