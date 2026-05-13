# Synchronization_Procedures

## 정의
Synchronization_Procedures는 UE가 셀의 시간 및 주파수 동기를 획득하고, 물리 계층 Cell ID를 검출하기 위해 수행하는 일련의 절차를 의미한다.

## 요약
UE는 [[SS_PBCH_Block_Generation]]을 통해 전송되는 PSS, SSS 및 PBCH를 수신하여 셀 탐색을 수행한다. 각 SS/PBCH block은 반 프레임 내에서 특정 후보 인덱스에 매핑되며, UE는 이를 기반으로 셀의 타이밍과 물리 계층 식별자를 결정한다. 공유 스펙(shared spectrum) 환경에서는 discovery burst transmission window 내에서 SS/PBCH block이 전송되며, UE는 이를 통해 동기를 획득한다.

## 상세 설명
UE는 셀 탐색을 위해 PSS와 SSS를 수신한다. SS/PBCH block은 PSS, SSS, PBCH가 연속적인 심볼에서 전송되는 구조를 가진다.

1. 후보 SS/PBCH block 인덱스 매핑:
   반 프레임 내에서 SS/PBCH block의 첫 번째 심볼 인덱스는 SCS(Subcarrier Spacing)와 주파수 대역에 따라 Case A(15 kHz)부터 Case G(960 kHz)까지 정의된다.
   - Case A: 15 kHz SCS, 3 GHz 이하 및 초과 대역에 따라 인덱스 결정
   - Case B: 30 kHz SCS, 3 GHz 이하 및 초과 대역에 따라 인덱스 결정
   - Case C: 30 kHz SCS, 1.88 GHz 기준 대역에 따라 인덱스 결정
   - Case D, E, F, G: 고주파수 대역(FR2, FR2-NTN, FR2-2)을 위한 높은 SCS 적용

2. 인덱스 결정:
   UE는 PBCH의 DM-RS 시퀀스 인덱스와 PBCH 페이로드 비트를 사용하여 후보 SS/PBCH block 인덱스를 결정한다.
   - LSB(Least Significant Bits)는 DM-RS 시퀀스 인덱스와 1:1 매핑된다.
   - MSB(Most Significant Bits)는 PBCH 페이로드 비트로부터 추출된다.

3. 주기성 및 공유 스펙 동작:
   - ssb-periodicityServingCell을 통해 반 프레임 주기성이 제공되며, 미제공 시 기본값은 1 반 프레임이다.
   - 공유 스펙 환경에서는 discoveryBurstWindowLength 내에서 SS/PBCH block이 전송된다. UE는 ssb-PositionsInBurst를 통해 전송되는 SS/PBCH block의 위치를 파악한다.
   - 공유 스펙에서 동일한 discovery burst transmission window 내의 SS/PBCH block들은 특정 조건 하에 quasi co-location(QCL) 관계를 가진다.

4. CORESET 0 결정:
   UE는 PBCH의 MIB 정보를 통해 Type0-PDCCH CSS set을 위한 CORESET 존재 여부를 판단한다.

## 인과 관계
- [[SS_PBCH_Block_Generation]] depends_on [[Synchronization_Procedures]] (동기화 신호 생성 및 전송 규격 준수)
- [[Type0_PDCCH_Monitoring]] depends_on [[Synchronization_Procedures]] (MIB 정보 기반 CORESET 0 설정)
- [[PBCH]] part_of [[Synchronization_Procedures]] (셀 탐색을 위한 필수 정보 전송)

## 관련 개념
- [[SS_PBCH_Block_Generation]] (implements)
- [[Type0_PDCCH_Monitoring]] (depends_on)
- [[PBCH]] (part_of)

## 스펙 근거
- TS 38.213 §4.1: Cell search 절차, SS/PBCH block 인덱스 매핑, 공유 스펙에서의 discovery burst 구성 및 QCL 가정에 관한 정의.

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) §4.1