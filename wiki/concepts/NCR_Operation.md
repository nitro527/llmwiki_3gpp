# NCR_Operation

## 정의
네트워크 제어 중계기(NCR, Network Controlled Repeater)는 [[PDCCH]]를 통해 기지국으로부터 제어 정보를 수신하는 NCR-MT(Mobile Termination) 엔티티와, 실제 신호를 중계하는 NCR-Fwd(Forwarding) 엔티티로 구성된 장치입니다.

## 요약
NCR은 NCR-MT를 통해 기지국과 제어 링크를 유지하며, 기지국으로부터 지시받은 빔 및 시간 자원 정보를 바탕으로 NCR-Fwd를 통해 액세스 링크에서 신호를 송수신합니다. NCR-MT의 동작은 일반적인 [[UE]]의 동작 절차를 따르며, NCR-Fwd는 제어 링크의 지시가 있을 때만 동작합니다.

## 상세 설명
NCR의 동작은 TS 38.213 §20에 정의된 바와 같이 NCR-MT와 NCR-Fwd의 협력으로 이루어집니다.

1. 기본 동작 및 제어:
   - NCR-MT는 [[UE]]와 동일한 셀 탐색, 시스템 정보 획득, 랜덤 액세스, [[UCI]] 보고, [[PDCCH]] 모니터링 절차를 수행합니다.
   - NCR-Fwd는 NCR-MT가 제어 링크를 통해 빔 지시를 수신한 후에만 액세스 링크에서 송수신을 수행합니다.
   - NCR-Fwd의 백홀 링크 타이밍은 NCR-MT의 프레임 타이밍을 따릅니다.
   - NCR-MT가 링크 복구 절차를 수행 중일 때는 NCR-Fwd의 송수신이 중단됩니다.

2. TDD 및 자원 관리:
   - NCR은 tdd-UL-DL-ConfigurationCommon 및 tdd-UL-DL-ConfigurationDedicated를 제공받아, 해당 설정에 따라 DL/UL 심볼에서만 송수신을 수행합니다.
   - 제어 링크와 백홀 링크를 동시에 송수신할 수 없는 경우, NCR-MT가 송신하는 시간 자원에서는 NCR-Fwd가 송신하지 않습니다.

3. 빔 및 TCI 상태 설정:
   - 제어 링크와 백홀 링크를 동시에 수신할 때, 백홀 링크의 [[TCI_State]]는 제어 링크의 TCI 상태와 동일하게 설정됩니다.
   - 동시 송신 시, 백홀 링크의 공간 필터(Spatial Filter)는 제어 링크의 공간 필터와 동일하게 설정됩니다.
   - 동시 송수신이 불가능한 경우, 백홀 링크의 QCL 파라미터나 공간 필터는 Unified TCI 상태, [[PDCCH]]의 CORESET 설정, 또는 MAC CE(NCR Downlink/Uplink Backhaul Link Beam Indication)를 통해 결정됩니다.

4. 액세스 링크 자원 및 빔 지시:
   - NCR은 주기적(Periodic) 또는 반정적(Semi-Persistent) 자원 세트를 설정받을 수 있습니다.
   - [[DCI_Format_2_8]]은 NCR-RNTI로 스크램블된 CRC를 가지며, 액세스 링크의 시간 자원과 빔 인덱스를 지시합니다.
   - 자원 간의 우선순위 충돌 시, priorityFlag 설정 여부와 DCI 지시 여부에 따라 적용할 빔 인덱스가 결정됩니다.

## 인과 관계
- [[PDCCH]] (depends_on) NCR-MT의 제어 정보 수신 및 빔 지시 획득
- [[UE]] (similar_to) NCR-MT의 기본 동작 절차
- [[TCI_State]] (affects) 백홀 링크 수신을 위한 QCL 파라미터 결정
- [[DCI_Format_2_8]] (triggers) 액세스 링크의 시간 자원 및 빔 인덱스 설정

## 관련 개념
- [[PDCCH]] (depends_on)
- [[UE]] (similar_to)
- [[TCI_State]] (affects)
- [[DCI_Format_2_8]] (triggers)
- [[UCI]] (part_of)

## 스펙 근거
- TS 38.213 §20: NCR-MT 및 NCR-Fwd 엔티티 정의 및 동작 절차
- TS 38.213 §20: TCI 상태 및 공간 필터 설정 규칙
- TS 38.213 §20: DCI format 2_8을 통한 액세스 링크 자원 및 빔 지시
- TS 38.213 §20: 자원 충돌 시 우선순위 결정 규칙

## 소스
- 3GPP TS 38.213 v18.0.0, "NR; Physical layer procedures for control"