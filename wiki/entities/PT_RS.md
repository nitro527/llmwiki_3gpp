# PT_RS

## 정의
[[PT_RS]] (Phase Tracking Reference Signal)는 고주파 대역에서 발생하는 위상 잡음(Phase Noise)을 보상하기 위해 [[PDSCH]] 및 [[PUSCH]] 전송 시 삽입되는 참조 신호입니다.

## 요약
[[PT_RS]]는 수신단에서 위상 추적을 수행하여 위상 잡음으로 인한 성능 열화를 방지합니다. UE는 상위 계층 파라미터 및 [[DCI]]를 통해 설정된 정보에 따라 [[PT_RS]]를 수신하거나 전송합니다.

## 상세 설명
[[PT_RS]]는 주로 고주파수 대역에서 오실레이터의 위상 잡음이 심해질 때 이를 추적하기 위해 사용됩니다. 

UE는 다음과 같은 UE Feature를 지원해야 합니다:
- [필수(cap)] 2-2: [[PDSCH]] beam switching
- [필수(cap)] 2-33: [[CSI_RS]] and [[CSI_IM]] reception for CSI feedback
- [필수(cap)] 2-44: Basic DL [[PT_RS]]
- [필수(cap)] 2-47: Basic UL [[PT_RS]]
- [필수(cap)] 2-60: Active spatial relations

또한, 다음의 선택적 기능을 지원할 수 있습니다:
- [선택] 37-7: SCG Failure Report for MRO
- [선택] 55-8: SCG Failure Report for CPAC
- [선택] 2-46: Downlink [[PT_RS]] density recommendation
- [선택] 2-48: Uplink [[PT_RS]]
- [선택] 2-49: Uplink [[PT_RS]] density recommendation
- [선택] 3-6: Dynamic SFI monitoring
- [선택] 6-25a: [[PDCCH]] blind detection capability for MCG and for SCG in synchronous NR-NR DC

## 인과 관계
- [[PT_RS]] (triggers) 위상 잡음 보상
- [[PDSCH]] (depends_on) [[PT_RS]] (위상 추적을 위한 참조 신호 포함 시)
- [[PUSCH]] (depends_on) [[PT_RS]] (위상 추적을 위한 참조 신호 포함 시)

## 관련 개념
- [[Reference_Signals]] (part_of)
- [[PTRS_Generation_Mapping]] (affects)
- [[PDSCH_Reception_Procedures]] (depends_on)
- [[PUSCH_PTRS_Transmission]] (depends_on)

## 스펙 근거
TS 38.214 §5.1.6.3에 따르면, [[PDSCH]] 수신을 위해 UE는 상위 계층 파라미터 `PTRS-DownlinkConfig`에 의해 설정된 경우 [[PT_RS]]를 수신합니다. 또한, [[DCI]] 내의 정보가 [[PT_RS]]의 존재 여부와 매핑 파라미터를 결정합니다.

## 소스
- 3GPP TS 38.214 V17.x.x, "NR; Physical layer procedures for data"
- 3GPP TS 38.822, "UE Feature List"