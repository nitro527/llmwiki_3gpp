# Bandwidth_Part_Operation

## 정의
[[Bandwidth_Part_Operation]]은 5G NR 시스템에서 UE가 서빙 셀의 전체 대역폭 내에서 특정 주파수 범위와 수치적 해석(Numerology)을 갖는 부분 대역폭을 설정하고, 이를 동적으로 전환하거나 관리하는 절차를 의미합니다.

## 요약
UE는 상위 계층 시그널링을 통해 최대 4개의 DL BWP와 4개의 UL BWP를 설정받을 수 있습니다. 활성 BWP는 [[DCI]]를 통해 동적으로 전환되거나, [[BWP_Inactivity_Timer]] 만료에 의해 기본 BWP로 복귀합니다. BWP 전환 시 UE는 새로운 BWP의 [[SCS]] 및 [[Cyclic_Prefix]]에 맞춰 [[PDCCH]], [[PDSCH]], [[PUCCH]], [[PUSCH]]를 송수신합니다.

## 상세 설명
TS 38.213 §12에 정의된 BWP 동작의 핵심 내용은 다음과 같습니다.

### BWP 설정
- UE는 서빙 셀당 최대 4개의 DL BWP와 4개의 UL BWP를 설정받습니다.
- 각 BWP는 [[Subcarrier_Spacing]], [[Cyclic_Prefix]], 주파수 위치(offset) 및 대역폭(length) 정보를 포함합니다.
- 초기 BWP(Initial BWP)는 SIB1을 통해 제공되거나, 특정 CORESET의 주파수 범위에 기반하여 결정됩니다.
- 전용 BWP 설정이 있는 경우, `firstActiveDownlinkBWP-Id` 및 `firstActiveUplinkBWP-Id`를 통해 초기 활성 BWP가 지정됩니다.

### BWP 전환 절차
- [[DCI]] 내의 BWP indicator 필드를 통해 활성 BWP를 전환합니다.
- BWP 전환이 지시되면 UE는 해당 BWP의 파라미터에 맞춰 DCI 해석을 수행합니다. 만약 DCI 필드 크기가 새로운 BWP의 해석과 다를 경우, 0을 채우거나(padding) LSB를 취하는(truncation) 방식으로 조정합니다.
- 서로 다른 [[SCS]]를 가진 BWP로 전환 시, 주파수 도메인 자원 할당(Type 2)은 MSB/LSB의 truncation 또는 zero-padding을 통해 재구성됩니다.
- BWP 전환 시 UE는 전환에 필요한 지연 시간 동안 송수신이 제한될 수 있으며, 이는 TS 38.133의 요구사항을 따릅니다.

### BWP 비활성 타이머
- `bwp-InactivityTimer`가 설정된 경우, UE는 타이머가 동작하는 동안 특정 조건이 충족되지 않으면 타이머를 감소시킵니다.
- 타이머가 만료되면 UE는 자동으로 설정된 기본 BWP(Default BWP)로 전환합니다. 기본 BWP가 설정되지 않은 경우 초기 BWP가 기본값으로 사용됩니다.

## 인과 관계
- [[Bandwidth_Part_Operation]] depends_on [[DCI_Field_Mapping]] (BWP 전환 지시를 위한 DCI 필드 해석)
- [[Bandwidth_Part_Operation]] triggers [[PDCCH_Monitoring_Adaptation]] (BWP 전환에 따른 PDCCH 모니터링 파라미터 변경)
- [[Bandwidth_Part_Operation]] affects [[PDSCH_Reception_Procedure]] (활성 DL BWP 내에서의 PDSCH 수신)
- [[Bandwidth_Part_Operation]] affects [[PUSCH_Transmission_Procedure]] (활성 UL BWP 내에서의 PUSCH 전송)
- [[Bandwidth_Part_Operation]] depends_on [[CORESET_Configuration]] (BWP 내 CORESET 설정 기반 PDCCH 모니터링)

## 관련 개념
- [[DCI]] (affects)
- [[Subcarrier_Spacing]] (part_of)
- [[PDCCH]] (depends_on)
- [[PDSCH]] (depends_on)
- [[PUSCH]] (depends_on)
- [[PUCCH]] (depends_on)
- [[CORESET_Configuration]] (depends_on)

## 스펙 근거
- TS 38.213 §12: Bandwidth part operation 전반에 대한 정의 및 절차
- TS 38.211 §6.3.1: BWP 관련 물리적 파라미터 및 자원 매핑
- TS 38.331: BWP 관련 상위 계층 파라미터 설정
- TS 38.133: BWP 전환 지연 시간 및 타이머 관련 요구사항

## 소스
- 3GPP TS 38.213 v18.0.0 (2024-03) §12