# PDSCH_TCI_State_Management

## 정의
[[PDSCH]] 수신을 위한 [[TCI]] 상태 지시, [[SFN]] 스킴 설정 및 [[QCL]] 가정 관리를 수행하는 절차를 의미한다.

## 요약
[[PDSCH]] 수신 시 [[UE]]는 [[DCI]]를 통해 지시된 [[TCI]] 상태를 기반으로 [[DMRS]] 포트에 대한 [[QCL]] 가정을 설정한다. 다중 [[TCI]] 상태 지시, [[SFN]] 스킴(Scheme A/B) 설정, 그리고 [[Multi-TRP]] 환경에서의 [[CORESET]] 풀 인덱스 기반 동작을 포함한다.

## 상세 설명
[[PDSCH]] 수신을 위한 [[TCI]] 상태 관리는 [[TS 38.214]] §5.1에 정의된 절차를 따른다.

1. 기본 [[QCL]] 가정:
   - [[SI-RNTI]], [[P-RNTI]], [[MCCH-RNTI]], [[G-RNTI]] 등으로 스케줄링된 [[PDSCH]]의 경우, [[DMRS]] 포트는 연관된 [[SSB]] 또는 [[CSI-RS]]와 [[QCL]] 관계(Doppler shift, Doppler spread, average delay, delay spread, spatial RX parameters)를 가진다.
   - [[RA-RNTI]] 또는 [[MSGB-RNTI]]로 스케줄링된 경우, [[RACH]] 절차에 사용된 [[SSB]] 또는 [[CSI-RS]] 자원과 [[QCL]] 가정을 공유한다.

2. [[TCI]] 상태 지시 및 [[SFN]] 스킴:
   - [[DCI]] 내 'Transmission Configuration Indication' 필드를 통해 하나 또는 두 개의 [[TCI]] 상태가 지시된다.
   - [[sfnSchemePDSCH]]가 'sfnSchemeA' 또는 'sfnSchemeB'로 설정된 경우, [[UE]]는 지시된 [[TCI]] 상태를 기반으로 [[QCL]] 가정을 설정한다.
   - [[sfnSchemePDSCH]]와 [[sfnSchemePDCCH]]가 동시에 설정된 경우, 동일한 스킴을 사용해야 한다.

3. [[Multi-TRP]] 및 [[CORESET]] 풀 인덱스:
   - [[PDCCH]]가 서로 다른 [[coresetPoolIndex]] 값을 가진 [[CORESET]]에 연관된 경우, [[UE]]는 시간/주파수 영역에서 중첩되거나 중첩되지 않는 [[PDSCH]] 수신을 기대할 수 있다.
   - 서로 다른 [[coresetPoolIndex]]를 가진 [[PDCCH]]가 스케줄링하는 경우, [[outOfOrderOperationDL-r16]] 기능이 보고되면 [[HARQ]] 프로세스 간의 비순차적 동작이 허용된다.

4. 반복 전송 및 [[TCI]] 상태:
   - [[repetitionScheme]]이 설정된 경우, 각 [[TCI]] 상태는 주파수 영역(fdmSchemeA/B) 또는 시간 영역(tdmSchemeA)의 전송 기회와 연관된다.
   - [[repetitionNumber]]가 설정된 경우, 다중 슬롯에 걸쳐 [[TCI]] 상태가 적용된다.

## 인과 관계
- [[PDSCH]] depends_on [[TCI]] (수신을 위한 QCL 가정 설정)
- [[PDSCH]] depends_on [[DCI]] (TCI 상태 지시 및 스케줄링 정보 수신)
- [[PDSCH]] depends_on [[QCL]] (DMRS 포트의 수신 파라미터 결정)
- [[PDSCH]] depends_on [[CORESET]] (coresetPoolIndex를 통한 다중 TRP 동작 제어)
- [[PDSCH]] depends_on [[SFN]] (SFN 스킴에 따른 TCI 상태 적용)

## 관련 개념
- [[PDSCH]] (part_of)
- [[TCI]] (implements)
- [[QCL]] (implements)
- [[DCI]] (triggers)
- [[CORESET]] (affects)
- [[SFN]] (affects)

## 스펙 근거
- TS 38.214 §5.1: PDSCH 수신 절차 및 TCI 상태 관리
- TS 38.214 §5.1.5: QCL 가정 및 TCI 상태 적용
- TS 38.214 §5.1.6: SFN 스킴 및 다중 TCI 상태 동작

## 소스
- 3GPP TS 38.214 v17.9.0 (Release 17)