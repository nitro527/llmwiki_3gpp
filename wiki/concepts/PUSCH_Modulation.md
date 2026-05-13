# PUSCH_Modulation

## 정의
PUSCH_Modulation은 [[PUSCH]] 전송을 위해 스크램블된 비트 블록을 복소수 심볼로 변환하는 물리 계층 처리 절차를 의미합니다.

## 요약
PUSCH_Modulation은 각 코드워드에 대해 스크램블된 비트 블록을 입력받아, 지원되는 변조 방식에 따라 복소수 심볼 블록을 생성합니다. 이 과정은 [[Modulation_Mapper]]의 일반적인 규칙을 따르며, 상위 계층에서 설정된 변조 및 코딩 방식(MCS)에 따라 결정됩니다.

## 상세 설명
PUSCH 전송을 위한 변조 과정은 다음과 같은 단계로 수행됩니다.

1. 입력 데이터: 각 코드워드 q에 대해 스크램블된 비트 블록 $b^{(q)}(0), \dots, b^{(q)}(M_{bit}^{(q)}-1)$이 입력됩니다.
2. 변조 매핑: 입력된 비트 블록은 [[Modulation_Mapper]]에 정의된 방식에 따라 복소수 심볼 블록 $d^{(q)}(0), \dots, d^{(q)}(M_{symb}^{(q)}-1)$로 변환됩니다.
3. 변조 방식: 지원되는 변조 방식은 π/2-BPSK, QPSK, 16QAM, 64QAM, 256QAM 등이 포함되며, 이는 TS 38.211 Table 6.3.1.2-1에 명시된 규격을 따릅니다.
4. 출력: 변환된 복소수 심볼 블록은 이후 [[PUSCH_Layer_Mapping]] 단계로 전달됩니다.

## 인과 관계
- [[PUSCH_Scrambling]] depends_on [[PUSCH_Modulation]] (스크램블된 비트가 변조의 입력으로 사용됨)
- [[PUSCH_Modulation]] depends_on [[Modulation_Mapper]] (변조 매핑의 기본 규칙을 참조함)
- [[PUSCH_Modulation]] affects [[PUSCH_Layer_Mapping]] (변조된 심볼이 레이어 매핑의 입력으로 사용됨)

## 관련 개념
- [[PUSCH]] (part_of)
- [[Modulation_Mapper]] (implements)
- [[PUSCH_Scrambling]] (depends_on)
- [[PUSCH_Layer_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §6.3.1.2: For each codeword q, the block of scrambled bits b(q) shall be modulated as described in clause 5.1 using one of the modulation schemes in Table 6.3.1.2-1, resulting in a block of complex-valued modulation symbols d(q).

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03) Physical channels and modulation