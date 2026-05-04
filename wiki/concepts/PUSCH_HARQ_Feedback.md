# PUSCH_HARQ_Feedback

## 정의
[[PUSCH]] 전송과 관련된 [[HARQ]]-ACK 정보 처리 및 유효성 판단 절차는 기지국이 전송한 [[DCI]]를 통해 [[UE]]가 상향링크 자원 상에서 HARQ-ACK 정보를 보고하거나, PUSCH 전송에 대한 피드백을 수신하는 메커니즘을 의미합니다.

## 요약
TS 38.213 §10.5에 따라, UE는 PUSCH 전송과 관련된 HARQ-ACK 정보를 처리하며, 여기에는 [[PUCCH]] 그룹별 공간적 번들링(spatial bundling) 및 다중화 규칙이 포함됩니다. 특히 PDSCH 스케줄링 이후의 PUSCH 전송 시 다양한 [[HARQ_ACK_Codebook_Determination]] 방식이 적용됩니다.

## 상세 설명
UE는 상향링크 전송 시 다음과 같은 HARQ-ACK 관련 절차를 수행합니다.

*   **공간적 번들링(Spatial Bundling):** UE는 [[PUCCH]] 또는 [[PUSCH]]를 통한 HARQ-ACK 보고 시, PUCCH 그룹별로 공간적 번들링을 수행할 수 있습니다(필수 기능 4-12).
*   **다중화(Multiplexing):** SR, HARQ-ACK, [[CSI]]가 동일한 슬롯 내에서 전송되어야 할 경우, PUCCH 또는 PUSCH에 피기백(piggyback)하여 전송합니다(필수 기능 4-19). 또한, 슬롯 내에서 서로 다른 시작 심볼을 가지는 경우에 대한 다중화 규칙(4-19a, 4-19b, 4-19c)이 정의되어 있습니다.
*   **PDSCH 스케줄링 이후 PUSCH 전송:** PDSCH가 UL 그랜트 이후 스케줄링된 경우, UE는 Type-1, Type-2, Type-3 HARQ-ACK 코드북을 PUSCH에 다중화하여 전송할 수 있습니다(선택 기능 55-4a, 55-4b, 55-4c). 이 과정에서 서로 다른 PUCCH 자원 결정(55-4d) 및 코드북 크기 결정(55-4e) 절차가 수반됩니다.
*   **기타 기능:** 유니캐스트 및 그룹 공통 PDSCH에 대한 피드백 다중화(33-3-5) 및 DCI format 1_3을 이용한 Type 3 HARQ-ACK 코드북 트리거(49-5b)가 지원됩니다.

## 인과 관계
*   [[DCI_Formats_Processing]] (triggers) PUSCH HARQ-ACK 피드백 절차
*   [[HARQ_ACK_Codebook_Determination]] (depends_on) PUSCH HARQ-ACK 다중화
*   [[UCI_Multiplexing_PUSCH]] (affects) PUSCH 내 HARQ-ACK 정보 전송

## 관련 개념
- [[PUSCH]] (part_of)
- [[HARQ]] (part_of)
- [[PUCCH]] (similar_to)
- [[UCI_Multiplexing_PUSCH]] (depends_on)
- [[HARQ_ACK_Codebook_Determination]] (depends_on)

## 스펙 근거
- TS 38.213 §10.5: HARQ-ACK information for PUSCH transmissions

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"