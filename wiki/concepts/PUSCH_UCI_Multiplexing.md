# PUSCH_UCI_Multiplexing

## 정의
[[PUSCH_UCI_Multiplexing]]은 [[UE]]가 [[PUSCH]] 전송 자원을 활용하여 [[UCI]]를 다중화하여 전송하는 물리 계층 절차를 의미하며, 여기에는 [[HARQ_ACK]], [[CSI]] 보고 등이 포함된다.

## 요약
[[PUSCH]] 전송 시 [[UCI]]를 다중화하는 것은 상향링크 자원 효율성을 극대화하기 위한 메커니즘이다. [[UE]]는 상위 계층 설정 및 [[DCI]] 지시에 따라 [[HARQ_ACK]] 및 [[CSI]] 보고를 [[PUSCH]]에 매핑하며, 이때 [[UCI]] 비트의 우선순위와 [[PUSCH]]의 가용 자원을 고려하여 전송을 수행한다. 특히 [[Configured_Grant]] 기반 전송이나 반복 전송 시에도 특정 조건에 따라 [[UCI]] 다중화가 적용된다.

## 상세 설명
[[PUSCH_UCI_Multiplexing]]은 다음과 같은 절차와 규칙을 따른다.

1. [[UCI]] 다중화 기본 원리:
   - [[UE]]는 [[PUSCH]] 전송이 예정된 경우, 해당 [[PUSCH]] 자원 내에 [[UCI]]를 다중화할 수 있다.
   - [[UCI]] 비트는 [[PUSCH]]의 [[Rate_Matching]] 및 [[Channel_Coding]] 절차와 연동되어 매핑된다.
   - [[HARQ_ACK]]는 [[PUSCH]] 전송 시 가장 높은 우선순위를 가지며, [[CSI]] 보고는 [[Aperiodic_CSI]] 또는 [[Semi_persistent_CSI]] 설정에 따라 다중화된다.

2. [[Configured_Grant]] 환경에서의 동작:
   - [[PUSCH_Configured_Grant_Operation]]을 수행하는 경우, [[repK-RV]] 파라미터가 설정되어 있으면 반복 전송 시 [[Redundancy_Version]] 패턴이 적용된다.
   - [[SRS_Resource_Set]]과 연관된 전송 기회(Transmission Occasion)에서 [[UCI]] 다중화가 필요한 경우, [[sequenceOffsetforRV]] 등을 통해 [[RV]] 시퀀스가 조정된다.
   - [[PUSCH]] 반복 전송 중 [[DCI_Format_0_1]]을 통해 [[DFI]] 플래그가 '1'로 설정되고 해당 [[HARQ_Process]]에 대한 [[ACK]]가 감지되면, [[UE]]는 해당 전송 블록의 반복을 즉시 종료한다.

3. 자원 가용성 및 제약:
   - [[UE]]는 [[PUSCH]] 전송을 위해 할당된 심볼 수가 전송 지속 시간 [[L]]보다 작을 경우 해당 전송 기회에서 [[PUSCH]]를 전송하지 않는다.
   - [[AvailableSlotCounting]]이 활성화된 경우, [[TDD_UL_DL_Configuration]] 또는 [[SSB]] 위치와 겹치는 심볼은 슬롯 카운트에서 제외된다.

## 인과 관계
- [[PUSCH_UCI_Multiplexing]] depends_on [[UCI_Bit_Generation]] (다중화할 UCI 비트 생성 전제)
- [[PUSCH_UCI_Multiplexing]] affects [[Rate_Matching]] (UCI 다중화에 따른 가용 자원 변화)
- [[PUSCH_UCI_Multiplexing]] depends_on [[PUSCH_Resource_Allocation]] (전송 자원 위치 및 크기 결정)
- [[PUSCH_UCI_Multiplexing]] triggers [[Channel_Coding]] (다중화된 UCI와 데이터의 통합 코딩)

## 관련 개념
- [[UCI_Multiplexing]] (implements)
- [[PUSCH_Configured_Grant_Operation]] (depends_on)
- [[HARQ_ACK_Reporting]] (affects)
- [[CSI_Reporting_Procedure]] (affects)
- [[Rate_Matching]] (depends_on)

## 스펙 근거
- TS 38.214 §6.1.2.3.1: PUSCH repetition Type A with a configured grant 절차 정의
- TS 38.214 §6.1.2.3.2: PUSCH repetition Type B with a configured grant 절차 정의

## 소스
- 3GPP TS 38.214 V16.9.0 (2022-03) "NR; Physical layer procedures for data"