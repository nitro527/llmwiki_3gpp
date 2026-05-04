# Sidelink_Transmission_Procedures

## 정의
[[Sidelink_Transmission_Procedures]]는 [[UE]]가 [[LTE]] [[Sidelink]] 전송을 수행하기 위해 [[NR]] [[Uu]] 인터페이스를 통해 네트워크로부터 자원을 할당받거나 제어받는 절차를 의미합니다. 특히 [[DCI]] format 3_1을 사용하여 LTE Sidelink의 [[SPS]] (Semi-Persistent Scheduling)를 설정, 활성화 및 해제하는 메커니즘을 포함합니다.

## 요약
본 절차는 NR 기지국이 LTE Sidelink 전송을 스케줄링하는 모드 3(Mode 3) 동작을 지원합니다. UE는 [[PDCCH]]를 통해 수신된 DCI format 3_1을 기반으로 LTE Sidelink 자원을 할당받으며, SPS 설정과 관련된 활성화 및 해제 명령을 처리합니다.

## 상세 설명
TS 38.213 §16.6에 따라, NR Uu 인터페이스를 통해 LTE Sidelink 전송을 수행하는 UE는 다음과 같은 절차를 따릅니다.

1. **DCI 기반 제어**: UE는 [[RNTI]]로 스크램블링된 DCI format 3_1을 모니터링합니다. 이 DCI는 LTE Sidelink 전송을 위한 자원 할당 및 SPS 관련 제어 정보를 포함합니다.
2. **SPS 활성화 및 해제**: 
   - DCI format 3_1 내의 특정 필드 값에 따라 LTE Sidelink SPS가 활성화되거나 해제됩니다.
   - 활성화 시, UE는 DCI에 명시된 자원 할당 파라미터와 주기(periodicity)를 사용하여 주기적인 Sidelink 전송을 수행합니다.
   - 해제 시, UE는 즉시 해당 SPS 자원 사용을 중단합니다.
3. **UE Capability**: 해당 기능을 수행하기 위해 UE는 'Transmitting LTE sidelink mode 3 scheduled by NR Uu' (Feature 15-7) 능력을 지원해야 합니다.

## 인과 관계
- [[DCI]] format 3_1 수신 (triggers) -> [[Sidelink]] SPS 활성화/해제
- [[Sidelink]] SPS 설정 (affects) -> [[PSSCH]] 및 [[PSCCH]] 전송 자원 결정
- [[NR]] Uu 인터페이스 (depends_on) -> LTE [[Sidelink]] 모드 3 스케줄링

## 관련 개념
- [[Sidelink]] (part_of)
- [[DCI_Formats_Processing]] (depends_on)
- [[PSSCH]] (affects)
- [[PSCCH]] (affects)

## 스펙 근거
- TS 38.213 §16.6: UE procedure for LTE sidelink transmission
- TS 38.822: Feature 15-7 (Transmitting LTE sidelink mode 3 scheduled by NR Uu)

## 소스
- 3GPP TS 38.213 Release 18, "NR; Physical layer procedures for control"