# Sidelink

## 정의
[[Sidelink]]는 기지국(gNB)을 거치지 않고 사용자 단말(UE) 간에 직접 데이터를 송수신하는 [[NR]]의 무선 인터페이스 기술을 의미합니다.

## 요약
[[Sidelink]]는 근접한 UE 간의 직접 통신을 지원하며, 물리 채널인 [[PSSCH]], [[PSCCH]], [[PSBCH]], [[PSFCH]]와 물리 신호인 [[S-SS/PSBCH 블록]], [[SL PRS]]를 통해 제어 정보, 데이터, 동기화 및 위치 측정 정보를 교환합니다. 주요 기능으로 모드 1(네트워크 스케줄링) 및 모드 2(단말 자율 선택) 자원 할당 방식을 지원하며, [[HARQ]] 피드백 및 [[CSI]] 보고 절차를 포함합니다.

## 상세 설명
[[Sidelink]] 통신은 다음과 같은 물리 채널 및 신호를 기반으로 동작합니다.

* [[PSSCH]] (Physical Sidelink Shared Channel): 사용자 데이터를 전송하는 채널로, [[SCI]]에 의해 자원이 할당됩니다.
* [[PSCCH]] (Physical Sidelink Control Channel): [[PSSCH]]의 복조 및 디코딩에 필요한 제어 정보인 [[SCI]]를 전송합니다.
* [[PSBCH]] (Physical Sidelink Broadcast Channel): [[S-SS/PSBCH 블록]]의 일부로, 시스템 정보 및 동기화 관련 정보를 전송합니다.
* [[PSFCH]] (Physical Sidelink Feedback Channel): [[HARQ]]-ACK 피드백을 전송하기 위해 사용됩니다.
* [[S-SS/PSBCH 블록]]: [[Sidelink]] 동기화를 위한 신호 세트로, [[S-PSS]], [[S-SSS]] 및 [[PSBCH]]로 구성됩니다.
* [[SL PRS]] (Sidelink Positioning Reference Signal): UE 간 위치 측정을 위한 참조 신호입니다.

UE는 [[Sidelink]] 자원 할당 모드에 따라 동작합니다. 모드 1에서는 기지국이 [[DCI]]를 통해 자원을 스케줄링하며, 모드 2에서는 UE가 센싱(Sensing) 결과를 바탕으로 자원을 직접 선택합니다. 또한, [[SL Carrier Aggregation]]을 통해 다중 캐리어 환경에서의 통신을 지원하며, [[In-device Coexistence]] 및 [[Co-channel Coexistence]]를 위한 절차를 수행합니다.

## 인과 관계
- [[Sidelink]] (depends_on) [[Synchronization Procedures]]
- [[Sidelink]] (depends_on) [[Sidelink Resource Allocation Procedures]]
- [[Sidelink]] (affects) [[Sidelink Power Control]]
- [[Sidelink]] (triggers) [[Sidelink HARQ Reporting]]
- [[Sidelink]] (part_of) [[PSSCH]]
- [[Sidelink]] (part_of) [[PSCCH]]
- [[Sidelink]] (part_of) [[PSBCH]]
- [[Sidelink]] (part_of) [[PSFCH]]
- [[Sidelink]] (part_of) [[S-SS/PSBCH 블록]]
- [[Sidelink]] (part_of) [[SL PRS]]

## 관련 개념
- [[Sidelink Transmission Procedures]] (depends_on)
- [[Sidelink Resource Selection]] (depends_on)
- [[Sidelink Congestion Control]] (depends_on)
- [[Sidelink Reference Signals]] (part_of)
- [[Half Duplex UE Operation]] (affects)

## 스펙 근거
- TS 38.211 §8.1: [[Sidelink]] 물리 채널 및 신호 개요
- TS 38.213 §16: [[Sidelink]] UE 절차 (동기화, 전력 제어, 자원 할당, [[HARQ]] 피드백)
- TS 38.214 §8: [[Sidelink]] 전송 및 수신 절차, 자원 할당, [[CSI]] 보고

## 소스
- 3GPP TS 38.211 "Physical channels and modulation"
- 3GPP TS 38.213 "Physical layer procedures for control"
- 3GPP TS 38.214 "Physical layer procedures for data"