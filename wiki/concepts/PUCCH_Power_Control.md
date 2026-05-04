# PUCCH_Power_Control

## 정의
[[PUCCH]] 전송 전력 제어는 [[UE]]가 상향링크 제어 채널인 [[PUCCH]]를 전송할 때, 기지국이 요구하는 수신 품질을 만족하면서도 간섭을 최소화하기 위해 전송 전력을 결정하는 절차를 의미합니다.

## 요약
[[PUCCH]] 전송 전력은 상위 계층에서 설정된 파라미터와 [[DCI]]를 통해 전달되는 [[TPC]] 명령을 조합하여 계산됩니다. 본 절차는 [[UE]]의 기본 전력 제어 능력(8-3) 및 2개의 [[PUCCH]] 폐루프(closed loop) 전력 제어(8-9)를 포함하며, 다중 [[TRP]] 환경에서의 반복 전송 및 공간적 관계 설정 등 다양한 확장 기능을 지원합니다.

## 상세 설명
[[TS 38.213]] §7.2.1에 따라, [[UE]]는 특정 슬롯 $i$에서 [[PUCCH]] 전송을 위한 전송 전력 $P_{PUCCH, b, f, c}(i, q_u, q_d, l)$을 다음과 같이 결정합니다.

1. **기본 전력 공식**: 전송 전력은 목표 전력($P_{O, PUCCH}$), 경로 손실 보상($\alpha$), 경로 손실 추정치($PL$), 그리고 폐루프 조정값($f_b(i, l)$)의 합으로 구성됩니다.
2. **폐루프 관리**: [[UE]]는 상위 계층 설정에 따라 하나 또는 두 개의 폐루프 전력 제어 상태를 유지할 수 있습니다. 이는 [[PUCCH]] 반복 전송이나 다중 [[TRP]] 시나리오에서 유연한 전력 제어를 가능하게 합니다.
3. **TPC 명령 처리**: [[DCI]] 내의 [[TPC]] 필드는 폐루프 상태를 업데이트하는 데 사용됩니다. 다중 [[TRP]] 환경에서는 두 번째 [[TPC]] 필드를 통해 추가적인 전력 조정이 가능합니다.
4. **포맷별 조정**: [[PUCCH]] 포맷에 따라 전력 제어 파라미터 세트가 다르게 적용될 수 있으며, 이는 [[PUCCH_Resource_Sets]]와 연계되어 동작합니다.

## 인과 관계
- [[PUCCH_Spatial_Setting]] (depends_on): 전력 제어에 필요한 경로 손실 추정 및 폐루프 인덱스 선택은 공간적 설정에 의존합니다.
- [[PUCCH_Resource_Sets]] (depends_on): 특정 [[PUCCH]] 포맷 및 자원 할당은 적용할 전력 제어 파라미터 세트를 결정합니다.
- [[Uplink_Power_Control]] (part_of): 본 절차는 전체 상향링크 전력 제어 프레임워크의 일부입니다.
- [[DCI_Formats_Processing]] (triggers): [[DCI]] 내의 [[TPC]] 명령은 폐루프 전력 상태를 갱신하는 트리거 역할을 합니다.

## 관련 개념
- [[Uplink_Power_Control]] (part_of)
- [[PUCCH_Spatial_Setting]] (depends_on)
- [[PUCCH_Resource_Sets]] (depends_on)
- [[DCI_Formats_Processing]] (triggers)
- [[PUCCH_Repetition]] (affects)

## 스펙 근거
- [[TS 38.213]] §7.2.1: [[PUCCH]] 전송 전력 결정 절차 및 UE 동작 정의
- [[TS 38.822]]: 
  - 8-3: Basic power control operation (필수)
  - 8-9: UL power control with 2 PUCCH closed loops (필수-cap)
  - 8-8: UL power control with 2 PUSCH closed loops (필수-cap)
  - 23-3-2c: Second TPC field for multi-TRP PUCCH repetition (선택)
  - 23-3-2d: Updating two Spatial relation or two sets of power control parameters for PUCCH group (선택)
  - 23-3-2e: Maximum number of power control parameter sets configured for multi-TRP PUCCH repetition in FR1 (선택)
  - 23-3-3: Multi-TRP PUCCH repetition-intra-slot (선택)
  - 4-1: Basic UL control channel (필수)
  - 4-2: 2 PUCCH of format 0 or 2 in consecutive symbols (선택)

## 소스
- 3GPP TS 38.213 Release 18 (v18.0.0) §7.2.1
- 3GPP TS 38.822 Release 18 (v18.0.0)