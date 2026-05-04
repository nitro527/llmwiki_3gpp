# DMRS_Generation_Mapping

## 정의
[[DMRS]](Demodulation Reference Signal)는 [[PDSCH]](Physical Downlink Shared Channel)의 복조를 위해 수신기에서 채널 추정을 수행하는 데 사용되는 기준 신호입니다.

## 요약
[[PDSCH]]를 위한 [[DMRS]]는 의사 난수 시퀀스(Pseudo-random sequence) 생성기를 통해 생성되며, 물리 자원 그리드에 매핑됩니다. 이 과정은 [[UE]]의 능력(Capability)에 따라 지원되는 매핑 타입(Type A, Type B)과 포트 구성에 따라 결정됩니다.

## 상세 설명
[[PDSCH]] [[DMRS]]의 생성 및 매핑 절차는 다음과 같습니다.

1. **시퀀스 생성**: [[DMRS]] 시퀀스는 TS 38.211 §7.4.1.1.1에 정의된 바와 같이 Gold 시퀀스를 기반으로 생성됩니다. 시퀀스 초기화 값은 슬롯 번호, 심볼 인덱스, 그리고 상위 계층에서 설정된 스크램블링 ID(n_ID_DMRS)에 의해 결정됩니다.
2. **자원 매핑**: TS 38.211 §7.4.1.1.2에 따라, 생성된 시퀀스는 물리 자원 블록(PRB) 내의 특정 부반송파와 심볼 위치에 매핑됩니다. 이때 [[CDM]](Code Division Multiplexing) 그룹을 사용하여 다중 안테나 포트 간의 직교성을 확보합니다.
3. **수신 절차**: [[UE]]는 TS 38.214 §5.1.6.2에 기술된 절차에 따라 수신된 [[DMRS]]를 사용하여 채널을 추정합니다. 이 과정에서 [[QCL]](Quasi-Co-Location) 정보가 고려되어야 하며, 다중 포트 간의 간섭을 제거하기 위한 디매핑이 수행됩니다.

## 인과 관계
- [[PDSCH]] 매핑 타입 A/B 설정 (depends_on) [[Frame_Structure_Numerology]]
- [[DMRS]] 포트 구성 (affects) [[PDSCH_Layer_Mapping]]
- [[QCL]] 파라미터 (affects) [[PDSCH_Reception_Procedures]]
- [[UE]] 처리 능력 (depends_on) [[DMRS]] 매핑 패턴

## 관련 개념
- [[PDSCH]] (part_of)
- [[DMRS]] (part_of)
- [[QCL]] (depends_on)
- [[CDM]] (affects)
- [[Physical_Resource_Grid]] (part_of)

## 스펙 근거
- TS 38.211 §7.4.1.1: [[PDSCH]]를 위한 [[DMRS]] 시퀀스 생성 및 자원 매핑 규정
- TS 38.211 §7.4.1.3: [[PDCCH]]를 위한 [[DMRS]] 시퀀스 생성 및 자원 매핑 규정
- TS 38.211 §7.4.1.4: [[PBCH]]를 위한 [[DMRS]] 시퀀스 생성 및 자원 매핑 규정
- TS 38.214 §5.1.6.2: [[PDSCH]] [[DMRS]] 수신 절차 및 채널 추정 규정

## 소스
- 3GPP TS 38.211 V18.0.0 (2023-12)
- 3GPP TS 38.214 V18.0.0 (2023-12)