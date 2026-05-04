# Sidelink_CSI_RS_Generation_Mapping

## 정의
[[Sidelink]] 통신에서 수신단이 채널 상태 정보를 측정할 수 있도록 송신단이 전송하는 [[CSI_RS]]의 시퀀스 생성 및 물리 자원 매핑 절차를 의미합니다.

## 요약
[[Sidelink_CSI_RS_Generation_Mapping]]은 [[Sidelink]] 환경에서 채널 품질 측정을 지원하기 위한 참조 신호 생성 및 매핑 규칙을 정의합니다. 주요 기능은 다음과 같습니다.
- [필수(cap)] 15-14: [[Sidelink]] [[CSI_RS]] 보고 기능을 지원합니다.
- [필수(cap)] 1-7: [[CSI_RS]] 기반의 [[Radio_Link_Monitoring]]을 지원합니다.
- [선택] 1-4, 1-5, 1-6, 1-8, 1-9, 1-11: 다양한 측정 환경(RRM, RS-SINR, RLM 등)에 따른 [[CSI_RS]] 활용을 선택적으로 지원합니다.
- [필수(cap)] 2-33a: [[PDSCH]] RE-mapping 패턴 지원을 포함합니다.

## 상세 설명
[[Sidelink_CSI_RS_Generation_Mapping]]은 크게 시퀀스 생성 단계와 물리 자원 매핑 단계로 구분됩니다.

1. 시퀀스 생성 (Sequence generation):
   [[CSI_RS]] 시퀀스는 의사 난수 생성기(pseudo-random sequence generator)를 사용하여 생성됩니다. 이는 [[Sequence_Generation]]에서 정의된 방식을 따르며, 슬롯 인덱스, 심볼 인덱스, 그리고 상위 계층에서 설정된 파라미터에 의해 초기화됩니다.

2. 물리 자원 매핑 (Mapping to physical resources):
   생성된 시퀀스는 [[Sidelink_Resource_Grid]] 내의 특정 자원 요소(Resource Element, RE)에 매핑됩니다. 이때 주파수 도메인과 시간 도메인에서의 밀도와 위치는 상위 계층 시그널링을 통해 설정된 구성에 따라 결정됩니다. 매핑 시 [[Sidelink]] 채널의 특성을 고려하여 다른 신호와의 간섭을 최소화하도록 설계됩니다.

## 인과 관계
- [[Sidelink_CSI_RS_Generation_Mapping]] depends_on [[Sequence_Generation]]
- [[Sidelink_CSI_RS_Generation_Mapping]] depends_on [[Sidelink_Resource_Grid]]
- [[Sidelink_CSI_RS_Generation_Mapping]] affects [[CSI_Reporting_Procedures]]
- [[Sidelink_CSI_RS_Generation_Mapping]] triggers [[Radio_Link_Monitoring]]

## 관련 개념
- [[CSI_RS]] (part_of)
- [[Sidelink]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[Sidelink_Resource_Grid]] (depends_on)
- [[CSI_Reporting_Procedures]] (affects)
- [[Radio_Link_Monitoring]] (triggers)

## 스펙 근거
- TS 38.211 §8.4.1.5.1: [[Sidelink]] [[CSI_RS]]의 일반적인 요구사항을 정의합니다.
- TS 38.211 §8.4.1.5.2: [[CSI_RS]] 시퀀스 생성 알고리즘을 명시합니다.
- TS 38.211 §8.4.1.5.3: [[CSI_RS]]를 물리 자원에 매핑하는 규칙을 규정합니다.

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03), "NR; Physical channels and modulation"
- 3GPP TS 38.822 V17.0.0 (2022-03), "NR; Sidelink communication enhancements"