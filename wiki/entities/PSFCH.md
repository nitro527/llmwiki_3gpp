# PSFCH

## 정의
[[PSFCH]]는 [[Sidelink]] 통신에서 수신측 [[UE]]가 송신측 [[UE]]에게 [[HARQ]] 피드백 정보를 전달하기 위해 사용하는 물리 채널입니다.

## 요약
[[PSFCH]]는 [[Sidelink]] 전송의 신뢰성을 높이기 위해 도입된 물리 채널로, 주로 [[PSSCH]]를 통해 수신된 데이터에 대한 [[HARQ]]-ACK 정보를 전송합니다. TS 38.211 §8.3.4에 정의된 바와 같이, [[PSFCH]]는 [[PSFCH]] format 0를 지원하며, 특정 자원 풀 내에서 시퀀스 기반으로 자원을 할당받아 동작합니다.

## 상세 설명
[[PSFCH]]는 [[Sidelink]] 모드 2 동작에서 [[HARQ]] 피드백을 지원하기 위해 사용됩니다. 

- 시퀀스 생성: [[PSFCH]] format 0는 TS 38.211 §8.3.4.2.1에 따라 특정 시퀀스를 생성하여 전송합니다. 이 시퀀스는 [[HARQ]]-ACK 정보에 따라 결정됩니다.
- 자원 매핑: TS 38.211 §8.3.4.2.2에 따라, [[PSFCH]]는 구성된 자원 풀 내의 물리 자원에 매핑됩니다. 이때 [[PSFCH]] 자원은 [[PSSCH]] 전송과 연관된 슬롯 및 자원 블록 인덱스에 기반하여 결정됩니다.
- [[Sidelink]] 피드백: 수신측 [[UE]]는 [[PSSCH]]를 통해 데이터를 수신한 후, 해당 데이터에 대한 성공 여부를 [[PSFCH]]를 통해 송신측 [[UE]]에게 보고합니다.

## 인과 관계
- [[PSSCH]] (depends_on) [[PSFCH]]: [[PSFCH]]는 [[PSSCH]] 전송에 대한 피드백을 제공하기 위해 존재합니다.
- [[Sidelink]] (part_of) [[PSFCH]]: [[PSFCH]]는 [[Sidelink]] 시스템의 물리 계층 채널 중 하나입니다.
- [[HARQ]] (affects) [[PSFCH]]: [[HARQ]] 피드백 정보가 [[PSFCH]]의 시퀀스 내용을 결정합니다.

## 관련 개념
- [[Sidelink]] (part_of)
- [[PSSCH]] (depends_on)
- [[HARQ]] (affects)
- [[PSFCH_Processing]] (triggers)

## 스펙 근거
- TS 38.211 §8.3.4: [[PSFCH]]의 일반적인 정의 및 물리 계층 구조
- TS 38.211 §8.3.4.2.1: [[PSFCH]] format 0의 시퀀스 생성 방식
- TS 38.211 §8.3.4.2.2: [[PSFCH]]의 물리 자원 매핑 규칙
- TS 38.213 §16.2.3: [[PSFCH]] 관련 절차 및 동작

## 소스
- 3GPP TS 38.211 "Physical channels and modulation"
- 3GPP TS 38.213 "Physical layer procedures for control"