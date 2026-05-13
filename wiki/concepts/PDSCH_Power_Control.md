# PDSCH_Power_Control

## 정의
PDSCH_Power_Control은 gNB가 하향링크 데이터 채널인 [[PDSCH]]의 전송 전력을 결정하고, 이와 연관된 참조 신호인 [[DMRS]] 및 [[PTRS]]와의 전력 비율(EPRE, Energy Per Resource Element)을 설정하는 절차를 의미합니다.

## 요약
gNB는 하향링크 전송 EPRE를 결정하며, UE는 측정 및 복조를 위해 특정 참조 신호 대비 PDSCH의 전력 비율을 가정합니다. SS/PBCH 블록, CSI-RS, DM-RS, PT-RS 간의 전력 관계는 상위 계층 파라미터 및 스펙에 정의된 테이블을 통해 결정됩니다.

## 상세 설명
gNB는 하향링크 전송 EPRE를 결정하며, UE는 측정 목적에 따라 다음과 같은 가정을 수행합니다.

1. 측정 관련 가정
- SS-RSRP, SS-RSRQ, SS-SINR 측정 시, UE는 하향링크 EPRE가 대역폭 전반에 걸쳐 일정하다고 가정합니다.
- SSS와 PBCH DM-RS 간의 EPRE 비율은 0 dB로 가정합니다.
- CSI-RS 측정 시, 특정 포트의 EPRE는 설정된 하향링크 대역폭 및 모든 OFDM 심볼에서 일정하다고 가정합니다.

2. 참조 신호 전력 유도
- SSS EPRE는 상위 계층 파라미터 ss-PBCH-BlockPower를 통해 유도됩니다.
- CSI-RS EPRE는 ss-PBCH-BlockPower와 상위 계층 파라미터 powerControlOffsetSS를 사용하여 유도됩니다. 만약 추가 PCI가 설정된 경우, ss-PBCH-BlockPower-r17을 참조합니다.

3. PDSCH와 DM-RS 간 전력 비율
- PDSCH EPRE와 DM-RS EPRE의 비율은 TS 38.214 Table 4.1-1에 따라 결정됩니다. 이는 DM-RS CDM 그룹 수에 의존하며, TS 38.211 §7.4.1.1.2에 정의된 DM-RS 스케일링 팩터가 적용됩니다.

4. PDSCH와 PT-RS 간 전력 비율
- PDSCH에 하나 또는 두 개의 PT-RS 포트가 할당된 경우, 상위 계층 파라미터 epre-Ratio 설정에 따라 TS 38.214 Table 4.1-2 또는 Table 4.1-2A를 사용하여 PT-RS EPRE와 PDSCH EPRE의 비율을 결정합니다.
- epre-Ratio가 설정되지 않은 경우, UE는 state '0'을 가정합니다. PT-RS 스케일링 팩터는 TS 38.211 §7.4.1.2.2에 정의된 바를 따릅니다.

5. 링크 복구
- 링크 복구 절차 시, PDCCH EPRE와 NZP CSI-RS EPRE의 비율은 0 dB로 가정합니다.

## 인과 관계
- [[PDSCH]] depends_on [[DMRS]] (PDSCH 복조를 위한 DM-RS EPRE 비율 참조)
- [[PDSCH]] depends_on [[PTRS]] (위상 추적을 위한 PT-RS EPRE 비율 참조)
- [[CSI_RS]] depends_on [[SS_PBCH_Block_Generation]] (CSI-RS 전력 유도를 위한 기준값 제공)

## 관련 개념
- [[PDSCH]] (affects)
- [[DMRS]] (affects)
- [[PTRS]] (affects)
- [[CSI_RS]] (affects)
- [[SS_PBCH_Block_Generation]] (affects)

## 스펙 근거
- TS 38.214 §4.1: 하향링크 전력 할당 및 EPRE 비율 설정 원칙
- TS 38.211 §7.4.1.1.2: DM-RS 스케일링 팩터 정의
- TS 38.211 §7.4.1.2.2: PT-RS 스케일링 팩터 정의
- TS 38.213 §6: 링크 복구 관련 PDCCH 전력 가정

## 소스
- 3GPP TS 38.214 V18.0.0 (2023-12)
- 3GPP TS 38.211 V18.0.0 (2023-12)
- 3GPP TS 38.213 V18.0.0 (2023-12)