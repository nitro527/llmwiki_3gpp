# DAPS_Handover_Operation

## 정의
DAPS(Dual Active Protocol Stack) 핸드오버는 [[UE]]가 소스 셀 그룹(Source MCG)과 타겟 셀 그룹(Target MCG)에 동시에 연결된 상태를 유지하며 핸드오버를 수행하는 절차를 의미한다.

## 요약
DAPS 핸드오버 중인 [[UE]]는 소스 셀과 타겟 셀 간의 독립적인 전력 제어 및 전송 우선순위 결정을 수행한다. 주파수 대역이 동일하거나 다른 경우에 따라 전송 충돌 해결 절차가 정의되며, 특정 조건 하에서 소스 셀로의 전송을 취소하거나 타겟 셀로의 전송을 우선시한다.

## 상세 설명
DAPS 핸드오버 시 [[UE]]는 소스 셀 그룹과 타겟 셀 그룹에 대해 독립적으로 전력 제어를 수행한다.

### 전력 제어 및 공유
- FR1 및 FR2 조합에 따라 각 셀 그룹별로 독립적인 전력 제어가 적용된다.
- 동일한 FR1 내에서 소스 및 타겟 셀 그룹이 구성된 경우, `p-DAPS-Target` 및 `p-DAPS-Source` 파라미터를 통해 최대 전력을 설정하며, `uplinkPowerSharingDAPS-Mode`에 따라 전력 공유 모드(Semi-static-mode1, Semi-static-mode2, Dynamic)를 결정한다.
- 각 모드에 따른 전력 결정은 [[Dual_Connectivity_Power_Sharing]]의 절차를 준수한다.

### 전송 충돌 해결 및 우선순위
- 인터-주파수(Inter-frequency) DAPS 핸드오버 시, `interFreqUL-TransCancellationDAPS-r16` 지원 여부와 전력 공유 능력에 따라 충돌 시 타겟 셀 전송을 우선하고 소스 셀 전송을 취소한다.
- 인트라-주파수(Intra-frequency) DAPS 핸드오버 시, 시간 자원이 중첩되면 항상 타겟 셀 전송을 우선하고 소스 셀 전송을 취소한다.
- 소스 셀 전송 취소 예외 조건:
  - 타겟 셀의 [[DCI]] 수신 후 [[PUSCH]] 준비 시간($N_2$) 이내인 경우.
  - 타겟 셀의 [[Random_Access_Response]] 수신 후 특정 시간 이내인 경우.
- 동일 주파수 대역 내에서 [[PRACH]]와 [[PUSCH]]/[[PUCCH]]/[[SRS]] 간의 시간적 간격이 특정 심볼 수 미만일 경우 전송이 제한된다.

### PDCCH 모니터링
- 소스 및 타겟 셀 그룹 모두에서 [[PDCCH]]를 모니터링할 때, 각 셀 그룹의 후보 수와 CCE 총합은 [[PDCCH_Monitoring_Capability]]에서 정의된 슬롯당 최대치를 초과할 수 없다.

## 인과 관계
- [[DAPS_Handover_Operation]] depends_on [[Dual_Connectivity_Power_Sharing]] (전력 공유 모드 결정 시)
- [[DAPS_Handover_Operation]] affects [[PUSCH_Power_Control]] (셀 그룹별 독립적 전력 제어 적용)
- [[DAPS_Handover_Operation]] triggers [[Transmission_Power_Prioritization]] (전송 충돌 시 우선순위 결정)
- [[DAPS_Handover_Operation]] depends_on [[PDCCH_Monitoring_Capability]] (PDCCH 후보 수 제한 준수)

## 관련 개념
- [[Dual_Connectivity_Power_Sharing]] (implements)
- [[PUSCH_Power_Control]] (affects)
- [[Transmission_Power_Prioritization]] (triggers)
- [[PDCCH_Monitoring_Capability]] (depends_on)
- [[PRACH]] (part_of)
- [[PUSCH]] (part_of)
- [[PUCCH]] (part_of)
- [[SRS]] (part_of)

## 스펙 근거
- TS 38.213 §15: DAPS 핸드오버 시 전력 제어, 전송 취소 절차 및 PDCCH 모니터링 제약 사항 정의.
- TS 38.214 §6.1.2: PUSCH 준비 시간($N_2$) 및 처리 능력 관련 정의.
- TS 38.133 §6.1.3.2: 인트라-주파수 DAPS 핸드오버 동작 정의.

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) §15