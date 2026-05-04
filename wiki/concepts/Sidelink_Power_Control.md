# Sidelink_Power_Control

## 정의
[[Sidelink]] 채널인 [[PSCCH]], [[PSSCH]], [[PSBCH]], [[PSFCH]]의 전송 전력을 결정하고, 다중 캐리어 환경에서 전력 제한 상황 발생 시 우선순위에 따라 전송 전력을 조정하는 L1 제어 절차를 의미한다.

## 요약
[[Sidelink]] 전력 제어는 단일 캐리어 및 다중 캐리어 환경에서 UE가 전송 전력 한계 내에서 효율적으로 자원을 활용하도록 설계되었다. 특히 [[SL_Carrier_Aggregation]] 환경에서는 캐리어 간 전력 우선순위 규칙을 적용하여 전송을 수행하며, 경로 손실(pathloss) 기반의 개방 루프(open loop) 전력 제어 메커니즘을 지원한다.

## 상세 설명
[[Sidelink]] 전송 전력 제어는 다음과 같은 핵심 요소로 구성된다.

1. **전력 제어 메커니즘**: UE는 설정된 파라미터와 경로 손실 추정치를 기반으로 [[PSCCH]] 및 [[PSSCH]]의 전송 전력을 계산한다. 이는 [[Uplink_Power_Control]]과 유사한 개방 루프 방식을 따른다.
2. **다중 캐리어 전력 우선순위**: [[SL_Carrier_Aggregation]] 환경에서 UE의 총 전송 전력이 최대 전력(P_max)을 초과하는 경우, UE는 각 캐리어 및 채널에 할당된 우선순위에 따라 전력을 감축하거나 일부 전송을 생략한다.
3. **UE Feature 지원**:
   - [필수(항상)] 15-1: Receiving NR sidelink
   - [필수(항상)] 15-3: Transmitting NR sidelink mode 2
   - [필수(cap)] 15-2: Transmitting NR sidelink mode 1 scheduled by NR Uu
   - [선택] 47-s1: Transmission/Reception using dynamic resource pool sharing
   - [선택] 15-23: Support of open loop SL power control and RSRP report
   - [선택] 32-4: Transmitting NR sidelink mode 2 with partial sensing
   - [선택] 32-4a: Transmitting NR sidelink mode 2 with random resource selection
   - [선택] 41-1-8: Support of random selection in a dedicated resource pool
   - [선택] 41-1-10: Support of full sensing in a dedicated resource pool
   - [선택] 41-1-17: Open loop SL pathloss based power control for SL-PRS and associated PSCCH and SL RSRP report for dedicated resource pool
   - [선택] 47-k2: SL multi-channel access for dynamic channel access mode
   - [선택] 47-k9: Sidelink mode 1 resource allocation in shared spectrum

## 인과 관계
- [[Sidelink_Transmission_Parameters]] (depends_on): 전력 제어 결과는 실제 전송 파라미터에 직접적인 영향을 미침.
- [[Sidelink_Congestion_Control]] (affects): 전력 제어 및 우선순위 결정은 채널 혼잡도 관리와 밀접하게 연관됨.
- [[Sidelink_Resource_Selection]] (triggers): 전력 제한으로 인한 전송 실패 시 자원 재선택 절차가 트리거될 수 있음.

## 관련 개념
- [[Sidelink]] (part_of)
- [[PSCCH]] (part_of)
- [[PSSCH]] (part_of)
- [[PSFCH]] (part_of)
- [[Uplink_Power_Control]] (similar_to)
- [[SL_Carrier_Aggregation]] (depends_on)

## 스펙 근거
- TS 38.213 §16.2.5에 따르면, [[SL_Carrier_Aggregation]] 환경에서 UE는 다수의 [[Sidelink]] 캐리어에 걸쳐 전송 전력을 배분하며, 우선순위 규칙에 따라 전력을 조정해야 한다.

## 소스
- 3GPP TS 38.213 Release 18 (v18.0.0) §16.2.5