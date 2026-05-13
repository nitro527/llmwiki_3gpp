# PDCCH_Validation

## 정의
[[PDCCH]] 검증은 [[UE]]가 수신한 [[DCI]] 포맷이 [[DL_SPS]], [[UL_Grant_Type_2]], [[SL_Configured_Grant_Type_2]]의 활성화(Activation) 또는 해제(Release)를 지시하는 유효한 제어 정보인지 확인하는 절차를 의미한다. 또한, [[SCell]]의 휴면(Dormancy) 상태를 제어하기 위한 지시 정보를 식별하는 과정도 포함한다.

## 요약
[[UE]]는 수신된 [[DCI]]의 [[CRC]]가 특정 [[RNTI]]로 스크램블링되었는지 확인하고, [[DCI_Field_Mapping]]에 정의된 특정 필드 값들이 스펙에서 요구하는 조건(예: NDI='0', 특정 필드 값 등)을 만족하는지 검사한다. 검증이 성공하면 해당 정보를 유효한 제어 명령으로 처리하며, 실패 시 정보를 폐기한다.

## 상세 설명
### DL SPS 및 UL Grant Type 2 검증
[[UE]]는 다음 조건들을 만족할 때 [[DL_SPS]] 할당 또는 [[UL_Grant_Type_2]]를 위한 [[PDCCH]]를 검증한다:
- [[CRC]]가 [[CS_RNTI]] 또는 [[G_CS_RNTI]]로 스크램블링됨
- 활성화된 전송 블록에 대한 [[NDI]] 필드가 '0'으로 설정됨
- [[DFI]] 플래그 필드가 존재하는 경우 '0'으로 설정됨
- [[Time_Domain_Resource_Assignment]] 필드가 단일 [[SLIV]]를 지시함
- [[PDSCH_to_HARQ_feedback_timing_indicator]] 필드가 유효한 값을 제공함

단일 설정인 경우 TS 38.213 Table 10.2-1 또는 10.2-2에 따라 필드 값을 검사하며, 다중 설정인 경우 [[HARQ_Process_Number]] 필드를 통해 특정 설정을 식별하고 Table 10.2-3 또는 10.2-4를 기준으로 검증한다.

### SL Configured Grant Type 2 검증
[[SL_Configured_Grant_Type_2]]의 경우 [[DCI_Format_3_0]]을 사용하며 다음을 검증한다:
- [[CRC]]가 [[SL_CS_RNTI]]로 스크램블링됨
- [[NDI]] 필드가 '0'으로 설정됨
- Table 10.2A-1 또는 10.2A-2의 필드 설정 준수

[[SL_PRS]] 활성화/해제의 경우 [[DCI_Format_3_2]]를 사용하며, [[SL_PRS_CS_RNTI]]로 스크램블링된 [[CRC]]와 활성화/해제 지시 필드('1'은 활성화, '0'은 해제)를 확인한다.

### SCell Dormancy 지시
[[SCell]] 휴면 지시는 [[DCI_Format_2_6]] 또는 [[DCI_Format_0_1]], [[DCI_Format_0_3]], [[DCI_Format_1_1]], [[DCI_Format_1_3]]을 통해 수행된다.
- [[DCI_Format_2_6]]: [[PS_RNTI]]를 사용하며, Wake-up 지시 비트와 [[SCell]] 그룹 휴면 비트맵을 포함한다.
- [[DCI_Format_0_1/0_3/1_1/1_3]]: 특정 조건(예: [[C_RNTI]] 또는 [[MCS_C_RNTI]] 스크램블링, 특정 필드 값 조합) 만족 시 [[SCell]] 휴면을 지시하는 비트맵으로 해석된다.

## 인과 관계
- [[PDCCH]] depends_on [[CRC_Calculation]] (검증을 위한 CRC 확인 전제)
- [[PDCCH_Validation]] triggers [[SCell_Dormancy_Management]] (휴면 지시 검증 성공 시 상태 전이)
- [[PDCCH_Validation]] implements [[DCI_Field_Mapping]] (필드 값 검증 규칙 적용)
- [[PDCCH_Validation]] depends_on [[Bandwidth_Part_Operation]] (BWP 내 설정된 RNTI 및 구성 정보 사용)

## 관련 개념
- [[DCI_Field_Mapping]] (implements)
- [[SCell_Dormancy_Management]] (triggers)
- [[Bandwidth_Part_Operation]] (depends_on)
- [[CRC_Calculation]] (depends_on)

## 스펙 근거
- TS 38.213 §10.2: DL SPS 및 UL Grant Type 2 PDCCH 검증 절차
- TS 38.213 §10.2A: SL Configured Grant Type 2 PDCCH 검증 절차
- TS 38.213 §10.3: SCell 휴면 지시 및 DCI 포맷 2_6 동작

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)