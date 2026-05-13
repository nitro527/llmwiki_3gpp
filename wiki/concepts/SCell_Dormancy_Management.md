# SCell_Dormancy_Management

## 정의
SCell_Dormancy_Management는 [[Carrier_Aggregation]] 환경에서 [[PDCCH]]를 통해 SCell의 활성 상태를 동적으로 제어하여 UE의 전력 소모를 최적화하는 절차를 의미한다. 이는 DCI 포맷 2_6을 이용한 DRX 연동 제어와 DCI 포맷 1_1/1_3을 이용한 즉각적인 BWP 전환 제어를 포함한다.

## 요약
본 절차는 SCell의 활성 상태를 관리하기 위해 두 가지 주요 메커니즘을 사용한다. 첫째, DCI 포맷 2_6을 통해 다음 long DRX cycle의 활성화 여부 및 SCell 그룹의 dormancy 상태를 지시한다. 둘째, DCI 포맷 1_1 또는 1_3을 통해 특정 SCell 그룹의 DL BWP를 dormant BWP 또는 활성 BWP로 즉시 전환한다. 이를 통해 UE는 불필요한 SCell 모니터링을 줄이고 전력 효율을 극대화한다.

## 상세 설명

### DCI 포맷 2_6을 이용한 관리
TS 38.213 §10.3에 따라, DRX 모드가 설정된 UE는 PCell 또는 SpCell에서 DCI 포맷 2_6을 모니터링한다.
- Wake-up indication bit: '0'은 다음 long DRX cycle에서 drx-onDurationTimer를 시작하지 않음을, '1'은 시작함을 의미한다.
- SCell dormancy bitmap: Wake-up bit 직후에 위치하며, 각 비트는 설정된 SCell 그룹에 대응한다.
- '0' 값은 해당 그룹의 SCell들에 대해 dormantBWP-Id로 설정된 DL BWP로 전환함을 의미한다.
- '1' 값은 현재 DL BWP가 dormant BWP인 경우 firstOutsideActiveTimeBWP-Id로, 그렇지 않은 경우 현재 활성 DL BWP를 유지함을 의미한다.
- UE는 Active Time 동안에는 DCI 포맷 2_6을 모니터링하지 않는다.

### DCI 포맷 1_1/1_3을 이용한 관리
Active Time 내에서 SCell의 dormancy 상태를 제어하기 위해 DCI 포맷 0_1/0_3/1_1/1_3 내의 SCell dormancy indication field를 사용한다.
- 비트맵의 각 비트는 dormancyGroupWithinActiveTime에 의해 설정된 SCell 그룹에 대응한다.
- '0' 값은 dormantBWP-Id로 설정된 DL BWP로 전환하고, '1' 값은 firstWithinActiveTimeBWP-Id 또는 현재 활성 BWP를 유지하도록 지시한다.
- DCI 포맷 1_1 또는 1_3이 특정 조건(예: CRC가 C-RNTI로 스크램블되고, 특정 필드 값이 0 또는 1로 설정된 경우)을 만족하면, 이를 PDSCH 스케줄링이 아닌 SCell dormancy 지시로 해석한다. 이때 UE는 해당 DCI 수신 후 일정 심볼 이후에 HARQ-ACK 정보를 보고해야 한다.

## 인과 관계
- [[PDCCH]] depends_on [[SCell_Dormancy_Management]] (DCI 포맷 2_6 및 1_1/1_3 모니터링을 통한 제어)
- [[Carrier_Aggregation]] affects [[SCell_Dormancy_Management]] (SCell 그룹 기반의 dormancy 관리 범위 결정)
- [[Bandwidth_Part_Operation]] implements [[SCell_Dormancy_Management]] (dormant BWP 및 활성 BWP 전환 수행)

## 관련 개념
- [[PDCCH]] (depends_on)
- [[Carrier_Aggregation]] (affects)
- [[Bandwidth_Part_Operation]] (implements)
- [[HARQ_ACK_Reporting]] (depends_on)

## 스펙 근거
- TS 38.213 §10.3: PDCCH monitoring indication and dormancy/non-dormancy behaviour for SCells
- TS 38.321: DRX operation and timer management
- TS 38.331: RRC configuration for dormancy groups and BWP IDs

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) §10.3