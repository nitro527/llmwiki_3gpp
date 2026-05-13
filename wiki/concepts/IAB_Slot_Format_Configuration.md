# IAB_Slot_Format_Configuration

## 정의
IAB_Slot_Format_Configuration은 Integrated Access-Backhaul(IAB) 노드에서 IAB-MT(Mobile Termination)와 IAB-DU(Distributed Unit) 간의 자원 충돌을 방지하고 효율적인 시분할 다중화(TDM)를 수행하기 위해 슬롯 내 심볼의 가용성(Hard, Soft, Unavailable)을 설정하고 동적으로 지시하는 절차를 의미한다.

## 요약
IAB 노드는 상위 노드로부터 IAB-MT를 위한 슬롯 포맷을 설정받으며, 동시에 IAB-DU의 각 셀에 대해 자원 가용성(HSNA: Hard, Soft, Not Available)을 설정한다. IAB-DU의 Soft 자원은 DCI format 2_5를 통해 동적으로 가용 여부가 지시되며, IAB-MT의 동작과 IAB-DU의 전송 간의 충돌을 방지하기 위해 Timing Case Indication 및 Guard Symbol 설정이 병행된다.

## 상세 설명
IAB 노드의 슬롯 포맷 및 자원 관리는 TS 38.213 §14에 따라 다음과 같이 수행된다.

1. IAB-MT 슬롯 포맷 설정
IAB-MT는 tdd-UL-DL-ConfigurationDedicated-IAB-MT를 통해 슬롯 포맷을 제공받는다. 이는 일반적인 UE의 설정과 유사하나, symbols-IAB-MT 파라미터를 통해 allDownlink, allUplink, 또는 explicit(상향/하향 심볼 수 지정) 방식으로 슬롯 내 심볼을 정의한다. 또한 DCI format 2_0을 통해 슬롯 포맷 조합(SFI)을 동적으로 수신할 수 있다.

2. IAB-DU 자원 설정 (HSNA)
IAB-DU의 각 셀은 gNB-DU Cell Resource Configuration을 통해 심볼 단위 또는 RB set 단위로 Hard, Soft, Unavailable 타입을 설정받는다.
- Hard: IAB-DU가 항상 전송/수신 가능. SS/PBCH block, Type0-PDCCH CSS, 주기적 CSI-RS, PRACH, SR 등이 포함된 심볼/RB set은 Hard로 간주됨.
- Soft: IAB-MT의 동작과 충돌하지 않거나, DCI format 2_5를 통해 가용(Available)으로 지시된 경우에만 IAB-DU가 전송/수신 가능.
- Unavailable: IAB-DU가 전송/수신 불가.

3. 동적 가용성 지시 (DCI format 2_5)
IAB-MT는 AI-RNTI로 스크램블된 DCI format 2_5를 모니터링하여 IAB-DU의 Soft 자원에 대한 가용성 정보를 수신한다. AI index 필드는 resourceAvailability 테이블(Table 14-3)에 따라 Soft 자원의 가용 여부를 결정한다.

4. 타이밍 및 가드 심볼
IAB-MT와 IAB-DU 간의 전환 시 발생하는 간섭을 방지하기 위해 Timing Case Indication MAC CE를 통해 Case-1, Case-6, Case-7 모드를 설정한다. 또한 Provided Guard Symbols MAC CE를 통해 IAB-MT와 IAB-DU 간 전환 시 사용하지 않을 가드 심볼 수를 설정한다.

## 인과 관계
- [[IAB_MT_Operation]] depends_on [[IAB_Slot_Format_Configuration]] (IAB-MT의 슬롯 포맷 및 타이밍 모드 결정)
- [[IAB_DU_Resource_Management]] depends_on [[IAB_Slot_Format_Configuration]] (IAB-DU의 자원 가용성 설정 및 DCI 2_5 기반 동적 제어)
- [[PDCCH_Monitoring_Procedures]] triggers [[IAB_Slot_Format_Configuration]] (DCI format 2_5 수신을 통한 Soft 자원 가용성 갱신)

## 관련 개념
- [[IAB_MT_Operation]] (implements)
- [[IAB_DU_Resource_Management]] (implements)
- [[Slot_Format_Indicator]] (similar_to)
- [[PDCCH_Monitoring_Procedures]] (depends_on)
- [[Timing_Advance_Adjustment]] (affects)

## 스펙 근거
- TS 38.213 §14: IAB-MT 및 IAB-DU를 위한 슬롯 포맷, HSNA 설정, DCI format 2_5 기반 자원 가용성 지시 절차 정의.
- TS 38.211 §4.3.1: IAB-MT 전송 타이밍 모드(Case-1, Case-6, Case-7) 정의.
- TS 38.321: Timing Delta MAC CE, Timing Case Indication MAC CE, Provided Guard Symbols MAC CE 관련 절차.
- TS 38.473: gNB-DU Cell Resource Configuration 및 HSNA Slot Configuration List 정의.

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §14