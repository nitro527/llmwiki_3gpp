# PSSCH_Layer_Mapping

## 정의
[[PSSCH]] (Physical Sidelink Shared Channel) 레이어 매핑은 변조된 심볼들을 하나 이상의 전송 레이어로 분배하여, 이후의 [[PSSCH_Precoding]] 단계에서 안테나 포트로 매핑될 수 있도록 준비하는 물리 계층 절차를 의미합니다.

## 요약
PSSCH 레이어 매핑은 [[Sidelink]] 통신에서 데이터 전송의 다중 안테나 효율을 극대화하기 위해 수행됩니다. 이 절차는 [[Modulation_Mapper]]로부터 출력된 복소수 심볼 블록을 입력받아, 설정된 레이어 수에 따라 적절한 레이어 구조로 변환합니다. 본 절차는 [[3GPP]] TS 38.211 규격에 정의된 일반적인 레이어 매핑 원칙을 따릅니다.

## 상세 설명
PSSCH 레이어 매핑 과정은 다음과 같은 단계로 진행됩니다.
1. 입력: [[PSSCH_Modulation]]을 거친 복소수 심볼 시퀀스가 입력됩니다.
2. 분배: 입력된 심볼 시퀀스는 전송 레이어 수($v$)에 따라 각 레이어로 순차적으로 분배됩니다.
3. 출력: 각 레이어는 $x^{(0)}(i), \dots, x^{(v-1)}(i)$와 같은 복소수 심볼 벡터로 구성되며, 이는 이후 [[PSSCH_Precoding]] 단계의 입력으로 전달됩니다.
4. 레이어 수 결정: 전송에 사용되는 레이어의 수는 상위 계층 시그널링 및 [[Sidelink_Transmission_Parameters]]에 의해 결정됩니다.

## 인과 관계
- [[PSSCH_Modulation]] (depends_on): 변조된 심볼 시퀀스가 레이어 매핑의 입력값이 됩니다.
- [[PSSCH_Precoding]] (triggers): 레이어 매핑의 결과물이 프리코딩 단계로 전달되어 안테나 포트 매핑이 수행됩니다.

## 관련 개념
- [[PSSCH]] (part_of)
- [[PSSCH_Modulation]] (depends_on)
- [[PSSCH_Precoding]] (triggers)
- [[Sidelink]] (part_of)

## 스펙 근거
- TS 38.211 §8.3.1.3에 따르면, PSSCH의 레이어 매핑은 복소수 심볼 블록을 하나 이상의 레이어로 매핑하는 절차를 규정합니다.

## 소스
- 3GPP TS 38.211 V16.9.0 (Release 16), "Physical channels and modulation", §8.3.1.3 Layer mapping