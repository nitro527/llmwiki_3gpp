# Sidelink_Resource_Conflict

## 정의
[[Sidelink_Resource_Conflict]]는 [[Sidelink]] 통신 환경에서 다수의 [[UE]]가 동일한 자원을 예약하거나 사용하여 발생하는 간섭 및 충돌 상황을 의미하며, 이를 감지하고 [[PSFCH]]를 통해 제어 정보를 교환하여 해결하는 절차를 말합니다.

## 요약
[[Sidelink]] 모드 2에서 [[UE]]는 자원 선택 및 예약 과정에서 발생할 수 있는 충돌을 방지하기 위해 [[PSFCH]]를 활용한 제어 정보 보고 절차를 수행합니다. 이는 [[Inter-UE_coordination]]을 통해 자원 사용 효율을 높이고 데이터 전송의 신뢰성을 확보하는 핵심 메커니즘입니다.

## 상세 설명
[[Sidelink_Resource_Conflict]]를 관리하기 위한 절차는 크게 [[PSFCH]]를 통한 제어 정보의 송신과 수신으로 나뉩니다.

1. **송신 절차 (Transmitting PSFCH with control information)**:
   - [[UE]]는 특정 자원 영역에서 충돌이 예상되거나 [[Inter-UE_coordination]] 정보가 필요한 경우 [[PSFCH]]를 통해 관련 제어 정보를 전송합니다.
   - 전송 시점과 자원은 상위 계층에서 설정된 파라미터와 [[Sidelink]] 자원 풀 구성에 따라 결정됩니다.

2. **수신 절차 (Receiving PSFCH with control information)**:
   - [[UE]]는 주변 [[UE]]로부터 전송된 [[PSFCH]]를 모니터링하여 제어 정보를 획득합니다.
   - 획득한 정보는 자원 재선택(re-selection)이나 예약된 자원의 변경 여부를 판단하는 데 사용됩니다.
   - [[TS_38.213]] §16.3.1에 따라, [[UE]]는 수신된 정보를 바탕으로 자원 충돌 가능성을 평가하고, 필요한 경우 [[Sidelink_Resource_Selection]] 절차를 다시 수행합니다.

## 인과 관계
- [[Sidelink_Resource_Selection]] (triggers) [[Sidelink_Resource_Conflict]] 감지
- [[Sidelink_Resource_Conflict]] (triggers) [[PSFCH]] 기반 제어 정보 보고
- [[PSFCH]] (part_of) [[Sidelink_Resource_Conflict]] 해결 절차

## 관련 개념
- [[Sidelink]] (part_of)
- [[PSFCH]] (part_of)
- [[Inter-UE_coordination]] (similar_to)
- [[Sidelink_Resource_Selection]] (depends_on)

## 스펙 근거
- [[TS_38.213]] §16.3: [[UE]] procedure for reporting and obtaining control information in [[PSFCH]]
- [[TS_38.213]] §16.3.0: [[UE]] procedure for transmitting [[PSFCH]] with control information
- [[TS_38.213]] §16.3.1: [[UE]] procedure for receiving [[PSFCH]] with control information

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18)