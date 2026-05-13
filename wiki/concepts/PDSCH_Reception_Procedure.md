# PDSCH_Reception_Procedure

## 정의
[[PDSCH]] 수신 절차는 [[UE]]가 [[PDCCH]]를 통해 수신된 [[DCI]] 정보를 바탕으로 하향링크 데이터를 복호화하고, [[HARQ]] 프로세스를 관리하며, 다중 [[PDSCH]] 수신 시 발생하는 시간/주파수 자원 충돌을 해결하는 물리 계층 동작을 의미한다.

## 요약
[[UE]]는 설정된 [[DCI]] 포맷(1_0, 1_1, 1_2, 1_3, 4_0, 4_1, 4_2)을 감지하여 [[PDSCH]]를 복호화한다. [[HARQ]] 프로세스 ID는 [[DCI]]에 의해 지시되며, 다중 [[PDSCH]] 스케줄링 시 순차적으로 증가한다. [[UE]]는 [[TDD]] 설정이나 [[HARQ]] 피드백 상태에 따라 수신 여부를 결정하며, [[CORESETPoolIndex]] 및 [[TCI_State]] 설정에 따라 다중 [[PDSCH]] 수신 및 [[QCL]] 가정을 수행한다.

## 상세 설명
1. **HARQ 프로세스 관리**: [[UE]]는 셀당 최대 16개(능력에 따라 32개)의 [[HARQ]] 프로세스를 지원한다. [[nrofHARQ-ProcessesForPDSCH]] 파라미터가 설정되지 않은 경우 기본값 8을 사용한다. [[DCI]]가 다중 [[PDSCH]]를 스케줄링할 경우, 첫 번째 [[PDSCH]]의 [[HARQ]] 프로세스 ID를 기준으로 이후 [[PDSCH]]에 대해 1씩 증가(modulo 연산 적용)시킨다. 단, [[UL]] 심볼과 충돌하는 경우 해당 [[PDSCH]]는 수신하지 않으며 [[HARQ]] 프로세스 ID도 증가시키지 않는다.

2. **수신 제약 및 충돌 해결**:
   - [[HARQ]] 피드백이 활성화된 경우, 해당 [[HARQ]] 프로세스에 대한 [[HARQ-ACK]] 전송이 완료될 때까지 동일한 프로세스에 대한 새로운 [[PDSCH]] 수신을 기대하지 않는다.
   - [[PDCCH]]가 스케줄링하는 [[PDSCH]]와 [[PDCCH]] 없이 수신되는 [[PDSCH]] 간의 충돌 시, [[PDCCH]]가 [[PDSCH]] 시작 최소 14심볼 이전에 종료되면 [[PDCCH]]로 스케줄링된 [[PDSCH]]를 우선 복호화한다.
   - [[CORESETPoolIndex]]가 서로 다른 [[PDCCH]]로 스케줄링된 경우, [[UE]]는 시간/주파수 영역에서 중첩된 [[PDSCH]] 수신을 수행할 수 있다.

3. **반복 전송 및 TCI 설정**:
   - [[repetitionScheme]]이 설정된 경우, 'tdmSchemeA', 'fdmSchemeA', 'fdmSchemeB'에 따라 다중 전송 기회(transmission occasion)를 수신한다.
   - [[sfnSchemePDSCH]]가 설정된 경우, [[SFN]] 동작에 따라 [[QCL]] 가정을 적용하여 [[PDSCH]]를 수신한다.

4. **PDSCH 없는 PDCCH 수신**: [[CS-RNTI]] 또는 [[G-CS-RNTI]]가 설정된 경우, [[UE]]는 [[PDCCH]] 없이 상위 계층 설정에 따라 [[PDSCH]]를 수신한다. 이때 [[sps-ConfigIndex]]가 낮은 순서대로 우선순위를 결정하여 충돌을 해결한다.

## 인과 관계
- [[PDCCH]] triggers [[PDSCH_Reception_Procedure]] (DCI를 통한 PDSCH 스케줄링)
- [[PDSCH_Reception_Procedure]] implements [[HARQ]] (HARQ 프로세스 ID 할당 및 관리)
- [[PDSCH_Reception_Procedure]] depends_on [[PDCCH_Validation]] (DCI 포맷 및 CRC 검증)
- [[PDSCH_Reception_Procedure]] affects [[HARQ_ACK_Reporting]] (수신된 PDSCH에 대한 피드백 생성)
- [[PDSCH_Reception_Procedure]] depends_on [[Slot_Format_Configuration]] (UL 심볼과의 충돌 여부 판단)
- [[PDSCH_Reception_Procedure]] depends_on [[PDSCH_TCI_State_Management]] (QCL 가정 적용)

## 관련 개념
- [[PDSCH]] (part_of)
- [[PDCCH]] (affects)
- [[HARQ]] (implements)
- [[TCI_State]] (depends_on)
- [[CORESET]] (depends_on)
- [[Slot_Format_Indicator]] (depends_on)

## 스펙 근거
- TS 38.214 §5.1: UE procedure for receiving the physical downlink shared channel
- TS 38.213 §9.2.3: HARQ-ACK timing
- TS 38.213 §9.2.5.4: HARQ-ACK deferral

## 소스
- 3GPP TS 38.214 V17.9.0 (2024-03)