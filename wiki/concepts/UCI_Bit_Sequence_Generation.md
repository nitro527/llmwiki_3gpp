# UCI Bit Sequence Generation

## 정의
[[UCI]] Bit Sequence Generation은 [[PUCCH]] 또는 [[PUSCH]]를 통해 상향링크 제어 정보를 전송하기 위해, 다양한 제어 정보 비트들을 결합하고 특정 필드 구조에 따라 정렬하여 하나의 비트 시퀀스를 생성하는 물리 계층 절차를 의미합니다.

## 요약
본 절차는 [[HARQ-ACK]], [[SR]], [[CSI]], [[CG-UCI]], [[UTO-UCI]]와 같은 제어 정보들을 전송 채널의 특성에 맞게 구성하는 과정입니다. 전송 매체(PUCCH 또는 PUSCH)와 우선순위 인덱스에 따라 비트 결합 방식이 결정되며, 이후 [[UCI_Channel_Coding]] 단계로 전달됩니다.

## 상세 설명
UCI 비트 시퀀스 생성은 전송 채널에 따라 크게 두 가지 경로로 구분됩니다.

### PUCCH를 위한 UCI 비트 생성
TS 38.212 §6.3.1에 정의된 절차를 따릅니다.
- HARQ-ACK/SR 전용: HARQ-ACK 비트와 SR 비트를 결합합니다.
- CSI 전용: CSI 보고를 위한 비트 시퀀스를 생성합니다.
- HARQ-ACK/SR 및 CSI 결합: 다중화 규칙에 따라 비트를 병합합니다.
- 우선순위 인덱스 기반: 서로 다른 우선순위를 가진 UCI가 존재할 경우, 우선순위 인덱스에 따라 비트 시퀀스를 분리하거나 결합합니다.

### PUSCH를 위한 UCI 비트 생성
TS 38.212 §6.3.2에 정의된 절차를 따릅니다.
- HARQ-ACK: PUSCH에 피기백(piggyback)되는 HARQ-ACK 비트를 생성합니다.
- CSI: PUSCH를 통해 전송되는 CSI 비트를 구성합니다.
- CG-UCI 및 UTO-UCI: 설정된 그랜트(Configured Grant) 기반의 UCI 및 비면허 대역용 UCI 정보를 생성합니다.
- HARQ-ACK와 CG-UCI/UTO-UCI 결합: 해당 정보들을 하나의 시퀀스로 통합합니다.
- 우선순위 인덱스 기반: PUSCH 상에서도 우선순위가 다른 UCI 간의 다중화 및 시퀀스 생성이 수행됩니다.

## 인과 관계
- [[UCI_Bit_Sequence_Generation]] (triggers) [[UCI_Channel_Coding]]
- [[UCI_Bit_Sequence_Generation]] (depends_on) [[HARQ_ACK_Codebook_Determination]]
- [[UCI_Bit_Sequence_Generation]] (depends_on) [[CSI_Reporting_Procedures]]
- [[UCI_Bit_Sequence_Generation]] (affects) [[UCI_Rate_Matching]]

## 관련 개념
- [[PUCCH]] (part_of)
- [[PUSCH]] (part_of)
- [[HARQ-ACK]] (part_of)
- [[CSI]] (part_of)
- [[SR]] (part_of)
- [[CG-UCI]] (part_of)
- [[UTO-UCI]] (part_of)
- [[UCI_Channel_Coding]] (depends_on)

## 스펙 근거
- [필수(cap)] 4-19: 동일 슬롯 내 SR/HARQ-ACK/CSI 다중화 (PUCCH/PUSCH)
- [필수(cap)] 4-28: 서로 다른 시작 심볼을 가진 PUSCH 상의 HARQ-ACK 다중화
- [선택] 4-19b, 4-19c, 10-35, 10-35b, 10-35c, 4-2, 4-19a, 10-35a, 10-36, 11-3g: 다양한 슬롯/서브슬롯 환경 및 비면허 대역에서의 UCI 다중화 지원
- TS 38.212 §6.3.1: PUCCH를 위한 UCI 비트 시퀀스 생성 절차
- TS 38.212 §6.3.2: PUSCH를 위한 UCI 비트 시퀀스 생성 절차

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03) "Multiplexing and channel coding"
- 3GPP TS 38.822 V18.0.0 (2024-03) "User Equipment (UE) radio transmission and reception features"