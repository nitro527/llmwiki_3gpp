# PDCCH_Modulation

## 정의
[[PDCCH]] 전송을 위해 스크램블링된 비트 시퀀스를 복소 심볼로 변환하는 물리 계층 절차를 의미합니다.

## 요약
[[PDCCH]]는 신뢰성 있는 제어 정보 전달을 위해 고정된 변조 방식인 QPSK를 사용합니다. 이는 UE의 능력과 관계없이 모든 NR 시스템에서 필수적으로 지원되는 변조 방식입니다.

## 상세 설명
TS 38.211 §7.3.2.4에 따르면, [[PDCCH]]를 통해 전송되는 비트 시퀀스는 [[Modulation_Mapper]]를 거쳐 복소 심볼로 매핑됩니다. 

- 변조 방식: QPSK (Quadrature Phase Shift Keying)
- 입력: 스크램블링된 비트 시퀀스
- 출력: 복소 심볼 시퀀스

QPSK 변조는 2비트를 하나의 복소 심볼로 매핑하여 전송 효율과 수신 성능의 균형을 맞춥니다. [[PDCCH]]는 제어 채널로서 높은 신뢰성이 요구되므로, 복잡한 고차 변조 대신 강건한 QPSK를 고정적으로 사용합니다.

## 인과 관계
- [[PDCCH_Scrambling]] (depends_on): 스크램블링된 비트가 [[PDCCH_Modulation]]의 입력으로 사용됩니다.
- [[Modulation_Mapper]] (part_of): [[PDCCH_Modulation]]은 [[Modulation_Mapper]]의 구체적인 구현 사례입니다.
- [[PDCCH_Resource_Mapping]] (triggers): 변조된 복소 심볼은 이후 자원 매핑 절차로 전달됩니다.

## 관련 개념
- [[PDCCH]] (part_of)
- [[Modulation_Mapper]] (part_of)
- [[PDCCH_Scrambling]] (depends_on)
- [[PDCCH_Resource_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §7.3.2.4: "The block of bits $b(0), \dots, b(M_{bit}-1)$ shall be modulated as specified in clause 5.1 using QPSK, resulting in a block of complex-valued modulation symbols $d(0), \dots, d(M_{symb}-1)$."

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03), "Physical channels and modulation"