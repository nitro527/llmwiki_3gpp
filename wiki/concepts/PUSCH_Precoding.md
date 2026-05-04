# PUSCH_Precoding

## 정의
[[PUSCH]] 프리코딩은 [[Layer_Mapping]]을 거친 데이터 심볼들을 실제 안테나 포트로 매핑하기 위해 선형 변환을 수행하는 과정입니다. 이는 [[DCI]]를 통해 전달된 프리코딩 정보 및 [[SRS]] 기반의 코드북/비코드북 설정을 바탕으로 수행됩니다.

## 요약
[[PUSCH]] 프리코딩은 안테나 포트 간의 공간적 다중화를 지원하며, [[DCI]] 포맷 0_1 및 0_2에 포함된 프리코딩 정보 필드와 [[SRI]]를 통해 제어됩니다. 본 기능은 [[Transform_Precoding]] 활성화 여부에 따라 적용 방식이 달라지며, Rel.18에서 도입된 향상된 [[DMRS]] 포트 및 [[PTRS]] 연관 설정을 포함합니다.

## 상세 설명
[[PUSCH]] 프리코딩은 TS 38.211 §6.3.1.5에 정의된 바와 같이, 레이어 매핑된 신호 $x(i)$에 대해 프리코딩 행렬 $W$를 곱하여 안테나 포트 신호 $y(i)$를 생성합니다.

1. **코드북 기반 프리코딩**: [[SRS]] 자원 지시자([[SRI]])를 통해 선택된 프리코딩 행렬이 적용됩니다.
2. **비코드북 기반 프리코딩**: [[UE]]가 보고한 [[SRS]] 자원을 기반으로 기지국이 결정한 프리코딩이 적용됩니다.
3. **DCI 필드 해석**: [[DCI]] 포맷 0_1 및 0_2의 'Precoding information and number of layers' 필드는 레이어 수와 프리코딩 행렬을 결정합니다.
4. **Rel.18 확장**: 
   - 1~8 레이어에 대한 향상된 [[DMRS]] 포트 지원.
   - 1 또는 2 포트 [[PTRS]]와 [[DMRS]] 간의 연관 설정.
   - Single-DCI 기반 STx2P(Spatial Transmission with 2 Panels) SDM/SFN 방식 지원.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) -> [[PUSCH_Precoding]]
- [[SRS_Generation_Mapping]] (depends_on) -> [[PUSCH_Precoding]]
- [[PUSCH_Precoding]] (affects) -> [[DMRS_Generation_Mapping]]
- [[PUSCH_Precoding]] (affects) -> [[PTRS_Generation_Mapping]]

## 관련 개념
- [[PUSCH]] (part_of)
- [[Layer_Mapping]] (depends_on)
- [[Transform_Precoding]] (affects)
- [[SRI]] (depends_on)
- [[DMRS]] (affects)
- [[PTRS]] (affects)
- [[DCI_Formats_Processing]] (affects)
- [[SRS_Generation_Mapping]] (affects)
- [[DMRS_Generation_Mapping]] (depends_on)
- [[PTRS_Generation_Mapping]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.1.5: [[PUSCH]] 프리코딩 수학적 모델 및 절차 정의.
- TS 38.212 §7.3.1.1.2: [[DCI]] 포맷 0_1 내 프리코딩 정보 필드 정의.
- TS 38.212 §7.3.1.1.3: [[DCI]] 포맷 0_2 내 프리코딩 정보 필드 정의.

## 소스
- 3GPP TS 38.211 V17.9.0 (Release 17/18)
- 3GPP TS 38.212 V17.9.0 (Release 17/18)
- 3GPP TS 38.822 (UE Feature Priority 관련 항목)

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/PUSCH_Layer_Mapping.md
- concepts/PUSCH_Precoding.md
- concepts/PUSCH_Resource_Mapping.md
- entities/PUSCH.md