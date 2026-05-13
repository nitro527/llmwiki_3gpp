# PRACH

## 정의
[[PRACH]]는 5G NR에서 단말이 네트워크에 초기 접속하거나, 동기화 상태를 유지하고, 상향링크 자원을 요청하기 위해 사용하는 물리 상향링크 채널입니다.

## 요약
[[PRACH]]는 랜덤 액세스 프리앰블을 전송하는 채널로, 시간 및 주파수 자원 상에서 특정 프리앰블 시퀀스를 통해 기지국과 통신을 시작합니다. 프리앰블 생성은 Zadoff-Chu 시퀀스를 기반으로 하며, 상위 계층 파라미터에 의해 설정된 자원 내에서 전송됩니다.

## 상세 설명
[[PRACH]]의 동작은 크게 프리앰블 시퀀스 생성과 물리 자원 매핑으로 나뉩니다.

### 프리앰블 생성
[[PRACH]] 프리앰블은 TS 38.211 §6.3.3.1에 따라 생성됩니다. 각 시간-주파수 자원(RACH occasion)에는 64개의 프리앰블이 정의됩니다. 프리앰블 시퀀스는 논리적 루트 시퀀스 인덱스(rootSequenceIndex)와 순환 시프트(cyclic shift)를 사용하여 생성됩니다.
- 루트 시퀀스 인덱스는 상위 계층 파라미터(prach-RootSequenceIndex 등)를 통해 결정됩니다.
- 순환 시프트 값은 제한된 세트(unrestricted, restricted type A, restricted type B) 설정에 따라 결정되며, 이는 프리앰블 포맷에 따라 지원 여부가 달라집니다.

### 물리 자원 매핑
[[PRACH]] 프리앰블은 TS 38.211 §6.3.3.2에 따라 물리 자원에 매핑됩니다.
- 시간 자원: 기지국이 설정한 PRACH configuration index에 따라 결정되며, FR1, FR2, FR2-NTN 등 주파수 대역 및 스펙트럼 유형에 따라 테이블이 구분됩니다.
- 주파수 자원: 상위 계층 파라미터(msg1-FrequencyStart, msg1-FDM 등)를 통해 초기 상향링크 대역폭 부분(BWP) 내에서 시작 위치와 FDM 개수가 결정됩니다.
- 전력 제어: 프리앰블 전송 시 전력은 TS 38.213에 명시된 전력 제어 절차를 따르며, 진폭 스케일링 인자(amplitude scaling factor)가 적용됩니다.

### 제어 및 설정
[[PRACH]] 전송은 [[PDCCH]]를 통한 PDCCH order에 의해 트리거될 수 있으며, 이때 [[DCI_Format_1_0]]이 사용됩니다. DCI 내의 Random Access Preamble index, SS/PBCH index, PRACH Mask index 필드 등이 실제 전송될 프리앰블과 RACH occasion을 결정하는 데 사용됩니다.

## 인과 관계
- [[PRACH_Preamble_Generation]] implements [[PRACH]] (프리앰블 시퀀스 생성 로직 구현)
- [[PRACH_Power_Control]] affects [[PRACH]] (전송 전력 제어)
- [[DCI_Format_1_0]] triggers [[PRACH]] (PDCCH order를 통한 랜덤 액세스 절차 시작)
- [[Frame_Structure]] depends_on [[PRACH]] (RACH occasion의 시간 자원 위치 결정)

## 관련 개념
- [[PRACH_Preamble_Generation]] (implements)
- [[PRACH_Power_Control]] (affects)
- [[DCI_Format_1_0]] (triggers)
- [[Frame_Structure]] (depends_on)
- [[Random_Access_Response]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.3.1: 프리앰블 시퀀스 생성 및 루트 시퀀스 인덱스 설정
- TS 38.211 §6.3.3.2: 물리 자원 매핑 및 PRACH configuration index
- TS 38.212 §7.3.1.2.1: DCI format 1_0을 통한 PRACH 제어 필드 정의

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03)
- 3GPP TS 38.212 V17.9.0 (2024-03)
- 3GPP TS 38.213 V17.9.0 (2024-03)