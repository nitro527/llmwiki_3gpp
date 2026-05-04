# RedCap UE Procedures

## 정의
[[RedCap_UE_Procedures]]는 3GPP 5G NR 표준에서 정의하는 Reduced Capability(RedCap) UE가 네트워크와 통신하기 위해 수행하는 물리 계층(L1) 절차를 의미합니다. 이는 제한된 대역폭과 기저대역 처리 능력을 가진 단말이 효율적으로 셀에 접속하고 데이터를 송수신하기 위한 규정입니다.

## 요약
RedCap UE는 일반적인 UE와 비교하여 감소된 대역폭 및 데이터 처리 능력을 가지며, 이를 지원하기 위해 초기 접속, [[BWP]] 구성, [[PUCCH]] 자원 할당 및 [[SS_PBCH_Block]] 처리 과정에서 특화된 절차를 따릅니다. 특히 FR1 대역에서의 대역폭 제한과 하프 듀플렉스(Half-Duplex) 동작이 주요 고려 사항입니다.

## 상세 설명
RedCap UE는 네트워크와의 통신 과정에서 다음과 같은 L1 절차를 수행합니다.

1. **초기 접속 및 SS/PBCH Block 처리**: RedCap UE는 셀 탐색 과정에서 [[SS_PBCH_Block]]을 수신합니다. 이때 RedCap UE 전용으로 설정된 초기 접속 파라미터를 사용하여 네트워크에 접속을 시도합니다.
2. **BWP 구성**: RedCap UE는 자신의 대역폭 능력에 맞는 [[Bandwidth_Part_Operation]]을 수행합니다. 네트워크는 RedCap UE가 지원하는 최대 대역폭 내에서 BWP를 할당하며, UE는 해당 BWP 내에서만 PDCCH 모니터링 및 데이터 송수신을 수행합니다.
3. **PUCCH 및 PUSCH 자원 설정**: RedCap UE는 제한된 자원 내에서 효율적인 상향링크 통신을 위해 [[PUCCH_Resource_Determination]] 및 [[PUSCH_Transmission_Procedures]]를 수행합니다.
4. **Half-Duplex 동작**: 페어드 스펙트럼(Paired spectrum) 환경에서 RedCap UE는 하프 듀플렉스 모드로 동작할 수 있으며, 이에 따른 송수신 타이밍 제약이 적용됩니다.

## 인과 관계
- [[SS_PBCH_Block]] (depends_on) [[RedCap_UE_Procedures]]
- [[Bandwidth_Part_Operation]] (affects) [[RedCap_UE_Procedures]]
- [[PUCCH_Resource_Determination]] (depends_on) [[RedCap_UE_Procedures]]
- [[Half_Duplex_UE_Operation]] (affects) [[RedCap_UE_Procedures]]

## 관련 개념
- [[Bandwidth_Part_Operation]] (depends_on)
- [[SS_PBCH_Block]] (depends_on)
- [[PUCCH_Resource_Determination]] (depends_on)
- [[Half_Duplex_UE_Operation]] (affects)

## 스펙 근거
- TS 38.213 §17: RedCap UE를 위한 L1 절차 정의
- TS 38.213 §17.1: RedCap UE의 초기 절차 (First procedures)
- TS 38.213 §17.1A: RedCap UE의 추가 절차 (Second procedures)
- TS 38.213 §17.2: 페어드 스펙트럼에서의 Half-Duplex UE 동작

## 소스
- 3GPP TS 38.213 V18.0.0 (2023-12) "NR; Physical layer procedures for control"