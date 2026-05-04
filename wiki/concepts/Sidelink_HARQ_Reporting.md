# Sidelink_HARQ_Reporting

## 정의
[[Sidelink]] 환경에서 수신된 데이터에 대한 [[HARQ]]-ACK 정보를 생성하고, 이를 상향링크 채널인 [[PUCCH]] 또는 [[PUSCH]]를 통해 기지국(gNB)으로 보고하는 절차를 의미합니다.

## 요약
UE는 [[Sidelink]]를 통해 수신한 데이터의 성공 여부를 판단하여 [[HARQ]]-ACK 정보를 생성합니다. 이 정보는 상향링크 제어 정보([[UCI]])의 일부로서 [[PUCCH]] 또는 [[PUSCH]]를 통해 기지국으로 전달됩니다. 이때 UE의 능력(Capability)에 따라 [[HARQ]]-ACK 코드북 구성 방식과 다중화(Multiplexing) 방식이 결정됩니다.

## 상세 설명
[[Sidelink]] [[HARQ]]-ACK 보고는 기지국이 UE의 [[Sidelink]] 수신 상태를 모니터링하고 자원 할당을 최적화하기 위해 수행됩니다.

1. **코드북 결정**: UE는 [[HARQ]]-ACK 정보를 보고하기 위해 [[Type-1_HARQ-ACK_codebook_determination]] 또는 [[Type-2_HARQ-ACK_codebook_determination]] 방식을 사용합니다. 이는 [[PUCCH]] 또는 [[PUSCH]]를 통한 보고 시점에 따라 결정됩니다.
2. **다중화**: UE는 [[SR_Reporting_Procedure]], [[CSI_Reporting_Procedures]]와 [[HARQ]]-ACK을 동일한 슬롯 내에서 다중화하여 전송할 수 있습니다.
3. **UE Capability**: 
   - [필수(cap)] HARQ-ACK spatial bundling for PUCCH or PUSCH per PUCCH group을 지원해야 합니다.
   - [필수(cap)] SR/HARQ-ACK/CSI multiplexing once per slot using a PUCCH (or HARQ-ACK/CSI piggybacked on a PUSCH) when SR/HARQ-ACK/CSI are supposed to be sent with the same starting symbol on the PUCCH resources를 지원해야 합니다.
   - [필수(cap)] HARQ-ACK multiplexing on PUSCH with different PUCCH/PUSCH starting OFDM symbols을 지원해야 합니다.
   - [선택] SR/HARQ-ACK/CSI multiplexing에 관한 다양한 조합(10-35, 10-35a, 10-35b, 10-35c, 10-36, 11-3g 등)을 지원할 수 있습니다.

## 인과 관계
- [[Sidelink_Shared_Channel_Procedures]] (depends_on)
- [[UCI_Multiplexing_PUCCH]] (affects)
- [[UCI_Multiplexing_PUSCH]] (affects)
- [[HARQ_ACK_Codebook_Determination]] (depends_on)

## 관련 개념
- [[PUCCH]] (part_of)
- [[PUSCH]] (part_of)
- [[HARQ]] (part_of)
- [[UCI]] (part_of)

## 스펙 근거
- TS 38.213 §16.5에 따르면, UE는 상향링크를 통해 [[HARQ]]-ACK 정보를 보고하기 위한 절차를 수행해야 합니다.
- TS 38.213 §16.5.1 및 §16.5.2에 따라 [[Type-1_HARQ-ACK_codebook_determination]] 및 [[Type-2_HARQ-ACK_codebook_determination]]이 정의됩니다.

## 소스
- 3GPP TS 38.213 Release 18 (v18.0.0) §16.5, §16.5.1, §16.5.2
- 3GPP TS 38.822 (UE Feature List)