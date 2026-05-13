# SR_Reporting

## 정의
[[SR]]은 [[UE]]가 상향링크 자원을 요청하기 위해 [[PUCCH]]를 통해 전송하는 물리 계층 제어 정보이며, LRR은 [[LBT]] 실패 상황에서 복구를 위해 수행하는 보고 절차를 의미한다.

## 요약
[[UE]]는 상위 계층으로부터 설정된 [[SchedulingRequestResourceConfig]]를 통해 [[PUCCH]] format 0 또는 format 1을 사용하여 [[SR]]을 전송한다. 또한, [[BFR]] 및 [[LBT]] 실패 복구를 위한 전용 자원 설정이 제공될 수 있으며, 각 설정은 주기성과 오프셋을 기반으로 결정된 전송 기회(transmission occasion)에서 수행된다.

## 상세 설명
[[UE]]는 상위 계층으로부터 제공받은 설정에 따라 [[SR]] 및 LRR을 수행한다.

1. 자원 설정:
   - [[SR]] 전송을 위해 [[SchedulingRequestResourceConfig]]가 제공되며, [[PUCCH]] format 0 또는 format 1이 사용된다.
   - LRR을 위해 [[schedulingRequestID-BFR-SCell]], [[schedulingRequestID-BFR]], [[schedulingRequestID-BFR2]] (twoLRRcapability 지원 시), 그리고 [[schedulingRequestID-LBT-SCell]]이 설정될 수 있다.
   - [[phy-PriorityIndex]]를 통해 0 또는 1의 우선순위 인덱스가 할당되며, 미제공 시 기본값은 0이다.

2. 전송 주기 및 기회 결정:
   - [[periodicityAndOffset]]을 통해 주기와 슬롯 오프셋이 제공된다.
   - 주기가 1 슬롯보다 큰 경우, 슬롯 번호 $n_f$와 프레임 번호 $n_s$에 대해 $(10 \cdot n_f + \lfloor n_s / 2 \rfloor) \pmod P = O$ 조건을 만족하는 슬롯에서 전송한다.
   - 주기가 1 슬롯인 경우 모든 슬롯이 전송 기회가 된다.
   - 주기가 1 슬롯보다 작은 경우, [[startingSymbolIndex]]를 기반으로 특정 심볼에서 전송이 시작된다.
   - 슬롯 내 가용 심볼 수가 [[nrofSymbols]]보다 작으면 해당 슬롯에서는 전송하지 않는다.

3. 전송 절차:
   - [[UE]]는 긍정적(positive) [[SR]]이 발생한 경우에만 [[PUCCH]] 자원을 통해 전송한다.
   - [[PUCCH]] format 0 사용 시 [[HARQ_ACK_Reporting]] 절차와 유사하게 $m_0$를 결정하고 $m_f = 0$으로 설정한다.
   - [[PUCCH]] format 1 사용 시 $b(0) = 0$으로 설정하여 전송한다.
   - 모든 전송은 상향링크 전송 제한 사항을 준수해야 한다.

## 인과 관계
- [[SR_Reporting]] depends_on [[PUCCH]] (SR 전송을 위한 물리 채널)
- [[SR_Reporting]] depends_on [[HARQ_ACK_Reporting]] (format 0 전송 시 파라미터 결정 방식 참조)

## 관련 개념
- [[PUCCH]] (part_of)
- [[HARQ_ACK_Reporting]] (depends_on)
- [[BFR]] (depends_on)

## 스펙 근거
- TS 38.213 §9.2.4: [[SR]] 설정, 주기성 결정, 전송 조건 및 format 0/1 전송 절차 정의

## 소스
- 3GPP TS 38.213 v18.0.0, "NR; Physical layer procedures for control"