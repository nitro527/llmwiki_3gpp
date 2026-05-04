# PUSCH_Frequency_Hopping

## 정의
[[PUSCH]] 주파수 호핑은 [[UE]]가 상향링크 전송 시 주파수 도메인에서 자원 블록 할당을 동적으로 변경하여 주파수 선택적 페이딩(frequency-selective fading) 환경에서 주파수 다이버시티 이득을 얻기 위한 기술이다.

## 요약
- [필수(항상)] [[SRS]], [[PUCCH]] 관련 기본 동작이 지원된다.
- [필수(cap)] PUSCH에 대한 Intra-slot 주파수 호핑이 지원된다.
- [선택] Inter-slot 주파수 호핑 및 강화된 Inter-slot 주파수 호핑(Inter-slot bundling 포함)이 지원된다.
- 주파수 호핑은 PUSCH Repetition Type A와 Type B, 그리고 다중 슬롯에 걸친 TB 처리에 적용된다.

## 상세 설명
PUSCH 주파수 호핑은 전송되는 데이터의 주파수 위치를 시간 경과에 따라 변경함으로써 채널 품질이 나쁜 특정 주파수 대역의 영향을 분산시킨다.

1. **Intra-slot 주파수 호핑**: 하나의 [[Slot]] 내에서 전송 심볼들을 두 개의 호핑 그룹으로 나누어 서로 다른 주파수 자원을 사용한다.
2. **Inter-slot 주파수 호핑**: 서로 다른 슬롯 간에 주파수 자원을 변경하여 전송한다.
3. **자원 할당**: 상위 계층 파라미터(예: `frequencyHopping`) 설정에 따라 호핑 모드가 결정되며, DCI(Downlink Control Information)를 통해 주파수 오프셋이 지시된다.
4. **PUSCH Repetition Type A/B**: 각 타입별로 정의된 호핑 규칙에 따라 자원 매핑이 수행된다. Type B의 경우 심볼 단위의 호핑 제어가 더 유연하게 적용된다.

## 인과 관계
- [[PUSCH_Resource_Allocation]] (depends_on): 주파수 호핑은 할당된 자원 블록 내에서 수행되므로 자원 할당 방식에 의존한다.
- [[PUSCH_Repetition_Procedures]] (affects): 반복 전송 시 호핑 여부에 따라 각 반복본의 주파수 위치가 결정된다.
- [[DMRS_Generation_Mapping]] (affects): 주파수 호핑 발생 시 [[DMRS]]의 위치와 시퀀스 매핑도 호핑 패턴을 따라야 한다.

## 관련 개념
- [[PUSCH]] (part_of)
- [[PUSCH_Repetition_Procedures]] (affects)
- [[PUSCH_Resource_Allocation]] (depends_on)
- [[DMRS_Generation_Mapping]] (affects)

## 스펙 근거
- TS 38.214 §6.3에 따르면, PUSCH 주파수 호핑 절차는 전송 타입에 따라 정의된다.
- TS 38.214 §6.3.1에 따르면, PUSCH Repetition Type A 및 다중 슬롯 TB 처리를 위한 주파수 호핑 규칙이 명시되어 있다.
- TS 38.214 §6.3.2에 따르면, PUSCH Repetition Type B를 위한 주파수 호핑 메커니즘이 정의되어 있다.

## 소스
- 3GPP TS 38.214 V17.9.0 (Release 17) "Physical layer procedures for data"
- 3GPP TS 38.822 "UE Feature List"