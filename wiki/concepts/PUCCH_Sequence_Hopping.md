# PUCCH_Sequence_Hopping

## 정의
[[PUCCH]] 전송 시 사용되는 시퀀스의 그룹 호핑(Group Hopping), 시퀀스 호핑(Sequence Hopping) 및 순환 시프트(Cyclic Shift) 호핑을 제어하는 물리 계층 절차를 의미합니다.

## 요약
PUCCH 시퀀스 호핑은 상향링크 제어 채널의 신뢰성을 높이고 셀 간 간섭을 무작위화하기 위해 적용됩니다. 
- [필수(항상)] 4-1: Basic UL control channel 지원
- [필수(cap)] 4-3, 4-4, 4-5: 주파수 호핑이 활성화된 PUCCH format 2, 3, 4 지원
- [필수(cap)] 4-6, 4-7: 주파수 호핑이 비활성화된 PUCCH format 0, 1, 2, 3, 4 지원
- [선택] 25-3b, 30-4f: PUCCH 반복 전송을 위한 서브슬롯/슬롯 간 주파수 호핑 및 [[DMRS]] 번들링 지원
- [선택] 33-4a, 33-5-1j: 멀티캐스트를 위한 NACK-only 기반 [[HARQ]]-ACK 피드백 지원
- [선택] 40-5-1b, 40-5-2b: [[SRS]] 콤 오프셋 및 순환 시프트 호핑과 그룹/시퀀스 호핑의 결합 지원

## 상세 설명
PUCCH 시퀀스 호핑은 크게 그룹/시퀀스 호핑과 순환 시프트 호핑으로 나뉩니다.

### Group and Sequence Hopping
PUCCH 전송을 위한 시퀀스 그룹 호핑은 상위 계층 파라미터 `pucch-GroupHopping`에 의해 결정됩니다. 
- `neither`: 그룹 호핑과 시퀀스 호핑이 모두 비활성화됩니다.
- `enabled`: 그룹 호핑이 활성화됩니다.
- `disabled`: 그룹 호핑이 비활성화됩니다.

시퀀스 호핑은 `pucch-GroupHopping`이 `enabled`로 설정된 경우에만 적용 가능하며, 특정 슬롯 내에서 시퀀스 그룹 내의 시퀀스 번호를 변경하여 간섭을 분산시킵니다.

### Cyclic Shift Hopping
순환 시프트 호핑은 PUCCH 포맷에 따라 적용 여부가 결정됩니다. 이는 동일한 자원을 사용하는 사용자 간의 직교성을 유지하거나, 채널 추정 성능을 향상시키기 위해 심볼 단위 또는 슬롯 단위로 순환 시프트 값을 변경하는 메커니즘입니다.

## 인과 관계
- [[PUCCH_Resource_Sets]] (depends_on): PUCCH 자원 설정에 따라 호핑 파라미터가 적용됨
- [[DMRS_Generation_Mapping]] (affects): 호핑된 시퀀스는 DMRS 생성 시 기준값으로 사용됨
- [[PUCCH_Format_Processing]] (part_of): PUCCH 신호 생성 과정의 일부로 수행됨

## 관련 개념
- [[PUCCH]] (part_of)
- [[DMRS]] (affects)
- [[HARQ]] (depends_on)
- [[SRS]] (similar_to)

## 스펙 근거
- TS 38.211 §6.3.2.2.1: Group and sequence hopping 절차 정의
- TS 38.211 §6.3.2.2.2: Cyclic shift hopping 절차 정의

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03) "Physical channels and modulation"
- 3GPP TS 38.822 V16.0.0 (2020-07) "UE features"