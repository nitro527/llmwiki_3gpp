# Slot_Format_Indicator

## 정의
[[Slot_Format_Indicator]]는 [[DCI]] format 2_0을 통해 기지국이 UE에게 슬롯 내 심볼의 방향(Downlink, Uplink, Flexible)을 동적으로 지시하고, 채널 점유 시간 및 RB 세트 가용성을 관리하는 물리 계층 절차를 의미한다.

## 요약
[[Slot_Format_Indicator]]는 SFI-RNTI로 스크램블된 [[PDCCH]]를 통해 전달되며, UE는 이를 통해 특정 슬롯의 심볼 구성을 파악한다. 이 정보는 [[TDD]] 환경에서 동적인 자원 할당 및 채널 접근 제어를 가능하게 하며, [[PDSCH]], [[PUSCH]], [[PUCCH]], [[SRS]] 등의 송수신 동작에 직접적인 제약 조건을 부여한다.

## 상세 설명
[[Slot_Format_Indicator]] 절차는 상위 계층 파라미터인 SlotFormatIndicator가 설정된 경우 수행된다.

1. **DCI format 2_0 구성**: UE는 SFI-RNTI와 dci-PayloadSize를 제공받으며, 특정 [[CORESET]] 내에서 [[PDCCH]] 후보를 모니터링한다. DCI 내에는 SFI-index 필드, 채널 점유 시간 필드, RB 세트 가용성 지시 필드 등이 포함될 수 있다.
2. **슬롯 포맷 지시**: SFI-index 필드는 Table 11.1.1-1에 정의된 슬롯 포맷을 지시한다. 'D'는 Downlink, 'U'는 Uplink, 'F'는 Flexible 심볼을 의미한다. 이는 활성 [[BWP]]의 슬롯들에 적용된다.
3. **채널 점유 및 RB 세트 관리**: CO-DurationsPerCell 필드는 잔여 채널 점유 시간을 슬롯 단위로 지시하며, availableRB-SetsPerCell 필드는 비면허 대역 등에서 특정 RB 세트의 가용 여부를 비트맵으로 알린다.
4. **심볼 방향에 따른 동작 제약**:
   - UE는 SFI가 지시하는 심볼 방향과 상충되는 송수신 동작(예: DL 심볼로 지시된 구간에서의 [[PUSCH]] 전송)을 수행하지 않는다.
   - Flexible 심볼의 경우, 별도의 DCI 지시가 없으면 상위 계층 설정에 따르거나, 특정 조건 하에서 송수신이 제한된다.
   - [[CSI_RS]], [[PDSCH]], [[PUCCH]], [[PUSCH]], [[PRACH]], [[SRS]] 전송 시 SFI 지시와 충돌이 발생하면, UE는 해당 동작을 취소하거나 부분적으로 수행한다. 이때 PUSCH 준비 시간인 N2 등을 고려하여 취소 여부를 결정한다.

## 인과 관계
- [[PDCCH]] depends_on [[Slot_Format_Indicator]] (DCI format 2_0 수신을 통한 슬롯 포맷 정보 획득)
- [[PDSCH]] affects [[Slot_Format_Indicator]] (SFI 지시에 따른 수신 가능 여부 결정)
- [[PUSCH]] affects [[Slot_Format_Indicator]] (SFI 지시에 따른 전송 가능 여부 결정)
- [[PUCCH]] affects [[Slot_Format_Indicator]] (SFI 지시에 따른 전송 가능 여부 결정)
- [[SRS]] affects [[Slot_Format_Indicator]] (SFI 지시에 따른 전송 가능 여부 결정)
- [[BWP]] depends_on [[Slot_Format_Indicator]] (활성 BWP 내 슬롯 포맷 적용)

## 관련 개념
- [[DCI]] (implements)
- [[PDCCH]] (implements)
- [[TDD]] (affects)
- [[BWP]] (affects)
- [[Slot_Format_Configuration]] (depends_on)

## 스펙 근거
- TS 38.213 §11.1.1: UE procedure for determining slot format
- TS 38.213 Table 11.1.1-1: Slot formats for normal cyclic prefix
- TS 38.214 §6.1: PUSCH preparation time 및 전송 취소 관련 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"