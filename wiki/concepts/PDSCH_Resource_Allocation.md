# PDSCH_Resource_Allocation

## 정의
[[PDSCH]] 자원 할당은 [[gNB]]가 [[UE]]에게 하향링크 데이터를 전송하기 위해 시간 및 주파수 도메인상의 물리적 자원을 지정하는 절차를 의미한다.

## 요약
[[PDSCH]] 자원 할당은 [[DCI]]를 통해 전달되는 정보를 기반으로 시간 도메인과 주파수 도메인에서 각각 수행된다. 시간 도메인에서는 슬롯 내의 시작 심볼과 길이를 결정하며, 주파수 도메인에서는 [[PRB]] 수준의 자원 블록 할당 방식(Type 0, Type 1)을 사용한다. 또한, 멀티캐스트/브로드캐스트를 위한 전용 할당 방식과 채널 추정 성능 향상을 위한 [[PRB]] 번들링 기법을 포함한다.

## 상세 설명
### 시간 도메인 자원 할당
[[TS 38.214 §5.1.2.1]]에 따라, [[PDSCH]]의 시간 도메인 자원 할당은 [[DCI]] 내의 'Time domain resource assignment' 필드를 통해 결정된다. 이 필드는 상위 계층에서 설정된 테이블의 행(row)을 가리키며, 각 행은 [[PDSCH]]의 시작 심볼 위치(S)와 길이(L), 그리고 [[Mapping_Type]]을 정의한다.

### 주파수 도메인 자원 할당
[[TS 38.214 §5.1.2.2]]에 따라 주파수 도메인 할당은 크게 두 가지 타입으로 나뉜다.
- **Resource allocation type 0**: [[Bitmap]]을 사용하여 [[VRB]] 그룹인 [[RBG]]를 할당한다.
- **Resource allocation type 1**: [[VRB]] 단위로 연속적인 자원을 할당한다.
- **Multicast/Broadcast**: [[TS 38.214 §5.1.2.2.3]]에 따라 멀티캐스트/브로드캐스트 전송을 위한 별도의 [[Resource_allocation_type_1]] 방식이 적용된다.

### PRB 번들링
[[TS 38.214 §5.1.2.3]]에 따라, [[UE]]는 인접한 [[PRB]]들에 대해 동일한 프리코딩이 적용된다고 가정할 수 있다. 이는 [[DMRS]] 기반의 채널 추정 성능을 최적화하기 위해 사용되며, [[PRB]] 번들링 크기는 상위 계층 설정에 따라 결정된다.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) [[PDSCH_Resource_Allocation]]
- [[PDSCH_Resource_Allocation]] (affects) [[PDSCH_Reception_Procedures]]
- [[PDSCH_Resource_Allocation]] (depends_on) [[Frame_Structure_Numerology]]

## 관련 개념
- [[PDSCH]] (part_of)
- [[DCI]] (triggers)
- [[PRB]] (part_of)
- [[Mapping_Type]] (depends_on)
- [[RBG]] (part_of)

## 스펙 근거
- [[TS 38.214 §5.1.2]]: PDSCH 자원 할당 일반 규정
- [[TS 38.214 §5.1.2.1]]: 시간 도메인 자원 할당
- [[TS 38.214 §5.1.2.2]]: 주파수 도메인 자원 할당 (Type 0, 1)
- [[TS 38.214 §5.1.2.2.3]]: 멀티캐스트/브로드캐스트를 위한 자원 할당
- [[TS 38.214 §5.1.2.3]]: PRB 번들링

## 소스
- 3GPP TS 38.214 V17.9.0 (2023-12) "Physical layer procedures for data"