# PRS

## 정의
[[PRS]] (Positioning Reference Signal)는 [[UE]]의 위치 측정을 위해 네트워크가 하향링크(DL)로 전송하는 전용 참조 신호입니다.

## 요약
[[PRS]]는 [[UE]]의 위치 기반 서비스(LCS)를 지원하기 위해 설계된 하향링크 참조 신호입니다. 본 신호는 [[DL-TDOA]], [[DL-AoD]], [[Multi-RTT]]와 같은 다양한 측위 기법을 지원하며, 주파수 도약(Frequency Hopping), 대역폭 집성(Bandwidth Aggregation), 그리고 반송파 위상(Carrier Phase) 측정을 위한 고급 기능을 포함합니다.

## 상세 설명
[[PRS]] 수신 절차는 [[TS 38.214]] §5.1.6.5에 정의되어 있으며, 주요 기능은 다음과 같습니다.

*   **PRS receiver frequency hopping**: [[UE]]는 설정된 주파수 도약 패턴에 따라 [[PRS]] 자원을 수신합니다. 이는 주파수 선택적 페이딩 환경에서 측위 정확도를 높이기 위해 사용됩니다.
*   **PRS for carrier phase positioning**: 고정밀 측위를 위해 [[PRS]]를 이용한 반송파 위상 측정을 지원합니다. 이는 일반적인 시간 기반 측정보다 높은 정밀도를 제공합니다.
*   **PRS bandwidth aggregation**: 여러 [[PRS]] 자원 세트가 서로 다른 대역폭에 걸쳐 설정된 경우, [[UE]]는 이를 결합하여 더 넓은 유효 대역폭을 확보함으로써 시간 도메인 분해능을 향상시킬 수 있습니다.

## 인과 관계
*   [[PRS]] 수신 능력(Capability)은 [[UE]]의 측위 보고 성능에 영향을 미칩니다.
*   [[PRS]] 자원 구성은 [[DL-TDOA]], [[DL-AoD]], [[Multi-RTT]]와 같은 측위 기법의 구현을 가능하게 합니다.

## 관련 개념
*   [[Reference_Signals]] (part_of)
*   [[PRS_Generation_Mapping]] (depends_on)
*   [[PRS_Measurement_Procedures]] (triggers)

## 스펙 근거
*   [[TS 38.214]] §5.1.6.5: PRS reception procedure
*   [[TS 38.214]] §5.1.6.5.1: PRS receiver frequency hopping
*   [[TS 38.214]] §5.1.6.5.2: PRS for carrier phase positioning
*   [[TS 38.214]] §5.1.6.5.3: PRS bandwidth aggregation for positioning measurements

## 소스
*   3GPP TS 38.214 V17.9.0 (Release 17)