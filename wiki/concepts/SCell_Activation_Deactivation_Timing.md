# SCell_Activation_Deactivation_Timing

## 정의
SCell_Activation_Deactivation_Timing은 [[PDSCH]]를 통해 수신된 MAC CE 기반의 SCell 활성화 또는 비활성화 명령에 대해, [[UE]]가 물리 계층에서 해당 동작을 적용해야 하는 시간적 요구사항을 의미한다.

## 요약
[[UE]]는 SCell 활성화 또는 비활성화 명령을 포함한 [[PDSCH]] 수신이 완료된 슬롯 n 이후, TS 38.133에 정의된 최소 요구사항 이내에 해당 동작을 수행해야 한다. 활성화의 경우 특정 슬롯 이후부터 동작이 적용되며, [[CSI]] 보고 및 sCellDeactivationTimer와 관련된 예외 처리가 존재한다.

## 상세 설명
[[UE]]가 SCell 활성화 명령을 포함하는 [[PDSCH]] 수신을 슬롯 n에서 종료하면, 해당 명령에 따른 동작은 TS 38.133에 정의된 최소 요구사항보다 늦지 않게 적용되어야 한다. 또한, 동작 적용은 슬롯 n + m보다 빠를 수 없다. 여기서 m은 해당 [[PDSCH]] 수신에 대한 [[HARQ_ACK_Reporting]]을 포함하는 [[PUCCH]] 전송 슬롯과 관련이 있으며, [[PUCCH]] 전송을 위한 SCS 설정에 따른 서브프레임당 슬롯 수에 의해 결정된다.

활성화 시 예외 사항은 다음과 같다:
- 슬롯 n + m에서 이미 활성화된 서빙 셀에 대한 [[CSI_Reporting_Procedure]] 관련 동작은 즉시 적용된다.
- sCellDeactivationTimer와 관련된 동작은 슬롯 n + m에서 적용된다.
- 슬롯 n + m에서 활성화되지 않은 서빙 셀에 대한 [[CSI_Reporting_Procedure]] 관련 동작은 해당 서빙 셀이 활성화된 이후 가장 빠른 슬롯에서 적용된다.

비활성화 명령의 경우, 명령 수신이 종료된 슬롯 n 이후 TS 38.133의 최소 요구사항 이내에 동작을 적용해야 한다. 단, 활성화된 서빙 셀에 대한 [[CSI_Reporting_Procedure]] 관련 동작은 슬롯 n + m에서 적용된다.

sCellDeactivationTimer가 만료되는 경우, [[UE]]는 TS 38.133의 최소 요구사항 이내에 비활성화 동작을 수행해야 하며, 활성화된 서빙 셀에 대한 [[CSI_Reporting_Procedure]] 관련 동작은 해당 서빙 셀의 [[PDSCH]] 수신을 위한 SCS 설정에 따른 슬롯 n + m 이후 첫 번째 슬롯에서 적용된다.

## 인과 관계
- [[PDSCH]] depends_on [[SCell_Activation_Deactivation_Timing]] (활성화/비활성화 명령 수신 경로)
- [[HARQ_ACK_Reporting]] depends_on [[SCell_Activation_Deactivation_Timing]] (활성화 타이밍 산출 기준)
- [[CSI_Reporting_Procedure]] depends_on [[SCell_Activation_Deactivation_Timing]] (활성화/비활성화에 따른 보고 시점 결정)

## 관련 개념
- [[PDSCH]] (depends_on)
- [[HARQ_ACK_Reporting]] (depends_on)
- [[CSI_Reporting_Procedure]] (depends_on)
- [[Carrier_Aggregation]] (part_of)

## 스펙 근거
- TS 38.213 §4.3: SCell 활성화/비활성화 타이밍 요구사항 및 예외 조건 정의
- TS 38.211 §4.3: SCS 설정에 따른 슬롯 구조 정의
- TS 38.321: MAC CE 기반 활성화/비활성화 명령 정의
- TS 38.133: 물리 계층 동작 적용을 위한 최소 요구 시간 정의

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) §4.3