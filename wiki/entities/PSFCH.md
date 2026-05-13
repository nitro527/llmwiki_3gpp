# PSFCH

## 정의
PSFCH는 5G NR Sidelink 통신에서 [[HARQ]]-ACK 정보 및 충돌 정보를 보고하기 위해 사용되는 물리 채널이다.

## 요약
PSFCH는 Sidelink 송신 UE가 수신 UE로부터 피드백을 받기 위해 사용하는 채널로, TS 38.211 §8.3.4에 정의되어 있다. UE는 PSFCH를 통해 HARQ-ACK 정보와 충돌 정보를 보고하며, 다수의 PSFCH 전송이 발생할 경우 우선순위 규칙에 따라 전송 전력을 결정하고 자원을 선택한다.

## 상세 설명
PSFCH는 Sidelink 자원 풀 내에서 HARQ-ACK 피드백을 지원하기 위해 설계되었다.

### 전력 제어 및 자원 선택
UE는 활성 SL BWP 내의 자원 풀에서 PSFCH 전송을 수행할 때, TS 38.213 §16.2.3에 따라 전송 전력을 결정한다.
- dl-P0-PSFCH 파라미터가 제공되는 경우, 이를 기반으로 전송 전력을 계산하며, 제공되지 않는 경우 별도의 전력 제어 로직을 따른다.
- 공유 스펙트럼 채널 접속(shared spectrum channel access) 환경에서는 sl-TransmissionStructureForPSFCH 설정에 따라 dedicatedInterlace 또는 commonInterlace 방식을 사용하여 PRB 단위의 전력을 산출한다.
- UE는 다수의 PSFCH 전송이 필요한 경우, 우선순위 필드 값에 따라 오름차순으로 전송을 결정한다. HARQ-ACK 정보를 포함하는 PSFCH를 우선적으로 처리하고, 이후 충돌 정보를 포함하는 PSFCH를 처리한다.

### 우선순위 및 동시 전송
TS 38.213 §16.2.4.2에 따라 PSFCH의 우선순위는 다음과 같이 결정된다.
- HARQ-ACK 정보를 포함하는 PSFCH의 우선순위는 해당 PSFCH와 연관된 [[SCI]] format 1-A의 우선순위 필드 값을 따른다.
- 충돌 정보를 포함하는 PSFCH의 우선순위는 충돌이 발생한 자원과 연관된 SCI format 1-A의 우선순위 값 중 가장 작은 값을 따른다.
- UE가 다수의 PSFCH를 동시에 전송하거나 수신해야 하는 경우, 가장 작은 우선순위 값을 가진 PSFCH 세트를 선택하여 처리한다.

## 인과 관계
- [[PSFCH]] depends_on [[SCI]] (PSFCH 전송을 위한 우선순위 및 제어 정보 획득)
- [[PSFCH]] affects [[Sidelink_Power_Control]] (PSFCH 전송 전력 결정 로직 적용)
- [[PSFCH]] affects [[Sidelink_Prioritization]] (우선순위 기반 PSFCH 전송 및 수신 처리)

## 관련 개념
- [[HARQ]] (depends_on)
- [[SCI]] (depends_on)
- [[Sidelink_Power_Control]] (affects)
- [[Sidelink_Prioritization]] (affects)
- [[PSFCH_Sequence_Generation]] (implements)
- [[PSFCH_Resource_Mapping]] (implements)

## 스펙 근거
- TS 38.211 §8.3.4: Physical sidelink feedback channel 정의
- TS 38.213 §16.2.3: PSFCH 전력 제어 및 전송 절차
- TS 38.213 §16.2.4.2: PSFCH 동시 전송/수신 및 우선순위 규칙

## 소스
- 3GPP TS 38.211 V17.9.0, "Physical channels and modulation"
- 3GPP TS 38.213 V17.8.0, "Physical layer procedures for control"