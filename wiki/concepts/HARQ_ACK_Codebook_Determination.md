# HARQ_ACK_Codebook_Determination

## 정의
[[HARQ_ACK_Codebook_Determination]]은 [[UE]]가 [[PDSCH]] 수신 또는 [[SPS]] 해제에 대한 응답으로 생성하는 [[HARQ_ACK]] 비트들의 집합을 결정하는 절차를 의미합니다.

## 요약
[[HARQ_ACK]] 코드북은 네트워크의 구성 방식에 따라 [[Semi-static]] 방식인 [[Type-1]]과 [[Dynamic]] 방식인 [[Type-2]], 그리고 [[One-shot]] 피드백을 위한 [[Type-3]]로 구분됩니다. 각 코드북은 [[PUCCH]] 또는 [[PUSCH]]를 통해 전송되며, [[CBG]] 기반 재전송 지원 여부 및 멀티캐스트/유니캐스트 처리에 따라 비트 매핑 규칙이 결정됩니다.

## 상세 설명
[[HARQ_ACK]] 코드북 결정 절차는 다음과 같은 주요 유형으로 나뉩니다.

1. [[Type-1]] (Semi-static): [[PDCCH]] 모니터링 기회와 [[PDSCH]] 수신 타이밍을 기반으로 코드북 크기를 고정합니다. [[TS 38.213]] §9.1.2에 따라 [[PUCCH]] 또는 [[PUSCH]]에서 전송됩니다.
2. [[Type-2]] (Dynamic): [[DCI]] 내의 [[DAI]] 필드를 활용하여 코드북 크기를 동적으로 결정합니다. [[TS 38.213]] §9.1.3에 정의되어 있으며, [[CBG]] 기반 재전송을 위한 서브 코드북 구성이 가능합니다.
3. [[Type-3]]: [[One-shot]] [[HARQ_ACK]] 피드백을 위해 사용되며, [[TS 38.213]] §9.1.4에 명시된 절차를 따릅니다.

[[CBG]] 기반 코드북은 [[PDSCH]] 수신 시 각 [[CBG]] 단위로 [[HARQ_ACK]] 정보를 생성하며, 이는 [[Type-1]] 및 [[Type-2]] 코드북 결정 절차 내에서 처리됩니다. 또한, [[UE]]는 특정 조건(예: 11-3c, 11-3d, 11-3e, 11-3f)에 따라 동일 서브슬롯 내에서 다중 [[PUCCH]] 전송을 수행하여 코드북을 전달할 수 있습니다.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) [[HARQ_ACK_Codebook_Determination]]
- [[HARQ_ACK_Codebook_Determination]] (affects) [[UCI_Multiplexing_PUCCH]]
- [[HARQ_ACK_Codebook_Determination]] (affects) [[UCI_Multiplexing_PUSCH]]
- [[PDSCH_CBG_Transmission]] (depends_on) [[HARQ_ACK_Codebook_Determination]]

## 관련 개념
- [[PUCCH]] (part_of)
- [[PUSCH]] (part_of)
- [[PDSCH]] (depends_on)
- [[HARQ_ACK]] (part_of)
- [[DCI_Formats_Processing]] (depends_on)

## 스펙 근거
- [[TS 38.213]] §9.1: [[HARQ_ACK]] 코드북 결정 절차 전반
- [[TS 38.213]] §9.1.1: [[CBG]] 기반 [[HARQ_ACK]] 코드북 결정
- [[TS 38.213]] §9.1.2: [[Type-1]] [[HARQ_ACK]] 코드북 결정
- [[TS 38.213]] §9.1.3: [[Type-2]] [[HARQ_ACK]] 코드북 결정
- [[TS 38.213]] §9.1.4: [[Type-3]] [[HARQ_ACK]] 코드북 결정
- [[TS 38.822]]: [[UE]] 기능(Feature) 우선순위 및 지원 항목

## 소스
- 3GPP TS 38.213 V18.0.0 "NR; Physical layer procedures for control"
- 3GPP TS 38.822 V18.0.0 "NR; User Equipment (UE) radio transmission and reception features"