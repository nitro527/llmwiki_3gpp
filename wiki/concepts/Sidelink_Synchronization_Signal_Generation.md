# Sidelink_Synchronization_Signal_Generation

## 정의
[[Sidelink]] 통신에서 [[UE]] 간의 시간 및 주파수 동기를 맞추기 위해 사용되는 [[S-PSS]](Sidelink Primary Synchronization Signal) 및 [[S-SSS]](Sidelink Secondary Synchronization Signal)의 시퀀스 생성 및 물리 자원 매핑 절차를 의미한다.

## 요약
[[Sidelink]] 동기화는 [[S-SSB]](Sidelink SS/PBCH block)를 통해 이루어지며, 이는 [[S-PSS]], [[S-SSS]], 그리고 [[PSBCH]]로 구성된다. 각 신호는 고유한 시퀀스 생성 규칙을 따르며, [[S-SS/PSBCH block]] 내의 특정 시간-주파수 자원에 매핑되어 전송된다.

## 상세 설명
### Physical-layer sidelink synchronization identities
[[S-PSS]] 및 [[S-SSS]]는 [[Sidelink]] 동기화 식별자(N_ID_SL)를 기반으로 생성된다. 이 식별자는 0부터 671까지의 값을 가지며, [[S-PSS]]와 [[S-SSS]]의 조합을 통해 결정된다.

### S-PSS 시퀀스 생성 및 매핑
- **시퀀스 생성**: [[S-PSS]]는 m-sequence를 기반으로 생성되며, [[Sidelink]] 동기화 식별자의 하위 2개 값에 의해 결정된다 (TS 38.211 §8.4.2.2.1).
- **자원 매핑**: [[S-PSS]]는 [[S-SS/PSBCH block]] 내에서 127개의 부반송파를 점유하며, 특정 OFDM 심볼에 매핑된다 (TS 38.211 §8.4.2.2.2, §8.4.3.1.1).

### S-SSS 시퀀스 생성 및 매핑
- **시퀀스 생성**: [[S-SSS]]는 Gold sequence를 기반으로 생성되며, [[Sidelink]] 동기화 식별자의 상위 336개 값에 의해 결정된다 (TS 38.211 §8.4.2.3.1).
- **자원 매핑**: [[S-SSS]] 또한 [[S-SS/PSBCH block]] 내에서 127개의 부반송파를 점유하며, [[S-PSS]]와 인접한 심볼에 매핑된다 (TS 38.211 §8.4.2.3.2, §8.4.3.1.2).

### S-SS/PSBCH block 구조
[[S-SS/PSBCH block]]은 시간 도메인에서 11개의 OFDM 심볼로 구성된다. [[S-PSS]]와 [[S-SSS]]는 이 블록 내에서 고정된 위치에 배치되어 [[UE]]가 동기 신호를 효율적으로 탐색할 수 있도록 한다 (TS 38.211 §8.4.3.1).

## 인과 관계
- [[Sidelink]] 동기화 식별자(N_ID_SL) 결정 (triggers) [[S-PSS]] 및 [[S-SSS]] 시퀀스 생성
- [[S-PSS]] 및 [[S-SSS]] 시퀀스 생성 (part_of) [[S-SS/PSBCH block]] 구성
- [[S-SS/PSBCH block]] 구성 (affects) [[Sidelink]] 시스템의 시간 및 주파수 동기화 정확도

## 관련 개념
- [[Sidelink]] (part_of)
- [[S-SSB]] (part_of)
- [[PSBCH]] (similar_to)
- [[Synchronization_Procedures]] (depends_on)

## 스펙 근거
- TS 38.211 §8.4.2: Sidelink synchronization signals 정의 및 시퀀스 생성 규칙
- TS 38.211 §8.4.3.1: S-SS/PSBCH block의 시간-주파수 구조 및 자원 매핑

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03) Physical channels and modulation