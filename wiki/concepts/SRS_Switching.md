# SRS_Switching

## 정의
SRS_Switching은 [[UE]]가 특정 서빙 셀에서 [[SRS]]를 전송하기 위해 다른 서빙 셀의 상향링크 전송을 일시적으로 중단하고 RF 리튜닝을 수행하는 절차를 의미한다.

## 요약
SRS_Switching은 [[Carrier_Aggregation]] 환경에서 [[SRS]] 전송을 위해 주파수 대역 간 또는 셀 간 RF 경로를 전환하는 메커니즘이다. [[DCI_Format_2_3]]을 통해 트리거되며, 전송 시 발생하는 RF 리튜닝 시간 동안 기존 상향링크 전송이 중단된다. 이때 발생하는 충돌을 방지하기 위해 우선순위 기반의 드롭 규칙이 적용된다.

## 상세 설명
SRS_Switching은 상향링크 전송이 설정되지 않은 셀에서 [[SRS]]를 전송하거나, 전력 제어 상태가 분리된 경우에 수행된다.

1. 설정 및 트리거:
   - 상위 계층 파라미터 carrierSwitching을 통해 설정되며, tpc-SRS-RNTI를 사용하여 [[DCI_Format_2_3]]을 수신한다.
   - srs-SwitchFromServCellIndex 및 srs-SwitchFromCarrier를 통해 전송이 중단될 셀과 캐리어를 지정한다.
   - [[DCI_Format_2_3]]은 typeA 또는 typeB 설정에 따라 TPC 커맨드와 [[SRS]] 요청 필드를 포함한다.

2. RF 리튜닝 및 전송:
   - [[SRS]] 전송 시 switchingTimeUL 및 switchingTimeDL에 정의된 RF 리튜닝 시간이 포함되며, 이 기간 동안 설정된 셀 집합 S(c2)의 상향링크 전송이 일시 중단된다.
   - n번째 비주기적 [[SRS]] 전송은 DCI 수신 후 최소 시간 간격(N 심볼 및 RF 리튜닝 시간의 합) 이후에 시작되어야 한다.

3. 충돌 해결 및 우선순위 규칙:
   - [[SRS]] 전송과 [[PUSCH]]/[[PUCCH]] 전송이 겹칠 경우 다음 규칙에 따라 우선순위를 결정한다.
   - [[HARQ_ACK]], [[SR]], [[RI]], [[CRI]], [[SSBRI]] 또는 [[PRACH]]를 포함하는 [[PUSCH]]/[[PUCCH]]와 [[SRS]]가 겹치면 [[SRS]]를 전송하지 않는다.
   - 주기적/반주기적 [[SRS]]와 비주기적 [[CSI]]를 포함하는 [[PUSCH]]가 겹치면 [[SRS]]를 전송하지 않는다.
   - 주기적/반주기적 [[CSI]]만 포함하는 [[PUCCH]]/[[PUSCH]]는 [[SRS]]와 겹칠 경우 드롭된다.
   - 비주기적 [[CSI]]만 포함하는 [[PUSCH]]는 비주기적 [[SRS]]와 겹칠 경우 드롭된다.

## 인과 관계
- [[SRS_Switching]] depends_on [[DCI_Format_2_3]] (SRS 전송 트리거 및 설정 정보 수신)
- [[SRS_Switching]] affects [[PUSCH]] (RF 리튜닝 기간 동안 상향링크 전송 중단)
- [[SRS_Switching]] affects [[PUCCH]] (RF 리튜닝 기간 동안 상향링크 전송 중단)
- [[SRS_Switching]] depends_on [[SRS]] (전송할 자원 및 설정 정보)

## 관련 개념
- [[Carrier_Aggregation]] (part_of)
- [[DCI_Format_2_3]] (triggers)
- [[SRS]] (implements)
- [[PUSCH]] (affects)
- [[PUCCH]] (affects)
- [[PRACH]] (affects)

## 스펙 근거
- TS 38.213 §11.4: SRS switching 설정 및 DCI format 2_3 동작 정의
- TS 38.214 §6.2.1.3: 캐리어 간 SRS 전송 절차, RF 리튜닝 시간, 우선순위 및 드롭 규칙 정의

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)
- 3GPP TS 38.214 V18.0.0 (2024-03)