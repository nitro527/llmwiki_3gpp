# PUCCH_SPS_HARQ_Deferral

## 정의
[[PUCCH_SPS_HARQ_Deferral]]은 [[SPS]] [[PDSCH]] 수신에 대한 [[HARQ_ACK_Reporting]]이 특정 조건에서 충돌하거나 전송 불가능한 경우, 이를 즉시 폐기하지 않고 이후의 유효한 [[PUCCH]] 또는 [[PUSCH]] 자원으로 지연시켜 다중화하는 절차를 의미합니다.

## 요약
[[SPS]] [[PDSCH]] 수신 후 결정된 [[PUCCH]] 자원이 [[TDD]] 설정, [[SSB]] 위치, 또는 [[CORESET]]과의 충돌로 인해 전송이 불가능하거나 우선순위가 낮은 경우, [[UE]]는 해당 [[HARQ_ACK]] 정보를 즉시 전송하지 않고 가장 빠른 다음 슬롯으로 지연시킵니다. 이 과정에서 지연된 정보는 이후 발생하는 다른 [[HARQ_ACK]] 정보와 다중화되어 전송됩니다.

## 상세 설명
TS 38.213 §9.2.5.4에 따라, [[UE]]가 [[sps-HARQ-Deferral]] 기능을 제공받은 경우 다음 절차를 수행합니다.

1. 초기 결정: [[UE]]는 [[SPS]] [[PDSCH]] 수신에 대한 [[HARQ_ACK]] 정보를 전송하기 위한 [[PUCCH]] 자원을 결정합니다. 이 자원은 [[SPS-PUCCH-AN-List]] 또는 [[n1PUCCH-AN]]을 통해 제공됩니다.
2. 전송 불가 조건: 결정된 [[PUCCH]] 자원이 다음 중 하나에 해당하여 전송할 수 없는 경우 지연 절차가 트리거됩니다.
   - [[tdd-UL-DL-ConfigurationCommon]] 또는 [[tdd-UL-DL-ConfigDedicated]]에 의해 다운링크로 지정된 심볼과 겹치는 경우
   - [[ssb-PositionsInBurst]]에 의해 [[SSB]]로 지정된 심볼과 겹치는 경우
   - [[Type0-PDCCH]] [[CORESET]]에 속하는 심볼과 겹치는 경우
   - 더 높은 우선순위의 [[PUCCH]] 또는 [[PUSCH]] 전송에 의해 취소된 경우
3. 지연 및 다중화: [[UE]]는 가장 빠른 두 번째 슬롯을 결정하여 해당 슬롯에서 [[HARQ_ACK]] 정보를 다중화합니다. 이때 지연된 [[HARQ_ACK]] 비트는 새로운 [[HARQ_ACK]] 비트와 결합되어 전송됩니다.
4. 절차 종료 조건: 다음의 경우 [[UE]]는 지연 절차를 중단합니다.
   - [[DCI]] 포맷을 통해 [[Type-3_HARQ-ACK_Codebook]] 전송이 트리거된 경우
   - [[pucch-sSCellPattern]]에 따른 셀 전환 패턴이 적용된 경우
   - 지연된 정보를 [[PUSCH]] 또는 [[SPS-PUCCH-AN-List]]에 포함되지 않은 [[PUCCH]] 자원으로 다중화하는 경우
   - 더 높은 우선순위의 전송과 겹치지 않는 유효한 [[PUCCH]] 자원으로 전송이 성공적으로 수행되는 경우

[[UE]]는 [[sps-HARQ-Deferral]]과 [[nrofSlots]] 또는 [[pucch-RepetitionNrofSlots]]를 동일한 우선순위의 [[PUCCH]] 자원에 대해 동시에 설정받지 않습니다.

## 인과 관계
- [[PUCCH_SPS_HARQ_Deferral]] depends_on [[SPS_PDSCH_Procedure]] (SPS PDSCH 수신에 대한 HARQ-ACK 보고가 전제)
- [[PUCCH_SPS_HARQ_Deferral]] affects [[HARQ_ACK_Reporting]] (지연된 HARQ-ACK 정보를 후속 슬롯으로 다중화하여 보고)
- [[PUCCH_SPS_HARQ_Deferral]] depends_on [[PUCCH_Resource_Selection]] (지연 대상이 되는 초기 PUCCH 자원 결정)
- [[PUCCH_SPS_HARQ_Deferral]] depends_on [[Directional_Collision_Handling]] (TDD 설정 등에 따른 전송 충돌 판단)

## 관련 개념
- [[SPS_PDSCH_Procedure]] (depends_on)
- [[HARQ_ACK_Reporting]] (affects)
- [[PUCCH_Resource_Selection]] (depends_on)
- [[Directional_Collision_Handling]] (depends_on)
- [[HARQ_ACK_Codebook_Determination]] (implements)

## 스펙 근거
- TS 38.213 §9.2.5.4: UE procedure for deferring HARQ-ACK for SPS PDSCH

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18)