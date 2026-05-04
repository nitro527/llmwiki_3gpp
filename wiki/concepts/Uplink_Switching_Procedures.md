# Uplink_Switching_Procedures

## 정의
[[Uplink_Switching_Procedures]]는 [[UE]]가 다중 상향링크 캐리어 또는 다중 밴드 환경에서 전송 경로를 동적으로 변경할 때 발생하는 물리 계층의 제어 절차를 의미합니다. 이는 [[EN-DC]] 및 [[Carrier_Aggregation]] 환경에서 제한된 RF 자원을 효율적으로 활용하기 위해 수행됩니다.

## 요약
본 절차는 [[UE]]가 서로 다른 상향링크 캐리어 간에 전송을 전환할 때 필요한 스위칭 갭(Switching Gap)을 관리하고, 다중 밴드 지원 시 발생하는 RF 제약을 해결합니다. 주요 동작 모드로는 2T/1T 모드 전환 및 다중 밴드 간의 동적 스위칭이 포함되며, 이는 [[PUSCH]], [[PUCCH]], [[SRS]] 등의 전송 타이밍에 영향을 미칩니다.

## 상세 설명
[[Uplink_Switching_Procedures]]는 다음과 같은 환경에서 정의됩니다.

* [[EN-DC]] 환경: [[E-UTRA]]와 [[NR]] 간의 상향링크 전송을 전환할 때, [[UE]]는 특정 스위칭 갭을 준수해야 합니다. 이는 [[TS_38_822]]에서 정의된 기능적 요구사항을 따르며, 상향링크 전송 간의 충돌을 방지합니다.
* [[Carrier_Aggregation]] 환경: 2개 이상의 상향링크 밴드를 사용하는 경우, [[UE]]의 RF 능력에 따라 동적 스위칭이 수행됩니다. 3개 또는 4개의 상향링크 밴드를 사용하는 경우, 각 밴드 조합에 따른 스위칭 제약이 적용됩니다.
* [[Supplementary_Uplink]] (SUL): [[SUL]]과 비-SUL 캐리어 간의 동적 스위칭이 지원되며, 이는 서로 다른 [[Frame_Structure_Numerology]]를 가질 수 있습니다.

## 인과 관계
* [[Uplink_Switching_Procedures]] (affects) [[PUSCH_Transmission_Procedures]]
* [[Uplink_Switching_Procedures]] (affects) [[SRS_Carrier_Switching]]
* [[Uplink_Switching_Procedures]] (depends_on) [[UE_Capability]]
* [[Uplink_Switching_Procedures]] (triggers) [[DL_Interruption]]

## 관련 개념
- [[EN-DC]] (depends_on)
- [[Carrier_Aggregation]] (depends_on)
- [[Supplementary_Uplink]] (depends_on)
- [[PUSCH]] (affects)
- [[SRS]] (affects)
- [[UE_Capability]] (depends_on)

## 스펙 근거
- [[TS_38_214]] §6.1.6에 따르면, [[UE]]는 상향링크 전송을 위해 캐리어 간 스위칭을 수행할 수 있으며, 이때 필요한 스위칭 갭을 적용해야 합니다.
- [[TS_38_214]] §6.1.6.1은 [[EN-DC]] 환경에서의 상향링크 스위칭 절차를 정의합니다.
- [[TS_38_214]] §6.1.6.2.0 및 §6.1.6.2.2는 각각 2개 밴드 및 3~4개 밴드 환경에서의 상향링크 스위칭 규칙을 명시합니다.
- [[TS_38_214]] §6.1.6.3은 [[SUL]] 환경에서의 상향링크 스위칭 절차를 정의합니다.

## 소스
- 3GPP TS 38.214 V17.x.x (Release 17)
- 3GPP TS 38.822 (UE Feature List)