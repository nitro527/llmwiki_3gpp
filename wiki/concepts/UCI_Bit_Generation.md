# UCI_Bit_Generation

## 정의
UCI_Bit_Generation은 상향링크 제어 정보인 [[UCI]]를 [[PUCCH]]를 통해 전송하기 위해, 다양한 제어 정보 필드들을 하나의 비트 시퀀스로 결합하고 정렬하는 물리 계층의 초기 처리 절차를 의미한다.

## 요약
UCI_Bit_Generation은 상위 계층으로부터 전달받은 [[HARQ_ACK_Reporting]], [[SR_Reporting]], 그리고 [[CSI_Reporting_Procedure]] 데이터를 특정 규칙에 따라 하나의 비트 스트림으로 구성한다. 이 과정에서 각 정보의 우선순위와 포맷에 따라 비트 필드가 배치되며, 이후 [[CRC_Calculation]] 및 [[Channel_Coding]] 단계로 전달된다.

## 상세 설명
TS 38.212 §6.3.1.1에 따라 UCI 비트 시퀀스 생성은 다음과 같은 절차를 따른다.

1. 정보 필드 구성: 전송할 UCI 정보는 [[HARQ_ACK_Codebook_Determination]] 결과인 HARQ-ACK 비트, 스케줄링 요청(SR) 비트, 그리고 채널 상태 정보(CSI) 비트로 구성된다.
2. 비트 시퀀스 결합: 각 정보 유형은 사전에 정의된 순서에 따라 하나의 비트 시퀀스 $a_0, a_1, \dots, a_{A-1}$로 결합된다. 여기서 $A$는 총 UCI 비트 수를 나타낸다.
3. 필드 매핑:
   - HARQ-ACK 정보가 포함되는 경우, 해당 비트들은 시퀀스의 앞부분에 배치된다.
   - SR 정보는 HARQ-ACK 비트 뒤에 이어지며, 설정된 SR 자원 인덱스에 따라 비트 값이 결정된다.
   - CSI 보고가 포함되는 경우, CSI 파트 1과 파트 2가 순차적으로 배치된다.
4. 데이터 정렬: 모든 UCI 비트는 MSB(Most Significant Bit)가 먼저 전송되도록 정렬되며, 각 필드의 크기는 RRC 설정 및 DCI 포맷에 의해 결정된다.

## 인과 관계
- [[UCI_Bit_Generation]] depends_on [[HARQ_ACK_Codebook_Determination]] (전송할 HARQ-ACK 비트 수 및 구성 결정)
- [[UCI_Bit_Generation]] triggers [[CRC_Calculation]] (생성된 비트 시퀀스에 대한 오류 검출 코드 생성)
- [[UCI_Multiplexing]] depends_on [[UCI_Bit_Generation]] (다양한 UCI 소스를 하나의 비트 스트림으로 통합)

## 관련 개념
- [[PUCCH]] (part_of)
- [[HARQ_ACK_Reporting]] (depends_on)
- [[SR_Reporting]] (depends_on)
- [[CSI_Reporting_Procedure]] (depends_on)
- [[CRC_Calculation]] (triggers)
- [[Channel_Coding]] (depends_on)

## 스펙 근거
- TS 38.212 §6.3.1.1: UCI bit sequence generation 절차 및 비트 필드 매핑 규칙 정의

## 소스
- 3GPP TS 38.212 V18.0.0, "Multiplexing and channel coding"