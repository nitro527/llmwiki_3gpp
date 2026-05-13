# CSI_Reporting_Procedure

## 정의
CSI_Reporting_Procedure는 gNB가 UE의 하향링크 채널 상태를 파악하기 위해, UE가 측정된 채널 정보를 보고하도록 제어하는 일련의 프레임워크 및 절차를 의미합니다.

## 요약
UE는 상위 계층 설정을 통해 CSI 보고를 위한 자원 및 보고 방식을 구성받으며, gNB로부터 DCI를 통해 비주기적 CSI 보고를 트리거받습니다. 보고되는 정보에는 CQI, PMI, CRI, SSBRI, LI, RI, L1-RSRP, L1-SINR, CapabilityIndex 및 TDCP가 포함됩니다.

## 상세 설명
CSI 보고 프레임워크는 상위 계층 파라미터에 의해 구성되는 보고 설정(CSI-ReportConfig, ltm-CSI-ReportConfig)과 자원 설정(CSI-ResourceConfig, LTM-CSI-ResourceConfig)을 기반으로 동작합니다.

1. 보고 트리거링: 비주기적 CSI 보고는 DCI format 0_1, 0_2 또는 0_3에 의해 트리거됩니다. DCI format 0_2 사용 시 reportTriggerSizeDCI-0-2 파라미터가 적용됩니다.
2. 트리거 상태 관리: UE는 CSI-AperiodicTriggerStateList 또는 CSI-SemiPersistentOnPUSCH-TriggerStateList를 통해 트리거 상태 리스트를 관리합니다. 각 트리거 상태는 하나 이상의 CSI-ReportConfig 또는 LTM-CSI-ReportConfig와 연관된 자원 집합 ID를 포함합니다.
3. 서브 설정: CSI-ReportConfig가 서브 설정 리스트로 구성된 경우, 트리거 상태는 하나 이상의 reportSubConfigId를 포함하여 보고의 세부 사항을 지정합니다.
4. 자원 제어: UE가 CSI 보고에 사용하는 시간 및 주파수 자원은 gNB에 의해 제어됩니다. 간섭 측정을 위한 자원 집합은 CSI-ReportConfig와 연관된 보고 설정에서만 존재할 수 있습니다.

## 인과 관계
- [[CSI_RS_Generation]] depends_on [[CSI_Reporting_Procedure]] (CSI 측정을 위한 기준 신호 생성)
- [[PUSCH_UTO_UCI_Reporting]] depends_on [[CSI_Reporting_Procedure]] (보고된 CSI 정보를 PUSCH로 전송)
- [[UCI_Multiplexing]] depends_on [[CSI_Reporting_Procedure]] (CSI 보고 데이터의 다중화)

## 관련 개념
- [[CSI_RS_Generation]] (implements)
- [[PUSCH_UTO_UCI_Reporting]] (affects)
- [[UCI_Multiplexing]] (affects)
- [[CSI_Processing_Criteria]] (depends_on)
- [[CSI_CQI_Determination]] (implements)

## 스펙 근거
- TS 38.214 §5.2.1: CSI 보고 프레임워크의 구성 요소 및 트리거링 메커니즘 정의
- TS 38.214 §5.2.1.1: 서브 설정 및 트리거 상태 관리 상세

## 소스
- 3GPP TS 38.214 V19.0.0 (2024-03)