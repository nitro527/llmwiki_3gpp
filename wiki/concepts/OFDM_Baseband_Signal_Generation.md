# OFDM_Baseband_Signal_Generation

## 정의
OFDM_Baseband_Signal_Generation은 주파수 영역의 복소 심볼을 시간 영역의 연속적인 신호로 변환하고, 다중 경로 페이딩 환경에서의 심볼 간 간섭(ISI)을 방지하기 위해 CP(Cyclic Prefix)를 삽입하는 5G NR의 물리 계층 신호 처리 절차를 의미합니다.

## 요약
5G NR은 하향링크(DL)와 상향링크(UL)에서 CP-OFDM 파형을 기본으로 사용하며, 상향링크에서는 커버리지 향상을 위해 DFT-S-OFDM 파형을 추가로 지원합니다. 기저대역 신호 생성은 IFFT(Inverse Fast Fourier Transform)를 통한 시간 영역 변환과 CP 삽입 과정을 거쳐 수행됩니다.

## 상세 설명
TS 38.211 §5.3에 따라 OFDM 기저대역 신호 생성은 다음과 같은 단계로 진행됩니다.

1. 시간 영역 신호 생성:
   각 심볼 $l$에 대해, 서브캐리어 $k$에 매핑된 복소 심볼 $a_{k,l}^{(p, \mu)}$는 IFFT를 통해 시간 영역 신호로 변환됩니다. 이때 사용되는 서브캐리어 간격(SCS) 설정 $\mu$에 따라 샘플링 레이트와 FFT 크기가 결정됩니다.

2. CP 삽입:
   시간 영역으로 변환된 신호의 뒷부분 일부를 복사하여 심볼의 앞부분에 붙이는 CP 삽입 과정이 수행됩니다. 이는 다중 경로 채널에서 발생하는 지연 확산으로 인한 ISI를 방지합니다.
   - CP 길이는 슬롯 내 심볼 위치와 SCS 설정에 따라 결정됩니다.
   - 일반 CP(Normal CP)와 확장 CP(Extended CP)가 존재하며, 대부분의 환경에서는 일반 CP가 사용됩니다.

3. 파형 특성:
   - CP-OFDM: 모든 서브캐리어에 독립적인 변조 심볼을 할당하여 주파수 선택적 채널에 강인한 특성을 가집니다.
   - DFT-S-OFDM: IFFT 이전에 DFT(Discrete Fourier Transform) 프리코딩을 수행하여 PAPR(Peak-to-Average Power Ratio)을 낮춤으로써 상향링크 단말의 전력 효율을 최적화합니다.

## 인과 관계
- [[PUSCH]] depends_on [[OFDM_Baseband_Signal_Generation]] (상향링크 데이터 전송을 위한 파형 생성)
- [[PDSCH]] depends_on [[OFDM_Baseband_Signal_Generation]] (하향링크 데이터 전송을 위한 파형 생성)
- [[PUSCH_Transform_Precoding]] depends_on [[OFDM_Baseband_Signal_Generation]] (DFT-S-OFDM 파형 생성을 위한 필수 단계)

## 관련 개념
- [[PUSCH]] (implements)
- [[PDSCH]] (implements)
- [[PUSCH_Transform_Precoding]] (part_of)
- [[Frame_Structure]] (affects)

## 스펙 근거
- TS 38.211 §5.3: OFDM baseband signal generation 절차 및 수식 정의
- TS 38.211 §5.3.1: CP-OFDM 파형 생성
- TS 38.211 §5.3.3: DFT-S-OFDM 파형 생성

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)