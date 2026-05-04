# PDSCH_DCI_Field_Processing

## 정의
[[PDSCH_DCI_Field_Processing]]은 [[PDCCH]]를 통해 전송되는 [[DCI]] format 1_0, 1_1, 1_2, 1_3 내의 필드들을 해석하여 [[PDSCH]] 수신 및 관련 [[HARQ]] 피드백 절차를 수행하기 위한 제어 정보 처리 과정을 의미합니다.

## 요약
[[DCI]] format 1_0, 1_1, 1_2, 1_3은 [[PDSCH]] 스케줄링을 위한 핵심 제어 정보를 포함합니다. 주요 필드로는 주파수 도메인 자원 할당, 시간 도메인 자원 할당, [[MCS]], [[HARQ]] 프로세스 번호, [[TPC]] 명령, 그리고 [[CSI]] 요청 등이 있습니다. UE는 이 필드들을 해석하여 [[PDSCH]] 수신 파라미터를 결정하고, 수신 성공 여부에 따른 [[HARQ-ACK]] 보고를 수행합니다.

## 상세 설명
[[DCI]] format 1_0, 1_1, 1_2, 1_3은 [[PDSCH]] 스케줄링을 위해 다음과 같은 공통 및 개별 필드를 포함합니다.

- 주파수 도메인 자원 할당: [[PDSCH]]가 할당된 [[PRB]] 위치를 지정합니다.
- 시간 도메인 자원 할당: [[PDSCH]]가 위치한 [[Slot]] 내의 심볼 위치 및 길이를 결정하는 인덱스를 제공합니다.
- [[HARQ]] 프로세스 번호: 수신된 데이터의 [[HARQ]] 프로세스를 식별합니다.
- [[MCS]]: [[PDSCH]]의 변조 방식 및 부호화율을 결정합니다.
- [[TPC]] 명령: [[PUCCH]] 전송 전력을 조절합니다.
- [[PDSCH]]-to-[[HARQ_ACK]] 타이밍 지시자: [[PDSCH]] 수신 후 [[HARQ-ACK]]을 전송하기까지의 슬롯 오프셋을 지정합니다.
- [[CBG]] 관련 필드: [[CBG]] 기반의 재전송을 지원하는 경우, [[CBG]] 전송 정보 및 플러싱 정보를 포함합니다.
- [[DCI]] format 1_1 및 1_2는 추가적으로 [[CSI]] 요청, [[Antenna_Port]] 지시, [[TCI]] 상태 지시 등을 포함하여 복잡한 MIMO 전송을 지원합니다.

## 인과 관계
- [[DCI]] 수신 (triggers) [[PDSCH]] 수신 절차
- [[PDSCH]] 수신 (affects) [[HARQ-ACK]] 생성
- [[TPC]] 필드 (affects) [[PUCCH_Power_Control]]
- [[HARQ]] 프로세스 번호 (depends_on) [[DCI]] 필드 해석

## 관련 개념
- [[PDSCH]] (part_of)
- [[PDCCH]] (part_of)
- [[HARQ]] (affects)
- [[DCI_Formats_Processing]] (similar_to)

## 스펙 근거
- TS 38.212 §7.3.1.2.1: [[DCI]] format 1_0의 필드 구성 및 해석 정의
- TS 38.212 §7.3.1.2.2: [[DCI]] format 1_1의 필드 구성 및 해석 정의
- TS 38.212 §7.3.1.2.3: [[DCI]] format 1_2의 필드 구성 및 해석 정의
- TS 38.212 §7.3.1.2.4: [[DCI]] format 1_3의 필드 구성 및 해석 정의

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03), "NR; Multiplexing and channel coding"