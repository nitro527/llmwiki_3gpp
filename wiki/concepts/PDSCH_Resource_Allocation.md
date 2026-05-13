# PDSCH_Resource_Allocation

## 정의
[[PDSCH]]의 시간 및 주파수 도메인 자원을 결정하는 절차로, [[DCI]]를 통해 전달되는 정보를 기반으로 물리적 자원 블록(PRB)과 OFDM 심볼 위치를 할당하는 과정이다.

## 요약
[[PDSCH]] 자원 할당은 시간 도메인에서 [[DCI]] 필드를 통한 테이블 인덱싱(K0, SLIV)으로, 주파수 도메인에서 Type 0 또는 Type 1 할당 방식을 통해 수행된다. 다중 PDSCH 스케줄링 및 반복 전송(Aggregation Factor)을 지원하며, 특정 조건 하에서 최소 스케줄링 오프셋 제한이 적용된다.

## 상세 설명
### 시간 도메인 자원 할당
[[DCI]]의 Time domain resource assignment 필드는 자원 할당 테이블의 행을 지시한다.
- K0: 스케줄링 [[DCI]]가 수신된 슬롯과 [[PDSCH]]가 수신되는 슬롯 간의 오프셋이다.
- SLIV (Start and Length Indicator Value): 시작 심볼 S와 연속된 심볼 길이 L을 결정한다.
  - $L \ge 1$이고 $1 \le L+S \le 14$인 경우, $SLIV = 14(S-1) + L - 1$
  - 그 외의 경우, $SLIV = 14(14-S+1) + 14-L-1$
- 매핑 타입: [[PDSCH]] 매핑 타입 A 또는 B가 정의된다.
- 다중 PDSCH 스케줄링: `pdsch-TimeDomainAllocationListForMultiPDSCH` 설정 시, 단일 [[DCI]]로 여러 [[PDSCH]]를 스케줄링할 수 있으며 각 [[PDSCH]]는 개별 SLIV, 매핑 타입, K0를 가진다.
- 반복 전송: `pdsch-AggregationFactor`가 설정된 경우, 동일한 심볼 할당이 연속된 슬롯에 적용된다.

### 주파수 도메인 자원 할당
- Type 0: 비트맵 기반으로, RIV(Resource Indication Value) 대신 가상 자원 블록(VRB) 그룹을 할당한다.
- Type 1: RIV를 사용하여 시작 PRB와 연속된 PRB 길이를 할당한다.
- [[DCI]] 포맷에 따라 고정되거나, 상위 계층 파라미터 `resourceAllocation`을 통해 동적으로 전환 가능하다.

### 최소 스케줄링 오프셋 제한
`minimumSchedulingOffsetK0`가 설정된 경우, [[DCI]]의 'Minimum applicable scheduling offset indicator' 필드에 따라 K0의 최소값이 제한된다. 이는 [[PDSCH]] 수신 준비 시간을 확보하기 위한 메커니즘이다.

## 인과 관계
- [[DCI]] triggers [[PDSCH_Resource_Allocation]] (자원 할당 정보 제공)
- [[PDSCH_Resource_Allocation]] affects [[PDSCH_Reception_Procedure]] (할당된 자원에 따른 수신 동작 수행)
- [[PDSCH_Resource_Allocation]] depends_on [[Bandwidth_Part_Operation]] (BWP 내에서 자원 할당 수행)
- [[PDSCH_Resource_Allocation]] implements [[Scheduling_Offset_Restriction]] (최소 K0 제한 적용)

## 관련 개념
- [[PDSCH]] (part_of)
- [[DCI]] (affects)
- [[Bandwidth_Part_Operation]] (depends_on)
- [[Scheduling_Offset_Restriction]] (implements)

## 스펙 근거
- TS 38.214 §5.1.2.1: 시간 도메인 자원 할당 및 SLIV, K0 결정 절차
- TS 38.214 §5.1.2.2: 주파수 도메인 자원 할당 Type 0 및 Type 1 정의
- TS 38.214 §5.1.2.1: 최소 스케줄링 오프셋 제한 및 다중 PDSCH 스케줄링 규칙

## 소스
- 3GPP TS 38.214 V17.9.0 (Release 17)