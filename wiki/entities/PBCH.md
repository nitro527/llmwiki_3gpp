# PBCH

## 정의
PBCH는 5G NR 시스템에서 셀의 초기 접속을 위해 필수적인 시스템 정보(MIB)를 전송하는 하향링크 물리 채널입니다.

## 요약
PBCH는 [[SS_PBCH_Block_Generation]]의 핵심 구성 요소로, 80ms 주기로 전송되는 마스터 정보 블록(MIB)을 나릅니다. 물리 계층에서는 페이로드 생성, 스크램블링, CRC 부착, 채널 코딩 및 레이트 매칭 과정을 거쳐 전송됩니다.

## 상세 설명
PBCH는 셀 탐색 및 초기 접속을 위한 정보를 UE에 전달합니다. TS 38.212 §7.1에 정의된 주요 처리 단계는 다음과 같습니다.

1. 페이로드 생성: MIB를 포함한 페이로드가 생성됩니다. 이는 [[PBCH_Payload_Generation]]을 통해 수행됩니다.
2. 스크램블링: 전송되는 비트들은 셀 식별자 및 타이밍 정보와 관련된 시퀀스로 스크램블링됩니다. 이는 [[PBCH_Scrambling]]을 통해 수행됩니다.
3. 전송 블록 CRC 부착: 오류 검출을 위해 CRC가 부착됩니다. 이는 [[CRC_Calculation]]을 통해 수행됩니다.
4. 채널 코딩: 폴라 코딩(Polar coding)을 사용하여 채널 코딩이 수행됩니다. 이는 [[Channel_Coding]]을 통해 수행됩니다.
5. 레이트 매칭: 물리 자원 매핑을 위해 정해진 크기로 비트가 조정됩니다. 이는 [[Rate_Matching]]을 통해 수행됩니다.

TS 38.211 §7.3.3에 따르면, PBCH는 SS/PBCH 블록 내에서 특정 시간-주파수 자원에 매핑되어 전송됩니다. PBCH의 복조를 위해서는 [[PBCH_DMRS_Generation]]을 통해 생성된 복조 참조 신호가 함께 사용됩니다.

## 인과 관계
- [[PBCH_Payload_Generation]] depends_on [[PBCH]] (PBCH 전송을 위한 데이터 생성)
- [[PBCH_Scrambling]] depends_on [[PBCH]] (PBCH 데이터의 스크램블링 수행)
- [[PBCH_DMRS_Generation]] depends_on [[PBCH]] (PBCH 복조를 위한 참조 신호 생성)
- [[SS_PBCH_Block_Generation]] depends_on [[PBCH]] (SS/PBCH 블록 구성의 필수 요소)
- [[Channel_Coding]] depends_on [[PBCH]] (PBCH 데이터의 오류 정정 부호화)
- [[Rate_Matching]] depends_on [[PBCH]] (PBCH 데이터의 자원 매핑을 위한 비트 조정)

## 관련 개념
- [[SS_PBCH_Block_Generation]] (part_of)
- [[PBCH_Payload_Generation]] (implements)
- [[PBCH_Scrambling]] (implements)
- [[PBCH_DMRS_Generation]] (affects)
- [[Channel_Coding]] (implements)
- [[Rate_Matching]] (implements)
- [[CRC_Calculation]] (implements)

## 스펙 근거
- TS 38.211 §7.3.3: Physical broadcast channel의 물리적 구조 및 매핑 정의
- TS 38.212 §7.1: Broadcast channel의 코딩 및 처리 절차 정의

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)
- 3GPP TS 38.212 V17.x.x (Multiplexing and channel coding)