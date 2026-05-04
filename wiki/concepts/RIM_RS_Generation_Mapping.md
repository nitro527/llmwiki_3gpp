# RIM_RS_Generation_Mapping

## 정의
[[RIM_RS_Generation_Mapping]]은 [[Reference_Signals]]의 일종인 RIM-RS(Remote Interference Management Reference Signal)를 생성하고 이를 물리 자원에 매핑하는 절차를 의미합니다. 이는 주로 네트워크 노드 간의 간섭을 관리하고 측정하기 위해 사용됩니다.

## 요약
RIM-RS는 특정 시퀀스 생성 규칙에 따라 생성되며, 설정된 시간 및 주파수 도메인 파라미터에 따라 물리 자원 그리드에 매핑됩니다. 이 과정은 TS 38.211 §7.4.1.6에 정의되어 있으며, RIM-RS 설정을 통해 시간, 주파수, 시퀀스 파라미터가 결정됩니다.

## 상세 설명
RIM-RS의 생성 및 매핑은 다음과 같은 단계로 구성됩니다.

1. **시퀀스 생성**: RIM-RS 시퀀스는 TS 38.211 §7.4.1.6.2에 따라 생성됩니다. 이는 [[Sequence_Generation]]의 원리를 따르며, 특정 파라미터 집합에 의해 결정됩니다.
2. **물리 자원 매핑**: 생성된 시퀀스는 TS 38.211 §7.4.1.6.3에 따라 [[Physical_Resource_Grid]] 내의 특정 자원 요소(RE)에 매핑됩니다.
3. **설정(Configuration)**: RIM-RS는 상위 계층 시그널링을 통해 설정됩니다.
    - 시간 도메인 파라미터: TS 38.211 §7.4.1.6.4.2에 따라 슬롯 및 심볼 위치가 결정됩니다.
    - 주파수 도메인 파라미터: TS 38.211 §7.4.1.6.4.3에 따라 서브캐리어 오프셋 및 대역폭이 결정됩니다.
    - 시퀀스 파라미터: TS 38.211 §7.4.1.6.4.4에 따라 시퀀스 ID 등이 설정됩니다.
4. **자원 트리플릿(Resource Triplet)**: RIM-RS 설정은 자원 트리플릿과 세트 ID 간의 매핑을 통해 관리됩니다(TS 38.211 §7.4.1.6.4.5).

## 인과 관계
- [[Reference_Signals]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[Physical_Resource_Grid]] (affects)

## 관련 개념
- [[Reference_Signals]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[Physical_Resource_Grid]] (affects)

## 스펙 근거
- TS 38.211 §7.4.1.6.1: RIM-RS 일반 사항
- TS 38.211 §7.4.1.6.2: RIM-RS 시퀀스 생성
- TS 38.211 §7.4.1.6.3: 물리 자원 매핑
- TS 38.211 §7.4.1.6.4: RIM-RS 설정 및 파라미터 매핑

## 소스
- 3GPP TS 38.211 V17.9.0 (2023-12), "Physical channels and modulation"