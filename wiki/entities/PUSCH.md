# PUSCH

## 정의
PUSCH(Physical Uplink Shared Channel)는 상향링크에서 상위 계층으로부터 전달된 데이터를 전송하기 위해 정의된 물리 채널입니다. TS 38.211 §6.1.1에 따라 상향링크 물리 채널 중 하나로 분류되며, 사용자 데이터 및 제어 정보를 전송하는 핵심적인 역할을 수행합니다.

## 요약
PUSCH는 상향링크 전송의 주된 채널로, 데이터 전송뿐만 아니라 HARQ-ACK, CSI와 같은 상향링크 제어 정보(UCI)를 피기백(piggyback)하여 전송할 수 있습니다. 전송을 위해 스크램블링, 변조, 레이어 매핑, 프리코딩, 자원 매핑 등의 물리 계층 처리 과정을 거치며, 전력 제어 파라미터에 의해 전송 전력이 결정됩니다.

## 상세 설명
PUSCH는 상위 계층에서 생성된 전송 채널인 UL-SCH를 물리 계층으로 매핑하여 전송합니다. 주요 동작 및 구성 요소는 다음과 같습니다.

1. 물리 계층 처리 과정:
   - [[PUSCH_Scrambling]]: 전송 데이터의 비트 단위 스크램블링 수행.
   - [[PUSCH_Modulation]]: [[Modulation_Mapper]]를 통해 심볼 생성.
   - [[PUSCH_Layer_Mapping]]: 다중 안테나 전송을 위한 레이어 매핑.
   - [[PUSCH_Transform_Precoding]]: DFT-s-OFDM 파형을 위한 변환 프리코딩(선택적).
   - [[PUSCH_Precoding]]: 안테나 포트 매핑을 위한 프리코딩 수행.
   - [[PUSCH_Resource_Mapping]]: [[OFDM_Baseband_Signal_Generation]]을 위해 자원 요소(RE)에 매핑.

2. 제어 정보 다중화:
   - [[PUSCH_UCI_Multiplexing]]을 통해 HARQ-ACK, CSI, SR 등을 데이터와 함께 전송할 수 있습니다.
   - HARQ-ACK 공간 번들링(spatial bundling)을 지원하며, 서로 다른 PUCCH/PUSCH 시작 OFDM 심볼을 가진 경우에도 HARQ-ACK 다중화가 가능합니다.

3. 전력 제어:
   - [[PUSCH_Power_Control]]을 통해 전송 전력이 결정되며, 이는 경로 손실 추정 및 TPC 명령 등에 의해 제어됩니다.

4. 특수 기능:
   - 상향링크 전송 시 서로 다른 우선순위 레벨을 가진 채널/신호 간의 다중화 및 우선순위 처리를 지원합니다.
   - 다중 CC(Component Carrier) 환경에서 [[SRS]] 및 [[PUCCH]]/PUSCH의 병렬 전송을 지원합니다.

## 인과 관계
- [[PUSCH_Transmission_Procedure]] depends_on [[PUSCH]] (PUSCH 전송을 위한 절차 수행)
- [[PUSCH_UCI_Multiplexing]] affects [[PUSCH]] (UCI가 PUSCH에 다중화되어 전송됨)
- [[PUSCH_Power_Control]] affects [[PUSCH]] (전송 전력 결정)
- [[PUSCH_Resource_Allocation]] depends_on [[PUSCH]] (자원 할당 정보에 따라 PUSCH 전송)
- [[DMRS]] implements [[PUSCH]] (채널 추정을 위한 참조 신호 제공)

## 관련 개념
- [[PUCCH]] (similar_to)
- [[UL-SCH]] (part_of)
- [[DMRS]] (part_of)
- [[PUSCH_Power_Control]] (affects)
- [[PUSCH_UCI_Multiplexing]] (affects)
- [[PUSCH_Resource_Allocation]] (depends_on)

## 스펙 근거
- TS 38.211 §6.1.1: 상향링크 물리 채널 정의
- TS 38.211 §6.3.1: PUSCH 물리 채널 구성
- TS 38.212 §4.1: 상향링크 전송 채널과 물리 채널 간의 매핑
- TS 38.214 §6: PUSCH 관련 절차

## 소스
- 3GPP TS 38.211 V16.9.0 (Physical channels and modulation)
- 3GPP TS 38.212 V16.9.0 (Multiplexing and channel coding)
- 3GPP TS 38.214 V16.9.0 (Physical layer procedures for data)