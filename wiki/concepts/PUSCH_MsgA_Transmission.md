# PUSCH_MsgA_Transmission

## 정의
[[PUSCH]] MsgA Transmission은 2-step [[RACH]] 절차(Type-2 random access procedure)에서 [[UE]]가 상향링크 자원을 통해 전송하는 초기 데이터 전송 절차를 의미합니다.

## 요약
Type-2 random access procedure에서 [[UE]]는 MsgA를 통해 [[PRACH]]와 [[PUSCH]]를 동시에 전송합니다. 이때 [[PUSCH]] 전송은 상위 계층 파라미터에 의해 설정된 자원 할당, [[DMRS]] 설정, 주파수 호핑 규칙을 따르며, 특정 조건에 따라 전송 유효성이 결정됩니다.

## 상세 설명
TS 38.213 §8.1A에 따라 Type-2 random access procedure를 수행하는 [[UE]]는 다음과 같은 절차를 따릅니다.

- **기본 전송**: [[UE]]는 [[PUSCH]] 전송을 위해 상위 계층에서 제공하는 설정 정보를 사용합니다. 이는 [[Basic PUSCH transmission]] (2-12)의 기본 요구사항을 준수합니다.
- **자원 할당**: [[PUSCH]] 자원은 MsgA 전송을 위해 설정된 [[BWP]] 내에서 결정됩니다.
- **DMRS 설정**: MsgA [[PUSCH]]를 위한 [[DMRS]]는 상위 계층 파라미터에 의해 설정된 시퀀스 및 매핑 규칙을 따릅니다.
- **주파수 호핑**: [[PUSCH]] 전송 시 주파수 호핑이 설정된 경우, [[UE]]는 정의된 호핑 패턴에 따라 자원을 활용합니다.
- **병렬 전송 및 우선순위**: 
    - [[Parallel MsgA and SRS/PUCCH/PUSCH transmissions across CCs in inter-band CA]] (9-3) 및 [[Parallel MsgA and SRS/PUCCH/PUSCH transmissions across CCs in intra-band non-contiguous CA]] (39-4)와 같은 다중 캐리어 환경에서의 병렬 전송이 지원됩니다.
    - [[Parallel SRS and PUCCH/PUSCH transmission across CCs in inter-band CA]] (4-25) 및 [[Parallel PRACH and SRS/PUCCH/PUSCH transmissions across CCs in inter-band CA]] (4-26) 조건이 충족될 경우 병렬 전송이 가능합니다.
    - [[Simultaneous transmission of SRS on an SUL/non-SUL carrier and PUSCH/PUCCH/SRS on the other UL carrier in the same cell]] (6-19)가 적용될 수 있습니다.
- **기타 기능**: 
    - [[Codebook based PUSCH MIMO transmission]] (2-14) 및 [[non-codebook based PUSCH transmission]] (2-15)를 지원합니다.
    - [[For SRS for CB PUSCH and antenna switching on FR1, zero slot offset for aperiodic SRS transmission]] (2-58)이 적용될 수 있습니다.
    - [[UL channel access for semi-static channel access mode]] (10-1a) 및 [[Enable configured UL transmissions when SFI field in DCI 2_0 is configured but DCI 2_0 is not detected]] (10-25)가 고려됩니다.
    - [[Extended CP range of more than one symbol for CG-PUSCH]] (10-13a)와 같은 확장된 CP 설정이 지원될 수 있습니다.

## 인과 관계
- [[RACH_Procedure_L1]] (triggers) MsgA 전송 절차를 시작함
- [[PUSCH_Resource_Allocation]] (depends_on) MsgA 전송을 위한 자원 위치를 결정함
- [[DMRS_Generation_Mapping]] (affects) MsgA [[PUSCH]]의 복조 성능을 결정함
- [[PUSCH_Frequency_Hopping]] (affects) 주파수 다이버시티를 제공함

## 관련 개념
- [[PUSCH]] (part_of)
- [[RACH]] (part_of)
- [[DMRS]] (depends_on)
- [[BWP]] (depends_on)

## 스펙 근거
- TS 38.213 §8.1A: Type-2 random access procedure에서의 [[PUSCH]] 전송 절차 정의

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"