# Pathloss_Estimation

## 정의
[[Pathloss_Estimation]]은 [[UE]]가 상향링크 전송 전력을 결정하기 위해 하향링크 참조 신호([[RS]])를 기반으로 무선 채널의 경로 손실을 계산하는 절차를 의미한다.

## 요약
[[UE]]는 [[PUSCH]], [[PUCCH]], [[SRS]] 전송을 위해 서빙 셀당 최대 4개의 경로 손실 추정치를 유지한다. 경로 손실 추정을 위한 [[RS]] 자원은 상위 계층 시그널링 또는 [[MAC_CE]]를 통해 업데이트되며, [[TCI_State]]와 연동되어 동적으로 관리될 수 있다.

## 상세 설명
[[UE]]는 상향링크 전송 전력 제어를 위해 경로 손실을 추정하며, TS 38.213 §7에 따라 다음의 규칙을 따른다.

1. 경로 손실 추정치 관리:
   - [[UE]]는 서빙 셀당 최대 4개의 경로 손실 추정치를 유지해야 한다. 단, [[SRS]]-PosResourceSet으로 설정된 [[SRS]]는 예외이다.
   - 설정된 [[RS]] 자원이 4개를 초과하는 경우, 스펙에서 정의된 우선순위 인덱스에 따라 자원을 유지한다.

2. [[MAC_CE]] 기반 업데이트:
   - [[MAC_CE]]를 통해 경로 손실 참조 [[RS]]가 업데이트되는 경우, [[UE]]는 해당 명령을 포함한 [[PDSCH]]에 대한 [[HARQ_ACK]]를 전송하는 슬롯 이후의 첫 번째 슬롯부터 새로운 경로 손실 추정치를 적용한다.
   - 적용 시점은 [[PDCCH]] 또는 [[PUSCH]]의 부반송파 간격([[SCS]]) 설정과 [[K_offset]] 값에 의해 결정된다.

3. [[TCI_State]] 연동:
   - [[TCI_State]] 또는 [[TCI_UL_State]]가 지시된 경우, 경로 손실 참조 [[RS]] 인덱스는 해당 상태와 연관된 pathlossReferenceRS-Id-r17 또는 pathlossReferenceRS-Id를 통해 제공된다.
   - [[PUSCH]], [[PUCCH]], [[SRS]] 각각에 대해 설정된 p0AlphaSet은 지시된 [[TCI_State]]와 연관된 값을 사용한다.
   - [[SRS]]의 경우, followUnifiedTCI-StateSRS 설정 여부에 따라 [[SRS]] 자원 세트 내의 가장 낮은 [[SRS_ResourceId]]를 가진 자원의 [[TCI_State]]를 참조할 수 있다.

## 인과 관계
- [[PUSCH_Power_Control]] depends_on [[Pathloss_Estimation]] (전송 전력 계산을 위한 필수 입력값)
- [[PUCCH_Power_Control]] depends_on [[Pathloss_Estimation]] (전송 전력 계산을 위한 필수 입력값)
- [[SRS_Power_Control]] depends_on [[Pathloss_Estimation]] (전송 전력 계산을 위한 필수 입력값)
- [[Pathloss_Estimation]] depends_on [[MAC_CE]] (경로 손실 참조 RS 업데이트 트리거)
- [[Pathloss_Estimation]] depends_on [[TCI_State]] (경로 손실 참조 RS 인덱스 획득)

## 관련 개념
- [[PUSCH_Power_Control]] (depends_on)
- [[PUCCH_Power_Control]] (depends_on)
- [[SRS_Power_Control]] (depends_on)
- [[MAC_CE]] (affects)
- [[TCI_State]] (affects)
- [[RS]] (part_of)

## 스펙 근거
- TS 38.213 §7: Uplink Power control 및 경로 손실 추정 절차 정의
- TS 38.213 §7.1.1: [[PUSCH]] 경로 손실 추정 및 [[TCI_State]] 연동
- TS 38.213 §7.2.1: [[PUCCH]] 경로 손실 추정 및 [[TCI_State]] 연동
- TS 38.213 §7.3.1: [[SRS]] 경로 손실 추정 및 [[TCI_State]] 연동

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"