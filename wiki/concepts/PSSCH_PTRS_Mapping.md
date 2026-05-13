# PSSCH_PTRS_Mapping

## 정의
[[PSSCH]] 전송 시 위상 잡음 보상을 위해 사용되는 [[PSSCH_PTRS_Generation]] 신호를 물리 자원 요소(Resource Element, RE)에 배치하는 절차를 의미한다.

## 요약
[[PSSCH]]에 할당된 자원 블록(Resource Block, RB) 내에서 특정 시간 및 주파수 규칙에 따라 [[PSSCH_PTRS_Generation]] 신호를 매핑한다. [[PSCCH]] 및 [[PSSCH_DMRS_Mapping]]과 충돌하지 않도록 설계되었으며, [[CRC_Calculation]] 결과값에 기반한 주파수 오프셋을 적용한다.

## 상세 설명
[[PSSCH]] PT-RS는 다음 조건이 모두 충족될 때 물리 자원에 매핑된다.
1. 해당 OFDM 심볼이 [[PSSCH]] 전송을 위해 할당된 심볼 범위 내에 존재함.
2. 해당 RE가 [[PSCCH]] 또는 [[PSSCH_DMRS_Mapping]]에 사용되지 않음.
3. 시간 및 주파수 인덱스가 정의된 규칙을 만족함.

시간 인덱스 결정 절차:
- [[PSSCH]] 할당 시작점으로부터 상대적인 시간 인덱스를 설정한다.
- [[PSSCH_DMRS_Mapping]] 심볼과 겹치는 경우 해당 심볼을 건너뛰고 다음 심볼을 선택하는 과정을 반복한다.

주파수 인덱스 결정 절차:
- 할당된 RB를 낮은 주파수부터 0부터 $N_{RB}^{PSSCH}-1$까지 번호를 매긴다.
- PT-RS가 매핑될 부반송파 인덱스 $k$는 다음 식을 따른다.
  $k = k_{ref}^{RE} + (i \cdot N_{RB}^{SC} + \text{offset}) \mod N_{RB}^{SC}$
- 여기서 $\text{offset}$은 [[PSCCH]]와 연관된 [[CRC_Calculation]] 결과값의 10진수 표현을 기반으로 결정된다.

[[PSSCH]] PT-RS는 [[PSCCH]] 또는 [[PSCCH_DMRS_Mapping]]이 포함된 RE에 매핑되지 않으며, 펑처링(puncturing)을 통해 해당 자원을 보호한다. 또한, 사이드링크 [[CSI_RS_Generation]]과 동일한 RE에 매핑되지 않도록 설계되었다.

## 인과 관계
- [[PSSCH_PTRS_Generation]] depends_on [[PSSCH_PTRS_Mapping]] (생성된 신호의 물리적 배치)
- [[PSSCH_PTRS_Mapping]] depends_on [[PSSCH_DMRS_Mapping]] (DMRS와 충돌 방지를 위한 자원 제외)
- [[PSSCH_PTRS_Mapping]] depends_on [[PSCCH_Resource_Mapping]] (PSCCH와 충돌 방지를 위한 자원 제외)
- [[PSSCH_PTRS_Mapping]] depends_on [[CRC_Calculation]] (주파수 오프셋 결정을 위한 파라미터 제공)

## 관련 개념
- [[PSSCH]] (part_of)
- [[PSCCH]] (affects)
- [[PSSCH_DMRS_Mapping]] (affects)
- [[PSSCH_PTRS_Generation]] (implements)
- [[CRC_Calculation]] (depends_on)

## 스펙 근거
- TS 38.211 §8.4.1.2.2에 따르면 PSSCH PT-RS의 물리 자원 매핑 규칙 및 시간/주파수 인덱스 결정 방식이 정의되어 있다.
- TS 38.211 §8.4.1.2.2의 Table 8.4.1.2.2-1은 PT-RS 매핑 파라미터 $K_{PT-RS}$를 규정한다.
- TS 38.214 §8.2.3 및 §8.4.3은 PT-RS 사용 여부 및 관련 파라미터를 명시한다.
- TS 38.212 §7.3.2는 PSCCH와 연관된 CRC 계산 방식을 정의한다.

## 소스
- 3GPP TS 38.211 V17.0.0 (Release 17) §8.4.1.2.2