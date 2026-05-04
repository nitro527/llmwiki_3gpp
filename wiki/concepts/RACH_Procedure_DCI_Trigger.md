# RACH_Procedure_DCI_Trigger

## 정의
[[PDCCH]] order를 통한 랜덤 액세스 절차 트리거는 네트워크가 [[UE]]에게 특정 [[PRACH]] 프리앰블을 전송하도록 지시하는 [[DCI]] 기반의 제어 메커니즘을 의미합니다.

## 요약
이 절차는 네트워크가 [[PDCCH]]를 통해 전송하는 [[DCI]] format 1_0을 사용하여 [[UE]]의 랜덤 액세스 절차를 개시하도록 트리거합니다. 이는 주로 [[CFRA]] (Contention-Free Random Access) 절차를 수행하기 위해 사용되며, [[UE]]는 수신된 [[DCI]] 필드에 포함된 프리앰블 인덱스 및 마스크 정보를 바탕으로 [[PRACH]] 전송을 수행합니다.

## 상세 설명
네트워크는 [[PDCCH]] order를 통해 [[UE]]에게 [[PRACH]] 전송을 지시할 수 있습니다. 이 과정에서 사용되는 [[DCI]] format 1_0은 다음과 같은 필드를 포함하여 [[RACH_Procedure_L1]]을 제어합니다.

- [[RA Preamble index]]: [[UE]]가 전송해야 할 [[PRACH]] 프리앰블의 식별자입니다.
- [[PRACH Mask index]]: [[UE]]가 해당 프리앰블을 전송할 수 있는 시간/주파수 자원(PRACH occasion)을 결정하는 마스크 값입니다.
- [[SSB]] index: 프리앰블 전송 시 참조할 [[SS_PBCH_Block]]을 지정합니다.

이 메커니즘은 다음과 같은 [[UE]] 기능과 연관됩니다:
- [필수(항상)] 3-0: Basic MAC procedures 및 1-1: Basic initial access channels and procedures를 통해 기본적인 랜덤 액세스 절차를 수행합니다.
- [선택] 40-2-4: 한 [[TRP]]에서 보낸 [[PDCCH]] order가 다른 [[TRP]]를 향한 [[CFRA]] 기반의 인터 셀 [[PRACH]] 전송을 트리거합니다.
- [선택] 40-2-4a: 한 [[TRP]]에서 보낸 [[PDCCH]] order가 다른 [[TRP]]를 향한 [[CFRA]] 기반의 인트라 셀 [[PRACH]] 전송을 트리거합니다.
- [선택] 45-5: [[RACH_Procedure_L1]] 기반의 조기 [[Timing_Advance_Adjustment]] 획득을 지원합니다.
- [선택] 22-9: [[PDCCH]] order로 트리거된 [[PRACH]] 전송이 다른 [[DCI]]에 의해 취소될 수 있습니다.
- [선택] 34-15: [[NTN]] 환경에서의 [[RA-SDT]] 절차를 지원합니다.

## 인과 관계
- [[PDCCH]] order 수신 (triggers) -> [[RACH_Procedure_L1]]
- [[DCI]] 필드 내 [[RA Preamble index]] (determines) -> [[PRACH]] 프리앰블 선택
- [[DCI]] 필드 내 [[PRACH Mask index]] (determines) -> [[PRACH_Resource_Mapping]]

## 관련 개념
- [[PDCCH]] (depends_on)
- [[PRACH]] (affects)
- [[RACH_Procedure_L1]] (triggers)
- [[DCI_Formats_Processing]] (part_of)
- [[SS_PBCH_Block]] (depends_on)

## 스펙 근거
- TS 38.212 §7.3.1.2.1에 따르면, [[DCI]] format 1_0은 랜덤 액세스 절차를 트리거하기 위한 필드들을 포함하며, 이는 [[PDCCH]] order를 통해 전송됩니다.

## 소스
- 3GPP TS 38.212 V18.0.0, "NR; Multiplexing and channel coding"
- 3GPP TS 38.822, "Study on physical layer enhancements for NR"