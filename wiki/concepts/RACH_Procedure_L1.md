# RACH_Procedure_L1

## 정의
[[RACH_Procedure_L1]]은 [[UE]]가 [[gNB]]와 상향링크 동기를 맞추고 초기 접속 또는 재접속을 수행하기 위해 물리 계층에서 수행하는 절차를 의미하며, 크게 4-step 절차인 Type-1과 2-step 절차인 Type-2로 구분됩니다.

## 요약
[[RACH_Procedure_L1]]은 [[PRACH]] 프리앰블 전송을 시작으로 [[RAR]] 수신 또는 MsgB 수신을 통해 상향링크 자원을 할당받고, 최종적으로 [[PUSCH]]를 통한 메시지 전송 및 [[PDSCH]]를 통한 경합 해결(Contention Resolution) 과정을 포함합니다. 본 절차는 [[Uplink_Power_Control]]의 일환인 [[PRACH_Power_Control]]을 기반으로 수행되며, [[HARQ_ACK_Codebook_Determination]] 및 [[UCI_Multiplexing_PUSCH]]와 관련된 다중화 기능을 지원합니다.

## 상세 설명
[[RACH_Procedure_L1]]은 다음과 같은 주요 단계로 구성됩니다.

1. [[PRACH]] 프리앰블 전송: [[UE]]는 상위 계층의 지시에 따라 [[PRACH_Sequence_Generation]]을 통해 생성된 프리앰블을 전송합니다.
2. Type-1 절차: [[PRACH]] 전송 후 [[gNB]]로부터 [[RAR]]을 수신합니다. 이후 [[RAR]]에 포함된 UL Grant를 사용하여 [[PUSCH]]를 전송합니다.
3. Type-2 절차: [[PRACH]]와 [[PUSCH]]를 동시에 전송하는 MsgA를 수행하며, 이후 [[gNB]]로부터 MsgB를 수신하여 응답을 처리합니다.
4. 경합 해결: [[PDSCH]]를 통해 수신된 UE Contention Resolution Identity를 확인하여 랜덤 액세스 절차의 성공 여부를 판단합니다.

본 절차 수행 시 [[HARQ_ACK_spatial_bundling]] 및 [[UCI_Multiplexing_PUSCH]]와 같은 기능이 요구되며, 특히 [[PUSCH]] 전송 시 서로 다른 시작 OFDM 심볼을 갖는 경우의 [[HARQ_ACK]] 다중화가 지원되어야 합니다. 또한, [[Inter-band_CA]] 환경에서 [[SRS]], [[PUCCH]], [[PUSCH]]와 병렬 전송이 발생할 경우 [[Uplink_Power_Prioritization]] 규칙에 따라 전송이 제어됩니다.

## 인과 관계
- [[PRACH_Power_Control]] (depends_on) [[RACH_Procedure_L1]]
- [[RACH_Procedure_L1]] (triggers) [[PUSCH]]
- [[RACH_Procedure_L1]] (triggers) [[PDSCH]]
- [[UCI_Multiplexing_PUSCH]] (affects) [[RACH_Procedure_L1]]

## 관련 개념
- [[PRACH]] (part_of)
- [[PUSCH]] (part_of)
- [[PDSCH]] (part_of)
- [[RAR]] (part_of)
- [[Uplink_Power_Control]] (depends_on)
- [[HARQ_ACK_Codebook_Determination]] (depends_on)

## 스펙 근거
- [[HARQ_ACK_spatial_bundling]] for [[PUCCH]] or [[PUSCH]]: TS 38.213 §8
- [[SR]]/[[HARQ_ACK]]/[[CSI]] multiplexing: TS 38.213 §8
- [[HARQ_ACK]] multiplexing on [[PUSCH]] with different starting OFDM symbols: TS 38.213 §8
- [[PRACH]] preamble transmission: TS 38.213 §8.1
- [[PUSCH]] for Type-2 random access: TS 38.213 §8.1A
- [[RAR]] for Type-1 random access: TS 38.213 §8.2
- [[RAR]] for Type-2 random access: TS 38.213 §8.2A
- [[PUSCH]] scheduled by [[RAR]] UL grant: TS 38.213 §8.3
- [[PDSCH]] with UE contention resolution identity: TS 38.213 §8.4

## 소스
- 3GPP TS 38.213 §8, §8.1, §8.1A, §8.2, §8.2A, §8.3, §8.4