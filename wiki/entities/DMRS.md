# DMRS

## 정의
[[DMRS]] (Demodulation Reference Signal)는 [[PDSCH]] 및 [[PUSCH]]와 같은 물리 채널의 복조를 위해 수신단에서 채널 추정을 수행하는 데 사용되는 참조 신호입니다.

## 요약
[[DMRS]]는 데이터 채널과 동일한 프리코딩이 적용되어 전송되며, 수신단에서 채널의 위상 및 진폭 변화를 보상하여 데이터를 정확하게 복조할 수 있도록 돕습니다. 본 페이지는 [[PDSCH]]를 위한 [[DMRS]] 설정, 포트 매핑, 스크램블링 및 [[QCL]] 가정을 다룹니다.

## 상세 설명
[[DMRS]]는 무선 채널 환경에서 데이터 심볼의 복조를 위한 기준점을 제공합니다. 

- UE Feature 지원:
  - 필수(항상): Basic downlink [[DMRS]] for scheduling type A, Basic downlink [[DMRS]] for scheduling type B, Basic uplink [[DMRS]] for scheduling type A, Basic uplink [[DMRS]] for scheduling type B
  - 필수(cap): [[PDSCH]] beam switching, Support 1+2 [[DMRS]] (downlink), Support 1+2 [[DMRS]] (uplink)
  - 선택: Support alternative additional [[DMRS]] location, Supported 2 symbols front-loaded [[DMRS]] (downlink), Supported 2 symbols front-loaded +2 symbols additional [[DMRS]] (downlink), Support 1+3 [[DMRS]] symbols (downlink)
  - 조건부: Support [[DMRS]] type (downlink)

[[DMRS]] 수신 절차는 상위 계층 파라미터에 의해 구성되며, 전송되는 [[PDSCH]]의 스케줄링 타입과 매핑 방식에 따라 결정됩니다. 수신단은 구성된 [[DMRS]] 포트와 [[QCL]] (Quasi-Co-Location) 정보를 활용하여 채널을 추정합니다.

## 인과 관계
- [[DMRS]] (depends_on) [[PDSCH]]
- [[DMRS]] (affects) [[PDSCH_Reception_Procedures]]
- [[DMRS]] (triggers) [[Channel_Estimation]]

## 관련 개념
- [[PDSCH]] (part_of)
- [[PUSCH]] (part_of)
- [[QCL]] (depends_on)
- [[DMRS_Generation_Mapping]] (similar_to)

## 스펙 근거
TS 38.214 §5.1.6.2에 따르면, [[PDSCH]] 복조를 위한 [[DMRS]] 수신 절차는 상위 계층에서 설정된 [[DMRS]] 구성 파라미터 및 [[DCI]]를 통해 전달된 스케줄링 정보를 기반으로 수행됩니다.

## 소스
- 3GPP TS 38.214 §5.1.6.2