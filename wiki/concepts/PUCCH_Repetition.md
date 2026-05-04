# PUCCH_Repetition

## 정의
[[PUCCH]] 반복 전송(Repetition)은 신뢰성 향상을 위해 동일한 [[UCI]] 정보를 다수의 슬롯(slot) 또는 서브슬롯(subslot)에 걸쳐 반복적으로 전송하는 물리 계층 절차를 의미합니다.

## 요약
PUCCH 반복은 상위 계층 파라미터 설정을 통해 활성화되며, 특정 [[PUCCH_Format_Processing]]에 대해 반복 횟수(K)를 지정하여 전송합니다. 이는 커버리지 확장 및 신뢰성 보장을 위해 사용되며, 다중 TRP 환경이나 비면허 대역(unlicensed spectrum) 등 다양한 시나리오에 최적화된 기능을 제공합니다.

## 상세 설명
TS 38.213 §9.2.6에 따라 PUCCH 반복 절차는 다음과 같이 수행됩니다.

- 반복 횟수(K): 상위 계층 파라미터 `nrofSlots`를 통해 K=2, 4, 8 등의 반복 횟수가 설정됩니다.
- 슬롯 기반 반복: UE는 설정된 K개의 연속적인 슬롯에서 동일한 PUCCH 자원을 사용하여 전송을 수행합니다.
- 서브슬롯 기반 반복: 특정 환경에서는 슬롯보다 작은 단위인 서브슬롯을 기준으로 반복 전송이 수행될 수 있습니다.
- 주파수 호핑: 반복 전송 시 주파수 다이버시티를 얻기 위해 서브슬롯 간 또는 슬롯 간 주파수 호핑이 적용될 수 있습니다.
- 다중 TRP 지원: Multi-TRP 환경에서 반복 전송을 위한 스킴(scheme 1) 및 순환 매핑(cyclic mapping) 등이 지원되며, 전력 제어를 위한 별도의 파라미터 세트가 구성될 수 있습니다.
- DMRS 번들링: 반복 전송되는 PUCCH 간의 채널 추정 성능을 높이기 위해 [[DMRS_Generation_Mapping]]을 결합하는 DMRS 번들링이 적용될 수 있습니다.

## 인과 관계
- [[PUCCH_Resource_Sets]] (depends_on): 반복 전송을 위한 자원 설정은 PUCCH 자원 세트 구성에 의존합니다.
- [[PUCCH_Power_Control]] (affects): 반복 전송 시 각 전송 구간에 대한 전력 제어 파라미터가 적용됩니다.
- [[UCI_Reporting_Different_Priorities]] (triggers): UCI 우선순위에 따라 반복 전송 여부나 방식이 결정될 수 있습니다.

## 관련 개념
- [[PUCCH]] (part_of)
- [[UCI_Processing_PUCCH]] (depends_on)
- [[PUCCH_Power_Control]] (affects)
- [[DMRS_Bundling_Procedures]] (similar_to)

## 스펙 근거
- TS 38.213 §9.2.6: PUCCH repetition procedure에 관한 전반적인 절차 정의
- TS 38.822: 
    - [필수(cap)] 4-23: PUCCH format 1, 3, 4에 대한 다중 슬롯 반복 (K=2, 4, 8)
    - [선택] 10-37: 비면허 대역에서의 PUCCH format 1, 3, 4 반복
    - [선택] 23-3-2, 23-3-2b, 23-3-2c, 23-3-2e, 23-3-3: Multi-TRP PUCCH 반복 관련 기능
    - [선택] 25-2: PUCCH format 0, 2에 대한 다중 슬롯 반복
    - [선택] 25-3, 25-3a, 25-3b: 서브슬롯 기반 반복 및 동적 지시, 주파수 호핑
    - [선택] 30-4d: DMRS 번들링

## 소스
- 3GPP TS 38.213 "NR; Physical layer procedures for control"
- 3GPP TS 38.822 "NR; User Equipment (UE) radio transmission and reception features"