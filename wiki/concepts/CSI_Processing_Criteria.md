# CSI_Processing_Criteria

## 정의
[[CSI_Processing_Criteria]]는 [[UE]]가 [[CSI_RS]]를 기반으로 [[CSI]]를 계산하고 보고하는 과정에서 준수해야 하는 처리 능력 및 시간적 제약 조건을 의미합니다.

## 요약
[[CSI]] 계산은 [[UE]]의 연산 자원과 처리 시간에 의존하며, [[TS_38_214]]에 정의된 기준에 따라 [[UE]]가 동시에 처리할 수 있는 [[CSI]] 보고의 양과 타이밍이 결정됩니다. [[UE]]는 할당된 [[CSI_RS]] 자원과 보고 설정에 따라 계산 부하를 관리하며, 특정 조건에서는 [[CSI]] 보고를 생략하거나 지연시킬 수 있습니다.

## 상세 설명
[[CSI_Processing_Criteria]]는 다음과 같은 요소들을 포함합니다:

- [[UE]] 처리 능력: [[UE]]는 자신의 하드웨어 성능에 따라 동시에 처리 가능한 [[CSI]] 계산 작업의 수를 제한합니다.
- [[CSI]] 계산 시간: [[CSI_RS]] 수신 시점부터 해당 [[CSI]] 보고가 준비되기까지 필요한 최소 시간을 보장해야 합니다.
- 동시 보고 제한: 여러 [[CSI]] 보고가 동일한 시점에 발생할 경우, [[UE]]는 우선순위 규칙에 따라 보고를 수행하거나 일부를 드롭합니다.
- [[CSI_RS]] 처리 프레임워크: [[SRS]], [[RRM]], [[RLM]] 등 다양한 목적의 [[CSI_RS]] 기반 측정에 대해 [[UE]]가 지원하는 기능(예: 1-7: [[CSI_RS]] based [[RLM]])에 따라 처리 우선순위가 결정됩니다.

## 인과 관계
- [[CSI_Computation_Timing]] (depends_on) [[CSI_Processing_Criteria]]
- [[CSI_Reporting_Procedures]] (depends_on) [[CSI_Processing_Criteria]]
- [[UE]] 처리 능력 (affects) [[CSI_Processing_Criteria]]

## 관련 개념
- [[CSI_RS]] (part_of)
- [[CSI_Computation_Timing]] (similar_to)
- [[CSI_Reporting_Procedures]] (similar_to)
- [[Radio_Link_Monitoring]] (depends_on)

## 스펙 근거
- [[TS_38_214]] §5.2.1.6에 따르면, [[UE]]는 [[CSI]] 계산을 위한 처리 기준을 만족해야 하며, 이는 [[UE]]의 능력치와 설정된 [[CSI]] 보고 파라미터에 의해 결정됩니다.

## 소스
- 3GPP TS 38.214 V19.0.0, "NR; Physical layer procedures for data"