# PRS_Measurement_Procedures

## 정의
[[PRS]] (Positioning Reference Signal) 측정 절차는 UE가 네트워크로부터 수신한 측위 참조 신호를 활용하여 위치 정보를 산출하고 이를 보고하는 일련의 L1/L2 과정을 의미한다.

## 요약
UE는 [[PRS]]를 활용하여 DL-TDOA, DL-AoD 등의 측위 기법을 수행한다. 이를 위해 주파수 호핑, 대역폭 집성, 캐리어 위상 측정 등 다양한 물리 계층 메커니즘을 지원하며, 측정 갭 및 우선순위 관리를 통해 효율적인 측정을 수행한다.

## 상세 설명
- **PRS receiver frequency hopping**: UE는 다중 대역폭 부분(BWP) 또는 캐리어에 걸쳐 설정된 [[PRS]] 자원을 수신하기 위해 주파수 호핑을 수행할 수 있다. 이는 주파수 선택적 페이딩 환경에서 측위 정확도를 높이기 위해 사용된다.
- **PRS for carrier phase positioning**: 고정밀 측위를 위해 UE는 [[PRS]]의 캐리어 위상을 측정한다. 이는 일반적인 ToA(Time of Arrival) 기반 측정보다 정밀한 거리 추정을 가능하게 한다.
- **PRS bandwidth aggregation**: UE는 서로 다른 대역폭에 걸쳐 있는 [[PRS]] 자원들을 결합하여 유효 대역폭을 확장함으로써 시간 도메인 분해능을 향상시킨다.
- **측정 절차**: UE는 RRC_CONNECTED 상태뿐만 아니라 RRC_INACTIVE 상태에서도 [[PRS]] 측정을 수행할 수 있으며, 측정 결과에는 LoS/NLoS 지시 정보 및 TEG(Timing Error Group) 정보가 포함될 수 있다.

## 인과 관계
- [[PRS_Generation_Mapping]] (depends_on): UE의 측정 절차는 네트워크가 생성하여 전송하는 [[PRS]]의 자원 설정에 의존한다.
- [[Frame_Structure_Numerology]] (affects): 측정에 사용되는 부반송파 간격(SCS) 및 슬롯 구조는 [[PRS]] 수신 타이밍과 측정 정확도에 영향을 미친다.

## 관련 개념
- [[PRS]] (part_of)
- [[Reference_Signals]] (part_of)
- [[Frame_Structure_Numerology]] (affects)

## 스펙 근거
- TS 38.214 §5.1.6.5.1에 따르면, UE는 설정된 파라미터에 따라 [[PRS]] 수신 시 주파수 호핑을 수행할 수 있다.
- TS 38.214 §5.1.6.5.2에 따르면, 캐리어 위상 기반 측위를 위한 [[PRS]] 수신 및 처리 절차가 정의된다.
- TS 38.214 §5.1.6.5.3에 따르면, 다중 대역폭에 걸친 [[PRS]] 자원 집성(Bandwidth Aggregation)을 통한 측정 절차가 규정된다.

## 소스
- 3GPP TS 38.214 V17.9.0 (2023-12) "NR; Physical layer procedures for data"