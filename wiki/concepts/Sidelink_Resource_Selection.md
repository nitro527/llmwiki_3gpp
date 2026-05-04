# Sidelink_Resource_Selection

## 정의
[[Sidelink]] 리소스 할당 모드 2(Mode 2)에서의 자원 선택 절차는 [[UE]]가 상위 계층으로부터 전송 요청을 받았을 때, [[PSSCH]] 전송을 위한 후보 자원 집합을 결정하고, 주변 [[UE]]들의 전송 정보를 바탕으로 간섭을 최소화할 수 있는 최적의 자원을 선택하는 과정을 의미합니다.

## 요약
모드 2 자원 선택은 [[Sensing]] 기반의 자원 제외 메커니즘을 핵심으로 합니다. [[UE]]는 [[Full_Sensing]] 또는 [[Partial_Sensing]]을 통해 수집된 정보를 바탕으로 후보 자원 집합에서 간섭 가능성이 높은 자원을 제외하며, 최종적으로 남은 자원 중 우선순위에 따라 전송 자원을 결정합니다. 또한, 다른 [[UE]]로부터 수신된 [[Inter_UE_Coordination]] 정보를 활용하여 선호되거나 선호되지 않는 자원 집합을 식별할 수 있습니다.

## 상세 설명
TS 38.214 §8.1.4에 따라 모드 2 자원 선택 절차는 다음과 같이 수행됩니다.

1. 후보 자원 결정: [[UE]]는 상위 계층에 의해 설정된 자원 풀 내에서 가능한 모든 자원을 후보 자원 집합으로 설정합니다.
2. [[Sensing]] 수행:
   - [[Full_Sensing]]: 자원 풀 전체에 대해 일정 기간 동안 [[PSCCH]]를 디코딩하고 [[RSRP]]를 측정하여 간섭을 평가합니다.
   - [[Partial_Sensing]]: 특정 시간/주파수 영역에 대해서만 선택적으로 [[Sensing]]을 수행하여 전력 소모를 줄입니다.
3. 자원 제외: 측정된 [[RSRP]]가 임계값을 초과하거나, 다른 [[UE]]의 [[SCI]]를 통해 예약된 자원인 경우 해당 자원을 후보 집합에서 제외합니다.
4. [[Inter_UE_Coordination]]: TS 38.214 §8.1.4A 및 §8.1.4C에 따라, 다른 [[UE]]로부터 수신된 선호(preferred) 또는 비선호(non-preferred) 자원 정보를 자원 선택 과정에 반영합니다. 이는 자원 충돌을 방지하고 효율적인 자원 공유를 가능하게 합니다.

## 인과 관계
- [[Sensing]] (depends_on) [[Sidelink_Resource_Selection]]
- [[Inter_UE_Coordination]] (affects) [[Sidelink_Resource_Selection]]
- [[PSSCH]] (part_of) [[Sidelink_Resource_Selection]]

## 관련 개념
- [[Sensing]] (depends_on)
- [[PSSCH]] (part_of)
- [[SCI]] (depends_on)
- [[Inter_UE_Coordination]] (affects)

## 스펙 근거
- TS 38.214 §8.1.4: UE procedure for determining the subset of resources to be reported to higher layers in PSSCH resource selection in sidelink resource allocation mode 2
- TS 38.214 §8.1.4A: UE procedure for determining a set of preferred or non-preferred resources for another UE's transmission
- TS 38.214 §8.1.4C: UE procedure for using a received non-preferred resource set

## 소스
- 3GPP TS 38.214 V17.x.x (Release 17) "Physical layer procedures for data"