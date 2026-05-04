# PUSCH_Resource_Allocation

## 정의
[[PUSCH]] 시간 도메인 자원 할당은 기지국이 [[DCI]]를 통해 [[UE]]에게 상향링크 데이터 전송을 위한 시간적 위치(슬롯 및 심볼)와 반복 전송 방식을 지시하는 절차를 의미합니다.

## 요약
[[PUSCH]] 시간 도메인 자원 할당은 [[DCI]] 내의 Time domain resource assignment 필드를 사용하여 수행됩니다. 이 필드는 RRC로 설정된 테이블의 행을 가리키며, 해당 행은 슬롯 오프셋 [[K2]], 시작 심볼 및 길이 지시자 [[SLIV]], 그리고 매핑 타입(Type A 또는 Type B)을 포함합니다. 또한, 다중 슬롯에 걸친 반복 전송 및 [[TB]] 처리를 지원합니다.

## 상세 설명
TS 38.214 §6.1.2.1에 따라 [[PUSCH]] 시간 도메인 자원 할당은 다음과 같은 메커니즘으로 결정됩니다.

1. **테이블 선택**: [[UE]]는 RRC 파라미터 `pusch-TimeDomainAllocationList`를 통해 제공되는 테이블을 사용합니다. 만약 해당 파라미터가 없으면 기본 테이블이 적용됩니다.
2. **슬롯 오프셋 [[K2]]**: [[DCI]]가 수신된 슬롯과 [[PUSCH]] 전송이 시작되는 슬롯 사이의 간격을 결정합니다.
3. **[[SLIV]] 매핑**: 시작 심볼(S)과 심볼 길이(L)를 결정하는 [[SLIV]] 값을 통해 전송 심볼 구간을 정의합니다.
4. **매핑 타입**: 
   - Type A: 슬롯 내에서 [[DMRS]] 위치가 고정적이며, 주로 슬롯 시작 부분에 위치합니다.
   - Type B: [[DMRS]] 위치가 할당된 심볼 구간에 따라 유연하게 결정됩니다.
5. **반복 전송**: [[PUSCH]] 반복 전송은 다중 슬롯에 걸쳐 수행될 수 있으며, 이는 [[TB]] 전송의 신뢰성을 높이기 위해 사용됩니다.

## 인과 관계
- [[DCI]] (triggers) [[PUSCH]] 전송
- [[K2]] (affects) [[PUSCH]] 전송 슬롯 위치
- [[SLIV]] (affects) [[PUSCH]] 심볼 구간
- [[PUSCH]] (part_of) [[PUSCH_Transmission_Procedures]]

## 관련 개념
- [[PUSCH]] (part_of)
- [[DCI]] (triggers)
- [[K2]] (affects)
- [[SLIV]] (affects)
- [[PUSCH_Transmission_Procedures]] (part_of)

## 스펙 근거
- TS 38.214 §6.1.2.1: 시간 도메인 자원 할당의 일반적인 절차 및 테이블 결정 방식 정의
- TS 38.214 §6.1.2.1.1: [[PUSCH]] 자원 할당 테이블 결정 로직 상세

## 소스
- 3GPP TS 38.214 V19.0.0 (2024-03)
- UE Feature Priority (TS 38.822):
  - [필수(cap)] 4-19: SR/HARQ-ACK/CSI multiplexing once per slot using a PUCCH (or HARQ-ACK/CSI piggybacked on a PUSCH)
  - [필수(cap)] 5-17: PUSCH repetitions over multiple slots
  - [선택] 4-19a, 4-19b, 4-19c: SR/HARQ-ACK/CSI 다중화 관련 기능
  - [선택] 5-14, 5-16: Type 1/2 configured PUSCH repetitions over multiple slots
  - [선택] 10-35, 10-35a, 10-35b, 10-35c, 10-38: 비면허 대역(unlicensed spectrum) 관련 PUSCH 반복 및 다중화 기능