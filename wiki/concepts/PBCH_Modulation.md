# PBCH_Modulation

## 정의
[[PBCH]] 데이터의 전송을 위해 수행되는 변조 방식으로, [[QPSK]]를 사용하는 절차를 의미합니다.

## 요약
[[PBCH]]는 시스템 정보의 핵심을 전달하는 물리 채널로서, 신뢰성 있는 전송을 위해 [[QPSK]] 변조 방식을 고정적으로 사용합니다. 이는 모든 [[UE]]가 초기 접속 과정에서 필수적으로 지원해야 하는 기능입니다.

## 상세 설명
[[PBCH]]를 통해 전송되는 비트 시퀀스는 [[Modulation_Mapper]]를 거쳐 복소 심볼로 변환됩니다. [[TS 38.211]] §7.3.3.2에 명시된 바와 같이, [[PBCH]]는 항상 [[QPSK]] 변조를 적용합니다. 

이 과정에서 입력된 비트들은 [[QPSK]] 성상도(constellation)에 따라 매핑되며, 이는 [[SS_PBCH_Block]] 내에서 전송되는 다른 신호들과 함께 물리 자원 그리드에 배치될 준비를 마칩니다. [[QPSK]]는 2비트를 하나의 심볼로 매핑하여 주파수 효율성과 강인한 수신 성능 사이의 균형을 맞춥니다.

## 인과 관계
- [[PBCH_Scrambling]] (depends_on): 스크램블링된 비트 시퀀스가 [[PBCH_Modulation]]의 입력으로 사용됩니다.
- [[Modulation_Mapper]] (part_of): [[PBCH_Modulation]]은 [[Modulation_Mapper]]의 구체적인 구현 사례 중 하나입니다.
- [[SS_PBCH_Block_Mapping]] (triggers): 변조된 심볼은 이후 [[SS_PBCH_Block_Mapping]] 과정을 통해 물리 자원에 매핑됩니다.

## 관련 개념
- [[PBCH]] (part_of)
- [[QPSK]] (similar_to)
- [[Modulation_Mapper]] (part_of)

## 스펙 근거
- [[TS 38.211]] §7.3.3.2: "For the PBCH, QPSK modulation shall be used."

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03), "Physical channels and modulation"