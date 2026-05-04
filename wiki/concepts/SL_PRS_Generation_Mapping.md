# SL_PRS_Generation_Mapping

## 정의
[[SL_PRS]]는 [[Sidelink]] 환경에서 UE 간의 측위(Positioning)를 지원하기 위해 전송되는 [[Reference_Signals]]의 일종입니다. 이는 [[Sidelink]] 통신 시스템 내에서 거리 측정 및 위치 추정을 위한 물리 계층 신호로 사용됩니다.

## 요약
[[SL_PRS]]는 [[TS_38_211]] §8.4.1.6에 정의된 절차에 따라 생성되며, 특정 시퀀스 생성 규칙을 따르고 물리 자원 그리드에 매핑됩니다. 본 기능은 [[Sidelink]] 측위 성능을 결정짓는 핵심 요소로, [[UE]]의 처리 능력 및 동기화 소스 설정과 밀접하게 연관되어 있습니다.

## 상세 설명
[[SL_PRS]]의 생성 및 매핑 절차는 크게 시퀀스 생성 단계와 물리 자원 매핑 단계로 나뉩니다.

1. **시퀀스 생성**: [[SL_PRS]] 시퀀스는 의사 난수(Pseudo-random) 시퀀스를 기반으로 생성됩니다. 이는 [[TS_38_211]] §8.4.1.6.2에 명시된 바와 같이, 특정 초기화 값(Initialization value)을 사용하여 [[Sequence_Generation]] 과정을 거칩니다.
2. **물리 자원 매핑**: 생성된 시퀀스는 [[Sidelink_Resource_Grid]] 내의 할당된 자원 요소(Resource Elements)에 매핑됩니다. [[TS_38_211]] §8.4.1.6.3에 따라, [[SL_PRS]]는 설정된 [[Sidelink]] 대역폭 파트(BWP) 내에서 시간 및 주파수 도메인 자원에 배치됩니다.

## 인과 관계
- [[SL_PRS]] 생성은 [[Sidelink_Resource_Allocation_Procedures]]에 의해 결정된 자원 풀 내에서 수행됩니다.
- [[Synchronization_Procedures]]를 통해 획득된 동기화 소스는 [[SL_PRS]] 전송 타이밍에 영향을 미칩니다.
- [[UE]]의 [[SL_PRS]] 처리 능력(Capability)은 해당 신호의 수신 및 측정 가능 여부를 결정합니다.

## 관련 개념
- [[Sidelink]] (part_of)
- [[Reference_Signals]] (similar_to)
- [[Sidelink_Resource_Grid]] (depends_on)
- [[Synchronization_Procedures]] (triggers)
- [[SL_PRS]] (part_of)

## 스펙 근거
- [[TS_38_211]] §8.4.1.6.1: [[SL_PRS]]의 일반적인 정의 및 목적
- [[TS_38_211]] §8.4.1.6.2: [[SL_PRS]] 시퀀스 생성 규칙
- [[TS_38_211]] §8.4.1.6.3: [[SL_PRS]]의 물리 자원 매핑 절차

## 소스
- 3GPP TS 38.211 V18.0.0 (2023-12), "Physical channels and modulation"