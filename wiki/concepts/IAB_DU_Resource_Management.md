# IAB_DU_Resource_Management

## 정의
IAB_DU_Resource_Management는 IAB-node의 DU(Distributed Unit)가 자원(심볼 및 RB 세트)의 가용성을 관리하고, 이를 IAB-MT(Mobile Termination)와 협력하여 동적으로 제어하는 절차를 의미한다.

## 요약
IAB-DU는 각 셀의 자원을 Hard, Soft, Unavailable 타입으로 설정하여 관리한다. Hard 자원은 DU가 독립적으로 사용할 수 있는 자원이며, Soft 자원은 IAB-MT의 동작 상태나 DCI format 2_5를 통한 가용성 지시에 따라 DU의 사용 여부가 결정되는 자원이다. Unavailable 자원은 DU가 송수신에 사용할 수 없는 자원을 의미한다.

## 상세 설명
IAB-DU의 자원 관리는 시간 도메인(심볼 단위)과 주파수 도메인(RB 세트 단위)에서 수행된다.

1. 자원 타입 설정
- Hard: DU가 항상 송수신에 사용할 수 있는 자원. SS/PBCH block, Type0-PDCCH CSS, 주기적 CSI-RS, PRACH, SR 등이 할당된 심볼이나 RB 세트는 Hard로 간주된다.
- Soft: IAB-MT의 동작과 연계되어 가용성이 결정되는 자원. IAB-MT가 해당 자원에서 송수신하지 않거나, IAB-MT의 송수신 동작이 DU의 자원 사용으로 인해 변경되지 않는 경우 DU가 사용할 수 있다.
- Unavailable: DU가 송수신을 수행하지 않는 자원.

2. 동적 가용성 지시 (DCI format 2_5)
- IAB-MT는 AI-RNTI로 스크램블된 CRC를 가진 DCI format 2_5를 모니터링하여 Soft 자원의 가용성을 확인한다.
- DCI format 2_5 내의 AI index 필드는 Soft 심볼 또는 Soft RB 세트의 가용성 상태를 나타낸다.
- IAB-MT가 DCI format 2_5를 수신하면, 해당 정보는 IAB-MT가 속한 셀 그룹의 모든 서빙 셀에 적용된다.
- 가용성 조합(Availability Combination)은 resourceAvailability 필드를 통해 정의되며, 이는 Table 14-3에 따라 Soft 자원의 가용 여부를 매핑한다.

3. 주파수 도메인 관리
- Frequency-Domain HSNA Configuration List를 통해 RB 세트별로 Hard, Soft, Unavailable 타입을 설정할 수 있다.
- RB 세트 크기는 IAB-MT의 최소 RBG 크기보다 커야 한다.
- 특정 RB 세트에 대한 설정이 없는 경우, 해당 심볼의 HSNA Slot Configuration List 설정을 따른다.

## 인과 관계
- [[IAB_MT_Operation]] depends_on [[IAB_DU_Resource_Management]] (IAB-MT의 송수신 상태가 DU의 Soft 자원 가용성에 직접적인 영향을 미침)
- [[DCI_Field_Mapping]] implements [[IAB_DU_Resource_Management]] (DCI format 2_5의 AI index 필드를 통해 자원 가용성 정보 전달)
- [[Slot_Format_Configuration]] affects [[IAB_DU_Resource_Management]] (슬롯 포맷 설정이 DU 자원의 기본 가용성 타입 결정에 관여)

## 관련 개념
- [[IAB_MT_Operation]] (depends_on)
- [[DCI_Field_Mapping]] (implements)
- [[Slot_Format_Configuration]] (affects)
- [[PDCCH_Monitoring_Procedures]] (depends_on)

## 스펙 근거
- TS 38.213 §14: IAB-DU의 Hard/Soft/Unavailable 자원 설정 및 DCI format 2_5를 통한 동적 가용성 지시 절차 정의
- TS 38.213 Table 14-3: resourceAvailability 값과 Soft 자원 가용성 타입 간의 매핑 정의

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §14