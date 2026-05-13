# PRACH_Preamble_Generation

## 정의
[[PRACH]] 랜덤 액세스 프리앰블 생성은 [[UE]]가 상향링크를 통해 기지국에 랜덤 액세스 절차를 시작하기 위해 사용하는 Zadoff-Chu 시퀀스 기반의 물리 계층 신호 생성 및 이를 특정 시간-주파수 자원에 매핑하는 절차를 의미합니다.

## 요약
랜덤 액세스 프리앰블은 루트 시퀀스(Root Sequence)로부터 순환 시프트(Cyclic Shift)를 적용하여 생성됩니다. 생성된 64개의 프리앰블은 [[SS_PBCH_Block_Generation]] 인덱스와 연관된 [[PRACH]] 자원(RO, RACH Occasion)에 매핑되며, 이는 Type-1 및 Type-2 랜덤 액세스 절차에 따라 구성됩니다.

## 상세 설명
### 프리앰블 시퀀스 생성
TS 38.211 §6.3.3.1에 따르면, 랜덤 액세스 프리앰블은 Zadoff-Chu 시퀀스를 기반으로 생성됩니다. 각 RO 내에서 64개의 프리앰블이 정의되며, 이는 논리적 루트 시퀀스 인덱스의 증가 순서와 해당 루트 시퀀스 내의 순환 시프트 값의 증가 순서에 따라 열거됩니다.
- 루트 시퀀스 인덱스는 상위 계층 파라미터(예: `prach-RootSequenceIndex`)에 의해 결정됩니다.
- 순환 시프트 $N_{CS}$는 프리앰블 포맷 및 제한된 세트(Unrestricted, Restricted Type A/B) 설정에 따라 결정됩니다.
- 64개의 프리앰블을 단일 루트 시퀀스로 생성할 수 없는 경우, 연속적인 논리적 인덱스를 가진 루트 시퀀스를 순환적으로 사용하여 추가 시퀀스를 확보합니다.

### SS/PBCH 블록과 PRACH 자원 매핑
TS 38.213 §8.1에 따라, [[UE]]는 상위 계층으로부터 SS/PBCH 블록 인덱스와 RO 간의 연관 관계를 제공받습니다.
- 매핑 순서: 
  1. 단일 RO 내 프리앰블 인덱스 증가 순
  2. 주파수 다중화된 RO의 주파수 자원 인덱스 증가 순
  3. [[Slot]] 내 시간 다중화된 RO의 시간 자원 인덱스 증가 순
  4. [[Slot]] 인덱스 증가 순
- 연관 주기(Association Period): SS/PBCH 블록 인덱스가 최소 한 번 이상 RO에 매핑되도록 하는 최소 정수 주기를 의미하며, 이는 `ssb-PositionsInBurst` 파라미터를 통해 결정됩니다.
- Type-1 및 Type-2 랜덤 액세스 절차에 따라 `ssb-perRACH-OccasionAndCB-PreamblesPerSSB` 등의 파라미터를 사용하여 특정 SS/PBCH 블록당 할당된 프리앰블 개수와 RO 개수를 결정합니다.

### 유효성 검사
비면허 대역(Unpaired spectrum)의 경우, RO가 SS/PBCH 블록과 겹치지 않아야 하며, 특정 심볼 간격(Table 8.1-2 참조)을 준수해야 하는 등 추가적인 유효성 조건이 적용됩니다.

## 인과 관계
- [[PRACH]] depends_on [[PRACH_Preamble_Generation]] (프리앰블 생성은 PRACH 전송의 필수 단계)
- [[PRACH_Preamble_Generation]] affects [[SS_PBCH_Block_Generation]] (SSB 인덱스 기반 자원 매핑을 통해 연동)
- [[PRACH_Preamble_Generation]] depends_on [[Frame_Structure]] (RO 매핑을 위한 슬롯 및 프레임 구조 참조)

## 관련 개념
- [[PRACH]] (part_of)
- [[SS_PBCH_Block_Generation]] (affects)
- [[Frame_Structure]] (depends_on)
- [[Slot]] (part_of)

## 스펙 근거
- TS 38.211 §6.3.3.1: 랜덤 액세스 프리앰블 시퀀스 생성 및 순환 시프트 파라미터 정의
- TS 38.213 §8.1: 랜덤 액세스 프리앰블 절차, SS/PBCH 블록과 RO 간의 매핑 규칙, RO 유효성 조건

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03)
- 3GPP TS 38.213 V17.9.0 (2024-03)