# PRACH_Resource_Mapping

## 정의
[[PRACH]] 물리 자원 매핑은 생성된 프리앰블 시퀀스를 시간 및 주파수 영역의 물리적 자원 요소(Resource Element, RE)에 할당하는 절차를 의미합니다.

## 요약
[[PRACH]] 전송을 위해 생성된 시퀀스는 TS 38.211 §6.3.3.2에 정의된 규칙에 따라 물리적 자원 그리드에 매핑됩니다. 이 과정에서 시퀀스는 서브캐리어 간격과 주파수 오프셋을 고려하여 특정 시간-주파수 자원에 배치됩니다.

## 상세 설명
[[PRACH]] 시퀀스 생성 후, 해당 시퀀스는 물리적 자원 매핑 과정을 거칩니다. TS 38.211 §6.3.3.2에 따르면, 매핑은 다음의 원칙을 따릅니다.

1. 시퀀스 매핑: 생성된 프리앰블 시퀀스는 정의된 서브캐리어 간격에 따라 주파수 영역의 연속적인 서브캐리어에 매핑됩니다.
2. 자원 할당: 매핑되는 시작 위치는 상위 계층에서 설정된 주파수 도메인 오프셋 파라미터에 의해 결정됩니다.
3. 시간 영역 매핑: [[PRACH]]가 할당된 슬롯 내의 심볼 위치는 설정된 프리앰블 포맷에 따라 결정되며, 해당 심볼 내에서 시퀀스가 전송됩니다.

## 인과 관계
- [[PRACH_Sequence_Generation]] (triggers) [[PRACH_Resource_Mapping]]
- [[PRACH_Resource_Mapping]] (affects) [[Physical_Resource_Grid]]

## 관련 개념
- [[PRACH]] (part_of)
- [[PRACH_Sequence_Generation]] (depends_on)
- [[Physical_Resource_Grid]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.3.2에 따르면, [[PRACH]] 시퀀스는 물리적 자원 요소에 매핑될 때 특정 주파수 오프셋과 서브캐리어 간격을 준수해야 합니다.

## 소스
- 3GPP TS 38.211 V17.x.x (Release 17), "Physical channels and modulation", Section 6.3.3.2