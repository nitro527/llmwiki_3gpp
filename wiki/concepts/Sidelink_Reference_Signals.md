# Sidelink_Reference_Signals

## 정의
[[Sidelink]] 통신 환경에서 [[UE]] 간의 채널 추정, 동기화, 위치 측정 및 데이터 복조를 위해 전송되는 참조 신호 체계입니다. 여기에는 [[CSI-RS]], [[DMRS]], [[PT-RS]], 그리고 [[PRS]]가 포함됩니다.

## 요약
[[Sidelink]] 참조 신호는 [[PSSCH]] 및 관련 채널의 품질 측정과 복조를 지원합니다. 전송 절차는 [[TS 38.214]] §8.2에 정의되어 있으며, 수신 절차는 §8.4에 명시되어 있습니다. 특히 [[SL PRS]]는 위치 측정 서비스를 위해 별도의 자원 할당 및 혼잡 제어 메커니즘을 따릅니다.

## 상세 설명
[[Sidelink]] 참조 신호의 주요 절차는 다음과 같습니다.

* [[CSI-RS]] 전송 및 수신: [[UE]]는 채널 상태 정보 측정을 위해 [[CSI-RS]]를 전송하며, 수신 측은 이를 바탕으로 채널 품질을 평가합니다.
* [[DMRS]] 전송 및 수신: [[PSSCH]] 복조를 위한 [[DMRS]]는 데이터 전송과 함께 수행되며, 수신 측은 이를 사용하여 [[RSRP]]를 계산합니다.
* [[PT-RS]] 전송 및 수신: 고주파 대역에서의 위상 잡음 보상을 위해 [[PT-RS]]가 사용됩니다.
* [[SL PRS]] 전송 및 수신: 위치 측정을 위한 [[SL PRS]]는 전용 자원 풀에서 관리됩니다. 시간 및 주파수 도메인에서의 자원 할당, 상위 계층 보고를 위한 자원 선택, 그리고 [[SCI]] format 1-B와 연관된 슬롯 결정 절차를 포함합니다. 또한, 전용 자원 풀 내에서의 혼잡 제어 절차가 적용됩니다.

## 인과 관계
- [[Sidelink]] 채널 환경 (depends_on) [[Sidelink_Reference_Signals]]
- [[SL PRS]] 전송 (triggers) [[SL_PRS_Generation_Mapping]]
- [[PSSCH]] 복조 (depends_on) [[DMRS]]
- [[Sidelink_Congestion_Control]] (affects) [[SL PRS]] 자원 할당

## 관련 개념
- [[CSI-RS]] (part_of)
- [[DMRS]] (part_of)
- [[PT-RS]] (part_of)
- [[PRS]] (part_of)
- [[PSSCH]] (depends_on)
- [[SCI]] (depends_on)

## 스펙 근거
- [[TS 38.214]] §8.2: [[UE]] procedure for transmitting sidelink reference signals
- [[TS 38.214]] §8.2.1: [[CSI-RS]] transmission procedure
- [[TS 38.214]] §8.2.2: [[PSSCH]] [[DMRS]] transmission procedure
- [[TS 38.214]] §8.2.3: [[PT-RS]] transmission procedure
- [[TS 38.214]] §8.2.4: [[SL PRS]] transmission procedure
- [[TS 38.214]] §8.4: [[UE]] procedure for receiving reference signals
- [[TS 38.214]] §8.4.1: [[CSI-RS]] reception procedure
- [[TS 38.214]] §8.4.2: [[DMRS]] reception procedure for [[RSRP]] computation
- [[TS 38.214]] §8.4.3: [[PT-RS]] reception procedure
- [[TS 38.214]] §8.4.4: [[SL PRS]] reception procedure

## 소스
- 3GPP TS 38.214 V18.0.0 (2024-03)