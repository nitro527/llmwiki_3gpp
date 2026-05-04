# Synchronization Procedures

## 정의
[[Synchronization_Procedures]]는 [[UE]]가 네트워크에 접속하기 위해 수행하는 초기 셀 탐색(Cell search) 과정과, 상향링크 및 하향링크 간의 정렬을 유지하기 위한 전송 타이밍 조정(Transmission timing adjustments) 절차를 의미합니다.

## 요약
본 절차는 [[UE]]가 [[SS_PBCH_Block]]을 탐색하여 하향링크 동기를 획득하고, 시스템 정보를 수신하며, 이후 네트워크와의 통신 과정에서 상향링크 전송 타이밍을 정밀하게 제어하는 메커니즘을 포함합니다. 주요 기능은 다음과 같습니다.
- [필수(항상)] 1-1: Basic initial access channels and procedures
- [필수(항상)] 3-1: Basic DL control channel
- [필수(항상)] 7-1: Channel coding
- [필수(항상)] 0-0: Basic EN-DC procedures
- [필수(항상)] 3-0: Basic MAC procedures
- [필수(cap)] 1-10: Support of SCell without SS/PBCH block
- [선택] 47-k2: SL multi-channel access for dynamic channel access mode
- [선택] 47-m6: Transmitting SSB repetitions within one RB set
- [선택] 1-11: Support of CSI-RS RRM measurement for SCell without SS/PBCH block
- [선택] 15-1: Receiving NR sidelink
- [선택] 15-2: Transmitting NR sidelink mode 1 scheduled by NR Uu
- [선택] 15-3: Transmitting NR sidelink mode 2

## 상세 설명
### 셀 탐색 (Cell search)
[[UE]]는 초기 접속 시 [[SS_PBCH_Block]]을 사용하여 하향링크 동기를 획득합니다. 이 과정에서 [[UE]]는 [[Synchronization_Signal_Generation]]을 통해 생성된 [[PSS]]와 [[SSS]]를 검출하여 셀 ID를 식별하고, [[PBCH]]를 복호화하여 시스템 프레임 번호 및 기타 필수 정보를 획득합니다. 이 과정은 TS 38.213 §4.1에 정의된 바와 같이 셀의 타이밍과 주파수 동기를 맞추는 핵심 단계입니다.

### 전송 타이밍 조정 (Transmission timing adjustments)
[[UE]]는 하향링크 수신 타이밍을 기준으로 상향링크 전송 타이밍을 결정합니다. TS 38.213 §4.2에 따르면, [[UE]]는 네트워크로부터 수신한 [[Timing_Advance_Adjustment]] 명령을 통해 상향링크 전송 시점을 조정합니다. 이는 서로 다른 거리의 [[UE]]들이 기지국에서 동일한 시점에 신호를 수신할 수 있도록 하여, 상향링크 채널 간의 간섭을 최소화합니다.

## 인과 관계
- [[SS_PBCH_Block]] 수신 (triggers) [[Synchronization_Procedures]]
- [[Synchronization_Procedures]] (affects) [[Timing_Advance_Adjustment]]
- [[Timing_Advance_Adjustment]] (depends_on) [[UE]]의 상향링크 전송 시점

## 관련 개념
- [[SS_PBCH_Block]] (part_of)
- [[Timing_Advance_Adjustment]] (affects)
- [[Synchronization_Signal_Generation]] (depends_on)
- [[PBCH]] (part_of)

## 스펙 근거
- TS 38.213 §4.1: Cell search 절차 정의
- TS 38.213 §4.2: Transmission timing adjustments 절차 정의

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"