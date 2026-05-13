# PUCCH_Repetition

## 정의
[[PUCCH]] 반복 전송은 [[HARQ-ACK]], [[SR]], 또는 [[CSI]]와 같은 상향링크 제어 정보를 포함하는 [[PUCCH]] 전송을 다수의 슬롯에 걸쳐 반복하여 전송함으로써 수신 신뢰도를 향상시키는 물리 계층 절차를 의미한다.

## 요약
[[PUCCH]] 반복 전송은 전용 [[PUCCH]] 자원 설정 여부에 따라 결정되며, 다수의 슬롯에 걸쳐 동일한 UCI를 반복 전송한다. 주파수 호핑, 공간 필터 적용, 그리고 전송 우선순위 규칙에 따라 동작하며, [[PUSCH]]와의 충돌 시 우선순위가 높은 [[PUCCH]]가 전송된다.

## 상세 설명
[[PUCCH]] 반복 전송은 TS 38.213 §9.2.6에 따라 다음과 같이 수행된다.

1. 반복 횟수 결정:
   - 전용 [[PUCCH]] 자원 설정이 없는 경우, numberOfMsg4HARQ-ACK-Repetitions 파라미터에 의해 반복 횟수가 결정된다.
   - 전용 [[PUCCH]] 자원이 설정된 경우, [[DCI]]에 의해 지시된 pucch-RepetitionNrofSlots 또는 nrofSlots 파라미터를 사용한다.

2. 전송 파라미터 유지:
   - 반복되는 각 [[PUCCH]] 전송은 동일한 심볼 개수(nrofSymbols)와 시작 심볼 인덱스를 가진다.
   - subslotLengthForPUCCH가 설정된 경우, 슬롯은 해당 파라미터에 정의된 심볼 수를 포함한다.

3. 주파수 호핑:
   - interslotFrequencyHopping 설정에 따라 슬롯 간 주파수 호핑을 수행한다.
   - pucch-DMRS-Bundling이 비활성화된 경우, 슬롯 단위로 호핑하며 짝수 슬롯은 startingPRB, 홀수 슬롯은 secondHopPRB를 사용한다.
   - pucch-DMRS-Bundling이 활성화된 경우, pucch-FrequencyHoppingInterval 또는 pucch-TimeDomainWindowLength에 정의된 간격마다 호핑을 수행한다.

4. 공간 필터 및 다중 패널 동작:
   - multipanelSFN-Scheme이 설정되고 applyIndicatedTCI-State가 'both'인 경우, 첫 번째와 두 번째 공간 도메인 필터를 동시에 사용하여 반복 전송한다.
   - 다중 패널 또는 다중 전력 제어 파라미터 세트가 설정된 경우, mappingPattern에 따라 cyclicMapping 또는 sequentialMapping 방식으로 공간 설정이나 전력 제어 파라미터를 교차 적용한다.

5. 충돌 및 우선순위 처리:
   - [[PUSCH]] 반복 전송(Type A/B)과 충돌 시, [[PUCCH]] 전송이 우선하며 [[PUSCH]]는 해당 슬롯에서 전송되지 않는다.
   - 다수의 [[PUCCH]]가 충돌할 경우, HARQ-ACK > SR > CSI(높은 우선순위) > CSI(낮은 우선순위) 순으로 우선순위를 결정하여 가장 높은 우선순위의 [[PUCCH]]를 전송한다.

## 인과 관계
- [[PUCCH_Repetition]] depends_on [[PUCCH_Resource_Selection]] (반복 전송을 위한 자원 할당 전제)
- [[PUCCH_Repetition]] affects [[PUCCH_Power_Control]] (반복 전송 시 전력 제어 파라미터 교차 적용)
- [[PUCCH_Repetition]] depends_on [[UCI_Multiplexing]] (충돌 시 우선순위 기반 다중화 결정)
- [[PUCCH_Repetition]] affects [[PUSCH_Transmission_Procedure]] (충돌 시 PUSCH 전송 억제)

## 관련 개념
- [[PUCCH]] (part_of)
- [[HARQ_ACK_Reporting]] (implements)
- [[SR_Reporting]] (implements)
- [[CSI_Reporting_Procedure]] (implements)
- [[PUCCH_Spatial_Setting]] (affects)
- [[DMRS_Bundling_Procedure]] (affects)

## 스펙 근거
- TS 38.213 §9.2.6: PUCCH repetition procedure 정의 및 동작 절차
- TS 38.213 §9.2.1: 주파수 호핑 및 자원 할당 규칙
- TS 38.213 §9.2.5: PUCCH/PUSCH 충돌 및 UCI 다중화 우선순위 규칙

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §9.2.6