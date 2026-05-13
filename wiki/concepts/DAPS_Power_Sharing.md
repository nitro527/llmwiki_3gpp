# DAPS_Power_Sharing

## 정의
DAPS_Power_Sharing은 [[DAPS_Handover_Operation]] 수행 중 소스 셀 그룹(Source MCG)과 타겟 셀 그룹(Target MCG) 간의 상향링크 전송 전력을 효율적으로 분배하고 제어하는 절차를 의미한다.

## 요약
DAPS 핸드오버 환경에서 UE는 소스 셀과 타겟 셀에 동시에 연결되어 상향링크 전송을 수행할 수 있다. 이때 UE는 각 셀 그룹에 대해 독립적인 전력 제어를 수행하거나, 설정된 모드에 따라 반정적 또는 동적 방식으로 전력을 공유하여 전체 전송 전력이 UE의 최대 전송 전력을 초과하지 않도록 관리한다.

## 상세 설명
DAPS 핸드오버 시 UE는 소스 MCG와 타겟 MCG를 동시에 구성받을 수 있다. TS 38.213 §15에 따른 주요 동작은 다음과 같다.

1. 기본 전력 제어: UE는 각 셀 그룹에 대해 [[PUSCH_Power_Control]], [[PUCCH_Power_Control]], [[SRS_Power_Control]] 등을 독립적으로 수행한다.
2. 전력 공유 모드: 동일한 주파수 대역(FR1)에서 소스 및 타겟 MCG가 구성된 경우, 상위 계층 파라미터인 uplinkPowerSharingDAPS-Mode를 통해 전력 공유 방식을 결정한다.
   - Semi-static-mode1: [[Dual_Connectivity_Power_Sharing]]의 모드 1과 유사하게 타겟 MCG를 MCG, 소스 MCG를 SCG로 간주하여 전력을 결정한다.
   - Semi-static-mode2: 동기화된 DAPS 핸드오버 환경에서만 사용 가능하며, 모드 2 방식의 전력 공유를 수행한다.
   - Dynamic: 동적 전력 공유 모드를 사용하여 실시간으로 전력을 분배한다.
3. 전송 취소(Cancellation): 전력 공유 모드가 설정되지 않았거나 관련 기능이 없는 경우, 소스 셀과 타겟 셀의 전송 자원이 시간적으로 겹치면 UE는 타겟 셀로만 전송하고 소스 셀의 전송을 취소한다.
4. 전송 취소 예외: 특정 조건(PDCCH 수신 후 PUSCH 준비 시간 등)을 만족하는 경우, UE는 소스 셀의 전송을 취소하지 않을 수 있다.
5. 자원 충돌 방지: 동일 주파수 대역 내에서 [[PRACH]] 전송과 다른 상향링크 채널(PUSCH/PUCCH/SRS)이 겹치는 경우, 특정 심볼 간격(delta)을 유지하여 충돌을 방지한다.

## 인과 관계
- [[DAPS_Handover_Operation]] depends_on [[DAPS_Power_Sharing]] (핸드오버 중 상향링크 전력 제어 전제)
- [[DAPS_Power_Sharing]] affects [[PUSCH_Power_Control]] (전력 공유 모드에 따른 전송 전력 제한)
- [[DAPS_Power_Sharing]] affects [[PUCCH_Power_Control]] (전력 공유 모드에 따른 전송 전력 제한)
- [[DAPS_Power_Sharing]] affects [[SRS_Power_Control]] (전력 공유 모드에 따른 전송 전력 제한)
- [[DAPS_Power_Sharing]] triggers [[Transmission_Power_Prioritization]] (전력 부족 시 우선순위에 따른 전송 결정)

## 관련 개념
- [[Dual_Connectivity_Power_Sharing]] (similar_to)
- [[DAPS_Handover_Operation]] (part_of)
- [[PUSCH_Power_Control]] (implements)
- [[PUCCH_Power_Control]] (implements)
- [[SRS_Power_Control]] (implements)
- [[PRACH]] (affects)

## 스펙 근거
- TS 38.213 §15: DAPS 핸드오버 기반의 상향링크 전력 제어 및 전력 공유 절차 정의
- TS 38.213 §7.6.2: NR-DC 환경에서의 전력 공유 모드 상세 동작
- TS 38.133 §6.1.3.2: Intra-frequency DAPS 핸드오버 동작 및 타이밍 요구사항

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"