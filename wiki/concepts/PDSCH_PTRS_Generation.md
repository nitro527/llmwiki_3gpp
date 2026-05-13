# PDSCH_PTRS_Generation

## 정의
[[PDSCH]] 전송 시 위상 잡음(Phase Noise)을 추적하고 보상하기 위해 사용되는 참조 신호인 Phase-tracking reference signal(PT-RS)의 시퀀스 생성 및 물리 자원 매핑 절차를 의미합니다.

## 요약
[[PDSCH]] PT-RS는 고주파 대역에서 발생하는 위상 잡음을 보상하기 위해 도입되었습니다. 시퀀스는 [[DMRS]]를 기반으로 생성되며, 상위 계층 설정 및 [[DCI]] 지시에 따라 특정 자원 블록과 OFDM 심볼에 매핑됩니다. 전송 전에는 전력 보정을 위한 스케일링 인자가 적용됩니다.

## 상세 설명
PT-RS 시퀀스 생성 및 매핑은 TS 38.211 §7.4.1.2에 정의된 절차를 따릅니다.

1. 시퀀스 생성:
   PT-RS 시퀀스는 서브캐리어 $k$에 대해 정의됩니다. 상위 계층 파라미터 dmrs-TypeEnh가 설정된 경우와 그렇지 않은 경우에 따라 [[DMRS]] 시퀀스를 기반으로 생성됩니다. 이때 $r_{m,n}(k)$는 위치 $l$과 서브캐리어 $k$에서의 [[DMRS]] 시퀀스를 참조합니다.

2. 자원 매핑:
   PT-RS는 [[PDSCH]]가 할당된 자원 블록 내에서만 존재하며, TS 38.214의 절차에 따라 사용 여부가 결정됩니다.
   - 전력 스케일링: PT-RS는 TS 38.214 §4.1에 명시된 전송 전력을 준수하기 위해 스케일링 인자 $\beta_{PT-RS}$가 적용됩니다.
   - 시간 도메인 매핑: PT-RS가 위치할 OFDM 심볼 인덱스 집합은 [[PDSCH]] 할당 시작점으로부터 계산됩니다. [[DMRS]] 심볼과 겹치는 경우를 고려하여 반복적으로 심볼 인덱스를 결정합니다.
   - 주파수 도메인 매핑: 할당된 자원 블록 내에서 서브캐리어 인덱스는 0부터 $N_{RB}^{PDSCH} \cdot N_{SC}^{RB} - 1$까지 번호가 매겨집니다. PT-RS가 매핑되는 서브캐리어는 다음 식을 따릅니다.
     $k = k_{ref} + (i \cdot N_{RB}^{PT-RS} + f(i, n_{RNTI})) \cdot N_{SC}^{RB} + \text{offset}$
     여기서 $k_{ref}$는 기준 서브캐리어, $N_{RB}^{PT-RS}$는 PT-RS 자원 블록 간격, $f(i, n_{RNTI})$는 RNTI와 연관된 함수입니다.
   - 오프셋: 상위 계층 파라미터 resourceElementOffset이 설정되지 않은 경우 'offset00'에 해당하는 값을 사용합니다.

3. 예외 사항:
   [[DMRS]], 비영전력 [[CSI_RS]], 영전력 [[CSI_RS]], [[SS_PBCH_Block]], 또는 감지된 [[PDCCH]]가 점유한 자원 요소에는 PT-RS가 매핑되지 않습니다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_PTRS_Generation]] (위상 잡음 보상을 위한 참조 신호 생성)
- [[PDSCH_PTRS_Generation]] depends_on [[DMRS_Sequence_Generation]] (PT-RS 시퀀스 생성 시 DMRS 참조)
- [[PDSCH_PTRS_Generation]] depends_on [[PDSCH_Resource_Mapping]] (PT-RS가 매핑될 자원 블록 범위 결정)

## 관련 개념
- [[PDSCH]] (depends_on)
- [[DMRS]] (depends_on)
- [[CSI_RS]] (depends_on)
- [[PDCCH]] (depends_on)
- [[SS_PBCH_Block]] (depends_on)

## 스펙 근거
- TS 38.211 §7.4.1.2.1 (Sequence generation)
- TS 38.211 §7.4.1.2.2 (Mapping to physical resources)
- TS 38.214 §4.1 (Transmission power)
- TS 38.214 §5.1.4 (Resource element availability)
- TS 38.214 §5.1.6.3 (PT-RS port association)

## 소스
- 3GPP TS 38.211 V18.0.0 (2023-12) "NR; Physical channels and modulation"