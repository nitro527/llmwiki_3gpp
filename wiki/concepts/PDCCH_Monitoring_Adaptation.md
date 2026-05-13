# PDCCH_Monitoring_Adaptation

## 정의
[[PDCCH]] 모니터링 적응은 [[UE]]가 전력 소모를 줄이기 위해 [[Search_Space_Set]] 그룹을 전환하거나, 특정 기간 동안 [[PDCCH]] 모니터링을 건너뛰는(skipping) 절차를 의미한다.

## 요약
[[PDCCH]] 모니터링 적응은 [[Search_Space_Set]] 그룹 스위칭과 [[PDCCH]] 모니터링 스킵핑으로 구성된다. [[UE]]는 [[DCI]]를 통해 모니터링 그룹을 변경하거나 특정 시간 동안 모니터링을 중단할 수 있으며, 타이머 기반의 자동 복귀 메커니즘과 특정 이벤트(SR, RACH 등) 발생 시의 예외 처리 절차를 포함한다.

## 상세 설명
[[PDCCH]] 모니터링 적응은 TS 38.213 §10.4에 정의된 절차를 따른다.

### Search Space Set Group Switching
- [[UE]]는 [[Search_Space_Set]] 그룹 인덱스를 할당받아 모니터링 그룹을 전환할 수 있다.
- [[DCI_Format_2_0]]을 통해 그룹 스위칭 플래그를 수신하거나, [[PDCCH]] 모니터링 적응 필드가 포함된 [[DCI]]를 통해 그룹을 변경한다.
- 그룹 전환은 [[Search_Space_Switch_Delay]]만큼의 심볼 이후 첫 번째 슬롯에서 적용된다.
- [[Search_Space_Switch_Timer]]가 설정된 경우, 타이머가 만료되면 [[UE]]는 자동으로 그룹 인덱스 0으로 복귀한다. 타이머는 슬롯마다 1씩 감소하며, [[C-RNTI]] 등이 포함된 [[DCI]] 수신 시 리셋된다.

### PDCCH Monitoring Skipping
- [[PDCCH_Skipping_Duration_List]]를 통해 제공된 기간 동안 [[UE]]는 [[PDCCH]] 모니터링을 건너뛸 수 있다.
- [[DCI]] 내의 1비트 또는 2비트 [[PDCCH]] 모니터링 적응 필드를 통해 스킵핑이 지시된다.
- 스킵핑 중에도 [[SR]]이 보류 중이거나 [[RACH]] 절차 중인 경우, 혹은 [[DRX]] 상태에 따라 모니터링을 재개해야 하는 예외 조건이 존재한다.
- [[PDCCH]] 모니터링 재개는 [[PUCCH]] 전송 완료 후 또는 [[NACK]] 기반의 재개 설정 시 특정 슬롯부터 수행된다.

## 인과 관계
- [[PDCCH]] depends_on [[PDCCH_Monitoring_Adaptation]] (모니터링 적응 설정에 따른 PDCCH 수신 여부 결정)
- [[DCI_Field_Mapping]] implements [[PDCCH_Monitoring_Adaptation]] (DCI 내 모니터링 적응 필드 정의)
- [[Bandwidth_Part_Operation]] affects [[PDCCH_Monitoring_Adaptation]] (BWP 변경 시 모니터링 상태 초기화)
- [[DRX_Operation]] affects [[PDCCH_Monitoring_Adaptation]] (DRX 상태에 따른 스킵핑 종료)

## 관련 개념
- [[PDCCH]] (affects)
- [[DCI]] (triggers)
- [[Search_Space_Set]] (affects)
- [[Bandwidth_Part_Operation]] (affects)
- [[DRX_Operation]] (affects)

## 스펙 근거
- TS 38.213 §10.4: Search space set group switching and skipping of PDCCH monitoring
- TS 38.213 §10.4A: PDCCH monitoring for early indication of paging
- TS 38.213 §10.4B: Indication of TRS resources

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18)