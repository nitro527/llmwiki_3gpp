# UCI_Reporting_Different_Priorities

## 정의
[[UCI]] Reporting Different Priorities는 서로 다른 우선순위(Priority 0 및 Priority 1)를 가진 [[HARQ-ACK]] 및 [[SR]] 정보를 [[PUCCH]] 또는 [[PUSCH]]를 통해 전송할 때, UE가 수행하는 다중화 및 전력 제어 절차를 의미합니다.

## 요약
본 절차는 서로 다른 우선순위를 가진 UCI가 동일한 슬롯 내에서 충돌하거나 다중화가 필요할 때, UE가 우선순위 규칙에 따라 자원을 할당하고 전력을 제어하는 메커니즘을 정의합니다. 특히 [[DCI]] format 1_3을 통한 다중 [[HARQ-ACK]] 코드북 구성 및 우선순위 기반의 전송 우선권 결정이 핵심입니다.

## 상세 설명
TS 38.213 §9.2.5.3에 따라, UE는 서로 다른 우선순위를 가진 UCI를 보고하기 위해 다음과 같은 절차를 수행합니다.

1. **UE Feature 지원**:
   - 25-16: 서로 다른 우선순위를 가진 HARQ-ACK의 PUCCH/PUSCH 다중화 지원.
   - 11-4: 우선순위가 다른 HARQ-ACK 코드북을 동시에 구성하기 위한 최대 1개의 sub-slot 기반 HARQ-ACK 코드북 지원.
   - 11-4a: 서로 다른 우선순위를 가진 HARQ-ACK 코드북을 지원하기 위한 2개의 sub-slot 기반 HARQ-ACK 코드북 동시 구성.
   - 11-4e: 2개의 sub-slot 기반 HARQ-ACK 코드북을 위해 동일 sub-slot 내 연속 심볼에서 format 0 또는 2의 2개 PUCCH 전송.
   - 49-6 및 49-6a: DCI format 1_3을 통해 서로 다른 우선순위의 HARQ-ACK 코드북을 동시에 구성.
   - 4-2: 연속 심볼에서 2개의 PUCCH format 0 또는 2 전송.
   - 4-19a, 4-19b, 4-19c, 10-35a, 10-35b: 슬롯 내에서 SR/HARQ-ACK/CSI의 다중화 및 전송 절차 지원.

2. **다중화 및 전송**:
   - 서로 다른 우선순위의 UCI가 동일한 슬롯 내에서 전송되어야 할 경우, UE는 우선순위가 높은 UCI를 우선적으로 처리합니다.
   - PUCCH 자원이 겹치거나 다중화가 필요한 경우, 정의된 우선순위 규칙에 따라 PUCCH format을 선택하거나 PUSCH에 피기백(piggyback)합니다.

3. **전력 제어**:
   - 우선순위가 다른 UCI 전송 시, UE는 [[Uplink_Power_Control]] 절차에 따라 각 우선순위에 할당된 전력 제어 파라미터를 적용합니다.
   - 전력 제한 상황 발생 시, 낮은 우선순위의 UCI 전송 전력을 줄이거나 생략할 수 있습니다.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) -> [[UCI_Reporting_Different_Priorities]]
- [[UCI_Reporting_Different_Priorities]] (affects) -> [[PUCCH_Power_Control]]
- [[UCI_Reporting_Different_Priorities]] (affects) -> [[PUSCH_Power_Control]]
- [[UCI_Reporting_Different_Priorities]] (depends_on) -> [[HARQ_ACK_Codebook_Determination]]

## 관련 개념
- [[HARQ-ACK]] (part_of)
- [[SR]] (part_of)
- [[PUCCH]] (part_of)
- [[PUSCH]] (part_of)
- [[Uplink_Power_Prioritization]] (similar_to)

## 스펙 근거
- TS 38.213 §9.2.5.3: UE procedure for reporting UCI of different priorities.

## 소스
- 3GPP TS 38.213 Release 18 (v18.0.0)