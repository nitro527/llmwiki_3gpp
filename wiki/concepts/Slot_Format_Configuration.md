# Slot_Format_Configuration

## 정의
[[Slot_Format_Configuration]]은 [[TDD]] 시스템에서 [[OFDM]] 심볼 단위로 하향링크(DL), 상향링크(UL), 또는 유연한(Flexible) 방향을 결정하는 절차를 의미합니다. 이는 반정적(Semi-static) 설정과 동적(Dynamic) 시그널링을 결합하여 무선 자원의 효율적인 운용을 가능하게 합니다.

## 요약
[[Slot_Format_Configuration]]은 상위 계층 파라미터인 `tdd-UL-DL-ConfigurationCommon` 및 `tdd-UL-DL-ConfigurationDedicated`를 통한 반정적 설정과, [[DCI]] format 2_0을 통한 [[SFI]](Slot Format Indicator) 동적 지시로 구성됩니다. UE는 이 두 가지 정보를 결합하여 특정 심볼의 방향을 결정하며, 충돌 발생 시 우선순위 규칙에 따라 [[PUCCH]], [[PUSCH]], [[PRACH]] 등의 전송을 제어합니다.

## 상세 설명
UE는 다음과 같은 계층적 절차를 통해 슬롯 포맷을 결정합니다.

1. 반정적 설정: 상위 계층 시그널링을 통해 주기적인 슬롯 구조가 설정됩니다. 이는 시스템 정보 블록이나 RRC 전용 시그널링을 통해 제공됩니다.
2. 동적 지시: [[PDCCH]]를 통해 전송되는 [[DCI]] format 2_0 내의 [[SFI]]를 사용하여 슬롯 내의 특정 심볼들을 동적으로 재설정할 수 있습니다.
3. 우선순위 및 충돌 처리: 
   - 25-1: [[SPS]] [[HARQ]]-ACK deferral in case of TDD collision 기능을 통해 TDD 충돌 시 [[HARQ]]-ACK 전송을 지연시킬 수 있습니다.
   - 22-9: [[DCI]] format 2_0을 사용한 [[SFI]] 지시나 특정 [[PDSCH]]/[[CSI_RS]] 스케줄링 [[DCI]]를 통해 [[PUCCH]], [[PUSCH]], [[PRACH]]의 전송을 취소(Cancellation)할 수 있습니다.
   - 20-5a: UL-Flexible-DL 슬롯 포맷 설정을 통해 유연한 자원 활용을 지원합니다.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) [[Slot_Format_Configuration]]의 동적 변경
- [[Slot_Format_Configuration]] (affects) [[PUCCH]], [[PUSCH]], [[PRACH]]의 전송 가능 여부
- [[Directional_Collision_Handling]] (depends_on) [[Slot_Format_Configuration]]에 따른 심볼 방향 결정

## 관련 개념
- [[DCI_Formats_Processing]] (depends_on)
- [[Directional_Collision_Handling]] (depends_on)
- [[PUCCH]] (affects)
- [[PUSCH]] (affects)
- [[PRACH]] (affects)
- [[SPS_HARQ_Deferral]] (part_of)

## 스펙 근거
- TS 38.213 §11.1에 따르면, UE는 상위 계층 파라미터와 [[DCI]] format 2_0을 결합하여 슬롯 내 각 심볼의 방향을 결정해야 합니다.
- TS 38.213 §11.1.1에 따르면, UE는 반정적 설정과 동적 [[SFI]] 지시가 충돌할 경우, 동적 지시를 우선하여 슬롯 포맷을 결정합니다.

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §11.1, §11.1.1