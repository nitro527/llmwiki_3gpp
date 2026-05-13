# PDSCH_SPS_Procedure

## 정의
[[PDSCH]] SPS(Semi-Persistent Scheduling) 절차는 상위 계층 파라미터에 의해 설정된 자원 구성을 바탕으로, [[PDCCH]]를 통한 동적 스케줄링 없이 주기적인 [[PDSCH]] 전송을 수신하는 메커니즘을 의미한다.

## 요약
SPS 기반 [[PDSCH]] 수신은 상위 계층에서 제공하는 설정 정보를 사용하여 수행된다. 동일한 슬롯 내에서 다수의 SPS [[PDSCH]]가 충돌하거나, [[Cell_DTX_DRX_Adaptation]]에 의해 비활성 기간으로 판단되는 경우, 특정 우선순위 규칙에 따라 수신할 [[PDSCH]]를 선택한다.

## 상세 설명
SPS [[PDSCH]] 수신은 상위 계층 파라미터 `sps-Config`를 통해 설정된다. UE는 [[CS-RNTI]] 또는 [[G-CS-RNTI]]로 스크램블된 [[PDCCH]]를 통해 SPS를 활성화하거나, 설정된 구성에 따라 PDCCH 없이 주기적인 수신을 수행한다.

동일 슬롯 내에서 PDCCH 없이 수신해야 하는 다수의 SPS [[PDSCH]]가 존재할 경우, 다음 절차에 따라 수신할 [[PDSCH]]를 결정한다:
1. 슬롯 내에서 [[Slot_Format_Configuration]]에 의해 UL 심볼로 지정된 영역이나, [[Cell_DTX_DRX_Adaptation]]의 비활성 기간과 겹치는 경우 해당 [[PDSCH]]는 제외된다.
2. 남은 SPS [[PDSCH]] 집합 Q에 대해, 가장 낮은 `sps-ConfigIndex`를 가진 [[PDSCH]]를 선택(Survivor PDSCH)한다.
3. 선택된 [[PDSCH]]와 시간적으로 겹치는 모든 다른 [[PDSCH]]를 집합 Q에서 제거한다.
4. 집합 Q가 비어있거나, UE가 지원하는 슬롯당 최대 유니캐스트/멀티캐스트 [[PDSCH]] 수에 도달할 때까지 위 과정을 반복한다.

또한, [[Cell_DTX_DRX_Adaptation]]이 활성화된 경우, 비활성 기간과 겹치는 SPS [[PDSCH]]는 디코딩하지 않는다.

## 인과 관계
- [[PDSCH]] (depends_on) [[PDSCH_SPS_Procedure]] (SPS 수신은 PDSCH 수신 절차의 일환)
- [[PDSCH_SPS_Procedure]] (depends_on) [[Cell_DTX_DRX_Adaptation]] (비활성 기간에 따른 수신 제한)
- [[PDSCH_SPS_Procedure]] (depends_on) [[Slot_Format_Configuration]] (UL 심볼과의 충돌 시 수신 제외)

## 관련 개념
- [[PDSCH]] (part_of)
- [[CS-RNTI]] (affects)
- [[G-CS-RNTI]] (affects)
- [[Cell_DTX_DRX_Adaptation]] (affects)
- [[Slot_Format_Configuration]] (affects)

## 스펙 근거
- TS 38.214 §5.1: SPS [[PDSCH]] 수신 및 HARQ 프로세스 관리 관련 일반 절차 정의
- TS 38.214 §5.1: 슬롯 내 다수 SPS [[PDSCH]] 수신 시 우선순위 선택 알고리즘(Step 0~3) 명시
- TS 38.214 §5.1: [[Cell_DTX_DRX_Adaptation]] 활성화 시 SPS [[PDSCH]] 수신 제한 조건 명시

## 소스
- 3GPP TS 38.214 v17.9.0 (Release 17)