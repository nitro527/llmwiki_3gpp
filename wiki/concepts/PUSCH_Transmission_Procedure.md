# PUSCH_Transmission_Procedure

## 정의
[[PUSCH]] 전송 절차는 [[UE]]가 상향링크 데이터를 전송하기 위해 [[DCI]]를 통한 동적 스케줄링 또는 상위 계층 파라미터에 의해 설정된 Configured Grant를 사용하는 메커니즘을 의미하며, 특히 RRC_INACTIVE 상태, LTM(L1-L2 Triggered Mobility), RACH-less 핸드오버 환경에서의 동작을 포함한다.

## 요약
[[PUSCH]] 전송은 동적 그랜트 기반 전송과 Configured Grant(Type 1 및 Type 2) 기반 전송으로 구분된다. RRC_INACTIVE 상태나 RACH-less 핸드오버 시, [[UE]]는 미리 설정된 자원과 [[SSB]] 인덱스 간의 매핑 관계를 통해 [[PUSCH]] 전송을 수행한다. 전송 전력, 공간 필터, [[HARQ]] 프로세스 ID 결정은 각 전송 모드와 설정된 TCI 상태에 따라 결정된다.

## 상세 설명
### Configured Grant Type 1 기반 전송
- RRC_INACTIVE 상태 또는 RACH-less 핸드오버 시, [[UE]]는 [[ConfiguredGrantConfig]]를 통해 하나 이상의 설정을 제공받는다.
- [[SSB]] 인덱스와 유효한 [[PUSCH]] 자원(PUSCH occasion) 간의 매핑은 [[sdt-SSB-Subset]] 또는 [[ssb-PositionsInBurst]]를 기반으로 결정된다.
- [[PUSCH]] occasion은 시간 및 주파수 자원으로 정의되며, [[DMRS]] 자원과 연관된다.
- 반복 전송(Repetition)이 설정된 경우, 모든 반복 전송은 동일한 [[SSB]] 인덱스에 매핑된다.
- [[PUSCH]] occasion의 유효성은 [[PRACH]] occasion과의 중첩 여부 및 TDD UL-DL 설정에 따라 결정된다.
- 전송 전력은 [[Pathloss_Estimation]]을 통해 결정되며, 연관된 [[SSB]] 또는 TCI 상태의 RS를 참조한다.

### 동적 그랜트 기반 전송
- [[PDCCH]]를 통해 수신된 [[DCI]] format 0_0, 0_1, 0_2, 0_3에 의해 스케줄링된다.
- [[HARQ]] 프로세스 ID는 [[DCI]]에 의해 지시되거나, 다중 [[PUSCH]] 스케줄링 시 순차적으로 증가한다.
- [[TCI_State]] 또는 [[TCI_UL_State]]가 설정된 경우, [[UE]]는 지시된 RS를 기반으로 상향링크 공간 필터를 결정한다.
- [[PDCCH]] 수신과 [[PUSCH]] 전송 간의 타이밍 및 [[Uplink_Cancellation_Indication]]에 의한 전송 취소 동작이 적용될 수 있다.

### RACH-less LTM 및 핸드오버 특수 동작
- LTM 셀 스위치 명령 MAC CE 수신 시, [[UE]]는 지시된 TCI 상태와 연관된 RS를 사용하여 [[PUSCH]] 전송을 수행한다.
- RACH-less 핸드오버 시, [[UE]]는 [[rrc-SSB-Subset]]을 사용하여 [[SSB]] 인덱스를 매핑하며, 전송 전력은 [[pathlossReferenceRS-Id]]를 참조한다.

## 인과 관계
- [[PUSCH]] depends_on [[DCI_Field_Mapping]] (동적 스케줄링 시 전송 파라미터 결정)
- [[PUSCH]] depends_on [[PUSCH_Configured_Grant_Operation]] (Configured Grant 기반 전송 시 자원 설정)
- [[PUSCH]] depends_on [[PUSCH_Power_Control]] (전송 전력 결정)
- [[PUSCH]] depends_on [[Timing_Advance_Adjustment]] (상향링크 동기화)
- [[PUSCH]] affects [[HARQ_ACK_Reporting]] (데이터 전송에 따른 피드백 수신)
- [[PUSCH]] depends_on [[DMRS_Resource_Mapping]] (채널 추정을 위한 참조 신호 매핑)

## 관련 개념
- [[PUSCH_Resource_Allocation]] (depends_on)
- [[PUSCH_Power_Control]] (depends_on)
- [[HARQ_ACK_Reporting]] (affects)
- [[DMRS_Resource_Mapping]] (depends_on)
- [[Timing_Advance_Adjustment]] (depends_on)
- [[PUSCH_Configured_Grant_Operation]] (depends_on)

## 스펙 근거
- TS 38.213 §19.1: Configured-grant based PUSCH transmission
- TS 38.213 §19.2: Random-access based PUSCH transmission
- TS 38.213 §21.1: Configured-grant PUSCH transmission in RACH-less LTM cell switch
- TS 38.213 §22.1: Configured-grant PUSCH transmission in RACH-less handover
- TS 38.214 §6.1: UE procedure for transmitting the physical uplink shared channel

## 소스
- 3GPP TS 38.213 (v18.0.0)
- 3GPP TS 38.214 (v18.0.0)