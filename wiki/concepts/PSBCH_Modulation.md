# PSBCH_Modulation

## 정의
[[PSBCH]] (Physical Sidelink Broadcast Channel) 데이터의 전송을 위해 비트 시퀀스를 복소 심볼로 변환하는 변조 절차를 의미합니다.

## 요약
[[PSBCH]]는 사이드링크 통신에서 시스템 정보를 브로드캐스트하기 위해 사용되는 채널로, TS 38.211 §8.3.3.2에 따라 QPSK 변조 방식을 사용하여 데이터를 심볼로 매핑합니다.

## 상세 설명
[[PSBCH]]의 변조 과정은 다음과 같은 단계로 수행됩니다.
1. 입력된 비트 시퀀스는 [[Modulation_Mapper]]를 통해 복소 심볼로 변환됩니다.
2. [[PSBCH]]에 적용되는 변조 방식은 QPSK로 고정되어 있습니다.
3. 변조된 심볼은 이후 [[PSBCH_Scrambling]] 과정을 거친 비트 시퀀스에 기반하여 생성되며, 최종적으로 물리 자원에 매핑됩니다.

## 인과 관계
- [[PSBCH_Scrambling]] (depends_on): [[PSBCH_Modulation]]은 스크램블링된 비트 시퀀스를 입력으로 받아 변조를 수행합니다.
- [[Modulation_Mapper]] (part_of): [[PSBCH_Modulation]]은 [[Modulation_Mapper]]의 기능을 활용하여 QPSK 변조를 수행합니다.

## 관련 개념
- [[PSBCH]] (part_of)
- [[Modulation_Mapper]] (depends_on)
- [[PSBCH_Scrambling]] (depends_on)

## 스펙 근거
- TS 38.211 §8.3.3.2에 따르면, [[PSBCH]]의 변조는 QPSK를 사용하여 수행되어야 합니다.

## 소스
- 3GPP TS 38.211 V16.9.0 (Release 16) §8.3.3.2