# DMRS

## 정의
[[PDSCH]] 수신을 위한 복조 참조 신호(Demodulation Reference Signal)로, 채널 추정 및 복조를 위해 사용되는 UE-specific 참조 신호.

## 요약
[[PDSCH]]의 복조를 위해 사용되는 참조 신호로, 상위 계층 파라미터 및 [[DCI]]를 통해 설정되는 구성 타입(Type 1, Type 2, Enhanced Type 1, Enhanced Type 2)에 따라 자원 요소(RE)에 매핑된다. 다중 사용자 환경에서 직교성을 유지하기 위해 CDM(Code Division Multiplexing) 그룹을 사용하며, co-scheduled UE 간의 자원 충돌을 방지하기 위한 제약 조건을 가진다.

## 상세 설명
[[PDSCH]] DMRS는 TS 38.214 §5.1.6.2에 정의된 절차에 따라 수신된다.

- 구성 타입 및 설정:
  - 상위 계층 파라미터 [[dmrs-Type]] 및 [[dmrs-TypeEnh]]를 통해 구성 타입이 결정된다.
  - [[maxLength]] 파라미터가 'len1'인 경우 단일 심볼 DMRS가, 'len2'인 경우 단일 또는 이중 심볼 DMRS가 스케줄링될 수 있다.
  - [[dmrs-AdditionalPosition]]을 통해 추가적인 DMRS 심볼 위치('pos0'~'pos3')를 설정할 수 있다.
  - 스크램블링 식별자(scrambling identity)는 상위 계층을 통해 0 또는 1로 설정 가능하다.

- 안테나 포트 매핑 및 CDM:
  - [[DCI]] format 1_1 등을 통해 안테나 포트가 지시되며, 각 구성 타입에 따라 CDM 그룹 내에서 직교 포트가 할당된다.
  - UE는 할당된 CDM 그룹 내의 나머지 직교 안테나 포트가 다른 UE의 [[PDSCH]] 전송에 사용되지 않는다고 가정할 수 있다.

- co-scheduled UE 간 제약:
  - UE는 co-scheduled UE와 DMRS 구성(front-loaded 심볼 수, 추가 DMRS 수, 심볼 위치, 구성 타입)이 동일하다고 가정해야 한다.
  - 서로 다른 DMRS 구성 타입(예: Type 1과 Type 2)을 사용하는 UE 간의 co-scheduling은 허용되지 않는다.
  - 동일 CDM 그룹 내의 co-scheduled UE는 동일한 [[dmrs-TypeEnh]] 설정 상태를 공유해야 한다.

- QCL(Quasi-Co-Location):
  - [[SS_PBCH_Block_Generation]]과 동일한 OFDM 심볼에서 수신될 경우, 'QCL-TypeD' 관계를 가정할 수 있다.

## 인과 관계
- [[PDSCH]] depends_on [[DMRS]] (채널 추정 및 복조를 위한 필수 참조 신호)
- [[DMRS_Sequence_Generation]] implements [[DMRS]] (참조 신호 시퀀스 생성)
- [[DMRS_Resource_Mapping]] implements [[DMRS]] (자원 요소 매핑 규칙)
- [[PDSCH_DMRS_Reception]] depends_on [[DMRS]] (수신 절차 수행)

## 관련 개념
- [[PDSCH]] (affects)
- [[DMRS_Sequence_Generation]] (implements)
- [[DMRS_Resource_Mapping]] (implements)
- [[PDSCH_DMRS_Reception]] (depends_on)
- [[DCI]] (affects)

## 스펙 근거
- TS 38.214 §5.1.6.2: DM-RS reception procedure 및 co-scheduled UE 제약 조건 정의
- TS 38.211 §7.4.1.1: DM-RS 시퀀스 생성 및 자원 매핑 규칙

## 소스
- 3GPP TS 38.214 v18.0.0 (Release 18) §5.1.6.2
- 3GPP TS 38.211 v18.0.0 (Release 18) §7.4.1.1