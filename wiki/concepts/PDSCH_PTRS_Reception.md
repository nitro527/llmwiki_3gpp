# PDSCH_PTRS_Reception

## 정의
[[PDSCH]] 수신 시 위상 잡음(Phase Noise) 보상을 위해 사용되는 [[PT-RS]]의 존재 여부, 밀도(Density), 그리고 [[DMRS]]와의 연관성을 결정하는 수신 절차.

## 요약
[[PDSCH]] 수신 시 상위 계층 파라미터인 phaseTrackingRS 설정 여부에 따라 [[PT-RS]] 존재 여부가 결정됩니다. [[PT-RS]]가 설정된 경우, 스케줄링된 MCS와 대역폭(RB 수)을 기반으로 시간 및 주파수 밀도가 결정되며, [[DMRS]] 포트와의 연관성을 통해 위상 추정을 수행합니다. 다중 TCI 상태가 지시된 경우, 각 TCI 상태에 대응하는 [[DMRS]] 포트와 연관된 [[PT-RS]] 포트가 할당됩니다.

## 상세 설명
[[PDSCH]] [[PT-RS]] 수신 절차는 TS 38.214 §5.1.6.3에 따라 다음과 같이 수행됩니다.

1. **설정 확인**: 상위 계층 파라미터 phaseTrackingRS가 DMRS-DownlinkConfig 내에 설정되어야 합니다. 설정되지 않은 경우 [[PT-RS]]는 존재하지 않는 것으로 간주합니다.
2. **밀도 결정**:
   - timeDensity(ptrs-MCSi) 및 frequencyDensity(NRBi) 파라미터가 설정된 경우, 스케줄링된 MCS와 RB 수에 따라 Table 5.1.6.3-1 및 Table 5.1.6.3-2를 참조하여 LPT-RS와 KPT-RS를 결정합니다.
   - 파라미터가 설정되지 않은 경우 기본값으로 LPT-RS = 1, KPT-RS = 2를 사용합니다.
   - 특정 MCS 임계값 미만이거나 RB 수가 3 미만인 경우, 또는 RNTI가 RA-RNTI, MSGB-RNTI, SI-RNTI, P-RNTI인 경우 [[PT-RS]]는 존재하지 않습니다.
3. **제약 조건**:
   - PDSCH 할당 기간이 2 심볼인 경우 LPT-RS가 2 또는 4이면 [[PT-RS]]는 전송되지 않습니다.
   - PDSCH 할당 기간이 4 심볼인 경우 LPT-RS가 4이면 [[PT-RS]]는 전송되지 않습니다.
4. **DMRS 연관성**:
   - [[PT-RS]] 포트는 [[DMRS]] 포트와 'typeA' 및 'typeD'에 대해 [[QCL]] 관계를 가집니다.
   - 단일 코드워드 스케줄링 시, [[PT-RS]] 포트는 할당된 [[DMRS]] 포트 중 가장 낮은 인덱스의 포트와 연관됩니다.
   - 두 개의 코드워드 스케줄링 시, 더 높은 MCS를 가진 코드워드의 가장 낮은 인덱스 [[DMRS]] 포트와 연관됩니다.
5. **다중 TCI 상태 대응**:
   - 두 개의 TCI 상태가 지시되고 [[DMRS]] 포트가 두 개의 CDM 그룹에 걸쳐 있는 경우, 각 TCI 상태의 가장 낮은 인덱스 [[DMRS]] 포트와 연관된 두 개의 [[PT-RS]] 포트를 수신합니다.
   - fdmSchemeA 또는 fdmSchemeB가 설정된 경우, 단일 [[PT-RS]] 포트가 할당되며 각 TCI 상태에 할당된 PRB에 따라 주파수 밀도가 결정됩니다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_PTRS_Reception]] (위상 잡음 보상을 위한 참조 신호 수신 절차)
- [[DMRS]] affects [[PDSCH_PTRS_Reception]] (PT-RS 포트 연관성 및 QCL 관계 결정)
- [[PDSCH_TCI_State_Management]] affects [[PDSCH_PTRS_Reception]] (다중 TCI 상태 시 PT-RS 포트 할당 방식 결정)

## 관련 개념
- [[PDSCH]] (depends_on)
- [[DMRS]] (affects)
- [[PDSCH_TCI_State_Management]] (affects)
- [[PT-RS]] (implements)

## 스펙 근거
- TS 38.214 §5.1.6.3: PT-RS reception procedure
- TS 38.211 §7.4.1.1.2: PDSCH allocation duration definition

## 소스
- 3GPP TS 38.214 v19.0.0 (2024-03)