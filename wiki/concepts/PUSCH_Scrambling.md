# PUSCH_Scrambling

## 정의
[[PUSCH]] 전송을 위해 채널 코딩된 비트 시퀀스에 의사 난수 시퀀스를 곱하여 데이터의 무작위성을 부여하는 물리 계층 처리 절차를 의미한다.

## 요약
[[PUSCH]] 데이터 스크램블링은 전송되는 비트 스트림의 간섭을 완화하고 수신기에서의 복조 성능을 향상시키기 위해 수행된다. 이 절차는 모든 [[PUSCH]] 전송에 필수적으로 적용되며, 특정 파라미터(RNTI, Cell ID 등)를 기반으로 생성된 스크램블링 시퀀스를 비트 단위로 XOR 연산하여 수행된다.

## 상세 설명
[[PUSCH]] 스크램블링은 [[Channel_Coding_General]] 이후, [[Modulation_Mapper]] 이전 단계에서 수행된다. 

1. 입력: 채널 코딩된 비트 시퀀스 $b(0), b(1), \dots, b(M_{bit}-1)$가 입력된다.
2. 시퀀스 생성: [[Sequence_Generation]]을 통해 생성된 스크램블링 시퀀스 $c(i)$가 사용된다.
3. 연산: 입력 비트와 스크램블링 시퀀스를 모듈로-2 연산(XOR)하여 출력 비트 $\tilde{b}(i)$를 생성한다.
   - $\tilde{b}(i) = (b(i) + c(i)) \mod 2$
4. 적용 범위: $i = 0, 1, \dots, M_{bit}-1$ 범위 내에서 수행된다.

본 절차와 관련된 UE 기능은 다음과 같다:
- [필수(항상)]: [[DFT-S-OFDM_waveform_for_UL]], [[Basic_PUSCH_transmission]]
- [필수(cap)]: [[Aperiodic_beam_report]], [[Active_spatial_relations]]
- [선택]: [[PUSCH_codebook_coherency_subset]], [[Codebook_based_PUSCH_MIMO_transmission]], [[Non-codebook_based_PUSCH_transmission]], [[Semi-persistent_beam_report_on_PUCCH]], [[Semi-persistent_beam_report_on_PUSCH]], [[Semi-persistent_CSI_report_on_PUCCH]], [[Semi-persistent_CSI_report_on_PUSCH]], [[For_SRS_for_CB_PUSCH_and_antenna_switching_on_FR1_zero_slot_offset_for_aperiodic_SRS_transmission]]

## 인과 관계
- depends_on: [[Channel_Coding_General]] (입력 비트 시퀀스 제공)
- triggers: [[Modulation_Mapper]] (스크램블링된 비트를 변조 심볼로 변환)
- part_of: [[PUSCH_Transmission_Parameters]]

## 관련 개념
- [[PUSCH]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[Modulation_Mapper]] (triggers)
- [[PUSCH_Modulation]] (affects)

## 스펙 근거
- TS 38.211 §6.3.1.1에 따르면, [[PUSCH]] 전송을 위한 비트 시퀀스 $b(0), \dots, b(M_{bit}-1)$는 스크램블링 시퀀스 $c(i)$와 XOR 연산을 통해 $\tilde{b}(i)$로 변환되어야 한다.

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03) "Physical channels and modulation", Section 6.3.1.1

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/PUSCH_Modulation.md
- entities/PUSCH.md