# PSFCH_Resource_Mapping

## 정의
[[PSFCH]] 전송을 위해 생성된 시퀀스를 물리적 자원 요소(Resource Elements, RE)에 매핑하고, 특정 조건에 따라 인터레이스(Interlace) 구조를 적용하며 심볼 복제를 수행하는 절차를 의미한다.

## 요약
[[PSFCH]]는 할당된 물리적 자원 상에서 시퀀스 매핑을 수행하며, 신뢰성 향상을 위해 인접한 OFDM 심볼로의 복제(Duplication)를 수행한다. 상위 계층 파라미터 설정에 따라 인터레이스 기반의 자원 매핑이 적용될 수 있다.

## 상세 설명
[[PSFCH]] 시퀀스는 전송 전력 규정을 준수하기 위해 진폭 스케일링 계수와 곱해진 후, 할당된 물리적 자원 요소에 매핑된다.

1. 기본 매핑 절차:
   - 시퀀스는 TS 38.213 §16.3에 정의된 두 번째 [[PSFCH]] 심볼에 할당된 자원 요소에 매핑된다.
   - 매핑은 할당된 물리적 자원 내에서 인덱스 $k$의 증가 순서대로 수행된다.
   - 매핑이 수행된 OFDM 심볼의 자원 요소는 바로 직전의 OFDM 심볼에 동일하게 복제된다.

2. 인터레이스 기반 매핑:
   - 상위 계층 파라미터 `sl-TransmissionStructureForPSFCH`가 'dedicatedInterlace'로 설정된 경우:
     - 할당된 물리적 자원 블록(Physical Resource Block, PRB) 내의 각 인터레이스 및 RB 세트에 대해 매핑이 반복된다.
     - 각 RB에 의존적인 시퀀스가 [[PSFCH_Sequence_Generation]]에 따라 생성되어 적용된다.
   - 상위 계층 파라미터 `sl-TransmissionStructureForPSFCH`가 'commonInterlace'로 설정된 경우:
     - 할당된 물리적 자원 블록 내의 각 RB에 대해 매핑이 반복된다.
     - 첫 번째 인터레이스의 각 RB에 적용되는 순환 시프트(Cyclic Shift) 값은 UE 구현에 따른다.

## 인과 관계
- [[PSFCH_Sequence_Generation]] depends_on [[PSFCH_Resource_Mapping]] (시퀀스 생성 결과가 매핑 절차의 입력으로 사용됨)
- [[PSFCH_Resource_Mapping]] affects [[PSFCH]] (물리적 자원 상의 신호 배치 결정)

## 관련 개념
- [[PSFCH]] (part_of)
- [[PSFCH_Sequence_Generation]] (depends_on)

## 스펙 근거
- TS 38.211 §8.3.4.2.2: PSFCH의 물리적 자원 매핑, 심볼 복제, 인터레이스 구조 설정 및 매핑 규칙 정의

## 소스
- 3GPP TS 38.211 V16.9.0 (Release 16)