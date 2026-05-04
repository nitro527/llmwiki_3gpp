# SPS_HARQ_Deferral

## 정의
[[SPS_HARQ_Deferral]]는 [[UE]]가 [[SPS]] [[PDSCH]] 수신에 대한 [[HARQ-ACK]] 보고를 즉시 수행하지 않고, 특정 조건에서 다음 가용 [[PUCCH]] 슬롯으로 연기하거나 재다중화하는 절차를 의미합니다.

## 요약
본 절차는 [[TS_38_213]] §9.2.5.4에 정의되어 있으며, [[UE]]가 [[SPS]] [[PDSCH]]에 대한 [[HARQ-ACK]] 정보를 전송해야 하는 [[PUCCH]] 자원이 다른 상향링크 전송과 충돌하거나, [[TDD]] 설정으로 인해 가용하지 않을 때 이를 보존하고 후속 전송 기회에 포함시키는 메커니즘입니다.

## 상세 설명
[[UE]]는 [[SPS]] [[PDSCH]] 수신에 대응하는 [[HARQ-ACK]] 정보를 보고해야 할 때, 다음과 같은 절차를 따릅니다.

1. **조건 확인**: [[UE]]가 [[SPS]] [[PDSCH]] 수신에 대응하는 [[HARQ-ACK]]을 보고해야 하는 [[PUCCH]] 슬롯이 [[TDD]] 설정에 의해 하향링크로 지정되거나, 다른 상향링크 전송과의 충돌로 인해 전송이 불가능한 경우를 판단합니다.
2. **보고 지연**: 해당 [[HARQ-ACK]] 정보는 즉시 폐기되지 않으며, 이후에 발생하는 유효한 [[PUCCH]] 전송 기회로 지연됩니다.
3. **재다중화**: 지연된 [[HARQ-ACK]] 정보는 이후 가용해진 [[PUCCH]] 자원에서 다른 [[UCI]]와 함께 [[UCI_Multiplexing_PUCCH]] 절차를 통해 재다중화되어 전송됩니다.
4. **UE Feature 지원**:
   - [필수(항상)] 4-1: [[PUCCH]]를 통한 기본적인 상향링크 제어 채널 전송 기능을 지원해야 합니다.
   - [선택] 25-1: [[TDD]] 충돌 상황에서의 [[SPS]] [[HARQ-ACK]] 지연 기능을 지원합니다.
   - [선택] 11-4a, 49-6a: 우선순위가 다른 [[HARQ-ACK_Codebook_Determination]]을 동시에 구성하는 기능을 지원합니다.
   - [선택] 33-5-1a, 33-5-1b, 33-5-1f, 33-5-1g, 33-5-1j: 멀티캐스트 [[SPS]] [[PDSCH]]에 대한 다양한 [[HARQ-ACK]] 피드백 모드(ACK/NACK 기반, NACK-only 기반 등)를 지원합니다.
   - [선택] 33-6-1a, 33-8-3: 멀티캐스트 [[SPS]]를 위한 우선순위 설정 및 [[PUCCH]] 자원 구성을 지원합니다.
   - [선택] 4-2: 연속된 심볼에서 2개의 [[PUCCH]] [[Format_0]] 또는 [[Format_2]] 전송을 지원합니다.

## 인과 관계
- [[SPS_HARQ_Deferral]] depends_on [[TDD]] 설정 및 상향링크 자원 충돌 상황
- [[SPS_HARQ_Deferral]] triggers [[UCI_Multiplexing_PUCCH]] 절차를 통한 정보 재구성
- [[SPS_HARQ_Deferral]] affects [[HARQ-ACK_Codebook_Determination]] 결과

## 관련 개념
- [[SPS]] (part_of)
- [[HARQ-ACK]] (part_of)
- [[PUCCH]] (part_of)
- [[UCI_Multiplexing_PUCCH]] (triggers)
- [[HARQ-ACK_Codebook_Determination]] (affects)

## 스펙 근거
- [[TS_38_213]] §9.2.5.4: UE procedure for deferring HARQ-ACK for SPS PDSCH

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"