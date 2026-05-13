# L1_L2_Triggered_Mobility

## 정의
L1/L2 Triggered Mobility(LTM)는 [[PDCCH]]를 통한 MAC CE 지시를 기반으로, RRC 재설정 절차 없이 후보 셀(Candidate Cell)로의 신속한 셀 전환을 수행하는 이동성 관리 절차를 의미한다.

## 요약
LTM은 후보 셀에 대한 [[SS_PBCH_Block_Generation]] 측정 및 동기화를 기반으로 하며, MAC CE를 통해 TCI 상태를 활성화하고 셀 전환을 명령한다. RACH-less 또는 RACH-based 방식을 통해 셀 전환이 이루어지며, 타이밍 어드밴스(TA) 적용 및 빔 관리를 포함한다.

## 상세 설명
LTM 절차는 다음과 같은 단계로 구성된다.

1. 후보 셀 설정 및 측정:
   네트워크는 LTM-Config를 통해 UE에게 후보 셀 목록과 각 셀의 SS/PBCH 블록을 제공한다. UE는 이를 바탕으로 동기화를 수행하고 L1-RSRP를 측정하여 ltm-CSI-ReportConfigToAddModList에 따라 보고한다.

2. TCI 상태 활성화 및 지시:
   Candidate Cell TCI States Activation/Deactivation MAC CE를 통해 후보 셀의 SS/PBCH 블록 또는 TRS와 연관된 TCI 상태를 활성화한다. 이후 LTM Cell Switch Command MAC CE가 수신되면, 활성화된 TCI 상태 중 하나가 지시되거나, MAC CE 내에서 직접 TCI 상태가 활성화 및 지시된다. 지시되지 않은 활성화된 TCI 상태는 자동으로 비활성화된다.

3. 셀 전환 및 타이밍 어드밴스:
   서빙 셀과 후보 셀의 ltm-UE-MeasuredTA-ID가 동일한 경우, UE는 셀 전환 명령 수신 후 후보 셀에서의 첫 번째 전송 시점에 적절한 TA를 적용한다.

4. RACH-based 및 RACH-less 전환:
   - RACH-based: [[PRACH]] 전송을 포함하며, 랜덤 액세스 절차 완료 후 후보 셀의 TCI 상태를 적용한다.
   - RACH-less: 별도의 랜덤 액세스 절차 없이 셀 전환 명령 직후 후보 셀의 TCI 상태를 적용한다.
   - UE는 후보 셀에 대한 PRACH 전송 파라미터를 EarlyUL-SyncConfig를 통해 제공받으며, 서빙 셀에서 수신한 PDCCH order에 의해 트리거된다. 서빙 셀과 후보 셀 간의 전송 충돌 발생 시, 특정 조건에 따라 서빙 셀 전송을 드롭하거나 후보 셀의 PRACH 전송에 전력 우선순위를 부여한다.

5. TCI 상태 적용 시점:
   UE는 MAC CE를 포함하는 PDSCH에 대한 HARQ-ACK 정보가 포함된 PUCCH 또는 PUSCH의 마지막 심볼 이후 특정 시간 내에 TCI 상태를 적용해야 한다.

## 인과 관계
- [[PDCCH]] triggers [[L1_L2_Triggered_Mobility]] (PDCCH order를 통한 PRACH 전송 트리거)
- [[L1_L2_Triggered_Mobility]] implements [[Timing_Advance_Adjustment]] (후보 셀 전환 시 TA 적용)
- [[L1_L2_Triggered_Mobility]] depends_on [[SS_PBCH_Block_Generation]] (후보 셀 동기화 및 측정 전제)
- [[L1_L2_Triggered_Mobility]] depends_on [[PDSCH_TCI_State_Management]] (TCI 상태 활성화 및 지시)
- [[L1_L2_Triggered_Mobility]] affects [[PRACH]] (후보 셀에서의 PRACH 전송 제어)

## 관련 개념
- [[PRACH]] (implements)
- [[PDCCH]] (triggers)
- [[SS_PBCH_Block_Generation]] (depends_on)
- [[Timing_Advance_Adjustment]] (implements)
- [[PDSCH_TCI_State_Management]] (depends_on)

## 스펙 근거
- TS 38.213 §21: LTM 절차, TCI 상태 활성화/지시, TA 적용, RACH-based/RACH-less 셀 전환 및 PRACH 전송 충돌 처리 규정.

## 소스
- 3GPP TS 38.213 v18.0.0 (2024-03) §21