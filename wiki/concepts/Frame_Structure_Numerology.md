# Frame_Structure_Numerology

## 정의
5G NR에서 시간 및 주파수 자원을 체계적으로 관리하기 위해 정의된 계층적 구조와 서브캐리어 간격(Subcarrier Spacing) 및 심볼 길이를 결정하는 파라미터 세트를 의미합니다.

## 요약
- [[CSI_Reporting_Procedures]]와 관련된 2-35: [[CSI_RS]] report framework는 필수(cap) 기능입니다.
- 다양한 처리 능력 및 자원 할당을 위해 2-15b, 5-5a, 5-5c, 5-13, 5-13a, 5-13c, 5-13d, 5-13e, 5-13f, 6-2, 6-3과 같은 선택적 기능들이 정의되어 있습니다.
- 프레임 구조는 10ms 길이의 무선 프레임 내에 서브프레임과 슬롯으로 구성되며, [[Numerology]]에 따라 슬롯의 길이와 개수가 결정됩니다.

## 상세 설명
TS 38.211 §4.2에 따르면, 5G NR은 다양한 서비스 요구사항을 충족하기 위해 여러 [[Numerology]]를 지원합니다. 각 뉴머롤로지는 서브캐리어 간격($\Delta f = 2^\mu \cdot 15$ kHz)과 사이클릭 프리픽스(Cyclic Prefix) 길이에 의해 정의됩니다.

TS 38.211 §4.3.1에 따라, 무선 프레임(Radio Frame)은 10ms의 길이를 가지며, 1ms 길이를 갖는 10개의 서브프레임으로 구성됩니다. 하나의 프레임은 총 10ms의 시간 구간을 가집니다.

TS 38.211 §4.3.2에 따라, 슬롯(Slot)은 뉴머롤로지 $\mu$에 따라 결정됩니다.
- 노멀 사이클릭 프리픽스(Normal Cyclic Prefix)의 경우, 한 슬롯은 14개의 OFDM 심볼로 구성됩니다.
- 슬롯의 개수는 뉴머롤로지 $\mu$에 따라 프레임당 슬롯 수($N_{slot}^{frame, \mu}$)와 서브프레임당 슬롯 수($N_{slot}^{subframe, \mu}$)로 정의됩니다.

## 인과 관계
- [[Numerology]]는 [[OFDM_Baseband_Signal_Generation]]의 서브캐리어 간격과 심볼 지속 시간을 결정합니다.
- 슬롯 구조는 [[PDSCH]] 및 [[PUSCH]]의 자원 할당 및 [[HARQ]] 타이밍을 결정하는 기본 단위가 됩니다.
- UE의 처리 능력(Capability 2 등)은 특정 슬롯 내에서 처리 가능한 [[PDSCH]] 또는 [[PUSCH]]의 개수(5-13, 5-13a, 5-13c, 5-13d, 5-13e, 5-13f)를 제한합니다.

## 관련 개념
- [[Numerology]] (depends_on)
- [[Slot]] (part_of)
- [[PDSCH]] (affects)
- [[PUSCH]] (affects)
- [[CSI_RS]] (depends_on)

## 스펙 근거
- TS 38.211 §4.2: Numerologies 정의
- TS 38.211 §4.3.1: Frames and subframes 구조
- TS 38.211 §4.3.2: Slots 정의 및 뉴머롤로지에 따른 구성

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03) "Physical channels and modulation"
- 3GPP TS 38.822 V16.0.0 (2020-07) "UE features"