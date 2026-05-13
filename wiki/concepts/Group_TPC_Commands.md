# Group_TPC_Commands

## 정의
Group_TPC_Commands는 [[DCI]] format 2_2를 사용하여 다수의 [[UE]]에 대해 [[PUCCH]] 또는 [[PUSCH]] 전송 전력을 동시에 제어하기 위한 메커니즘입니다.

## 요약
Group_TPC_Commands는 [[PDCCH]]를 통해 전송되는 DCI format 2_2를 활용하여, 개별 UE의 전력 제어 루프를 효율적으로 업데이트합니다. UE는 상위 계층 설정을 통해 TPC-PUCCH-RNTI 또는 TPC-PUSCH-RNTI를 할당받고, 특정 [[CORESET]] 및 [[Search_Space_Configuration]] 내에서 해당 DCI를 모니터링합니다. 각 DCI 필드는 2비트의 TPC 커맨드로 구성되며, 특정 인덱스를 통해 타겟 셀 및 캐리어의 전력 조정 상태를 제어합니다.

## 상세 설명
Group_TPC_Commands는 TS 38.213 §11.3에 따라 다음과 같이 동작합니다.

### PUCCH 전력 제어
UE는 PUCCH 전송을 위해 다음 정보를 제공받습니다.
- tpc-PUCCH-RNTI: DCI format 2_2의 [[CRC]]를 스크램블링하는 RNTI입니다.
- TPC 커맨드 필드: DCI format 2_2 내의 2비트 필드로, TS 38.213 §7.2.1에 정의된 값으로 매핑됩니다.
- 인덱스 정보: PCell, PUCCH-sSCell, PUCCH-SCell 등 각 셀 그룹 내의 TPC 커맨드 위치를 지정하는 인덱스(tpc-IndexPCell, tpc-IndexPUCCH-sScell, tpc-IndexPUCCH-Scell 등)가 제공됩니다.
- 폐루프 인덱스: twoDifferentTPC-Loop-PUCCH 및 twoPUCCH-PC-AdjustmentStates가 설정된 경우, DCI format 2_2에 추가된 1비트 필드를 통해 두 개의 PUCCH 전력 제어 조정 상태 중 하나를 선택합니다.

### PUSCH 전력 제어
UE는 PUSCH 전송을 위해 다음 정보를 제공받습니다.
- tpc-PUSCH-RNTI: DCI format 2_2의 CRC를 스크램블링하는 RNTI입니다.
- TPC 커맨드 필드: DCI format 2_2 내의 2비트 필드로, TS 38.213 §7.1.1에 정의된 값으로 매핑됩니다.
- 인덱스 정보: tpc-Index 및 tpc-IndexSUL을 통해 업링크 캐리어 및 보조 업링크 캐리어의 TPC 커맨드 위치를 지정합니다.
- 타겟 셀: targetCell 파라미터를 통해 제어 대상 셀을 지정하며, 미제공 시 DCI를 수신한 셀이 대상이 됩니다.
- 폐루프 인덱스: twoDifferentTPC-Loop-PUSCH 및 twoPUSCH-PC-AdjustmentStates가 설정된 경우, DCI format 2_2에 추가된 1비트 필드를 통해 두 개의 PUSCH 전력 제어 조정 상태 중 하나를 선택합니다.

## 인과 관계
- [[DCI]] depends_on [[PDCCH_Monitoring_Procedures]] (DCI format 2_2 수신을 위한 모니터링 절차)
- [[Group_TPC_Commands]] affects [[PUCCH_Power_Control]] (PUCCH 전력 제어 루프 업데이트)
- [[Group_TPC_Commands]] affects [[PUSCH_Power_Control]] (PUSCH 전력 제어 루프 업데이트)

## 관련 개념
- [[PUCCH_Power_Control]] (affects)
- [[PUSCH_Power_Control]] (affects)
- [[PDCCH]] (implements)
- [[DCI]] (implements)

## 스펙 근거
- TS 38.213 §11.3: Group TPC commands for PUCCH/PUSCH 동작 정의
- TS 38.213 §7.1.1: PUSCH 전력 제어 커맨드 매핑
- TS 38.213 §7.2.1: PUCCH 전력 제어 커맨드 매핑
- TS 38.213 §10.1: PDCCH 모니터링 및 DCI 수신 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"