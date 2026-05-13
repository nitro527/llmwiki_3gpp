# Timing_Advance_Adjustment

## 정의
[[Timing_Advance_Adjustment]]는 [[UE]]가 상향링크 전송 시 기지국([[gNB]])에서의 수신 타이밍을 정렬하기 위해 전송 시점을 앞당기거나 지연시키는 물리 계층 절차를 의미한다.

## 요약
[[UE]]는 [[gNB]]로부터 수신한 [[Timing_Advance_Command]]를 해석하여 상향링크 전송 타이밍을 조정한다. 이는 [[TAG]] 단위로 관리되며, [[BWP]] 변경, 위성 통신(NTN) 또는 ATG 환경에서의 전파 지연 사전 보상 등을 포함한다. 전송 타이밍 조정은 [[PUSCH]], [[PUCCH]], [[SRS]] 전송에 적용된다.

## 상세 설명
[[UE]]는 상향링크 전송 타이밍을 유지하기 위해 다음과 같은 메커니즘을 수행한다.

1. **Timing Advance Offset**: [[UE]]는 서빙 셀에 대해 [[n-TimingAdvanceOffset]] 값을 제공받는다. 만약 [[CORESET]]에 대한 [[coresetPoolIndex]]가 설정된 경우, 각 [[TCI_State]]와 연관된 공간 필터에 따라 서로 다른 두 개의 오프셋 값을 사용할 수 있다. 제공받지 못한 경우 [[TS_38_133]]에 따른 기본값을 사용한다.
2. **Timing Advance Command 해석**:
   - [[Random_Access_Response]] 또는 절대적 [[Timing_Advance_Command]] [[MAC_CE]] 수신 시, 인덱스 값 $T_A$ (0~3846)를 통해 시간 정렬량을 결정한다. SCS가 $\mu$ kHz일 때 시간 정렬량은 $T_A \times 16 \times 64 \times 2^{-\mu} \times T_c$이다.
   - 일반적인 경우, 인덱스 값 $T_A$ (0~63)를 통해 현재 타이밍 값을 조정하며, SCS가 $\mu$ kHz일 때 조정량은 $(T_A - 31) \times 16 \times 64 \times 2^{-\mu} \times T_c$이다.
3. **적용 시점**: [[Timing_Advance_Command]] 수신 후, 특정 처리 시간(PDSCH 처리 시간 및 PUSCH 준비 시간 고려) 이후의 상향링크 슬롯부터 조정된 타이밍이 적용된다.
4. **BWP 변경**: [[UE]]가 활성 [[BWP]]를 변경하는 경우, 새로운 [[BWP]]의 SCS를 기준으로 타이밍 값을 결정한다. 조정 적용 후에는 절대적인 타이밍 값을 유지한다.
5. **위성 및 ATG 환경**: 위성 또는 ATG 환경에서 [[UE]]는 상위 계층에서 제공하는 궤도 정보(ephemeris) 또는 위치 정보를 사용하여 왕복 전파 지연을 사전 보상한다. 이는 [[ta-Common]], [[ta-CommonDrift]] 등의 파라미터를 사용하여 계산된 일방향 전파 지연을 기반으로 수행된다.

## 인과 관계
- [[Timing_Advance_Adjustment]] depends_on [[Timing_Advance_Command]] (TA 커맨드 수신을 통한 타이밍 갱신)
- [[Timing_Advance_Adjustment]] affects [[PUSCH]] (상향링크 전송 시점 제어)
- [[Timing_Advance_Adjustment]] affects [[PUCCH]] (상향링크 전송 시점 제어)
- [[Timing_Advance_Adjustment]] affects [[SRS]] (상향링크 전송 시점 제어)
- [[Timing_Advance_Adjustment]] depends_on [[Bandwidth_Part_Operation]] (BWP 변경 시 SCS 기반 타이밍 재계산)

## 관련 개념
- [[TAG]] (part_of)
- [[MAC_CE]] (implements)
- [[TS_38_211]] (implements)
- [[TS_38_213]] (implements)
- [[TS_38_321]] (implements)

## 스펙 근거
- TS 38.213 §4.2: 상향링크 전송 타이밍 조정 절차 및 파라미터 정의
- TS 38.211 §4.3.1: 타이밍 어드밴스 관련 시간 단위 및 기본 수식
- TS 38.321 §5.2: MAC 계층에서의 Timing Advance Command 처리

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)
- 3GPP TS 38.211 V18.0.0 (2024-03)
- 3GPP TS 38.321 V18.0.0 (2024-03)