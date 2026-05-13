# Slot_Format_Configuration

## 정의
[[Slot_Format_Configuration]]은 TDD(Time Division Duplex) 시스템에서 각 슬롯 내의 OFDM 심볼을 DL(Downlink), UL(Uplink), 또는 Flexible로 정의하여 무선 자원의 가용성을 결정하는 절차를 의미한다.

## 요약
[[Slot_Format_Configuration]]은 상위 계층 파라미터인 tdd-UL-DL-ConfigurationCommon과 tdd-UL-DL-ConfigurationDedicated를 통해 수행된다. 공통 설정은 셀 전체의 기본 프레임 구조를 정의하며, 전용 설정은 특정 슬롯의 Flexible 심볼을 재정의하여 유연한 자원 할당을 가능하게 한다. 이를 통해 UE는 각 심볼의 송수신 가능 여부를 판단하고, 충돌 발생 시 우선순위 규칙에 따라 동작을 결정한다.

## 상세 설명
TS 38.213 §11.1에 따라 슬롯 포맷은 다음과 같이 결정된다.

1. **공통 설정 (tdd-UL-DL-ConfigurationCommon)**:
   - referenceSubcarrierSpacing을 통해 기준 SCS를 설정한다.
   - pattern1 및 선택적인 pattern2를 통해 슬롯 주기, DL 슬롯 수, DL 심볼 수, UL 슬롯 수, UL 심볼 수를 정의한다.
   - 각 슬롯은 DL, UL, 또는 Flexible 심볼로 구성되며, Flexible 심볼은 상위 계층 설정이나 DCI를 통해 동적으로 용도가 결정될 수 있다.

2. **전용 설정 (tdd-UL-DL-ConfigurationDedicated)**:
   - tdd-UL-DL-ConfigurationCommon에서 Flexible로 지정된 심볼만을 재정의할 수 있다.
   - slotSpecificConfigurationsToAddModList를 통해 특정 슬롯 인덱스에 대해 allDownlink, allUplink, 또는 explicit(DL 심볼 수 및 UL 심볼 수 명시) 설정을 적용한다.
   - 공통 설정에서 DL로 지정된 심볼을 UL로, 또는 그 반대로 변경하는 것은 허용되지 않는다.

3. **심볼 가용성 및 충돌 처리**:
   - UE는 DL로 표시된 심볼에서 [[PDSCH]], [[PDCCH]], [[CSI_RS]] 등을 수신하며, UL로 표시된 심볼에서 [[PUSCH]], [[PUCCH]], [[PRACH]], [[SRS]]를 송신한다.
   - Flexible 심볼의 경우, DCI를 통한 동적 지시가 없으면 상위 계층 설정에 따라 동작한다.
   - 단일 반송파 동작 시, 송수신 충돌이 발생하면 [[Directional_Collision_Handling]] 절차를 따르거나, 특정 우선순위 규칙에 따라 채널/신호의 수신 또는 송신을 취소한다. 특히 [[PUSCH]] 또는 [[PUCCH]] 송신과 [[PDCCH]] 수신이 겹칠 경우, UE의 처리 능력(partialCancellationPUCCH-PUSCH-PRACH-TX)에 따라 부분적 취소가 수행될 수 있다.

## 인과 관계
- [[Slot_Format_Configuration]] affects [[PDCCH_Monitoring_Procedures]] (슬롯 내 심볼 가용성에 따른 PDCCH 모니터링 제한)
- [[Slot_Format_Configuration]] affects [[PDSCH_Reception_Procedure]] (DL 심볼 가용성에 따른 PDSCH 수신 여부 결정)
- [[Slot_Format_Configuration]] affects [[PUSCH_Transmission_Procedure]] (UL 심볼 가용성에 따른 PUSCH 송신 여부 결정)
- [[Slot_Format_Configuration]] affects [[Directional_Collision_Handling]] (TDD 충돌 발생 시 우선순위 제어)
- [[Slot_Format_Configuration]] depends_on [[Frame_Structure]] (슬롯 및 심볼 구조 기반 설정)

## 관련 개념
- [[Slot_Format_Indicator]] (triggers)
- [[Directional_Collision_Handling]] (implements)
- [[Bandwidth_Part_Operation]] (affects)
- [[Uplink_Cancellation_Indication]] (affects)

## 스펙 근거
- TS 38.213 §11.1: 슬롯 포맷 설정 파라미터 및 우선순위 규칙 정의
- TS 38.213 §11.1: Flexible 심볼의 동적 자원 할당 및 충돌 처리 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"