# PUSCH_PTRS_Transmission

## 정의
[[PUSCH]] [[PT_RS]] 전송 절차는 위상 잡음(Phase Noise)으로 인한 성능 저하를 보상하기 위해 [[UE]]가 상향링크 데이터 채널 전송 시 [[Reference_Signals]]의 일종인 [[PT_RS]]를 생성하고 매핑하는 과정을 의미합니다.

## 요약
[[PUSCH]] [[PT_RS]] 전송은 [[PUSCH_Transform_Precoding]] 활성화 여부에 따라 결정됩니다. 이 절차는 [[PT_RS]] 밀도 결정, 안테나 포트 매핑, 그리고 전력 제어를 포함하며, 네트워크 설정에 따라 [[UE]]가 적절한 시간-주파수 자원에 [[PT_RS]]를 배치하여 전송합니다.

## 상세 설명
[[PT_RS]] 전송 절차는 크게 두 가지 모드로 나뉩니다.

1. [[PUSCH_Transform_Precoding]]이 비활성화된 경우:
   - [[UE]]는 상위 계층 파라미터인 `PTRS-UplinkConfig`에 따라 [[PT_RS]] 전송 여부와 밀도를 결정합니다.
   - 주파수 밀도는 스케줄링된 대역폭에 따라 결정되며, 시간 밀도는 스케줄링된 심볼 수와 설정된 임계값에 따라 결정됩니다.
   - [[PT_RS]]는 [[DMRS_Generation_Mapping]]과 연관된 안테나 포트에 매핑됩니다.

2. [[PUSCH_Transform_Precoding]]이 활성화된 경우:
   - [[PT_RS]]는 [[PUSCH_Transform_Precoding]]이 적용된 신호의 위상 잡음을 보상하기 위해 사용됩니다.
   - 이 경우 [[PT_RS]]는 데이터 심볼과 함께 변환 프리코딩 과정을 거치며, 특정 서브캐리어에 매핑됩니다.

전력 제어 측면에서, [[PT_RS]]의 전송 전력은 [[PUSCH_Power_Control]] 프레임워크 내에서 결정되며, 데이터 심볼 대비 [[PT_RS]]의 전력 오프셋(Power Offset)은 상위 계층 시그널링을 통해 설정됩니다.

## 인과 관계
- [[PUSCH_Transform_Precoding]] (affects) [[PUSCH_PTRS_Transmission]]
- [[DMRS_Generation_Mapping]] (depends_on) [[PUSCH_PTRS_Transmission]]
- [[PUSCH_Power_Control]] (affects) [[PUSCH_PTRS_Transmission]]

## 관련 개념
- [[PUSCH]] (part_of)
- [[PT_RS]] (part_of)
- [[PUSCH_Transform_Precoding]] (affects)
- [[DMRS_Generation_Mapping]] (depends_on)
- [[PUSCH_Power_Control]] (affects)

## 스펙 근거
- TS 38.214 §6.2.3에 따르면, [[UE]]는 [[PUSCH]] 전송 시 [[PT_RS]] 전송 절차를 수행해야 합니다.
- TS 38.214 §6.2.3.1에 따르면, [[PUSCH_Transform_Precoding]]이 비활성화된 경우의 [[PT_RS]] 밀도 및 매핑 규칙이 정의되어 있습니다.
- TS 38.214 §6.2.3.2에 따르면, [[PUSCH_Transform_Precoding]]이 활성화된 경우의 [[PT_RS]] 전송 절차가 정의되어 있습니다.

## 소스
- 3GPP TS 38.214 v19.0.0, "Physical layer procedures for data"
- 3GPP TS 38.214 §6.2.3, §6.2.3.1, §6.2.3.2