# PUCCH_Resource_Selection

## 정의
[[PUCCH_Resource_Selection]]은 [[UE]]가 상향링크 제어 정보([[UCI]])를 전송하기 위해 적절한 [[PUCCH]] 자원을 결정하는 절차를 의미하며, 상위 계층 설정 및 [[DCI]] 필드 정보를 기반으로 수행됩니다.

## 요약
[[UE]]는 전용 [[PUCCH]] 자원 설정 여부에 따라 공통 자원 세트 또는 전용 자원 세트에서 자원을 선택합니다. [[UCI]] 페이로드 크기, [[HARQ_ACK_Codebook_Determination]] 결과, 그리고 [[PDCCH]] 수신 시의 [[DCI]] 내 PUCCH 자원 지시자 필드 값을 조합하여 최종적인 [[PUCCH]] 자원을 결정합니다.

## 상세 설명
[[UE]]가 전용 [[PUCCH]] 자원 설정을 받지 못한 경우, TS 38.213 §9.2.1에 따라 [[pucch-ResourceCommon]]을 통해 제공된 인덱스를 사용하여 초기 상향링크 [[Bandwidth_Part_Operation]] 내에서 자원을 결정합니다. 이 자원 세트는 16개의 자원을 포함하며, 각 자원은 [[PUCCH]] 포맷, 시작 심볼, 지속 시간, PRB 오프셋, 순환 이동(cyclic shift) 인덱스 세트를 정의합니다.

[[UE]]가 [[DCI]] 포맷을 통해 [[PDSCH]] 수신을 스케줄링받거나 [[HARQ_ACK]] 정보를 수신할 때, [[PUCCH]] 자원 인덱스 $r_{PUCCH}$는 다음 식을 통해 결정됩니다:
$r_{PUCCH} = \lfloor \frac{n_{CCE,0} \cdot K}{N_{CCE}} \rfloor + \Delta_{PRI}$
여기서 $n_{CCE,0}$는 [[PDCCH]] 수신을 위한 첫 번째 [[CCE]] 인덱스이며, $N_{CCE}$는 [[CORESET]] 내의 총 [[CCE]] 수, $\Delta_{PRI}$는 [[DCI]] 내의 PUCCH 자원 지시자 필드 값입니다.

전용 [[PUCCH]] 자원 설정이 제공된 경우, [[UE]]는 상위 계층으로부터 하나 이상의 [[PUCCH_ResourceSet]]을 설정받습니다. 각 세트는 [[maxPayloadSize]]를 통해 전송 가능한 최대 [[UCI]] 비트 수를 정의합니다. [[UE]]는 전송할 [[UCI]] 페이로드 크기에 따라 적절한 [[PUCCH_ResourceSet]]을 선택합니다:
- 첫 번째 세트([[pucch-ResourceSetId]] = 0): 최대 2비트 [[UCI]]
- 이후 세트: 설정된 [[maxPayloadSize]] 또는 기본값 1706비트를 기준으로 페이로드 크기에 따라 선택

[[SPS_PUCCH_AN_List]]가 제공된 경우, [[UE]]는 [[SPS]] [[PDSCH]] 수신에 대한 [[HARQ_ACK]] 전송 시 리스트의 각 엔트리에 정의된 [[sps-PUCCH-AN-ResourceID]]를 사용하여 자원을 결정합니다.

## 인과 관계
- [[PUCCH_Resource_Selection]] depends_on [[DCI_Field_Mapping]] (PUCCH 자원 지시자 필드 값 사용)
- [[PUCCH_Resource_Selection]] depends_on [[HARQ_ACK_Codebook_Determination]] (UCI 페이로드 크기 결정)
- [[PUCCH_Resource_Selection]] triggers [[PUCCH_Format_Processing]] (결정된 자원에 따른 포맷 처리 수행)
- [[PUCCH_Resource_Selection]] affects [[PUCCH_Power_Control]] (선택된 자원의 포맷 및 파라미터에 따른 전력 제어)

## 관련 개념
- [[PUCCH]] (part_of)
- [[UCI]] (affects)
- [[DCI]] (affects)
- [[PDCCH]] (depends_on)
- [[Bandwidth_Part_Operation]] (depends_on)
- [[HARQ_ACK_Codebook_Determination]] (depends_on)

## 스펙 근거
- TS 38.213 §9.2.1: PUCCH 자원 세트 구성 및 자원 선택 공식
- TS 38.213 §9.2.2: 전용 PUCCH 자원 설정 및 파라미터 정의
- TS 38.213 §9.2.3: UCI 페이로드 크기에 따른 자원 세트 선택 규칙

## 소스
- 3GPP TS 38.213 v18.0.0, "NR; Physical layer procedures for control"