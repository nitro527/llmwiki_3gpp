# PUSCH_Resource_Allocation

## 정의
[[PUSCH]] 전송을 위해 시간 및 주파수 도메인에서 물리적 자원을 할당하는 절차로, [[DCI]]를 통한 동적 스케줄링 또는 상위 계층 설정에 기반하여 결정되는 메커니즘입니다.

## 요약
[[PUSCH]] 자원 할당은 시간 도메인에서 슬롯 오프셋(K2)과 심볼 위치를 결정하고, 주파수 도메인에서 Type 0, 1, 2 중 하나의 방식을 사용하여 자원 블록(RB)을 할당합니다. 이는 [[PDCCH]]를 통해 수신된 [[DCI]] 정보와 상위 계층 파라미터에 의해 제어됩니다.

## 상세 설명
### 시간 도메인 자원 할당
[[PUSCH]]의 시간 도메인 자원 할당은 [[DCI]] 내의 'Time domain resource assignment' 필드를 통해 결정됩니다.
- K2 값 결정: [[TS 38.214]] §6.1.2.1.1에 따라, [[DCI]] 포맷과 [[RNTI]] 유형에 따라 적용할 테이블이 결정됩니다. 서브캐리어 간격(SCS)에 따른 파라미터 j와 Δ(RAR/fallbackRAR의 경우)를 사용하여 최종 슬롯 오프셋 K2를 산출합니다.
- 테이블 참조: [[TS 38.214]] Table 6.1.2.1.1-1부터 1C까지 각 [[DCI]] 포맷별로 적용 가능한 테이블이 정의되어 있으며, 이를 통해 시작 심볼(S)과 길이(L)를 포함한 슬롯 내 위치를 결정합니다.

### 주파수 도메인 자원 할당
[[PUSCH]] 주파수 도메인 자원 할당은 세 가지 타입으로 구분됩니다.
- Type 0: 비트맵 기반 할당으로, [[Transform_Precoding]]이 비활성화된 경우에만 지원됩니다.
- Type 1: RIV(Resource Indication Value) 기반 할당으로, [[Transform_Precoding]] 활성화 여부와 관계없이 지원됩니다.
- Type 2: 인터레이스(Interlace) 기반 할당으로, [[DCI]] 포맷 0_1/0_3에서 `useInterlacePUCCH-PUSCH`가 설정된 경우 사용됩니다.
- RB 인덱싱: 활성 [[Bandwidth_Part_Operation]] 내에서 가장 낮은 RB를 기준으로 인덱싱이 수행됩니다. [[DCI]]에 BWP 지시자 필드가 포함된 경우, 해당 BWP 내에서 자원을 할당합니다.

## 인과 관계
- [[PUSCH]] depends_on [[PDCCH_Resource_Mapping]] (DCI를 통한 자원 할당 정보 수신)
- [[PUSCH]] depends_on [[Bandwidth_Part_Operation]] (BWP 내에서 RB 인덱싱 수행)
- [[PUSCH]] depends_on [[Transform_Precoding]] (Type 0 자원 할당 사용 여부 결정)
- [[PUSCH]] depends_on [[DCI_Field_Mapping]] (Time/Frequency domain resource assignment 필드 해석)

## 관련 개념
- [[PUSCH]] (part_of)
- [[PDCCH]] (affects)
- [[Bandwidth_Part_Operation]] (affects)
- [[Transform_Precoding]] (affects)
- [[DCI_Field_Mapping]] (implements)

## 스펙 근거
- TS 38.214 §6.1.2.1.1: PUSCH 시간 도메인 자원 할당 테이블 결정 및 K2, j, Δ 파라미터 정의
- TS 38.214 §6.1.2.2: PUSCH 주파수 도메인 자원 할당 타입(Type 0, 1, 2) 및 RB 인덱싱 규칙

## 소스
- 3GPP TS 38.214 v19.0.0 (Release 19)