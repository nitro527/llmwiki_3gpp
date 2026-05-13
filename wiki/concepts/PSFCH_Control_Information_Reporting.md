# PSFCH_Control_Information_Reporting

## 정의
[[PSFCH]]를 통해 전송되는 제어 정보 보고 절차로, 사이드링크 통신에서 수신된 데이터에 대한 [[HARQ-ACK]] 정보 또는 채널 점유와 관련된 충돌 정보(Conflict Information)를 송신측에 전달하는 메커니즘을 의미합니다.

## 요약
[[PSFCH]]는 사이드링크에서 [[HARQ-ACK]] 피드백 및 충돌 정보를 보고하기 위한 물리 채널입니다. UE는 상위 계층에서 설정된 자원 풀 내에서 특정 타이밍과 자원 매핑 규칙에 따라 제어 정보를 생성하고 전송합니다. 이 과정은 사이드링크 데이터 전송의 신뢰성을 보장하고 자원 효율성을 최적화하는 데 목적이 있습니다.

## 상세 설명
[[PSFCH]]를 통한 제어 정보 보고는 TS 38.213 §16.3에 정의된 절차를 따릅니다.

1. 제어 정보 구성: [[PSFCH]]를 통해 보고되는 정보는 크게 두 가지 유형으로 구분됩니다.
   - [[HARQ-ACK]] 정보: [[PSSCH]]를 통해 수신된 데이터 패킷에 대한 성공(ACK) 또는 실패(NACK) 상태를 나타냅니다.
   - 충돌 정보(Conflict Information): 사이드링크 자원 풀 내에서 다른 UE와의 전송 충돌을 감지하거나 보고하기 위한 정보입니다.

2. 자원 및 타이밍:
   - [[PSFCH]] 자원은 상위 계층 파라미터에 의해 설정된 자원 풀 내에서 결정됩니다.
   - 전송 타이밍은 [[PSSCH]] 수신 시점과 연동되며, 특정 슬롯 오프셋을 적용하여 결정됩니다.

3. 시퀀스 생성 및 매핑:
   - 보고할 정보는 [[PSFCH_Sequence_Generation]]을 통해 시퀀스로 변환됩니다.
   - 생성된 시퀀스는 [[PSFCH_Resource_Mapping]]에 따라 물리 자원 요소(RE)에 매핑되어 전송됩니다.

4. 보고 절차:
   - UE는 [[PSSCH]] 수신 후, 설정된 타이밍에 따라 [[PSFCH]] 자원을 선택합니다.
   - 다중 사용자 환경에서 충돌을 방지하기 위해 자원 선택은 설정된 규칙에 따라 결정됩니다.

## 인과 관계
- [[PSFCH]] depends_on [[PSFCH_Sequence_Generation]] (제어 정보 전송을 위한 시퀀스 생성 필수)
- [[PSFCH]] depends_on [[PSFCH_Resource_Mapping]] (물리 자원 할당을 위한 매핑 절차 필수)
- [[PSFCH]] triggers [[HARQ-ACK]] (수신된 데이터에 대한 피드백 보고)

## 관련 개념
- [[PSFCH]] (part_of)
- [[HARQ-ACK]] (implements)
- [[PSSCH]] (depends_on)
- [[Sidelink_Resource_Configuration]] (depends_on)

## 스펙 근거
- TS 38.213 §16.3: UE procedure for reporting and obtaining control information in PSFCH

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"