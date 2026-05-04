# PUSCH_Transmission_Procedures

## 정의
[[PUSCH]] 전송 절차는 [[UE]]가 상향링크 데이터를 기지국으로 전송하기 위해 수행하는 전송 스킴 결정, 자원 할당, 그리고 [[Transform_Precoding]] 적용 과정을 의미한다.

## 요약
[[PUSCH]] 전송은 [[Codebook_Based_Transmission]]과 [[Non_Codebook_Based_Transmission]]으로 구분되며, 시간 및 주파수 영역에서의 자원 할당 방식과 [[Configured_Grant_Transmission]]을 통한 전송을 포함한다. 또한, 특정 조건에서 [[Transform_Precoding]]을 적용하여 전송 효율을 최적화한다.

## 상세 설명
1. **전송 스킴**:
   - [[Codebook_Based_Transmission]]: [[DCI]] 내의 [[TPMI]]를 기반으로 프리코딩 행렬을 결정하여 전송한다.
   - [[Non_Codebook_Based_Transmission]]: [[SRS]] 자원 기반의 프리코딩을 사용하여 [[UE]]가 스스로 프리코딩을 결정한다.

2. **자원 할당**:
   - 시간 영역: [[Slot]] 내의 시작 심볼과 길이를 결정하며, [[PUSCH_Repetition_Procedures]]를 통해 반복 전송을 수행한다.
   - 주파수 영역: [[Uplink_Resource_Allocation_Type_0]], [[Uplink_Resource_Allocation_Type_1]], [[Uplink_Resource_Allocation_Type_2]]를 사용하여 [[Physical_Resource_Block]]을 할당한다.
   - [[Configured_Grant_Transmission]]: [[DCI]] 없이 미리 설정된 자원을 사용하여 전송하며, [[PUSCH_Repetition_Procedures]]를 통한 반복 전송이 가능하다.

3. **Transform Precoding**:
   - [[UE]]는 상위 계층 파라미터 `transformPrecoder` 설정에 따라 [[DFT-s-OFDM]] 파형을 생성하기 위해 [[Transform_Precoding]]을 적용한다.

## 인과 관계
- [[DCI]] (triggers) [[PUSCH]] 전송
- [[SRS]] (affects) [[Non_Codebook_Based_Transmission]]의 프리코딩 결정
- `transformPrecoder` 설정 (affects) [[Transform_Precoding]] 적용 여부
- [[Configured_Grant_Transmission]] (depends_on) 상위 계층 설정

## 관련 개념
- [[PUSCH]] (part_of)
- [[Codebook_Based_Transmission]] (similar_to)
- [[Non_Codebook_Based_Transmission]] (similar_to)
- [[Transform_Precoding]] (depends_on)
- [[Configured_Grant_Transmission]] (part_of)
- [[PUSCH_Repetition_Procedures]] (affects)

## 스펙 근거
- TS 38.214 §6.1.1: [[PUSCH]] 전송 스킴 정의
- TS 38.214 §6.1.2: 시간 및 주파수 영역 자원 할당 및 [[Configured_Grant_Transmission]] 절차
- TS 38.214 §6.1.3: [[Transform_Precoding]] 적용 절차

## 소스
- 3GPP TS 38.214 v16.9.0 (Release 16)