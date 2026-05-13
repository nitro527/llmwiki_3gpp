# PSSCH_Modulation

## 정의
[[PSSCH]] 전송을 위해 스크램블링된 비트 블록을 복소수 변조 심볼 블록으로 변환하는 물리 계층 절차를 의미한다.

## 요약
[[PSSCH]]는 단일 코드워드 전송을 지원하며, 스크램블링된 비트 블록을 입력받아 [[Modulation_Mapper]]를 통해 복소수 심볼로 매핑한다. 변조 방식은 전송 목적에 따라 [[QPSK]] 또는 지원되는 다양한 변조 방식을 사용한다.

## 상세 설명
[[PSSCH]]의 변조 과정은 TS 38.211 §8.3.1.2에 정의되어 있다.

1. 입력 데이터: 스크램블링된 비트 블록이 입력되며, 이를 복소수 변조 심볼 블록으로 변환한다.
2. 변조 방식:
   - 특정 제어 정보나 기본 전송의 경우, TS 38.211 §5.1에 기술된 [[QPSK]] 방식을 사용한다.
   - 데이터 전송의 경우, TS 38.211 §8.3.1.2의 Table 8.3.1.2-1에 명시된 변조 방식 중 하나를 선택하여 사용한다.
3. 매핑 절차: 변조된 심볼은 이후 [[PSSCH_Resource_Mapping]] 과정을 거쳐 물리 자원에 배치된다.

## 인과 관계
- [[PSSCH_Scrambling]] depends_on [[PSSCH_Modulation]] (스크램블링된 비트가 변조 입력으로 사용됨)
- [[PSSCH_Modulation]] depends_on [[Modulation_Mapper]] (변조 심볼 생성을 위한 매핑 규칙 적용)
- [[PSSCH_Modulation]] affects [[PSSCH_Resource_Mapping]] (변조된 심볼이 자원 매핑의 입력이 됨)

## 관련 개념
- [[PSSCH]] (part_of)
- [[Modulation_Mapper]] (implements)
- [[PSSCH_Scrambling]] (depends_on)
- [[PSSCH_Resource_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §8.3.1.2: PSSCH 변조 절차 및 지원되는 변조 방식 정의
- TS 38.211 §5.1: 변조 매핑 일반 규칙

## 소스
- 3GPP TS 38.211 V17.9.0, "NR; Physical channels and modulation"