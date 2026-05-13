# PUCCH_Priority_Handling

## 정의
[[PUCCH_Priority_Handling]]은 서로 다른 우선순위(Priority 0 및 Priority 1)를 가진 [[UCI]]가 시간적으로 중첩될 때, 이를 단일 [[PUCCH]] 자원에 다중화하거나 우선순위에 따라 처리하는 물리 계층 절차를 의미한다.

## 요약
UE가 서로 다른 우선순위를 가진 [[HARQ-ACK]] 정보를 포함하는 [[PUCCH]]들을 동시에 전송해야 하는 상황에서, 상위 계층 설정(uci-MuxWithDiffPrio)에 따라 이를 하나의 PUCCH 자원으로 다중화하여 전송한다. 이때 자원 선택, 전송 전력 결정, 그리고 비트 매핑 규칙이 우선순위가 높은 정보를 보호하도록 설계되어 있다.

## 상세 설명
UE가 우선순위 0과 1을 가진 HARQ-ACK 정보를 포함하는 PUCCH들을 중첩하여 전송해야 할 때, TS 38.213 §9.2.5.3에 따라 다음 절차를 수행한다.

1. 자원 결정:
   - UE는 우선순위 1에 해당하는 PUCCH 설정으로부터 자원 집합을 결정한다.
   - DCI format에 의해 우선순위 1의 전송이 트리거된 경우, 해당 DCI가 지시하는 자원을 사용하거나, SPS PUCCH 자원 리스트에서 자원을 선택한다.

2. 다중화 및 인코딩:
   - 우선순위 0과 1의 HARQ-ACK 비트들을 동일한 PUCCH 자원에 다중화한다.
   - [[PUCCH_Format_Processing]]에서 Format 2, 3, 4를 사용하는 경우, 코드 레이트(maxCodeRateLP)를 고려하여 필요한 PRB 수를 결정한다. 이때 CRC 비트를 포함한 전체 비트 수와 목표 코드 레이트를 만족하는 최소 PRB 수를 산출한다.

3. 전력 제어:
   - PUCCH Format 2, 3, 4 사용 시, 전송 전력은 우선순위 1의 UCI만을 포함한다고 가정하고 계산하되, 다중화된 비트 수에 따라 파라미터를 조정한다.
   - Format 1 사용 시, 모든 HARQ-ACK 비트가 우선순위 1을 가진 것으로 간주하여 전력을 결정한다.

4. 비트 매핑:
   - Format 0 사용 시, 우선순위 1과 0의 비트를 각각 Table 9.2.3-4의 첫 번째와 두 번째 비트로 배치한다.
   - Format 1 사용 시, QPSK 심볼의 첫 번째와 두 번째 비트로 각각 우선순위 1과 0의 정보를 매핑한다.

5. 인터레이스 전송:
   - InterlaceAllocation이 제공된 경우, 설정된 PRB 수에 따라 첫 번째 또는 두 번째 인터레이스를 선택하거나 두 인터레이스를 모두 사용하여 전송한다.

## 인과 관계
- [[PUCCH_Priority_Handling]] depends_on [[UCI_Multiplexing]] (다중화 로직 활용)
- [[PUCCH_Priority_Handling]] affects [[PUCCH_Power_Control]] (우선순위 기반 전력 계산식 변경)
- [[PUCCH_Priority_Handling]] depends_on [[PUCCH_Format_Processing]] (다중화된 UCI의 포맷별 인코딩 및 자원 매핑)

## 관련 개념
- [[UCI]] (depends_on)
- [[PUCCH]] (part_of)
- [[HARQ_ACK_Reporting]] (affects)
- [[PUCCH_Power_Control]] (affects)
- [[PUCCH_Format_Processing]] (depends_on)

## 스펙 근거
- TS 38.213 §9.2.5.3: UE procedure for reporting UCI of different priorities
- TS 38.213 §9.2.1: PUCCH resource set determination
- TS 38.213 §7.2.1: PUCCH power control

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18)