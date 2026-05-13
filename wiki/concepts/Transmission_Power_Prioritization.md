# Transmission_Power_Prioritization

## 정의
다중 채널([[PUSCH]], [[PUCCH]], [[PRACH]], [[SRS]]) 또는 다중 셀/캐리어 환경에서 [[UE]]의 총 전송 전력이 허용된 최대 전력 제한을 초과할 경우, 각 채널에 전력을 할당하기 위해 적용되는 우선순위 결정 절차를 의미한다.

## 요약
[[UE]]는 단일 셀 내 두 개의 상향링크 캐리어, [[Carrier_Aggregation]], 또는 LTM-Config가 설정된 후보 셀 등에서 전송 시, 각 심볼 단위로 총 전송 전력이 최대 허용 전력($P_{CMAX}$)을 초과하지 않도록 제어한다. 전력 제한 상황 발생 시, 스펙에 정의된 우선순위 규칙에 따라 채널별로 전력을 배분하며, 우선순위가 동일한 경우 셀의 종류(PCell 우선)나 캐리어 설정에 따라 전력을 우선 할당한다.

## 상세 설명
[[UE]]는 매 심볼마다 [[PUSCH]], [[PUCCH]], [[PRACH]], [[SRS]] 전송 전력의 선형 합이 해당 주파수 범위의 최대 허용 전력($P_{CMAX}$)을 초과하지 않도록 관리한다. 전력 할당 우선순위는 내림차순으로 다음과 같다.

1. 후보 셀에서의 [[PRACH]] 전송
2. PCell에서의 [[PRACH]] 전송
3. 더 높은 우선순위 인덱스를 가진 [[PUCCH]] 또는 [[PUSCH]] 전송
4. 동일한 우선순위 인덱스를 가진 경우:
   - [[HARQ_ACK_Reporting]] 정보, [[SR]], [[LRR]]을 포함하는 [[PUCCH]] 또는 해당 우선순위 인덱스의 [[HARQ_ACK_Reporting]] 정보를 포함하는 [[PUSCH]]
   - [[CSI]]를 포함하는 [[PUCCH]] 또는 [[PUSCH]]
   - 우선순위 인덱스에 해당하는 [[HARQ_ACK_Reporting]]이나 [[CSI]]가 없는 [[PUSCH]], 또는 Type-2 랜덤 액세스 절차의 PCell [[PUSCH]]
   - prioSCellPRACH-OverSP-PeriodicSRS-r17이 설정된 경우: 비주기적 [[SRS]] 또는 PCell 이외의 서빙 셀에서의 [[PRACH]]
   - 반정적(Semi-persistent) 및/또는 주기적 [[SRS]]
   - 기타: 비주기적 [[SRS]]가 반정적/주기적 [[SRS]]보다 높은 우선순위를 가지며, PCell 이외의 서빙 셀에서의 [[PRACH]]가 포함됨

동일한 우선순위 내에서 [[Carrier_Aggregation]] 환경일 경우, MCG 또는 SCG의 PCell 전송이 SCell 전송보다 우선한다. 두 개의 상향링크 캐리어 환경에서는 [[PUCCH]]가 설정된 캐리어가 우선하며, 둘 다 설정되지 않은 경우 비보조(non-supplementary) 상향링크 캐리어가 우선한다.

## 인과 관계
- [[PUSCH]] depends_on [[Transmission_Power_Prioritization]] (전력 제한 시 전송 전력 할당 우선순위 적용)
- [[PUCCH]] depends_on [[Transmission_Power_Prioritization]] (전력 제한 시 전송 전력 할당 우선순위 적용)
- [[PRACH]] depends_on [[Transmission_Power_Prioritization]] (전력 제한 시 전송 전력 할당 우선순위 적용)
- [[SRS]] depends_on [[Transmission_Power_Prioritization]] (전력 제한 시 전송 전력 할당 우선순위 적용)
- [[Carrier_Aggregation]] depends_on [[Transmission_Power_Prioritization]] (다중 셀 환경에서의 전력 공유 및 우선순위 결정)

## 관련 개념
- [[PUSCH_Power_Control]] (implements)
- [[PUCCH_Power_Control]] (implements)
- [[SRS_Power_Control]] (implements)
- [[PRACH_Power_Control]] (implements)
- [[Carrier_Aggregation]] (affects)

## 스펙 근거
- TS 38.213 §7.5: 전력 제한 상황에서의 우선순위 결정 규칙 및 전력 할당 절차 정의
- TS 38.101-1/2: FR1 및 FR2에서의 $P_{CMAX}$ 정의

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) §7.5