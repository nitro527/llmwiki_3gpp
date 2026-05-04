# PSBCH

## 정의
[[PSBCH]]는 [[Sidelink]] 통신에서 [[SL-BCH]]를 전송하기 위해 사용되는 물리 채널입니다. 이는 사이드링크 장치 간의 동기화 및 시스템 정보 전달을 위한 핵심적인 물리 계층 채널입니다.

## 요약
[[PSBCH]]는 [[Sidelink]] 환경에서 동기화 신호와 함께 전송되어, 수신 장치가 사이드링크 시스템의 기본 파라미터를 획득할 수 있도록 지원합니다. TS 38.211 §8.3.3에 따라 [[Scrambling]], [[Modulation]], 그리고 물리 자원 매핑 과정을 거쳐 전송됩니다.

## 상세 설명
[[PSBCH]]의 전송 과정은 다음과 같은 단계로 구성됩니다.

1. [[Scrambling]]: [[PSBCH]]를 통해 전송되는 비트 시퀀스는 TS 38.211 §8.3.3.1에 정의된 바와 같이 [[Scrambling]] 과정을 거칩니다. 이는 물리 계층에서의 데이터 보호 및 간섭 완화를 목적으로 합니다.
2. [[Modulation]]: 스크램블링된 비트들은 TS 38.211 §8.3.3.2에 따라 [[QPSK]] 방식으로 [[Modulation]]됩니다.
3. [[Mapping to physical resources]]: 변조된 심볼들은 TS 38.211 §8.3.3.3에 정의된 규칙에 따라 물리 자원 그리드에 매핑됩니다. 이때 [[Sidelink]] 동기화 신호와 함께 [[SS-PBCH-Block]] 구조와 유사한 방식으로 자원을 점유합니다.

## 인과 관계
- [[Synchronization procedures]] (depends_on) [[PSBCH]]
- [[PSBCH_Scrambling]] (part_of) [[PSBCH]]
- [[PSBCH_Modulation]] (part_of) [[PSBCH]]
- [[Sidelink_Resource_Grid]] (affects) [[PSBCH]]

## 관련 개념
- [[Sidelink]] (part_of)
- [[SL-BCH]] (part_of)
- [[SS-PBCH-Block]] (similar_to)
- [[Synchronization_Procedures]] (depends_on)

## 스펙 근거
- TS 38.211 §8.3.3: Physical sidelink broadcast channel 정의 및 전송 절차
- TS 38.211 §8.3.3.1: [[PSBCH]] [[Scrambling]] 절차
- TS 38.211 §8.3.3.2: [[PSBCH]] [[Modulation]] 방식
- TS 38.211 §8.3.3.3: 물리 자원 매핑 규칙
- TS 38.213 §16.1: [[Sidelink]] 동기화 절차에서의 [[PSBCH]] 역할

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03)
- 3GPP TS 38.212 V17.9.0 (2024-03)
- 3GPP TS 38.213 V17.9.0 (2024-03)