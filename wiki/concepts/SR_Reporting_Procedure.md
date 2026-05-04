# SR_Reporting_Procedure

## 정의
[[SR]] (Scheduling Request) Reporting Procedure는 [[UE]]가 상향링크 데이터를 전송하기 위해 [[gNB]]로부터 [[PUSCH]] 자원을 할당받고자 할 때 사용하는 제어 절차입니다.

## 요약
[[UE]]는 상위 계층으로부터 설정된 [[PUCCH]] 자원을 통해 [[SR]]을 전송합니다. 이 과정에서 [[HARQ-ACK]] 또는 [[CSI]]와 같은 다른 [[UCI]] 정보와 다중화되어 전송될 수 있으며, 특정 조건에 따라 [[PUSCH]]로 피기백(piggyback)되어 전송되기도 합니다.

## 상세 설명
[[SR]] 전송 절차는 다음과 같은 핵심 메커니즘을 포함합니다.

- [[UE]]는 상위 계층에 의해 설정된 [[PUCCH]] 자원을 사용하여 [[SR]]을 전송합니다.
- [[SR]] 전송이 설정된 [[Slot]]에서, [[UE]]는 해당 [[SR]]에 할당된 [[PUCCH]] 자원이 [[HARQ-ACK]] 또는 [[CSI]] 전송과 겹치는 경우, TS 38.213 §9.2.5.1에 명시된 다중화 규칙에 따라 이를 결합하여 전송합니다.
- [[UE]]가 [[SR]]을 전송할 때, 해당 [[SR]]이 긍정(positive) 상태라면 [[gNB]]는 이를 감지하여 [[PUSCH]] 자원 할당을 위한 [[DCI]]를 전송합니다.
- 다중 SR 설정이 가능한 경우, [[UE]]는 각 [[SR]] 설정에 대해 독립적인 전송 기회를 가집니다.
- [[UE]]는 [[PUCCH]] 자원 상에서 [[SR]]/[[HARQ-ACK]]/[[CSI]] 다중화 시, 동일한 시작 심볼을 가지거나 서로 다른 시작 심볼을 가지는 경우에 대해 각각 정의된 우선순위 및 다중화 절차를 따릅니다.

## 인과 관계
- [[SR]] 전송 (triggers) [[PDCCH]] 기반의 [[PUSCH]] 자원 할당
- [[PUCCH]] 자원 설정 (depends_on) [[SR]] 전송 가능 여부
- [[HARQ-ACK]] 또는 [[CSI]]의 존재 (affects) [[SR]]의 [[PUCCH]] 다중화 방식

## 관련 개념
- [[PUCCH]] (part_of)
- [[PUSCH]] (depends_on)
- [[HARQ-ACK]] (affects)
- [[CSI]] (affects)
- [[DCI]] (triggers)

## 스펙 근거
- TS 38.213 §9.2.4: [[UE]] procedure for reporting [[SR]]
- TS 38.213 §9.2.5.1: [[UE]] procedure for multiplexing [[HARQ-ACK]] or [[CSI]] and [[SR]] in a [[PUCCH]]

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"