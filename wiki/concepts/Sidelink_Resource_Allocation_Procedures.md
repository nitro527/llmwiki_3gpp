# Sidelink_Resource_Allocation_Procedures

## 정의
[[Sidelink_Resource_Allocation_Procedures]]는 [[UE]]가 [[PSSCH]] 및 [[SL_PRS]] 전송을 위해 시간 및 주파수 도메인에서 적절한 자원을 결정하는 절차를 의미합니다. 이는 [[SCI]] format 1-A 및 1-B를 통해 전달되는 정보를 기반으로 수행됩니다.

## 요약
본 절차는 [[Sidelink]] 통신에서 자원 효율성을 극대화하기 위해 [[SCI]]를 통해 자원을 예약하거나, [[Inter-UE_coordination]]을 통해 선호/비선호 자원 집합을 식별하는 과정을 포함합니다. 특히 [[SL_PRS]] 전송 시 전용 자원 풀을 활용하는 메커니즘을 정의합니다.

## 상세 설명
[[Sidelink_Resource_Allocation_Procedures]]는 크게 다음과 같은 메커니즘으로 구성됩니다.

1. **PSSCH 자원 결정 (SCI format 1-A 기반)**:
   - [[UE]]는 수신된 [[SCI]] format 1-A의 정보를 바탕으로 [[PSSCH]] 전송을 위한 슬롯과 자원 블록을 결정합니다.
   - [[TRIV]] (Time Resource Indicator Value) 및 [[FRIV]] (Frequency Resource Indicator Value) 매핑을 통해 시간 및 주파수 자원을 할당합니다.
   - 자원 예약 정보를 활용하여 향후 전송할 자원을 미리 확보할 수 있습니다.

2. **선호/비선호 자원 집합 처리**:
   - [[Inter-UE_coordination]]을 통해 전달된 선호(preferred) 또는 비선호(non-preferred) 자원 집합 정보를 해석하여, 해당 자원 내에서 전송을 수행하거나 회피하는 절차를 수행합니다.

3. **SL PRS 자원 결정 (SCI format 1-B 기반)**:
   - 전용 [[SL_PRS]] 자원 풀 내에서 [[SCI]] format 1-B를 사용하여 [[SL_PRS]] 전송을 위한 슬롯 및 자원 블록을 결정합니다.
   - 이는 [[SL_PRS]] 전송을 위한 모드 1 및 모드 2 동작을 지원하며, 전용 자원 풀에서의 효율적인 위치 선정을 보장합니다.

## 인과 관계
- [[SCI]] (triggers) [[Sidelink_Resource_Allocation_Procedures]]
- [[Sidelink_Resource_Allocation_Procedures]] (affects) [[PSSCH]]
- [[Sidelink_Resource_Allocation_Procedures]] (affects) [[SL_PRS]]
- [[Inter-UE_coordination]] (depends_on) [[Sidelink_Resource_Allocation_Procedures]]

## 관련 개념
- [[PSSCH]] (part_of)
- [[SL_PRS]] (part_of)
- [[SCI]] (part_of)
- [[Inter-UE_coordination]] (similar_to)

## 스펙 근거
- TS 38.214 §8.1.5에 따르면, [[SCI]] format 1-A와 연관된 [[PSSCH]] 전송을 위한 슬롯 및 자원 블록 결정 절차가 정의됩니다.
- TS 38.214 §8.1.5A에 따르면, 선호 또는 비선호 자원 집합에 의해 지시되는 슬롯 및 자원 블록 결정 절차가 정의됩니다.
- TS 38.214 §8.2.4.2A에 따르면, 전용 [[SL_PRS]] 자원 풀에서 [[SCI]] format 1-B와 연관된 슬롯 및 [[SL_PRS]] 자원 결정 절차가 정의됩니다.

## 소스
- 3GPP TS 38.214 V18.0.0 (2024-03) "Physical layer procedures for data"