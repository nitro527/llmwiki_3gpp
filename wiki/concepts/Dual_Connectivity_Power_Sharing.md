# Dual_Connectivity_Power_Sharing

## 정의
Dual_Connectivity_Power_Sharing은 EN-DC, NE-DC 및 NR-DC와 같이 다중 셀 그룹(Cell Group)이 설정된 환경에서, UE가 각 셀 그룹의 상향링크(UL) 전송 전력을 총 전력 제한(Total UE Transmit Power) 내에서 효율적으로 분배하고 제어하는 메커니즘을 의미합니다.

## 요약
다중 연결 환경에서 UE는 각 셀 그룹(MCG 및 SCG)에 대해 독립적으로 전력 제어를 수행하되, 전체 전송 전력이 UE의 최대 전력 등급(Maximum Power Class)을 초과하지 않도록 동적 또는 반정적 방식으로 전력을 공유합니다. 이는 상향링크 전송의 신뢰성을 유지하면서도 규정된 전력 제한을 준수하기 위한 필수적인 PHY 계층 절차입니다.

## 상세 설명
TS 38.213 §7.6에 따라, 다중 연결 환경에서의 전력 공유는 다음과 같은 원칙을 따릅니다.

1. 총 전력 제한: UE는 MCG와 SCG에서 동시에 전송되는 모든 상향링크 채널 및 신호의 총 전송 전력이 해당 UE의 설정된 최대 전력(P_total)을 초과하지 않도록 보장해야 합니다.
2. 동적 전력 공유: UE는 각 셀 그룹으로부터 수신된 상향링크 승인(Grant) 및 전력 제어 명령을 기반으로 실시간으로 전력을 할당합니다. 만약 총 요구 전력이 P_total을 초과할 경우, UE는 사전에 정의된 우선순위 규칙에 따라 각 채널의 전송 전력을 스케일링하거나 일부 전송을 생략합니다.
3. 전력 할당 모드:
   - 반정적 모드(Semi-static): 상위 계층 시그널링을 통해 각 셀 그룹에 할당된 최대 전력 비율을 고정하여 운영합니다.
   - 동적 모드(Dynamic): UE가 채널 상태와 트래픽 요구량을 고려하여 셀 그룹 간 전력을 유연하게 재분배합니다.
4. 우선순위 처리: 전력 제한 상황 발생 시, [[PUCCH]] 전송, [[PUSCH]] 전송, [[SRS]] 전송 간의 우선순위가 적용되며, 특히 [[Transmission_Power_Prioritization]] 절차를 통해 긴급도가 높은 제어 정보가 우선적으로 보호됩니다.

## 인과 관계
- [[PUSCH_Power_Control]] depends_on Dual_Connectivity_Power_Sharing (다중 연결 시 총 전력 제한 내에서 PUSCH 전력 결정)
- [[PUCCH_Power_Control]] depends_on Dual_Connectivity_Power_Sharing (다중 연결 시 총 전력 제한 내에서 PUCCH 전력 결정)
- [[SRS_Power_Control]] depends_on Dual_Connectivity_Power_Sharing (다중 연결 시 총 전력 제한 내에서 SRS 전력 결정)
- [[Transmission_Power_Prioritization]] depends_on Dual_Connectivity_Power_Sharing (전력 부족 시 채널 간 우선순위 결정)
- [[Power_Headroom_Report]] affects Dual_Connectivity_Power_Sharing (전력 공유 상태를 네트워크에 보고하여 스케줄링 최적화)

## 관련 개념
- [[PUSCH_Power_Control]] (depends_on)
- [[PUCCH_Power_Control]] (depends_on)
- [[SRS_Power_Control]] (depends_on)
- [[Transmission_Power_Prioritization]] (depends_on)
- [[Power_Headroom_Report]] (affects)

## 스펙 근거
- TS 38.213 §7.6: Dual connectivity 환경에서의 상향링크 전력 공유 및 제한 절차 정의

## 소스
- 3GPP TS 38.213 V18.0.0, "NR; Physical layer procedures for control"