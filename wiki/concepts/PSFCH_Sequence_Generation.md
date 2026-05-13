# PSFCH_Sequence_Generation

## 정의
[[PSFCH]] format 0에서 사용하는 시퀀스를 생성하기 위한 절차로, 상위 계층 파라미터 및 슬롯 내 자원 위치 정보를 기반으로 시퀀스 초기화 및 호핑 파라미터를 결정하는 과정이다.

## 요약
[[PSFCH]] format 0 시퀀스는 TS 38.211 §6.3.2.2에 정의된 기본 시퀀스 생성 방식을 따르되, 슬롯 내 심볼 인덱스, 인터레이스 설정, 그리고 호핑 ID를 반영하여 생성된다. 특히 상위 계층 파라미터인 sl-TransmissionStructureForPSFCH 설정에 따라 자원 블록 번호 계산 방식이 달라지며, sl-PSFCH-HopID 설정 여부에 따라 시퀀스 초기화 값이 결정된다.

## 상세 설명
[[PSFCH]] format 0의 시퀀스 $r(m)$은 TS 38.211 §8.3.4.2.1에 따라 생성된다.

1. 기본 시퀀스 생성: TS 38.211 §6.3.2.2의 절차를 따르며, 시퀀스 생성에 필요한 파라미터 $c_{init}$는 TS 38.213 §16.3에 정의된 값을 사용한다.
2. 자원 블록 번호($n_{ID}^{PSFCH}$):
   - 상위 계층 파라미터 sl-TransmissionStructureForPSFCH가 'dedicatedInterlace'로 설정된 경우, $n_{ID}^{PSFCH}$는 해당 인터레이스 내의 자원 블록 번호로 결정된다.
   - 그 외의 경우 $n_{ID}^{PSFCH} = 0$으로 설정된다.
3. 심볼 인덱스($l'$):
   - $l'$은 슬롯 내 OFDM 심볼 인덱스로, TS 38.213에 따라 결정된 [[PSFCH]] 전송의 두 번째 OFDM 심볼에 대응하는 값을 사용한다.
4. 호핑 파라미터:
   - 상위 계층 파라미터 sl-PSFCH-HopID가 설정된 경우, 해당 값을 사용하여 시퀀스 생성 파라미터를 결정한다.
   - 설정되지 않은 경우, 기본값으로 0을 사용한다.

## 인과 관계
- [[PSFCH]] depends_on [[PSFCH_Sequence_Generation]] (시퀀스 생성 절차를 통해 물리 신호 구성)
- [[PSFCH_Resource_Mapping]] depends_on [[PSFCH_Sequence_Generation]] (생성된 시퀀스를 자원에 매핑)

## 관련 개념
- [[PSFCH]] (part_of)
- [[PSFCH_Resource_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §8.3.4.2.1: Sequence generation for PSFCH format 0
- TS 38.211 §6.3.2.2: Sequence generation (base procedure)
- TS 38.213 §16.3: PSFCH related parameters

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03) Physical channels and modulation