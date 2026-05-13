# Sidelink_Carrier_Aggregation

## 정의
Sidelink_Carrier_Aggregation은 다중 캐리어 환경에서 사이드링크 통신을 수행하기 위해 여러 캐리어에 걸쳐 동기화, 전력 제어 및 자원 할당을 관리하는 기술입니다.

## 요약
다중 캐리어 사이드링크 환경에서 UE는 각 캐리어별로 [[Synchronization_Procedures]]를 독립적으로 수행합니다. S-SS/PSBCH 블록 및 PSCCH/PSSCH 전송 시, 시간적으로 중첩되는 다중 캐리어 전송의 총 전력이 허용치를 초과할 경우 전력 감소 또는 전송 드롭 절차를 통해 전력 제한을 준수합니다. 또한, PSFCH 전송 및 수신 시에도 다중 캐리어 간의 시간 정렬과 동일한 전력 수준을 유지하도록 구성됩니다.

## 상세 설명
TS 38.213 §16.2.5에 따라 다중 캐리어 사이드링크 동작은 다음과 같이 수행됩니다.

1. 동기화: UE는 설정된 각 캐리어에 대해 개별적으로 동기화 절차를 수행합니다. 이때 sl-StartSymbol, sl-LengthSymbols, cyclicPrefix, subcarrierSpacing은 모든 캐리어에서 동일한 값으로 (pre)configuration되어야 합니다.
2. S-SS/PSBCH 블록 전력 제어: 각 캐리어별로 전력을 결정한 후, 시간적으로 중첩되는 전송의 총합이 허용치를 초과하면 UE는 자율적으로 전력을 감소시켜 제한치를 준수합니다.
3. PSCCH/PSSCH 전력 제어 및 우선순위 처리:
   - 각 캐리어별로 전력을 결정한 후, 총 전력이 허용치를 초과하면 우선순위 값이 가장 큰(즉, 우선순위가 낮은) PSCCH/PSSCH 전송의 전력을 감소시킵니다.
   - 동일한 우선순위 값을 가진 전송이 다수일 경우, UE는 자율적으로 하나를 선택하여 전력을 감소시킵니다.
   - 전력 감소 후에도 총 전력이 허용치를 초과하면, 해당 전송을 드롭하고 나머지 전송에 대해 동일한 절차를 반복합니다.
4. PSFCH 동작:
   - 다중 캐리어에서 PSFCH 송수신이 동시에 발생할 경우, 모든 PSFCH를 고려하여 송신 또는 수신할 PSFCH를 결정합니다.
   - 다중 캐리어에서 PSFCH를 송신할 경우, 단일 캐리어 절차를 확장하여 적용하며, 모든 캐리어에서 시간 자원 정렬과 동일한 전력 수준을 유지해야 합니다.

## 인과 관계
- [[Synchronization_Procedures]] depends_on [[Sidelink_Carrier_Aggregation]] (다중 캐리어 동기화 수행 전제)
- [[Sidelink_Power_Control]] affects [[Sidelink_Carrier_Aggregation]] (다중 캐리어 전력 제한 준수)
- [[Sidelink_Prioritization]] affects [[Sidelink_Carrier_Aggregation]] (우선순위 기반 전송 드롭 결정)

## 관련 개념
- [[Synchronization_Procedures]] (implements)
- [[Sidelink_Power_Control]] (implements)
- [[Sidelink_Prioritization]] (implements)
- [[PSBCH]] (part_of)
- [[PSCCH]] (part_of)
- [[PSSCH]] (part_of)
- [[PSFCH]] (part_of)

## 스펙 근거
- TS 38.213 §16.2.5: 다중 캐리어 사이드링크 동작, 전력 제어 및 우선순위 기반 드롭 절차 정의
- TS 38.213 §16.1: 사이드링크 동기화 절차 참조
- TS 38.213 §16.2.0, §16.2.1, §16.2.2: 전력 결정 절차 참조
- TS 38.213 §16.2.3, §16.2.4.2: PSFCH 송수신 절차 참조
- TS 38.101-1 §6.2E.4A: PSFCH 전력 관련 정의

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"