# PDSCH_Layer_Mapping

## 정의
[[PDSCH]]의 코드워드(codeword) 단위로 생성된 복소 변조 심볼들을 공간 다중화(spatial multiplexing)를 위해 하나 이상의 레이어(layer)로 분배하는 물리 계층 절차를 의미한다.

## 요약
[[PDSCH]] 전송을 위해 준비된 복소 변조 심볼들은 전송 레이어 수에 따라 정의된 매핑 규칙에 따라 레이어에 할당된다. 이 과정은 공간 다중화를 지원하며, 코드워드와 레이어 간의 관계는 TS 38.211의 테이블에 명시된 매핑 방식을 따른다.

## 상세 설명
[[PDSCH]] 전송 시, 각 코드워드 $q$에 대한 복소 변조 심볼들은 하나 이상의 레이어 $v$로 매핑된다. 

1. 기본 동작:
   - 각 코드워드 $q$의 복소 변조 심볼들은 레이어 $0, 1, \dots, \nu-1$로 매핑된다.
   - 여기서 $\nu$는 전송 레이어의 총 개수를 나타낸다.
   - 각 레이어당 변조 심볼의 개수는 $M_{symb}^{layer}$로 정의된다.

2. 매핑 절차:
   - TS 38.211 §7.3.1.3의 Table 7.3.1.3-1에 따라, 코드워드 수와 레이어 수의 조합에 따른 매핑 방식이 결정된다.
   - 단일 코드워드 전송 시에는 해당 코드워드의 심볼들이 모든 레이어에 순차적으로 분배된다.
   - 다중 코드워드 전송 시에는 각 코드워드가 특정 레이어 집합에 할당되어 공간 다중화가 수행된다.

3. 특수 케이스:
   - 다중 [[mTRP]] 환경에서의 [[DCI]] 기반 전송이나 멀티캐스트 [[PDSCH]] 전송 시, 지원되는 최대 MIMO 레이어 수에 따라 매핑 규칙이 조정될 수 있다.
   - [[PDSCH]] 매핑 타입 A 및 B에 따라 심볼의 가용성이 달라지며, 이는 레이어 매핑 이후의 자원 매핑 단계와 연계된다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_Layer_Mapping]] (변조 심볼의 레이어 할당을 통한 공간 다중화 수행)
- [[PDSCH_Layer_Mapping]] affects [[PDSCH_Resource_Mapping]] (레이어별 심볼이 물리 자원 요소에 매핑되는 기준 제공)

## 관련 개념
- [[PDSCH]] (part_of)
- [[PDSCH_Resource_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §7.3.1.3: Codeword-to-layer mapping for spatial multiplexing에 대한 정의 및 Table 7.3.1.3-1 명시

## 소스
- 3GPP TS 38.211 V17.0.0, "Physical channels and modulation"