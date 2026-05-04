# PTRS_Generation_Mapping

## 정의
[[PT-RS]]는 고주파 대역에서 발생하는 위상 잡음(Phase Noise)을 보상하기 위해 [[PDSCH]] 및 [[PUSCH]] 전송에 사용되는 [[Reference_Signals]]의 일종입니다.

## 요약
[[PT-RS]]는 시간 및 주파수 영역에서 위상 추적을 수행하여 수신단에서의 위상 잡음 영향을 최소화합니다. [[PUSCH]]의 경우 [[Transform_Precoding]] 활성화 여부에 따라 시퀀스 생성 및 매핑 방식이 달라지며, [[PDSCH]]는 설정된 파라미터에 따라 자원 요소에 매핑됩니다. [[DCI]]를 통해 [[DMRS]] 포트와 연관되어 전송됩니다.

## 상세 설명
### PT-RS 시퀀스 생성
- [[PT-RS]] 시퀀스는 의사 난수 생성기(Pseudo-random sequence generator)를 기반으로 생성됩니다. 
- [[PUSCH]]에서 [[Transform_Precoding]]이 비활성화된 경우, 시퀀스는 [[DMRS]]와 유사하게 특정 초기화 값에 의해 결정됩니다 (TS 38.211 §6.4.1.2.1.1).
- [[Transform_Precoding]]이 활성화된 경우, 시퀀스는 [[PUSCH_Transform_Precoding]]의 특성을 고려하여 생성됩니다 (TS 38.211 §6.4.1.2.1.2).
- [[PDSCH]]의 경우, 상위 계층 파라미터에 의해 시퀀스 생성 파라미터가 결정됩니다 (TS 38.211 §7.4.1.2.1).

### 자원 매핑
- [[PT-RS]]는 할당된 [[Physical_Resource_Grid]] 내의 특정 부반송파와 심볼에 매핑됩니다.
- [[PUSCH]]의 경우, [[DMRS]] 포트와의 연관성에 따라 [[Precoding]] 및 자원 매핑이 수행됩니다 (TS 38.211 §6.4.1.2.2).
- [[PDSCH]]의 경우, 설정된 시간/주파수 밀도에 따라 자원 요소에 매핑됩니다 (TS 38.211 §7.4.1.2.2).

### DCI 기반 연관
- [[PT-RS]]는 [[DCI_Formats_Processing]]을 통해 스케줄링되며, [[DMRS]] 포트와 연관되어 전송됩니다. 
- Rel.18에서 도입된 향상된 [[DMRS]] 포트 지원을 위해 1개 또는 2개의 [[PT-RS]] 포트가 사용될 수 있으며, 이는 [[PUSCH]]의 랭크(Rank) 및 전송 방식(Codebook/Non-codebook)에 따라 결정됩니다.

## 인과 관계
- [[DCI]] 설정 (triggers) [[PT-RS]] 전송
- [[Transform_Precoding]] (affects) [[PT-RS]] 시퀀스 생성 및 매핑
- [[DMRS]] 포트 설정 (depends_on) [[PT-RS]] 포트 수 및 매핑

## 관련 개념
- [[DMRS]] (depends_on)
- [[PUSCH]] (part_of)
- [[PDSCH]] (part_of)
- [[Transform_Precoding]] (affects)
- [[DCI_Formats_Processing]] (triggers)

## 스펙 근거
- TS 38.211 §6.4.1.2: [[PUSCH]]용 [[PT-RS]] 생성 및 매핑
- TS 38.211 §7.4.1.2: [[PDSCH]]용 [[PT-RS]] 생성 및 매핑
- TS 38.212 §7.3.1.1.2: [[DCI]] Format 0_1 내 [[PT-RS]] 관련 필드
- TS 38.214 §5.1.6.3: [[PT-RS]] 수신 절차

## 소스
- 3GPP TS 38.211 V18.x.x (Physical channels and modulation)
- 3GPP TS 38.212 V18.x.x (Multiplexing and channel coding)
- 3GPP TS 38.214 V18.x.x (Physical layer procedures for data)