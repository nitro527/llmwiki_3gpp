# IAB_Timing_Control

## 정의
[[IAB_Timing_Control]]은 [[IAB_Node]] 내의 [[IAB-MT]]가 상위 노드(Donor 또는 Parent IAB-Node)와의 통신을 위해 전송 타이밍을 조정하는 메커니즘을 의미하며, 특히 Case-1, Case-6, Case-7으로 분류되는 타이밍 모드와 [[MAC_CE]]를 통한 타이밍 오프셋 제어를 포함합니다.

## 요약
[[IAB-MT]]는 네트워크 토폴로지 및 전송 환경에 따라 서로 다른 타이밍 모드를 적용합니다. 필수 기능으로 [[PUCCH_Spatial_Setting]]을 위한 [[MAC_CE]] 기반의 [[PUCCH]] 리소스 지시, [[MAC_CE]] 내의 eLCID 필드 사용, 그리고 [[PUCCH]] 리소스 내 SR/[[HARQ]]-ACK/[[CSI]] 다중화 기능이 요구됩니다. 또한, Case-1, 6, 7 각각에 대한 타이밍 정렬(Timing Alignment) 기능이 선택적으로 지원됩니다.

## 상세 설명
[[IAB_Node]]는 무선 백홀을 통해 데이터를 전달하며, [[IAB-MT]]는 상위 노드와 동기화를 유지해야 합니다. 

- 필수 기능(Capability):
  - [[PUCCH_Spatial_Setting]]을 위한 [[MAC_CE]] 기반의 [[PUCCH]] 리소스 지시 기능이 지원됩니다.
  - [[MAC]] 서브헤더 내 1-옥텟 eLCID 필드 사용이 필수입니다.
  - 동일한 시작 심볼을 갖는 SR, [[HARQ]]-ACK, [[CSI]]를 하나의 [[PUCCH]] 리소스에서 다중화하여 전송하는 기능이 필수입니다.

- 타이밍 모드 및 조정:
  - Case-1, Case-6, Case-7은 [[IAB-MT]]가 상위 노드로부터 수신하는 신호와 자신의 전송 타이밍 간의 관계를 정의합니다.
  - Timing Delta 및 Case Indication [[MAC_CE]]를 통해 [[IAB-MT]]는 전송 타이밍을 동적으로 조정할 수 있습니다.
  - 선택적 기능으로 Case-1, Case-6, Case-7에 대한 OTA(Over-The-Air) 타이밍 정렬이 지원됩니다.
  - UL-Flexible-DL 슬롯 포맷과 관련된 유연한 슬롯 구성 기능이 선택적으로 지원됩니다.
  - [[PDCCH]] 모니터링 오케이션은 Case-2 환경에서 슬롯 내 임의의 심볼에서 가능하며, DCI gap이나 span gap을 포함하는 구성이 선택적으로 지원됩니다.
  - [[HARQ]]-ACK 및 [[CSI]]에 대한 동적 beta-offset 구성 및 지시 기능이 선택적으로 지원됩니다.

## 인과 관계
- [[MAC_CE]] (triggers) [[IAB_Timing_Control]] 타이밍 조정
- [[IAB_Node]] (depends_on) [[IAB_Timing_Control]]
- [[PUCCH]] (part_of) [[IAB_Timing_Control]] 리소스 관리

## 관련 개념
- [[IAB_Node]] (part_of)
- [[MAC_CE]] (affects)
- [[PUCCH]] (depends_on)
- [[HARQ]] (depends_on)
- [[CSI]] (depends_on)
- [[Slot_Format_Configuration]] (affects)

## 스펙 근거
- TS 38.213 §14: IAB-MT의 전송 타이밍 모드 및 타이밍 조정 절차 정의
- TS 38.822: IAB-MT 관련 기능(Feature) 요구사항 및 Capability 정의

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"
- 3GPP TS 38.822 V16.0.0 (2020-07) "Study on Integrated Access and Backhaul (IAB)"