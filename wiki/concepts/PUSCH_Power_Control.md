# PUSCH_Power_Control

## 정의
[[PUSCH]] 전송 전력 제어는 [[UE]]가 상향링크 데이터 채널인 [[PUSCH]]를 전송할 때, 기지국과의 통신 품질을 유지하면서 간섭을 최소화하기 위해 송신 전력을 결정하는 절차를 의미합니다.

## 요약
[[PUSCH]] 전송 전력은 경로 손실 보상, [[TPC]] 명령, [[MCS]] 및 대역폭 할당량 등을 고려하여 계산됩니다. 이 과정은 [[DCI]]를 통한 동적 스케줄링, [[Configured_Grant_Transmission]] 기반 전송, 그리고 [[RACH_Procedure_L1]]와 연동되어 수행됩니다.

## 상세 설명
[[UE]]는 [[PUSCH]] 전송을 위해 다음과 같은 핵심 요소들을 고려하여 전력을 산출합니다.

*   **기본 전력 제어**: [필수(항상)] 8-3: Basic power control operation에 따라, [[UE]]는 설정된 최대 전력 내에서 전송 전력을 결정합니다.
*   **공간 관계 및 TCI**: [필수(cap)] 2-60: Active spatial relations 및 [필수(cap)] 2-4: TCI states for PDSCH에 따라, [[UE]]는 설정된 [[TCI]] 상태 및 공간 관계 정보를 활용하여 전력 제어 파라미터를 적용합니다.
*   **Closed Loop 제어**: [필수(cap)] 8-8: UL power control with 2 PUSCH closed loops에 따라, [[UE]]는 두 개의 독립적인 [[TPC]] 루프를 운용하여 전력 제어의 정밀도를 높입니다.
*   **동적 스케줄링 및 설정된 전송**: [[DCI]]를 통한 [[SRI]] 및 [[TPMI]] 매핑을 통해 전력 제어 루프를 선택하며, [[Configured_Grant_Transmission]]의 경우 미리 설정된 파라미터를 사용합니다.
*   **선택적 기능**:
    *   11-8: Enhanced UL power control scheme을 통한 고도화된 제어
    *   11-5: [[PUSCH_Repetition_Procedures]] Type B 적용 시의 전력 제어
    *   23-3-1b: Multi-TRP [[PUSCH]] 반복 전송을 위한 두 번째 [[TPC]] 필드 활용
    *   25-15: 고우선순위 DG-[[PUSCH]]와 저우선순위 CG-[[PUSCH]] 간의 물리 계층 우선순위 처리
    *   40-7-1g-2: Codebook2를 위한 Full power [[TPMI]] 그룹 활용
    *   50-1b, 50-1c, 50-1d: [[DCI]]를 통한 다중 [[PUSCH]] CG Type 2의 설정 및 해제 절차

## 인과 관계
*   [[DCI_Formats_Processing]] (triggers) [[PUSCH]] 전력 계산을 위한 [[TPC]] 및 [[SRI]] 정보 제공
*   [[Uplink_Power_Control]] (part_of) [[PUSCH]] 전력 제어의 상위 개념
*   [[PUSCH_Transmission_Procedures]] (depends_on) 계산된 전력 값에 따른 실제 신호 전송
*   [[RACH_Procedure_L1]] (affects) 초기 전력 설정 및 [[TPC]] 누적치 초기화

## 관련 개념
- [[Uplink_Power_Control]] (part_of)
- [[PUSCH]] (part_of)
- [[TPC]] (depends_on)
- [[SRI]] (depends_on)
- [[TPMI]] (depends_on)
- [[Configured_Grant_Transmission]] (depends_on)
- [[RACH_Procedure_L1]] (affects)

## 스펙 근거
TS 38.213 §7.1에 따르면, [[UE]]는 [[PUSCH]] 전송을 위해 설정된 전력 제어 파라미터와 [[DCI]]로부터 수신된 정보를 결합하여 전송 전력을 결정합니다. TS 38.213 §7.1.1은 [[UE]]가 전력 제어 루프를 어떻게 관리하고, [[TPC]] 명령을 어떻게 누적하거나 절대값으로 적용하는지에 대한 세부 동작을 규정합니다.

## 소스
- 3GPP TS 38.213 v18.0.0, "Physical layer procedures for control"
- 3GPP TS 38.822, "UE features for 5G NR"