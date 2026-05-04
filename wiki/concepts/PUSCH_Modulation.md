# PUSCH_Modulation

## 정의
[[PUSCH]] 데이터 변조는 스크램블링된 비트 시퀀스를 복소수 심볼로 매핑하는 물리 계층 절차를 의미합니다.

## 요약
[[PUSCH]] 전송을 위해 필수적으로 수행되는 과정으로, 상위 계층에서 설정된 변조 방식(QPSK, 16QAM, 64QAM, 256QAM 등)에 따라 비트 스트림을 심볼로 변환합니다. 본 절차는 [[DFT-S-OFDM]] 및 [[CP-OFDM]] 파형 모두에 적용되며, [[UE]]의 능력에 따라 다양한 변조 차수를 지원합니다.

## 상세 설명
[[PUSCH]] 데이터 변조는 다음과 같은 단계와 규칙을 따릅니다.

1. 입력: 스크램블링된 비트 시퀀스 $b(i)$가 [[Modulation_Mapper]]로 입력됩니다.
2. 변조 방식 선택: [[UE]]는 상위 계층 파라미터에 의해 지시된 변조 방식(MCS)을 사용합니다.
3. 심볼 매핑: 선택된 변조 방식에 따라 비트 시퀀스는 복소수 심볼 $d(i)$로 매핑됩니다.
   - 지원되는 변조 방식: $\pi/2$-BPSK, QPSK, 16QAM, 64QAM, 256QAM.
   - 특히 $\pi/2$-BPSK는 [[PUSCH]]에 [[Transform_Precoding]]이 적용된 경우에 주로 사용됩니다.
4. 출력: 생성된 복소수 심볼은 이후 [[PUSCH_Layer_Mapping]] 단계로 전달됩니다.

### UE Feature 지원 현황
- [필수(항상)]: [[DFT-S-OFDM]] waveform, [[CP-OFDM]] waveform, [[UL]] modulation scheme, Basic [[PUSCH]] transmission.
- [필수(cap)]: Aperiodic beam report.
- [선택]: Low PAPR [[DMRS]] for [[PUSCH]] with [[Transform_Precoding]] and with $\pi/2$ BPSK, Extended [[CP]], [[PUSCH]] codebook coherency subset, Codebook based [[PUSCH]] [[MIMO]] transmission, non-codebook based [[PUSCH]] transmission, Semi-persistent beam report on [[PUCCH]].

## 인과 관계
- [[PUSCH_Scrambling]] (triggers) [[PUSCH_Modulation]]
- [[PUSCH_Modulation]] (affects) [[PUSCH_Layer_Mapping]]
- [[Transform_Precoding]] (depends_on) [[PUSCH_Modulation]] (특정 변조 방식 선택 시)

## 관련 개념
- [[PUSCH]] (part_of)
- [[Modulation_Mapper]] (similar_to)
- [[DFT-S-OFDM]] (depends_on)
- [[CP-OFDM]] (depends_on)
- [[PUSCH_Transform_Precoding]] (affects)

## 스펙 근거
- TS 38.211 §6.3.1.2에 따르면, [[PUSCH]] 전송을 위한 변조는 상위 계층에서 설정된 변조 방식에 따라 비트 시퀀스를 복소수 심볼로 매핑하며, 지원되는 변조 방식은 $\pi/2$-BPSK, QPSK, 16QAM, 64QAM, 256QAM을 포함합니다.

## 소스
- 3GPP TS 38.211 v16.9.0 (Release 16) §6.3.1.2
- 3GPP TS 38.822 (UE Feature list)

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/PUSCH_Modulation.md
- concepts/PUSCH_Transform_Precoding.md
- entities/PUSCH.md