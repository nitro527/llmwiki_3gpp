# PSFCH_Processing

## 정의
[[PSFCH]] (Physical Sidelink Feedback Channel) Processing은 [[Sidelink]] 통신에서 [[HARQ]]-ACK 정보 및 자원 충돌 정보를 송수신하기 위해 수행되는 물리 계층 절차를 의미합니다.

## 요약
PSFCH는 사이드링크 통신에서 데이터 수신 성공 여부를 송신측에 알리는 피드백 채널입니다. UE는 [[TS 38.213]] §16.3에 따라 PSFCH를 송신하거나 수신하며, [[TS 38.211]] §8.3.4.2에 정의된 [[PSFCH_format_0]]를 사용하여 시퀀스를 생성하고 물리 자원에 매핑합니다.

## 상세 설명
PSFCH 송수신 절차는 다음과 같은 단계로 구성됩니다.

1. 시퀀스 생성: PSFCH는 [[PSFCH_format_0]]를 사용하며, TS 38.211 §8.3.4.2.1에 따라 특정 시퀀스 기반으로 생성됩니다.
2. 자원 매핑: 생성된 시퀀스는 TS 38.211 §8.3.4.2.2에 따라 물리 자원 그리드에 매핑됩니다. 이때 자원 할당은 사이드링크 자원 풀 설정에 따릅니다.
3. 송신 절차: UE는 [[PSSCH]] 수신 후 HARQ-ACK 정보를 생성합니다. TS 38.213 §16.3.0에 따라, UE는 설정된 자원 내에서 PSFCH를 전송하며, 이때 전력 제어는 사이드링크 전력 제어 메커니즘을 따릅니다.
4. 수신 절차: UE는 TS 38.213 §16.3.1에 따라 상대 UE로부터 전송된 PSFCH를 수신하고, HARQ-ACK 정보를 디코딩하여 데이터 재전송 여부를 결정합니다.

## 인과 관계
- [[PSSCH]] 수신 (triggers) [[PSFCH_Processing]]
- [[PSFCH_Processing]] (depends_on) [[Sidelink_Resource_Selection]]
- [[PSFCH_Processing]] (affects) [[Sidelink_HARQ_Reporting]]

## 관련 개념
- [[PSFCH]] (part_of)
- [[PSSCH]] (depends_on)
- [[HARQ]] (depends_on)
- [[Sidelink_Power_Control]] (affects)
- [[Sidelink_Resource_Conflict]] (affects)

## 스펙 근거
- TS 38.211 §8.3.4.2: PSFCH format 0의 시퀀스 생성 및 자원 매핑 정의
- TS 38.213 §16.3: PSFCH를 통한 제어 정보 송수신 절차
- TS 38.213 §16.3.0: PSFCH 송신 절차
- TS 38.213 §16.3.1: PSFCH 수신 절차
- TS 38.213 §16.2.5: SL Carrier Aggregation 환경에서의 PSFCH 동작

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)
- 3GPP TS 38.213 V17.x.x (Physical layer procedures for control)