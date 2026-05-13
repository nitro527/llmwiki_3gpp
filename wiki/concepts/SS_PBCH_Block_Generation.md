# SS/PBCH 블록 구성

## 정의
SS/PBCH 블록은 5G NR에서 초기 접속 및 셀 탐색을 위해 전송되는 물리 계층 신호의 집합으로, [[PSS]], [[SSS]], 그리고 [[PBCH]]와 그에 수반되는 [[DMRS]]로 구성된다.

## 요약
SS/PBCH 블록은 4개의 OFDM 심볼로 구성되며, 주파수 영역에서 240개의 부반송파를 점유한다. 이 블록은 셀의 동기화, 시스템 정보 획득, 그리고 채널 추정을 위한 기준 신호를 제공하며, 네트워크 환경에 따라 다양한 부반송파 간격 및 주파수 대역에 맞게 매핑된다.

## 상세 설명
TS 38.211 §7.4.2 및 §7.4.3에 따라 SS/PBCH 블록의 구성 및 매핑은 다음과 같이 정의된다.

1. 구성 요소:
   - [[PSS]] (Primary Synchronization Signal): 첫 번째 OFDM 심볼에 위치하며, 127개의 부반송파를 사용한다.
   - [[SSS]] (Secondary Synchronization Signal): 세 번째 OFDM 심볼에 위치하며, 127개의 부반송파를 사용한다.
   - [[PBCH]] (Physical Broadcast Channel): 두 번째 및 네 번째 OFDM 심볼 전체와, 세 번째 OFDM 심볼의 일부(SSS 주변)를 점유한다.
   - [[PBCH_DMRS_Generation]] (Demodulation Reference Signal): PBCH의 복조를 위해 사용되며, PBCH가 점유하는 심볼 내에 매핑된다.

2. 시간-주파수 자원 매핑:
   - SS/PBCH 블록은 시간 영역에서 4개의 연속적인 OFDM 심볼을 점유한다.
   - 주파수 영역에서는 240개의 부반송파를 점유하며, 이는 20개의 [[Resource_Block]]에 해당한다.
   - PSS와 SSS는 각각 127개의 부반송파를 사용하며, 나머지 부반송파는 0으로 설정되거나 PBCH 및 DMRS에 의해 사용된다.
   - PBCH는 240개의 부반송파 중 DMRS가 위치하지 않는 자원을 활용하여 전송된다.

3. 전송 절차:
   - SS/PBCH 블록은 특정 주파수 위치(GSCN)에서 전송되며, 네트워크 설정에 따라 반복 전송될 수 있다.
   - 초기 접속 시 UE는 PSS와 SSS를 통해 셀 ID를 식별하고, PBCH를 통해 MIB(Master Information Block)를 수신한다.

## 인과 관계
- [[PSS]] (part_of) SS/PBCH 블록 구성의 핵심 요소
- [[SSS]] (part_of) SS/PBCH 블록 구성의 핵심 요소
- [[PBCH]] (part_of) SS/PBCH 블록 구성의 핵심 요소
- [[PBCH_DMRS_Generation]] (part_of) SS/PBCH 블록 내 채널 추정용 기준 신호
- [[Synchronization_Procedures]] (depends_on) SS/PBCH 블록 수신을 통한 셀 동기화

## 관련 개념
- [[PSS]] (part_of)
- [[SSS]] (part_of)
- [[PBCH]] (part_of)
- [[PBCH_DMRS_Generation]] (part_of)
- [[Synchronization_Procedures]] (depends_on)
- [[Frame_Structure]] (depends_on)

## 스펙 근거
- TS 38.211 §7.4.2: Synchronization signals (PSS, SSS 정의 및 매핑)
- TS 38.211 §7.4.3: SS/PBCH block (블록 구조 및 자원 매핑)

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)