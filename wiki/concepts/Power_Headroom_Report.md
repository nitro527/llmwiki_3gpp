# Power_Headroom_Report

## 정의
Power Headroom Report(PHR)는 UE가 현재 서빙 셀의 활성 UL BWP에서 가용한 송신 전력 여유분을 기지국에 보고하는 절차를 의미하며, Type 1(PUSCH용)과 Type 3(SRS용)으로 구분된다.

## 요약
PHR은 UE가 실제 전송을 수행하는지 혹은 참조 포맷을 사용하는지에 따라 계산 방식이 결정된다. 다중 캐리어 구성, 이중 연결(DC) 환경, 그리고 특정 전력 공유 모드에 따라 PH 계산 시 고려되는 전송 가정과 서빙 셀의 범위가 달라진다.

## 상세 설명
PHR은 TS 38.213 §7.7에 정의된 바와 같이 크게 두 가지 타입으로 나뉜다.
- Type 1 PH: 활성 UL BWP 내의 PUSCH 전송 기회에 유효한 전력 헤드룸.
- Type 3 PH: 활성 UL BWP 내의 SRS 전송 기회에 유효한 전력 헤드룸.

UE는 PHR 계산 시 실제 전송(Actual transmission)을 기반으로 할지, 혹은 참조 포맷(Reference format)을 기반으로 할지를 결정해야 한다.
1. DCI에 의해 트리거된 PUSCH 전송의 경우: PHR을 트리거한 DCI를 수신한 PDCCH 모니터링 시점까지 수신된 DCI 및 상위 계층 시그널링을 기반으로 결정한다.
2. Configured Grant(CG) PUSCH 전송의 경우: 해당 PUSCH 전송의 첫 번째 심볼에서 T_proc,2를 뺀 시점까지 수신된 정보를 기반으로 결정한다. 여기서 T_proc,2는 TS 38.214에 정의된 절차를 따르며, d2,1=1, d2,2=0을 가정한다.

이중 연결(DC) 환경에서의 PH 계산:
- SCG가 구성된 경우, phr-ModeOtherCG가 'virtual'로 설정되면 해당 CG에서 전송되는 PHR은 다른 CG의 서빙 셀에서 PUSCH/PUCCH 전송이 없다고 가정하고 계산한다.
- NR-DC 환경에서 MCG와 SCG가 모두 FR1 또는 FR2에서 동작할 경우, 상대 CG의 서빙 셀에서 전송이 없다고 가정하여 PH를 계산한다.
- EN-DC/NE-DC 환경에서 동적 전력 공유가 가능한 경우, E-UTRA 서브프레임과 NR 슬롯의 길이에 따라 PHR 보고 시점이 결정된다. 슬롯 길이가 다르면 E-UTRA 서브프레임과 완전히 겹치는 첫 번째 NR 슬롯의 PH를 보고하며, 슬롯 길이가 같으면 겹치는 첫 번째 NR 슬롯의 PH를 보고한다.

## 인과 관계
- [[PUSCH_Power_Control]] depends_on [[Power_Headroom_Report]] (전력 제어 파라미터 최적화)
- [[SRS_Power_Control]] depends_on [[Power_Headroom_Report]] (SRS 전력 할당 최적화)
- [[Dual_Connectivity_Power_Sharing]] affects [[Power_Headroom_Report]] (DC 환경에서의 PH 계산 가정 변경)
- [[Transmission_Power_Prioritization]] affects [[Power_Headroom_Report]] (전력 우선순위 결정에 따른 헤드룸 변화)

## 관련 개념
- [[PUSCH_Power_Control]] (implements)
- [[SRS_Power_Control]] (implements)
- [[Dual_Connectivity_Power_Sharing]] (affects)
- [[Transmission_Power_Prioritization]] (affects)

## 스펙 근거
- TS 38.213 §7.7: Power headroom report 정의 및 계산 절차
- TS 38.214 §6.2: T_proc,2 및 PUSCH 전송 타이밍 관련 파라미터
- TS 38.321: PHR 트리거링 및 MAC 계층 보고 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) §7.7