# IAB_Resource_Configuration

## 정의
[[IAB_Node]]가 네트워크 내에서 자원을 효율적으로 관리하기 위해 사용하는 자원 구성 체계로, 시간 및 주파수 영역에서 자원의 가용성을 Hard, Soft, Unavailable로 분류하고 이를 동적으로 제어하는 절차를 의미합니다.

## 요약
[[IAB_DU]]는 상위 계층 시그널링을 통해 자원을 구성하며, 특정 자원 영역에 대해 [[DCI]] format 2_5를 사용하여 가용성 지시(Availability Indication, AI)를 수행함으로써 동적인 자원 활용을 가능하게 합니다.

## 상세 설명
[[IAB_Node]]의 자원 구성은 다음과 같은 세 가지 유형으로 구분됩니다.

* Hard 자원: [[IAB_DU]]가 항상 가용하다고 간주하는 자원입니다.
* Soft 자원: 상위 계층에 의해 구성되지만, 실제 가용 여부는 [[DCI]] format 2_5를 통한 동적 지시에 따라 결정되는 자원입니다.
* Unavailable 자원: [[IAB_DU]]가 해당 자원을 사용하지 않는 것으로 간주하는 자원입니다.

[[IAB_DU]]는 [[PDCCH]]를 통해 전송되는 [[DCI]] format 2_5를 수신하여, Soft 자원으로 설정된 영역의 가용성을 업데이트합니다. 만약 [[IAB_DU]]가 특정 Soft 자원에 대해 가용성 지시를 받지 못한 경우, 해당 자원은 Unavailable로 간주됩니다. 또한, [[IAB_Node]]는 [[HSNA]] (Hard/Soft/Not-Available) 설정을 통해 자원 사용 우선순위와 제약 사항을 관리합니다.

## 인과 관계
- [[IAB_Node]] (part_of)
- [[DCI]] (triggers) [[IAB_Resource_Configuration]]의 가용성 상태 변경
- [[IAB_DU]] (depends_on) [[IAB_Resource_Configuration]]을 통한 자원 스케줄링

## 관련 개념
- [[IAB_Node]] (part_of)
- [[DCI]] (affects)
- [[IAB_DU]] (depends_on)

## 스펙 근거
- TS 38.213 §14.1에 따르면, [[IAB_DU]]는 상위 계층 파라미터 `resourceType`을 통해 Hard, Soft, Unavailable 자원을 구성함.
- TS 38.213 §14.2에 따르면, [[DCI]] format 2_5는 Soft 자원의 가용성을 지시하기 위해 사용되며, 지시되지 않은 Soft 자원은 Unavailable로 처리됨.

## 소스
- 3GPP TS 38.213 V18.0.0 (Release 18), "NR; Physical layer procedures for control"