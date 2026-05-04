# IAB_Node

## 정의
[[IAB_Node]]는 5G NR 네트워크에서 무선 백홀(Wireless Backhaul)과 액세스(Access) 기능을 동시에 수행하는 노드를 의미하며, [[IAB-MT]]와 [[IAB-DU]]라는 두 가지 논리적 개체로 구성됩니다.

## 요약
[[IAB_Node]]는 상위 노드(Donor 또는 다른 IAB 노드)와 무선으로 연결되어 백홀 트래픽을 전달하는 [[IAB-MT]] 기능과, 하위 단말(UE) 또는 하위 IAB 노드에게 서비스를 제공하는 [[IAB-DU]] 기능을 수행합니다. TS 38.213 §14에 따라 자원 구성, 타이밍 모드, 그리고 가용성 지시를 통해 효율적인 무선 자원 관리를 수행합니다.

## 상세 설명
[[IAB_Node]]의 동작은 크게 다음과 같은 핵심 메커니즘으로 구분됩니다.

1. **IAB-MT 및 IAB-DU 동작**: [[IAB-MT]]는 상위 노드와 연결되어 제어 및 사용자 평면 트래픽을 송수신하며, [[IAB-DU]]는 하위 노드나 단말을 위한 스케줄링 및 자원 할당을 담당합니다.
2. **자원 구성 및 가용성**: [[IAB-Node]]는 상위 노드로부터 수신한 설정에 따라 자원을 하드(Hard), 소프트(Soft), 또는 사용 불가(Not available) 자원으로 구분합니다. 소프트 자원은 [[IAB-DU]]의 가용성 지시(Availability Indication)에 따라 동적으로 결정됩니다.
3. **타이밍 모드**: [[IAB-Node]]는 상위 노드와의 동기화를 위해 특정 타이밍 모드를 따르며, 이는 [[IAB_Timing_Control]]을 통해 관리됩니다.
4. **기능 지원**:
   - [필수(항상)] [[Basic_initial_access_channels_and_procedures]]를 통한 초기 접속 절차 지원.
   - [필수(cap)] [[Inter-IAB-node_discovery_and_measurements]]를 위한 [[SS_PBCH_Block]] 수신 설정.
   - [선택] [[RACH_Procedure_L1]] 확장을 위한 백홀 RACH 자원 주기 설정.
   - [선택] [[Directional_Collision_Handling]]을 통한 DC 동작 시 충돌 제어.
   - [선택] [[BAP_Header_Rewriting]] 및 [[F1AP_over_NR_RRC]] 지원.
   - [선택] [[MT-SDT]] 및 [[MT-SDT_for_NTN]]을 통한 소량 데이터 전송.
   - [선택] [[SSB-based_RRM_for_semi-static_channel_access_mode]] 및 [[UL_to_DL_COT_sharing]] 지원.
   - [선택] [[UL-Flexible-DL_slot_formats]]를 통한 유연한 슬롯 구성.

## 인과 관계
- [[IAB-DU]]의 자원 가용성 지시는 [[IAB-MT]]의 백홀 자원 활용도에 영향을 미침 (affects).
- [[IAB-Node]]의 동작은 [[IAB_Resource_Configuration]]에 따라 결정됨 (depends_on).
- [[IAB-Node]]는 [[SS_PBCH_Block]] 수신 설정을 통해 인접 노드 발견을 트리거함 (triggers).

## 관련 개념
- [[IAB-MT]] (part_of)
- [[IAB-DU]] (part_of)
- [[IAB_Timing_Control]] (depends_on)
- [[IAB_Resource_Configuration]] (depends_on)
- [[Directional_Collision_Handling]] (similar_to)

## 스펙 근거
- TS 38.213 §14: Integrated access-backhaul operation에 관한 전반적인 절차 및 자원 관리 규정.

## 소스
- 3GPP TS 38.213, "NR; Physical layer procedures for control" (Release 18)