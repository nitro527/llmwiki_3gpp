# CSI_RS

## 정의
[[CSI_RS]] (Channel State Information Reference Signal)는 5G NR 시스템에서 채널 상태 정보 측정, 빔 관리, 이동성 관리, 그리고 시간/주파수 추적을 위해 네트워크가 UE에 전송하는 하향링크 참조 신호입니다.

## 요약
[[CSI_RS]]는 다양한 목적에 따라 구성되며, UE는 상위 계층 시그널링을 통해 설정된 자원 정보를 바탕으로 신호를 수신하고 측정합니다. 주요 기능으로는 [[TRS]] (Tracking Reference Signal)를 통한 동기화 추적, L1-RSRP 및 L1-SINR 계산, 그리고 이동성 측정이 포함됩니다.

## 상세 설명
[[CSI_RS]]는 목적에 따라 다음과 같이 구분되어 운용됩니다.

- [[TRS]]: 시간 및 주파수 오프셋 추적을 위해 사용되는 [[CSI_RS]] 구성입니다. UE는 이를 통해 주파수 오프셋 및 시간 동기화를 정밀하게 유지합니다.
- L1-RSRP 및 L1-SINR 계산: UE는 설정된 [[CSI_RS]] 자원을 사용하여 하향링크 채널의 품질을 측정합니다. 이는 빔 관리 및 링크 적응에 활용됩니다.
- 이동성 관리: 네트워크는 UE의 핸드오버나 셀 선택/재선택을 지원하기 위해 [[CSI_RS]] 기반의 이동성 측정을 수행하도록 설정할 수 있습니다.
- 기타 측정: [[RLM]] (Radio Link Monitoring) 및 [[BFD]] (Beam Failure Detection) 등을 위해 특정 [[CSI_RS]] 자원이 활용됩니다.

## 인과 관계
- [[CSI_RS]] (affects) [[CSI_Reporting_Procedures]]
- [[CSI_RS]] (depends_on) [[Radio_Link_Monitoring]]
- [[CSI_RS]] (triggers) [[L1_L2_Triggered_Mobility]]
- [[CSI_RS]] (part_of) [[Reference_Signals]]

## 관련 개념
- [[TRS]] (similar_to)
- [[SS_PBCH_Block]] (similar_to)
- [[CSI_RS_Generation_Mapping]] (part_of)
- [[Radio_Link_Monitoring]] (depends_on)

## 스펙 근거
- TS 38.214 §5.1.6에 따르면, UE는 상위 계층 파라미터에 의해 설정된 [[CSI_RS]] 자원을 수신하고 측정 절차를 수행합니다.
- TS 38.214 §5.1.6.1.1에 따르면, [[TRS]]는 시간 및 주파수 추적을 위한 특정 [[CSI_RS]] 구성으로 정의됩니다.
- TS 38.214 §5.1.6.1.2에 따르면, L1-RSRP 및 L1-SINR 계산을 위한 [[CSI_RS]] 수신 절차가 규정되어 있습니다.
- TS 38.214 §5.1.6.1.3에 따르면, 이동성 측정을 위한 [[CSI_RS]] 활용 절차가 정의되어 있습니다.

## 소스
- 3GPP TS 38.214 v19.0.0, "Physical layer procedures for data"
- UE Capability Feature 2-51: [[TRS]] (CSI-RS for tracking)
- UE Capability Feature 1-7: [[CSI_RS]] based [[RLM]]