# PUSCH_Layer_Mapping

## 정의
[[PUSCH]] 레이어 매핑은 [[Modulation_Mapper]]를 통해 생성된 복소수 변조 심볼들을 하나 이상의 전송 레이어에 할당하는 물리 계층 절차를 의미합니다.

## 요약
[[PUSCH]] 전송을 위해 생성된 변조 심볼들은 지정된 레이어 수에 따라 분배됩니다. 이 과정은 다중 안테나 전송을 지원하기 위한 필수 단계이며, 코드워드 단위의 심볼을 공간적으로 다중화된 레이어에 매핑하여 최종적으로 [[PUSCH_Precoding]] 단계로 전달합니다.

## 상세 설명
[[PUSCH]] 전송을 위해 생성된 복소수 변조 심볼들은 최대 4개의 레이어로 매핑됩니다. TS 38.211 §6.3.1.3에 따라, 코드워드 $q$에 대한 복소수 변조 심볼 $d^{(q)}(0), \dots, d^{(q)}(M_{symb}^{(q)}-1)$은 레이어 $x(i) = [x^{(0)}(i) \dots x^{(\nu-1)}(i)]^T$로 매핑됩니다.

여기서 $\nu$는 전송 레이어의 수이며, $M_{symb}^{(layer)}$는 각 레이어당 변조 심볼의 수를 나타냅니다. 매핑 규칙은 TS 38.211의 Table 7.3.1.3-1을 따르며, 이는 전송되는 코드워드 수와 레이어 구성에 따라 결정됩니다. 

이 절차는 단일 코드워드 전송뿐만 아니라, 다중 안테나 기술을 활용한 코드북 기반 및 비코드북 기반 [[PUSCH]] 전송 시에도 동일하게 적용됩니다. 또한, 다중 TRP 환경에서의 반복 전송이나 설정된 그랜트 기반의 전송 시에도 해당 레이어 매핑 규칙을 통해 심볼이 공간적으로 분산됩니다.

## 인과 관계
- [[Modulation_Mapper]] depends_on [[PUSCH_Layer_Mapping]] (변조 심볼 생성 후 레이어 매핑 수행)
- [[PUSCH_Layer_Mapping]] affects [[PUSCH_Precoding]] (매핑된 레이어 데이터를 기반으로 프리코딩 수행)

## 관련 개념
- [[PUSCH]] (part_of)
- [[Modulation_Mapper]] (depends_on)
- [[PUSCH_Precoding]] (affects)

## 스펙 근거
- TS 38.211 §6.3.1.3: Layer mapping 절차 및 레이어 매핑 규칙 정의

## 소스
- 3GPP TS 38.211 V16.9.0, "Physical channels and modulation"