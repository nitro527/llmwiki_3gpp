# SRS_Generation_Mapping

## 정의
[[SRS]] (Sounding Reference Signal)는 기지국이 상향링크 채널 상태 정보를 획득하고, 빔 관리, 위치 측정 및 주파수 선택적 스케줄링을 수행하기 위해 UE가 전송하는 상향링크 참조 신호입니다.

## 요약
SRS는 상위 계층 시그널링을 통해 설정된 자원 집합 내에서 생성 및 매핑되며, [[DCI]] (Downlink Control Information) 포맷 0_1 또는 0_2의 SRS 자원 지시자(SRS resource indicator) 필드를 통해 동적으로 트리거되거나 주기적으로 전송될 수 있습니다.

## 상세 설명
SRS 전송 절차는 크게 시퀀스 생성, 물리 자원 매핑, 그리고 슬롯 설정으로 구분됩니다.

### 시퀀스 생성
SRS 시퀀스는 TS 38.211 §6.4.1.4.2에 따라 정의됩니다. 기본적으로 [[Sequence_Generation]] 절차를 따르며, 특정 순환 시프트(cyclic shift)와 직교 커버 코드(orthogonal cover code)를 적용하여 다중 UE 간의 직교성을 확보합니다.

### 물리 자원 매핑
TS 38.211 §6.4.1.4.3에 따라 SRS는 설정된 대역폭 내에서 주파수 도메인과 시간 도메인 자원에 매핑됩니다. 
- 주파수 도메인: 콤(comb) 구조를 사용하여 자원을 할당하며, 주파수 호핑(frequency hopping)이 설정된 경우 특정 슬롯 간격으로 중심 주파수가 변경됩니다.
- 시간 도메인: 슬롯 내 마지막 1~6개의 OFDM 심볼을 사용할 수 있습니다.

### DCI를 통한 트리거링
기지국은 [[DCI_Formats_Processing]]을 통해 SRS 전송을 요청합니다.
- [[DCI]] 포맷 0_1 및 0_2 내의 SRS 자원 지시자 필드는 상위 계층에서 설정된 SRS 자원 집합 중 하나를 선택하여 전송을 지시합니다.
- 이는 비주기적(aperiodic) SRS 전송을 위해 사용되며, 채널 상태 정보 획득 및 빔 관리에 필수적입니다.

### UE Feature 지원
- [필수(항상)] [[PUSCH]] 전송을 위한 기본 SRS 동작을 지원합니다.
- [선택] [[PUSCH]] MIMO 전송(codebook/non-codebook based) 및 다중 TRP 전송을 위한 SRS 자원 설정을 지원합니다.
- [선택] 상향링크 빔 관리 및 위치 측정(positioning)을 위한 고도화된 SRS 자원 할당을 지원합니다.

## 인과 관계
- [[Frame_Structure_Numerology]] (depends_on): SRS의 시간/주파수 자원 매핑은 슬롯 구조와 뉴머롤로지에 의존합니다.
- [[DCI_Formats_Processing]] (triggers): DCI 내의 SRS 자원 지시자는 비주기적 SRS 전송을 트리거합니다.
- [[SRS_Power_Control]] (affects): SRS 전송 전력은 상향링크 전력 제어 절차에 의해 결정됩니다.
- [[SRS_Carrier_Switching]] (affects): 다중 반송파 환경에서 SRS 전송을 위해 반송파 간 스위칭이 발생할 수 있습니다.

## 관련 개념
- [[SRS_Power_Control]] (affects)
- [[SRS_Carrier_Switching]] (affects)
- [[SRS_Collision_Handling]] (affects)
- [[Sequence_Generation]] (part_of)
- [[Physical_Resource_Grid]] (part_of)

## 스펙 근거
- TS 38.211 §6.4.1.4: SRS 자원, 시퀀스 생성 및 물리 자원 매핑 규정
- TS 38.212 §7.3.1.1.2: DCI 포맷 0_1 내 SRS 자원 지시자 정의
- TS 38.212 §7.3.1.1.3: DCI 포맷 0_2 내 SRS 자원 지시자 정의
- TS 38.214 §6.2.1: UE SRS 전송 절차 및 주파수 호핑, 위치 측정 관련 규정

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03)
- 3GPP TS 38.212 V16.8.0 (2022-03)
- 3GPP TS 38.214 V16.9.0 (2022-03)
- 3GPP TS 38.822 V16.0.0 (2020-07)