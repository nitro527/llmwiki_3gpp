# Sidelink_Power_Control

## 정의
Sidelink_Power_Control은 NR Sidelink 통신에서 [[PSBCH]], [[PSSCH]], [[PSCCH]], [[PSFCH]], 그리고 [[SL_PRS]]와 같은 채널들의 전송 전력을 결정하는 절차를 의미합니다.

## 요약
NR Sidelink 전송 전력은 각 채널의 특성과 자원 풀(resource pool) 설정에 따라 결정됩니다. 기본적으로 UE는 최대 전송 전력 내에서 경로 손실(pathloss) 보상 및 전력 제어 파라미터를 사용하여 전송 전력을 계산하며, 공유 스펙트럼(shared spectrum) 환경이나 다중 채널 접근 시에는 추가적인 전력 분배 및 우선순위 기반의 전력 제어 메커니즘이 적용됩니다.

## 상세 설명
Sidelink 채널별 전송 전력 결정 절차는 다음과 같습니다.

### S-SS/PSBCH
S-SS/PSBCH 블록의 전송 전력은 TS 38.213 §16.2.0에 따라 결정됩니다. UE는 활성 SL BWP 내에서 anchor RB-set에 대해 전력을 계산하며, 공유 스펙트럼 동작 시 anchor RB-set에 할당된 전력을 제외한 잔여 전력을 비-anchor RB-set에 균등하게 분배합니다. 전력 계산식은 경로 손실 보상을 위한 파라미터(dl-P0-PSBCH, dl-Alpha-PSBCH)와 기준 신호(RS) 자원을 기반으로 합니다.

### PSSCH 및 PSCCH
PSSCH의 전송 전력은 TS 38.213 §16.2.1에 정의됩니다. UE는 우선순위와 CBR(Channel Busy Ratio) 측정값에 기반한 sl-MaxTxPower를 고려하여 전력을 결정합니다. PSCCH와 PSSCH가 동시에 전송되는 경우, PSCCH의 전력은 PSSCH의 전력 결정 절차를 참조하여 결정됩니다. 전용 SL PRS 자원 풀에서의 PSCCH 전력은 해당 슬롯의 SL PRS 전송 전력과 동일하게 설정됩니다.

### PSFCH
PSFCH 전송 전력은 TS 38.213 §16.2.3에 따라 HARQ-ACK 정보 및 충돌 정보 전송을 위해 결정됩니다. UE는 동시에 전송 가능한 최대 PSFCH 개수 내에서 전력을 계산하며, 공유 스펙트럼 동작 시 interlace 구조(dedicated 또는 common)에 따라 전력을 분배합니다. 우선순위 필드 값에 따라 전송할 PSFCH를 자율적으로 선택하고, 이에 따른 전력 누적 및 분배 규칙을 따릅니다.

### SL PRS
SL PRS 전송 전력은 TS 38.213 §16.2.3A에 정의됩니다. 공유 자원 풀인지 전용 자원 풀인지에 따라 sl-MaxTxPower 또는 sl-PRS-MaxTx-Power를 사용합니다. 경로 손실 보상을 위해 PSSCH 또는 SL PRS DM-RS를 기반으로 한 RSRP 측정값을 활용하며, 유니캐스트 전송 시 보고된 RSRP 값을 반영하여 전력을 조정합니다.

## 인과 관계
- [[Sidelink_Resource_Configuration]] depends_on [[Sidelink_Power_Control]] (자원 풀 설정에 따른 전력 파라미터 적용)
- [[Sidelink_Congestion_Control]] affects [[Sidelink_Power_Control]] (CBR 측정값에 따른 최대 전송 전력 제한)
- [[Sidelink_Transmission_Procedure]] depends_on [[Sidelink_Power_Control]] (전송 전력 결정 후 실제 신호 송신)
- [[Transmission_Power_Prioritization]] affects [[Sidelink_Power_Control]] (다중 채널 전송 시 전력 우선순위 조정)

## 관련 개념
- [[PSBCH]] (part_of)
- [[PSSCH]] (part_of)
- [[PSCCH]] (part_of)
- [[PSFCH]] (part_of)
- [[SL_PRS]] (part_of)
- [[Sidelink_Congestion_Control]] (affects)
- [[Transmission_Power_Prioritization]] (affects)

## 스펙 근거
- TS 38.213 §16.2.0 (S-SS/PSBCH 전력 제어)
- TS 38.213 §16.2.1 (PSSCH 전력 제어)
- TS 38.213 §16.2.2 (PSCCH 전력 제어)
- TS 38.213 §16.2.3 (PSFCH 전력 제어)
- TS 38.213 §16.2.3A (SL PRS 전력 제어)

## 소스
- 3GPP TS 38.213 V18.0.0 (NR; Physical layer procedures for control)