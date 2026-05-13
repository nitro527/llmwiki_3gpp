# PUCCH_Cell_Switching

## 정의
[[PUCCH_Cell_Switching]]은 [[UE]]가 [[PUCCH]] 전송을 수행할 셀을 [[PCell]]과 [[PUCCH-sSCell]] 사이에서 동적으로 또는 반정적으로 전환하는 절차를 의미한다.

## 요약
[[PUCCH_Cell_Switching]]은 [[PUCCH-sSCell]]이 설정되고 활성화된 상태에서 적용된다. [[UE]]는 상위 계층 시그널링을 통한 주기적 패턴([[pucch-sSCellPattern]]) 또는 [[DCI]] 내의 [[PUCCH]] 셀 지시자 필드를 통해 전송 셀을 결정한다. 이 과정에서 [[PUCCH]] 전송 전력은 전환된 셀의 설정에 따라 [[PUCCH_Power_Control]] 절차를 거쳐 재산출된다.

## 상세 설명
[[PUCCH_Cell_Switching]]은 [[PUCCH-sSCell]]이 설정되고 활성화된 경우에 수행된다. 단, [[PCell]]의 [[tdd-UL-DL-ConfigurationCommon]]에 의해 제공되는 기준 [[SCS]] 설정의 심볼을 포함하는 슬롯에서는 적용되지 않는다.

1. 반정적 전환: [[pucch-sSCellPattern]]을 통해 주기적인 셀 전환 패턴이 제공된다. 패턴의 각 비트는 기준 [[SCS]] 슬롯에 대응하며, '0'은 [[PCell]], '1'은 [[PUCCH-sSCell]]을 나타낸다. [[UE]]는 패턴이 지시하는 셀 이외의 셀에서는 [[PUCCH]]를 전송하지 않는다. 슬롯 중첩 발생 시, [[PCell]]의 슬롯이 [[PUCCH-sSCell]]의 여러 슬롯과 겹치면 첫 번째 슬롯을 우선한다.

2. 동적 전환: [[pucch-sSCellDyn]], [[pucch-sSCellDynDCI-1-2]], 또는 [[pucch-sSCellDynDCI-1-3]]이 설정된 경우, [[HARQ-ACK]] 정보를 생성하는 [[DCI]] 포맷 내의 [[PUCCH]] 셀 지시자 필드를 통해 셀을 결정한다. 단, [[SPS]] [[PDSCH]] 수신과 관련된 [[HARQ-ACK]] 전송은 항상 [[PCell]]에서 수행된다.

3. 전력 제어: [[PUCCH-sSCell]]에서 [[PUCCH]] 전송 시, [[PUCCH_Config]] 내의 [[pucch-PowerControl]] 파라미터를 적용한다. 여기에는 [[p0-PUCCH-Value]], [[pucch-PathlossReferenceRS-Id]], 그리고 [[TPC]] 명령을 통한 전력 제어 조정 상태가 포함된다. [[TPC]] 명령은 [[PUCCH-sSCell]] 전송을 위해 다중화된 [[HARQ-ACK]] 관련 [[DCI]] 또는 [[TPC-PUCCH-RNTI]]로 스크램블된 [[DCI]] 포맷 2_2를 통해 제공된다.

## 인과 관계
- [[PUCCH_Cell_Switching]] depends_on [[PUCCH_Power_Control]] (전환된 셀에서의 전력 산출을 위해 필수)
- [[PUCCH_Cell_Switching]] affects [[HARQ_ACK_Reporting]] (전송 셀 결정에 따른 보고 경로 변경)
- [[PUCCH_Cell_Switching]] affects [[SR_Reporting]] (전송 셀 결정에 따른 보고 경로 변경)
- [[PUCCH_Cell_Switching]] affects [[CSI_Reporting_Procedure]] (전송 셀 결정에 따른 보고 경로 변경)

## 관련 개념
- [[PUCCH]] (part_of)
- [[PCell]] (part_of)
- [[DCI]] (triggers)
- [[HARQ_ACK_Reporting]] (affects)
- [[PUCCH_Power_Control]] (implements)

## 스펙 근거
- TS 38.213 §9.A: [[PUCCH_Cell_Switching]]의 전반적인 동작 및 설정 조건 정의
- TS 38.213 §7.2.1: [[PUCCH-sSCell]]에서의 전력 제어 파라미터 적용 규정
- TS 38.212 §5: [[PUCCH]] 셀 지시자 필드 관련 규정
- TS 38.214 §5.2.1.4: [[CSI]] 보고를 위한 [[PUCCH]] 전송 셀 결정

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"