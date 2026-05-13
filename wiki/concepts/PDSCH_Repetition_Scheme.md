# PDSCH_Repetition_Scheme

## 정의
[[PDSCH]] 반복 전송 스킴은 동일한 전송 블록(TB)을 여러 번 전송하여 수신 신뢰도를 높이거나 커버리지를 확장하기 위한 물리 계층 전송 기법으로, 시간 영역(TDM) 또는 주파수 영역(FDM)을 활용하여 구성된다.

## 요약
[[PDSCH]] 반복 전송은 상위 계층 파라미터인 repetitionScheme을 통해 'tdmSchemeA', 'fdmSchemeA', 'fdmSchemeB'로 설정되거나, PDSCH-TimeDomainResourceAllocation 내의 repetitionNumber를 통해 슬롯 간 반복 전송으로 구현된다. 각 스킴은 전송 자원 할당 방식과 [[TCI_State_Management]] 연동 방식에 따라 구분되며, HARQ 프로세스 ID 관리 및 [[DMRS]] 포트 할당 규칙을 따른다.

## 상세 설명
TS 38.214 §5.1에 정의된 PDSCH 반복 전송의 주요 동작은 다음과 같다.

1. **tdmSchemeA**: 하나의 슬롯 내에서 두 개의 PDSCH 전송 기회(occasion)를 가진다. 각 전송 기회는 시간 영역에서 비중첩 자원을 할당받으며, 두 기회 모두 해당 슬롯 내에서 수신되어야 한다.
2. **fdmSchemeA**: 하나의 TB에 대해 단일 PDSCH 전송 기회를 가지며, 각 [[TCI_State_Management]]는 주파수 영역에서 비중첩 자원 할당과 연동된다.
3. **fdmSchemeB**: 동일한 TB에 대해 두 개의 PDSCH 전송 기회를 가지며, 각 전송 기회는 서로 다른 TCI state와 연동되고 주파수 영역에서 비중첩 자원을 할당받는다.
4. **repetitionNumber 기반 슬롯 간 반복**: PDSCH-TimeDomainResourceAllocation에 repetitionNumber가 설정된 경우, 여러 연속적인 슬롯에 걸쳐 동일한 TB를 반복 전송한다. DCI를 통해 1개 또는 2개의 TCI state가 지시될 수 있으며, 이에 따라 반복 전송 시 TCI state 적용 방식이 결정된다.
5. **HARQ 프로세스 관리**: 반복 전송 시 각 PDSCH 기회가 UL 심볼과 중첩되면 해당 기회는 수신되지 않으며, HARQ 프로세스 ID는 증가하지 않는다. 또한, HARQ 피드백이 비활성화되지 않은 경우, 해당 HARQ 프로세스에 대한 HARQ-ACK 전송이 완료될 때까지 동일한 프로세스에 대한 추가 PDSCH 수신을 기대하지 않는다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_Repetition_Scheme]] (반복 전송 설정 시 전송 기회 결정)
- [[PDSCH_Repetition_Scheme]] affects [[DMRS]] (반복 전송 시 CDM 그룹 및 포트 할당 규칙 적용)
- [[PDSCH_Repetition_Scheme]] affects [[TCI_State_Management]] (반복 전송 기회별 TCI state 매핑)
- [[PDSCH_Repetition_Scheme]] depends_on [[PDCCH]] (DCI를 통한 반복 스킴 및 자원 할당 정보 수신)

## 관련 개념
- [[PDSCH]] (implements)
- [[DMRS]] (affects)
- [[TCI_State_Management]] (affects)
- [[PDCCH]] (depends_on)
- [[HARQ]] (affects)

## 스펙 근거
- TS 38.214 §5.1: PDSCH 수신 절차 및 반복 전송 스킴(tdmSchemeA, fdmSchemeA, fdmSchemeB) 정의
- TS 38.214 §5.1.2.1: 시간 영역 자원 할당 및 슬롯 간 반복 전송 규칙
- TS 38.214 §5.1.2.3: 주파수 영역 자원 할당 및 FDM 기반 반복 전송 규칙

## 소스
- 3GPP TS 38.214 V17.9.0 (Release 17) Physical layer procedures for data