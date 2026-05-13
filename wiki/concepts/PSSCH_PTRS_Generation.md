# PSSCH_PTRS_Generation

## 정의
PSSCH_PTRS_Generation은 사이드링크 통신에서 위상 잡음(Phase Noise)으로 인한 성능 저하를 보상하기 위해 [[PSSCH]] 전송 시 사용하는 [[PT-RS]] 시퀀스를 생성하는 절차를 의미한다.

## 요약
[[PSSCH]]를 위한 [[PT-RS]]는 프리코딩된(precoded) 형태로 생성되며, 특정 안테나 포트와 레이어에 대해 정의된다. 시퀀스 생성은 [[DMRS]]와 연관된 심볼 위치 및 파라미터를 기반으로 수행된다.

## 상세 설명
[[PSSCH]]를 위한 프리코딩된 [[PT-RS]] 시퀀스는 레이어 $i$의 서브캐리어 $k$에 대해 다음과 같이 정의된다.

$r_{PT-RS, i}(k) = r_{m, n}^{p}(k)$

여기서 각 파라미터의 정의는 다음과 같다.
- 안테나 포트 $p$는 [[TS 38.214]]의 8.2.3 절에 따라 [[PT-RS]] 전송과 연관된 포트로 결정된다.
- 시퀀스 생성에 사용되는 파라미터는 연관된 [[DMRS]]가 포함된 첫 번째 [[PSSCH]] 심볼의 위치에서 [[TS 38.211]] 8.4.1.1.1 절에 정의된 값을 따른다.

[[PT-RS]]는 위상 잡음이 심한 고주파 대역에서 수신기의 위상 추적 성능을 향상시키기 위해 삽입되며, [[PSSCH]]의 데이터 심볼과 함께 다중화되어 전송된다.

## 인과 관계
- [[PSSCH_PTRS_Generation]] depends_on [[PSSCH_DMRS_Generation]] (DMRS 파라미터 참조)
- [[PSSCH_PTRS_Generation]] triggers [[PSSCH_PTRS_Mapping]] (생성된 시퀀스의 자원 매핑)

## 관련 개념
- [[PSSCH]] (part_of)
- [[PT-RS]] (implements)
- [[DMRS]] (depends_on)

## 스펙 근거
- TS 38.211 §8.4.1.2.1: Sequence generation for PSSCH PT-RS

## 소스
- 3GPP TS 38.211 V18.0.0, "NR; Physical channels and modulation"