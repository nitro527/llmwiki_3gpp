# PSCCH

## 정의
[[PSCCH]] (Physical Sidelink Control Channel)는 [[Sidelink]] 통신에서 송신 단말이 수신 단말에게 데이터 전송을 위한 제어 정보를 전달하는 물리 채널입니다.

## 요약
[[PSCCH]]는 [[SCI]] (Sidelink Control Information)를 전송하기 위한 채널로, 1st-stage [[SCI]] 포맷인 [[SCI]] format 1-A 및 1-B를 운반합니다. 물리 계층에서는 [[Scrambling]], [[Modulation]], [[Channel_Coding]] 및 자원 매핑 과정을 거쳐 전송됩니다.

## 상세 설명
[[PSCCH]]는 [[PSSCH]] (Physical Sidelink Shared Channel)의 전송 파라미터를 수신 단말에 알리는 역할을 수행합니다.

- **SCI 포맷**: TS 38.212 §8.3에 따라 [[PSCCH]]는 1st-stage [[SCI]]를 전송합니다. 이는 [[SCI]] format 1-A 또는 1-B를 포함하며, [[PSSCH]]의 자원 할당 및 전송 파라미터 정보를 담고 있습니다.
- **채널 코딩**: TS 38.212 §8.3.3에 따라 [[SCI]] 비트 시퀀스는 [[Channel_Coding_General]] 절차를 거치며, 이후 [[Rate_Matching]] 과정을 통해 [[PSCCH]] 자원에 매핑됩니다.
- **물리 계층 처리**: 
  - [[Scrambling]]: TS 38.211 §8.3.2.1에 따라 [[PSCCH]] 전송 전 비트 레벨에서 스크램블링이 수행됩니다.
  - [[Modulation]]: TS 38.211 §8.3.2.2에 따라 QPSK 변조 방식이 사용됩니다.
  - 자원 매핑: TS 38.211 §8.3.2.3에 따라 [[PSCCH]]는 특정 주파수 및 시간 자원에 매핑되며, [[Sidelink_DMRS_Generation_Mapping]]을 통해 참조 신호와 함께 전송됩니다.

## 인과 관계
- [[SCI]] (depends_on) [[PSCCH]]
- [[PSCCH]] (triggers) [[PSSCH]]
- [[Channel_Coding_General]] (affects) [[PSCCH]]
- [[Sidelink_DMRS_Generation_Mapping]] (part_of) [[PSCCH]]

## 관련 개념
- [[Sidelink]] (part_of)
- [[PSSCH]] (triggers)
- [[SCI]] (part_of)
- [[Channel_Coding_General]] (depends_on)
- [[Rate_Matching]] (depends_on)
- [[Sidelink_DMRS_Generation_Mapping]] (part_of)

## 스펙 근거
- TS 38.211 §8.3.2: [[PSCCH]]의 물리적 구조, 스크램블링, 변조 및 자원 매핑 정의
- TS 38.212 §8.3: [[PSCCH]]를 통한 [[SCI]] 전송, 포맷, CRC 및 채널 코딩 정의
- TS 38.213 §16.2.2: [[PSCCH]] 관련 절차 정의

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03)
- 3GPP TS 38.212 V16.8.0 (2022-03)
- 3GPP TS 38.213 V16.8.0 (2022-03)