# Modulation_Mapper

## 정의
[[Modulation_Mapper]]는 전송을 위해 입력된 비트 시퀀스를 복소수 심볼(complex-valued modulation symbols)로 변환하는 물리 계층의 처리 절차를 의미합니다.

## 요약
[[Modulation_Mapper]]는 입력된 비트들을 정의된 변조 방식에 따라 성상도(constellation) 상의 복소수 값으로 매핑합니다. 5G NR에서는 [[CP-OFDM]] 및 [[DFT-S-OFDM]] 파형을 지원하며, 지원되는 변조 방식은 [[π/2-BPSK]], [[BPSK]], [[QPSK]], [[16QAM]], [[64QAM]], [[256QAM]], [[1024QAM]]을 포함합니다.

## 상세 설명
[[Modulation_Mapper]]는 입력된 비트 시퀀스를 특정 변조 차수에 따라 그룹화하여 복소수 심볼로 변환합니다.

- [[π/2-BPSK]]: 1비트를 입력받아 위상 회전이 적용된 BPSK 심볼로 매핑합니다. 주로 [[PUSCH]]에서 [[DFT-S-OFDM]] 사용 시 PAPR(Peak-to-Average Power Ratio)을 낮추기 위해 사용됩니다.
- [[BPSK]]: 1비트를 입력받아 성상도 상의 두 지점으로 매핑합니다.
- [[QPSK]]: 2비트를 입력받아 4개의 성상도 지점으로 매핑합니다.
- [[16QAM]], [[64QAM]], [[256QAM]], [[1024QAM]]: 각각 4, 6, 8, 10비트를 입력받아 해당 차수의 QAM 성상도 지점으로 매핑합니다.

이 과정은 채널 코딩 및 [[Scrambling]] 이후, [[Layer_Mapping]] 이전에 수행됩니다.

## 인과 관계
- [[Scrambling]] (depends_on) [[Modulation_Mapper]]
- [[Modulation_Mapper]] (affects) [[Layer_Mapping]]
- [[DFT-S-OFDM]] (depends_on) [[π/2-BPSK]]
- [[CP-OFDM]] (depends_on) [[QPSK]], [[16QAM]], [[64QAM]], [[256QAM]], [[1024QAM]]

## 관련 개념
- [[PUSCH]] (affects)
- [[PDSCH]] (affects)
- [[CP-OFDM]] (depends_on)
- [[DFT-S-OFDM]] (depends_on)
- [[Layer_Mapping]] (depends_on)

## 스펙 근거
- TS 38.211 §5.1에 따르면, 입력 비트 시퀀스는 정의된 변조 방식에 따라 복소수 심볼로 매핑되어야 합니다.
- TS 38.211 §5.1.1 ~ §5.1.7은 각각 [[π/2-BPSK]], [[BPSK]], [[QPSK]], [[16QAM]], [[64QAM]], [[256QAM]], [[1024QAM]]의 매핑 규칙을 규정합니다.
- UE Feature Priority 관련:
  - DL/UL modulation scheme (0-3, 0-4) 및 CP-OFDM/DFT-S-OFDM waveform (0-1, 0-2)은 필수 지원 사항입니다.
  - 1024QAM for PDSCH (36-1, 36-1a) 및 새로운 64QAM MCS table (5-34)은 선택적 기능으로 정의됩니다.

## 소스
- 3GPP TS 38.211 V19.0.0 (2024-03) "Physical channels and modulation"