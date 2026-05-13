# UCI_Multiplexing

## 정의
[[UCI_Multiplexing]]은 [[UE]]가 상향링크 제어 정보([[UCI]])인 [[HARQ-ACK]], [[CSI]], [[SR]]을 [[PUSCH]] 전송 시 데이터와 함께 다중화하거나, 다중 [[PUCCH]]/[[PUSCH]] 전송 간의 시간적 충돌이 발생할 때 우선순위 규칙에 따라 전송을 제어하는 절차를 의미합니다.

## 요약
[[UCI_Multiplexing]]은 상향링크 자원 효율성을 극대화하기 위해 데이터와 제어 정보를 동일한 [[PUSCH]] 자원에 매핑하거나, 서로 다른 우선순위([[Priority_Index]])를 가진 채널 간의 충돌을 해결합니다. TS 38.212 및 TS 38.213에 정의된 절차에 따라, [[UCI]]의 종류와 비트 수, [[PUSCH]]의 [[IMCS]] 값, 그리고 채널 간 우선순위에 따라 자원 할당 및 드롭(drop) 여부가 결정됩니다.

## 상세 설명
### PUSCH 상의 UCI 다중화 (TS 38.212 §6.2.7)
[[PUSCH]] 전송 시 [[UCI]]를 다중화하는 과정은 다음과 같은 단계로 수행됩니다.
1. 다중 [[UL-SCH]] 전송 블록이 존재하는 경우, 가장 높은 [[IMCS]] 값을 가진 전송 블록에 [[UCI]]를 다중화합니다. 동일한 [[IMCS]]인 경우 첫 번째 전송 블록을 사용합니다.
2. [[HARQ-ACK]], [[CSI_Part_1]], [[CSI_Part_2]]의 비트 수에 따라 자원 요소([[RE]])를 계산하고, [[DMRS]] 심볼을 제외한 가용 자원에 매핑합니다.
3. 주파수 호핑([[PUSCH_Frequency_Hopping]]) 설정 여부에 따라 [[RE]] 집합을 정의하고, 단계별로 [[UCI]] 비트를 데이터 비트와 결합합니다.
   - Step 1: [[HARQ-ACK]] (2비트 이하) 및 [[CG-UCI]] 처리
   - Step 2: [[HARQ-ACK]] (2비트 초과) 처리
   - Step 3: [[CSI]] 처리
   - Step 4: [[UL-SCH]] 데이터 매핑
   - Step 5: [[HARQ-ACK]] (2비트 이하) 최종 매핑
   - Step 6: 최종 다중화된 비트 시퀀스 생성

### 우선순위 기반 충돌 해결 (TS 38.213 §9)
서로 다른 우선순위([[Priority_Index]] 0 또는 1)를 가진 채널이 시간적으로 겹칠 경우 다음 규칙을 적용합니다.
1. 동일 우선순위 내 충돌: [[PUCCH_Repetition]] 및 [[PUCCH_Format_Processing]] 규칙에 따라 해결합니다.
2. 서로 다른 우선순위 간 충돌:
   - [[uci-MuxWithDiffPrio]]가 설정된 경우, 높은 우선순위의 채널에 낮은 우선순위의 [[UCI]]를 다중화하거나, 낮은 우선순위 채널을 드롭합니다.
   - [[HARQ-ACK]] 정보가 포함된 경우, 높은 우선순위 채널을 우선적으로 전송하고 낮은 우선순위 채널은 취소합니다.
   - [[SR]] 또는 [[CSI]]는 낮은 우선순위 채널에서 드롭될 수 있습니다.

## 인과 관계
- [[UCI_Multiplexing]] depends_on [[PUSCH_Resource_Mapping]] (UCI 매핑을 위한 자원 위치 파악)
- [[UCI_Multiplexing]] affects [[PUSCH_Modulation]] (UCI 다중화에 따른 변조 심볼 구성 변경)
- [[UCI_Multiplexing]] depends_on [[HARQ_ACK_Codebook_Determination]] (다중화할 HARQ-ACK 비트 결정)
- [[UCI_Multiplexing]] triggers [[Transmission_Power_Prioritization]] (우선순위 결정에 따른 전력 제어)

## 관련 개념
- [[PUSCH]] (part_of)
- [[PUCCH]] (part_of)
- [[HARQ_ACK_Reporting]] (depends_on)
- [[CSI_Reporting_Procedure]] (depends_on)
- [[SR_Reporting]] (depends_on)
- [[Priority_Index]] (affects)

## 스펙 근거
- TS 38.212 §6.2.7: Data and control multiplexing 절차 정의
- TS 38.213 §9: UE procedure for reporting control information 및 우선순위 충돌 해결 규칙

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03)
- 3GPP TS 38.213 V18.0.0 (2024-03)