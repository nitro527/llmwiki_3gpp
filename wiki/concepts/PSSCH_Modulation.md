# PSSCH_Modulation

## 정의
[[PSSCH]] 데이터 변조는 [[Sidelink]] 통신에서 전송되는 비트 시퀀스를 복소 심볼(complex-valued modulation symbols)로 매핑하는 물리 계층 절차를 의미합니다.

## 요약
[[PSSCH]] 변조는 [[CP-OFDM]] 파형을 기반으로 수행되며, 상위 계층에서 설정된 변조 방식에 따라 비트 시퀀스를 복소 심볼로 변환합니다. 본 절차는 [[UE]]의 [[Sidelink]] 송수신 능력 및 설정된 [[MCS]] 테이블에 따라 다양한 변조 차수를 지원합니다.

## 상세 설명
[[PSSCH]] 데이터 변조 과정은 다음과 같은 특징을 가집니다.

1. **파형 지원**: [[PSSCH]]는 기본적으로 [[CP-OFDM]] 파형을 사용합니다.
2. **변조 방식**: 입력된 비트 시퀀스는 [[Modulation_Mapper]]를 통해 복소 심볼로 매핑됩니다. 지원되는 변조 방식은 [[UE]]의 능력에 따라 결정됩니다.
3. **UE Feature**:
   - [필수(항상)]: [[CP-OFDM]] waveform for DL and UL, [[DFT-S-OFDM]] waveform for UL, [[DL_modulation_scheme]], [[UL_modulation_scheme]]
   - [선택]: [[Extended_CP]], Receiving [[NR_sidelink]], Transmitting [[NR_sidelink]] mode 1 scheduled by [[NR_Uu]], Transmitting [[NR_sidelink]] mode 2, 256QAM [[sidelink]] transmission, Low-spectral efficiency 64QAM [[MCS]] table, Support of rank 2 transmission, Support of rank 2 reception

## 인과 관계
- [[PSSCH_Scrambling]] (depends_on): [[PSSCH]] 변조 이전에 스크램블링된 비트 시퀀스가 입력으로 사용됩니다.
- [[PSSCH_Layer_Mapping]] (affects): 변조된 복소 심볼은 이후 레이어 매핑 과정을 거쳐 안테나 포트로 분배됩니다.
- [[Modulation_Mapper]] (part_of): [[PSSCH]] 변조는 [[Modulation_Mapper]]의 기능을 활용하여 수행됩니다.

## 관련 개념
- [[PSSCH]] (part_of)
- [[Modulation_Mapper]] (depends_on)
- [[CP-OFDM]] (depends_on)
- [[MCS]] (affects)

## 스펙 근거
- TS 38.211 §8.3.1.2에 따르면, [[PSSCH]]에 대한 복소 심볼 생성은 [[CP-OFDM]] 파형을 사용하며, 상위 계층에서 제공하는 변조 방식에 따라 [[Modulation_Mapper]]를 통해 수행됩니다.

## 소스
- 3GPP TS 38.211 V17.x.x (Release 17) "Physical channels and modulation" §8.3.1.2