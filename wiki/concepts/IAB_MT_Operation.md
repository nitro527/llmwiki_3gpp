# IAB_MT_Operation

## 정의
IAB-MT(Integrated Access and Backhaul Mobile Termination)는 IAB 노드가 상위 노드(Donor gNB 또는 다른 IAB 노드)와 통신하기 위해 사용하는 기능적 엔티티로, 일반적인 [[UE]]의 동작을 기반으로 하되 IAB 네트워크의 특수성을 반영한 셀 탐색, 시스템 정보 획득, 랜덤 액세스 및 전송 타이밍 제어 절차를 수행한다.

## 요약
IAB-MT는 기본적으로 [[UE]]와 동일한 절차를 따르지만, 초기 셀 선택 시 SS/PBCH 블록 주기를 16 프레임으로 가정하며, 백홀 링크를 위한 특화된 [[PRACH]] 설정 및 타이밍 모드(Case-1, Case-6, Case-7)를 지원한다. 또한, IAB-DU의 자원 관리와 연동하여 슬롯 포맷을 구성하고, 동적 자원 가용성 지시(AI)를 통해 IAB-DU와 IAB-MT 간의 자원 충돌을 관리한다.

## 상세 설명
IAB-MT의 동작은 TS 38.213 §14에 정의되어 있으며, 주요 특징은 다음과 같다.

### 셀 탐색 및 랜덤 액세스
- 초기 셀 선택 시 IAB-MT는 SS/PBCH 블록이 포함된 하프 프레임이 16 프레임 주기로 발생한다고 가정한다.
- [[PRACH]] 전송을 위한 프레임 및 슬롯 결정은 TS 38.211을 따르며, SS/PBCH 블록과 PRACH 기회(Occasion) 간의 매핑을 위해 Table 14-1에 정의된 연관 주기(Association Period)를 사용한다. 이 연관 패턴 주기는 최대 640ms를 넘지 않도록 설정된다.

### IAB-MT 전송 타이밍 모드
IAB-MT는 상위 노드로부터 Timing Case Indication MAC CE를 통해 슬롯별 전송 타이밍 모드를 지시받는다.
- Case-1: 일반적인 [[UE]]와 동일한 상향링크 전송 타이밍을 적용한다.
- Case-6: IAB-MT의 전송 시간을 IAB-DU의 전송 시간과 일치시킨다.
- Case-7: 상위 노드로부터 제공된 타이밍 어드밴스 오프셋을 적용하여 TTA + NTA,offset,2 · Tc로 상향링크 전송 타이밍을 결정한다.

### 슬롯 포맷 및 자원 관리
- IAB-MT는 tdd-UL-DL-ConfigurationDedicated-IAB-MT를 통해 슬롯 포맷을 제공받으며, 이는 일반적인 슬롯 포맷 설정과 유사하게 하향링크, 상향링크, 유연한(Flexible) 심볼을 정의한다.
- IAB-DU의 자원은 Hard, Soft, Unavailable 타입으로 설정된다. Soft 심볼은 IAB-MT의 전송/수신 상태나 DCI format 2_5를 통한 가용성 지시(AI)에 따라 IAB-DU가 사용할 수 있다.

### 자원 가용성 지시 (AI)
- IAB-MT는 AI-RNTI로 스크램블된 DCI format 2_5를 모니터링하여 IAB-DU의 Soft 자원 가용성을 확인한다.
- DCI format 2_5의 AI 인덱스 필드는 IAB-DU의 Soft 심볼 또는 Soft RB 세트가 사용 가능한지 여부를 지시하며, 이는 IAB-DU와 IAB-MT 간의 전송 충돌을 방지하는 핵심 메커니즘이다.

## 인과 관계
- [[PRACH]] depends_on [[IAB_MT_Operation]] (IAB-MT의 백홀 RACH 절차 수행)
- [[Slot_Format_Configuration]] depends_on [[IAB_MT_Operation]] (IAB-MT 전용 슬롯 포맷 설정 적용)
- [[Timing_Advance_Adjustment]] depends_on [[IAB_MT_Operation]] (Case-7 타이밍 오프셋 적용)
- [[IAB_DU_Resource_Management]] depends_on [[IAB_MT_Operation]] (Soft 자원 가용성 지시를 통한 DU 자원 제어)

## 관련 개념
- [[PRACH]] (implements)
- [[Slot_Format_Configuration]] (implements)
- [[Timing_Advance_Adjustment]] (implements)
- [[IAB_DU_Resource_Management]] (affects)
- [[PDCCH_Monitoring_Adaptation]] (depends_on)

## 스펙 근거
- TS 38.213 §14: IAB-MT의 셀 탐색, RACH, 타이밍 모드 및 자원 가용성 지시 절차 정의
- TS 38.211 §4.3.1: IAB-MT 전송 타이밍 모드 관련 파라미터 정의
- TS 38.321: Timing Delta MAC CE, Timing Case Indication MAC CE, Case-7 Timing advance offset MAC CE 정의
- TS 38.473: gNB-DU Cell Resource Configuration 및 HSNA Slot Configuration 정의

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §14