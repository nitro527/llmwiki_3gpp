# Coexistence_Operation

## 정의
[[Coexistence_Operation]]은 동일한 [[UE]] 내에서 서로 다른 무선 접속 기술(예: E-UTRA와 NR)을 동시에 사용할 때, 간섭을 최소화하고 효율적인 자원 활용을 위해 프레임 경계를 정렬하는 무선 접속 기술 간의 조정 절차를 의미합니다.

## 요약
본 절차는 서로 다른 무선 접속 기술 간의 채널 또는 신호가 시간 분할 다중화(TDM) 방식으로 동작할 때, [[UE]]가 각 기술의 프레임 인덱스를 인지하고 있다면 서브프레임 경계를 일치시켜 간섭을 방지하는 메커니즘입니다. 서브프레임 경계 정렬은 [[UE]]의 구현 방식에 따라 수행됩니다.

## 상세 설명
TS 38.213 §16.7에 명시된 바와 같이, [[UE]]가 E-UTRA 무선 접속 기술을 사용하는 제1 채널/신호와 NR 무선 접속 기술을 사용하는 제2 채널/신호를 동시에 송수신해야 하는 상황에서 다음 조건을 만족할 때 경계 정렬이 수행됩니다.

1. 제1 채널/신호와 제2 채널/신호가 시간 분할 다중화(TDM)되어 동작하는 경우
2. [[UE]]가 제1 채널/신호의 프레임 인덱스와 제2 채널/신호의 프레임 인덱스를 모두 알고 있는 경우

이러한 조건 하에서 [[UE]]는 각 채널 또는 신호를 송수신할 때, 제2 채널/신호의 서브프레임 경계가 제1 채널/신호의 서브프레임 경계와 일치하도록 조정합니다. 이 정렬 과정은 별도의 상위 계층 시그널링에 의존하지 않고 [[UE]]의 내부 구현 수단(UE implementation means)을 통해 달성됩니다. 이는 기기 내 공존(In-device coexistence) 및 동일 채널 공존(Co-channel coexistence) 환경에서 무선 자원의 충돌을 방지하고 성능을 최적화하는 핵심적인 동작입니다.

## 인과 관계
- [[Frame_Structure]] depends_on [[Coexistence_Operation]] (프레임 경계 정렬을 통한 시간 자원 동기화)
- [[Coexistence_Operation]] affects [[Synchronization_Procedures]] (서브프레임 경계 정렬을 위한 시간 동기화 정보 활용)

## 관련 개념
- [[Frame_Structure]] (part_of)
- [[Synchronization_Procedures]] (depends_on)

## 스펙 근거
- TS 38.213 §16.7: Operation for in-device coexistence and for co-channel coexistence

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03), "NR; Physical layer procedures for control"