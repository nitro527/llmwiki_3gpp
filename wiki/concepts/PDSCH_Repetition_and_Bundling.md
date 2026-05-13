# PDSCH_Repetition_and_Bundling

## 정의
[[PDSCH]] 반복 전송 및 PRB 번들링은 데이터 전송의 신뢰성을 높이고 채널 추정 성능을 최적화하기 위해 동일한 전송 블록(TB)을 여러 슬롯에 걸쳐 반복하거나, 주파수 도메인에서 인접한 자원 블록들을 하나의 프리코딩 단위로 묶어 처리하는 물리 계층 절차를 의미한다.

## 요약
- PDSCH 반복은 [[pdsch-AggregationFactor]] 또는 [[repetitionNumber]]를 통해 설정되며, 동일한 시간 도메인 자원 할당(SLIV)을 여러 슬롯에 적용하여 전송 신뢰도를 향상시킨다.
- PRB 번들링은 [[Precoding_Resource_Block_Group]] (PRG) 단위를 설정하여 채널 추정 및 프리코딩 입도를 제어하며, 정적 또는 동적 방식으로 구성 가능하다.
- 특정 반복 스킴(TDM, FDM) 설정 시, [[TCI_State]] 매핑을 통해 다중 전송 기회를 효율적으로 관리한다.

## 상세 설명

### PDSCH 반복 전송 (Repetition)
- 시간 도메인 반복: [[pdsch-AggregationFactor]]가 설정된 경우, 동일한 SLIV가 설정된 수만큼의 연속적인 슬롯에 적용된다. 각 반복 전송 시의 [[Redundancy_Version]]은 TS 38.214 §5.1.2.1의 테이블에 따라 결정된다.
- 다중 슬롯 반복: [[repetitionNumber]]가 설정된 경우, 동일한 SLIV가 여러 슬롯에 걸쳐 반복되며, 이는 주로 멀티캐스트 또는 특정 DCI 포맷 기반의 전송에서 사용된다.
- TDM/FDM 기반 반복: [[repetitionScheme]]이 설정된 경우, [[TCI_State]] 매핑을 통해 전송 기회를 분할한다.
    - tdmSchemeA: 지시된 TCI 상태 수에 따라 다중 전송 기회를 생성하며, 각 기회는 동일한 심볼 길이를 가진다.
    - fdmSchemeA/B: 주파수 도메인에서 PRG를 분할하여 서로 다른 TCI 상태를 적용한다. fdmSchemeA는 wideband 설정 시 PRB를 절반으로 나누고, PRG 단위 설정 시 홀수/짝수 PRG를 구분하여 할당한다.

### PRB 번들링 (PRB Bundling)
- 프리코딩 입도: UE는 [[Precoding_Resource_Block_Group]] (PRG) 내에서 동일한 프리코딩이 적용된다고 가정한다. PRG 크기는 {2, 4, wideband} 중 하나로 설정된다.
- 동적 번들링: [[prb-BundlingType]]이 'dynamicBundling'으로 설정된 경우, DCI 내의 'bundling size indicator' 필드를 통해 실시간으로 PRG 크기를 변경할 수 있다.
- 정적 번들링: 'staticBundling' 설정 시, 상위 계층 파라미터 [[bundleSize]]에 의해 고정된 값을 사용한다.
- wideband 설정 시: UE는 비연속적인 PRB 할당을 기대하지 않으며, 할당된 전체 대역폭에 대해 동일한 프리코딩이 적용됨을 가정한다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_Repetition_and_Bundling]] (반복 및 번들링 설정에 따른 물리 자원 매핑 결정)
- [[PDSCH_Repetition_and_Bundling]] affects [[PDSCH_Resource_Mapping]] (반복 전송 및 PRG 단위에 따른 자원 요소 매핑 변경)
- [[PDSCH_Repetition_and_Bundling]] depends_on [[TCI_State_Management]] (반복 스킴에 따른 TCI 상태 매핑 및 적용)
- [[PDSCH_Repetition_and_Bundling]] affects [[DMRS_Resource_Mapping]] (PRG 단위에 따른 DMRS 프리코딩 입도 결정)

## 관련 개념
- [[PDSCH]] (part_of)
- [[TCI_State_Management]] (depends_on)
- [[PDSCH_Resource_Mapping]] (affects)
- [[DMRS_Resource_Mapping]] (affects)
- [[Redundancy_Version]] (depends_on)

## 스펙 근거
- TS 38.214 §5.1.2.1: PDSCH 시간 도메인 자원 할당 및 반복 전송 절차
- TS 38.214 §5.1.2.3: PRB 번들링 및 프리코딩 입도 설정
- TS 38.211 §7.4.1.1.2: PDSCH 매핑 타입 정의

## 소스
- 3GPP TS 38.214 V17.9.0 (Release 17)
- 3GPP TS 38.211 V17.9.0 (Release 17)