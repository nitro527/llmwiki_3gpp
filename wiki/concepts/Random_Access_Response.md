# Random_Access_Response

## 정의
[[Random_Access_Response]] (RAR)는 [[UE]]가 [[PRACH]]를 전송한 후, 네트워크로부터 수신하는 응답 메시지입니다. 이는 [[Type-1_Random_Access_Procedure]] 또는 [[Type-2_Random_Access_Procedure]] 과정에서 상향링크 자원 할당, 타이밍 조정, 혹은 성공 여부를 확인하기 위해 사용됩니다.

## 요약
[[UE]]는 [[PRACH]] 전송 후 특정 윈도우 내에서 [[RA-RNTI]] 또는 [[MsgB-RNTI]]로 스크램블된 [[DCI_Format_1_0]]을 검출합니다. 검출 성공 시 [[PDSCH]]를 통해 전달되는 전송 블록을 수신하며, 상위 계층은 이를 해석하여 상향링크 그랜트(RAR UL Grant)를 획득하거나 [[PUCCH]]를 통한 [[HARQ-ACK]] 전송을 수행합니다.

## 상세 설명
### Type-1 랜덤 액세스 응답
[[UE]]는 [[PRACH]] 전송 후 상위 계층에 의해 제어되는 윈도우 동안 [[RA-RNTI]]로 스크램블된 [[DCI_Format_1_0]]을 모니터링합니다. 윈도우는 [[PRACH]] 전송의 마지막 심볼 이후 최소 1심볼 뒤의 첫 번째 [[CORESET]]에서 시작하며, [[ra-ResponseWindow]]에 의해 길이가 결정됩니다. [[DCI_Format_1_0]] 검출 및 [[PDSCH]] 수신 성공 시, 상위 계층은 [[RAPID]]를 확인하여 일치할 경우 [[PUSCH]] 전송을 위한 RAR UL Grant를 물리 계층에 전달합니다. RAR UL Grant에는 주파수 호핑 플래그, [[MCS]], [[TPC_Command]], 채널 액세스 정보 등이 포함됩니다.

### Type-2 랜덤 액세스 응답
[[Type-2_Random_Access_Procedure]]에서는 [[MsgB-RNTI]]로 스크램블된 [[DCI_Format_1_0]]을 사용합니다. [[MsgB]]는 두 가지 유형으로 나뉩니다.
- FallbackRAR: [[Type-1_Random_Access_Procedure]]와 유사하게 RAR UL Grant를 제공하여 [[PUSCH]] 전송을 유도합니다.
- SuccessRAR: [[PUCCH]] 자원 지시자 및 [[HARQ_ACK_Reporting]] 타이밍을 포함하여 [[HARQ-ACK]] 피드백을 직접 수행합니다. [[PUCCH]] 자원은 [[pucch-ResourceCommon]]에서 제공되며, 슬롯 타이밍은 [[HARQ_Feedback_Timing_Indicator]] 필드에 의해 결정됩니다.

### 공통 절차 및 특수 케이스
- SFN 검증: [[DCI_Format_1_0]] 내의 SFN 필드 LSB가 [[PRACH]] 전송 시점의 SFN과 일치해야 합니다.
- QCL 가정: [[UE]]는 [[PDCCH]] 수신 시 [[SS_PBCH_Block_Generation]] 또는 [[CSI_RS_Generation]]과 동일한 QCL 속성을 가정할 수 있습니다.
- 실패 시 동작: 윈도우 내 응답 검출 실패 시, 상위 계층은 [[PRACH]] 재전송을 지시할 수 있으며, 이때 [[UE]]는 PDSCH 처리 시간 등을 고려하여 최소 대기 시간을 준수해야 합니다.

## 인과 관계
- [[Random_Access_Response]] depends_on [[PRACH]] (랜덤 액세스 절차의 응답으로 발생)
- [[Random_Access_Response]] triggers [[PUSCH]] (RAR UL Grant를 통한 상향링크 전송 트리거)
- [[Random_Access_Response]] triggers [[PUCCH]] (SuccessRAR 수신 시 HARQ-ACK 전송 트리거)
- [[Random_Access_Response]] depends_on [[DCI_Format_1_0]] (RAR 수신을 위한 제어 정보 검출)
- [[Random_Access_Response]] depends_on [[PDSCH]] (RAR 메시지 전달을 위한 데이터 채널)

## 관련 개념
- [[RA-RNTI]] (depends_on)
- [[MsgB-RNTI]] (depends_on)
- [[PRACH]] (depends_on)
- [[PUSCH]] (affects)
- [[PUCCH]] (affects)
- [[DCI_Format_1_0]] (depends_on)
- [[PDSCH]] (depends_on)
- [[HARQ_ACK_Reporting]] (affects)

## 스펙 근거
- TS 38.213 §8.2: Type-1 랜덤 액세스 응답 절차 및 RAR UL Grant 필드 정의
- TS 38.213 §8.2A: Type-2 랜덤 액세스 응답 절차 및 SuccessRAR/FallbackRAR 정의
- TS 38.214 §6.1.2.1.1: PUSCH 전송 타이밍 및 관련 파라미터
- TS 38.321: 랜덤 액세스 윈도우 및 상위 계층 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"