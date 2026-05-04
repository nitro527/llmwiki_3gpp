# PDSCH_Modulation

## 정의
[[PDSCH]] 데이터 전송을 위해 전송 블록(Transport Block)으로부터 생성된 비트 시퀀스를 복소 심볼(Complex-valued modulation symbols)로 변환하는 물리 계층 절차를 의미합니다.

## 요약
[[PDSCH]] 변조는 [[CP-OFDM]] 파형을 기반으로 수행되며, 상위 계층에서 설정된 변조 방식에 따라 비트 시퀀스를 매핑합니다. 이 과정은 [[Modulation_Mapper]]를 통해 수행되며, 지원되는 변조 차수(Modulation order)는 [[UE]]의 능력 및 채널 환경에 따라 결정됩니다.

## 상세 설명
TS 38.211 §7.3.1.2에 명시된 바와 같이, [[PDSCH]]를 위한 복소 심볼 생성 과정은 다음과 같습니다.

1. 입력 비트 시퀀스: [[PDSCH_Scrambling]]을 거친 스크램블된 비트 시퀀스가 입력됩니다.
2. 변조 매핑: 입력된 비트 시퀀스는 [[Modulation_Mapper]]에 의해 복소 심볼로 변환됩니다.
3. 지원 변조 방식: [[QPSK]], [[16QAM]], [[64QAM]], [[256QAM]]이 기본적으로 지원되며, 특정 조건(예: FR1 대역)에서는 [[1024QAM]]이 추가로 지원될 수 있습니다.
4. 멀티캐스트 지원: 멀티캐스트 [[PDSCH]]를 위해 별도로 정의된 최대 변조 차수 제한이 적용될 수 있습니다.

## 인과 관계
- [[PDSCH_Scrambling]] (triggers) [[PDSCH_Modulation]]
- [[PDSCH_Modulation]] (affects) [[PDSCH_Layer_Mapping]]
- [[UE]] 능력 (depends_on) [[PDSCH_Modulation]]

## 관련 개념
- [[PDSCH]] (part_of)
- [[Modulation_Mapper]] (part_of)
- [[CP-OFDM]] (depends_on)
- [[PDSCH_Scrambling]] (depends_on)

## 스펙 근거
- TS 38.211 §7.3.1.2: PDSCH 변조 절차 및 복소 심볼 매핑 정의
- TS 38.822: 
    - 0-1: [[CP-OFDM]] waveform for DL and UL (필수)
    - 0-3: DL modulation scheme (필수)
    - 2-1: Basic [[PDSCH]] reception (필수)
    - 33-2i: Supported maximal modulation order for multicast [[PDSCH]] (선택)
    - 33-2j: Supported maximum modulation order used for maximum data rate calculation for multicast [[PDSCH]] (선택)
    - 36-1: [[1024QAM]] for [[PDSCH]] for FR1 (선택)
    - 36-1a: [[1024QAM]] for [[PDSCH]] for FR1 with maximum 2 MIMO layers restriction (선택)
    - 36-2b: MU-MIMO Interference Mitigation advanced receiver with modulation order detection (선택)
    - 0-5: Extended CP (선택)

## 소스
- 3GPP TS 38.211 V19.0.0 (2024-03) "Physical channels and modulation"
- 3GPP TS 38.822 V18.0.0 (2024-03) "UE features"