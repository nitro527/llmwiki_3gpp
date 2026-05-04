# Sidelink_PTRS_Generation_Mapping

## 정의
[[Sidelink_PTRS_Generation_Mapping]]은 [[PSSCH]] 전송 시 위상 잡음(Phase Noise)을 보상하기 위해 사용되는 [[PT_RS]]의 시퀀스 생성 및 물리 자원 매핑 절차를 의미합니다.

## 요약
[[Sidelink_PTRS_Generation_Mapping]]은 [[PSSCH]]의 복조 성능을 향상시키기 위해 위상 추적 참조 신호를 생성하고 이를 [[Physical_Resource_Grid]]에 배치하는 과정을 정의합니다. 본 기능과 관련된 UE Feature는 다음과 같습니다.

* [필수(cap)] 2-44: Basic DL PTRS
* [필수(cap)] 2-47: Basic UL PTRS
* [선택] 2-46: Downlink PTRS density recommendation
* [선택] 2-48: Uplink PTRS
* [선택] 2-49: Uplink PTRS density recommendation
* [선택] 15-1: Receiving NR sidelink
* [선택] 15-3: Transmitting NR sidelink mode 2
* [선택] 15-22: Support of fewer than 14 consecutive sidelink symbols in a slot
* [선택] 16-2b-1a: Downlink PTRS
* [선택] 32-4: Transmitting NR sidelink mode 2 with partial sensing
* [선택] 32-4a: Transmitting NR sidelink mode 2 with random resource selection
* [선택] 37-7: SCG Failure Report for MRO

## 상세 설명
[[PSSCH]]를 위한 [[PT_RS]]는 송신단과 수신단 사이의 위상 잡음 영향을 완화하기 위해 설계되었습니다.

### 시퀀스 생성
[[PT_RS]] 시퀀스는 [[TS_38_211]] §8.4.1.2.1에 따라 생성됩니다. 시퀀스 생성은 [[Sequence_Generation]]의 기본 원리를 따르며, 특정 초기화 값에 의해 결정되는 의사 난수 시퀀스를 기반으로 합니다.

### 물리 자원 매핑
[[PT_RS]]는 [[TS_38_211]] §8.4.1.2.2에 따라 [[PSSCH]]가 할당된 자원 블록 내의 특정 부반송파와 심볼 위치에 매핑됩니다. 이 과정은 [[Sidelink_Resource_Grid]] 상에서 데이터 심볼과의 간섭을 최소화하고 위상 추적 효율을 극대화하도록 구성됩니다.

## 인과 관계
* [[Sidelink_Transmission_Parameters]] (depends_on): [[PT_RS]]의 설정은 전송 파라미터에 따라 결정됩니다.
* [[PSSCH_Resource_Mapping]] (affects): [[PT_RS]]가 매핑되는 자원은 [[PSSCH]]의 자원 할당 결과에 영향을 받습니다.
* [[Sidelink_Reference_Signals]] (part_of): [[PT_RS]]는 사이드링크 참조 신호 체계의 일부입니다.

## 관련 개념
- [[PSSCH]] (part_of)
- [[PT_RS]] (similar_to)
- [[Sidelink_Resource_Grid]] (depends_on)
- [[Sequence_Generation]] (depends_on)

## 스펙 근거
* TS 38.211 §8.4.1.2.1: [[PT_RS]] 시퀀스 생성 절차 정의
* TS 38.211 §8.4.1.2.2: [[PT_RS]]의 물리 자원 매핑 규칙 정의

## 소스
* 3GPP TS 38.211 V17.0.0 (Release 17)