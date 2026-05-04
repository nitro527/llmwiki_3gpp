# PBCH

## 정의
[[PBCH]] (Physical Broadcast Channel)는 5G NR 시스템에서 시스템 정보의 일부인 [[MIB]] (Master Information Block)를 전송하기 위해 정의된 하향링크 물리 채널입니다.

## 요약
[[PBCH]]는 [[SS_PBCH_Block]]의 일부로서 초기 접속 절차에서 필수적인 역할을 수행합니다. [[PBCH]] 전송을 위해서는 [[PBCH_Payload_Generation]]을 통해 비트를 생성하고, [[PBCH_Scrambling]]을 거쳐 [[PBCH_Modulation]]을 수행한 뒤, 최종적으로 물리 자원에 매핑됩니다.

## 상세 설명
[[PBCH]]의 처리 과정은 다음과 같습니다:

1. **[[PBCH_Payload_Generation]]**: [[MIB]]를 포함한 페이로드가 생성되며, TS 38.212 §7.1.1에 따라 [[Transport_Block_CRC_Attachment]]가 수행됩니다.
2. **[[Channel_Coding]]**: 생성된 비트 시퀀스는 TS 38.212 §7.1.4에 따라 Polar 코딩을 사용하여 채널 코딩됩니다.
3. **[[Rate_Matching]]**: 채널 코딩된 비트는 TS 38.212 §7.1.5에 정의된 레이트 매칭 과정을 거쳐 물리 채널 자원에 맞게 조정됩니다.
4. **[[PBCH_Scrambling]]**: TS 38.211 §7.3.3.1에 따라 스크램블링 시퀀스가 적용됩니다. 이는 셀 식별자 및 [[SS_PBCH_Block]] 인덱스와 연관된 파라미터를 사용합니다.
5. **[[PBCH_Modulation]]**: TS 38.211 §7.3.3.2에 따라 QPSK 변조가 수행됩니다.
6. **[[Mapping_to_physical_resources]]**: TS 38.211 §7.3.3.3에 따라 [[SS_PBCH_Block]] 내의 특정 시간-주파수 자원 요소(RE)에 매핑됩니다.

## 인과 관계
- [[SS_PBCH_Block]] (part_of) [[PBCH]]
- [[PBCH_Payload_Generation]] (depends_on) [[MIB]]
- [[PBCH_Scrambling]] (affects) [[PBCH_Modulation]]
- [[Channel_Coding]] (affects) [[Rate_Matching]]

## 관련 개념
- [[SS_PBCH_Block]] (part_of)
- [[MIB]] (depends_on)
- [[PBCH_Scrambling]] (part_of)
- [[PBCH_Modulation]] (part_of)
- [[Channel_Coding]] (part_of)
- [[Rate_Matching]] (part_of)

## 스펙 근거
- TS 38.211 §7.3.3: [[PBCH]]의 물리적 특성, 스크램블링, 변조 및 자원 매핑 정의
- TS 38.212 §7.1: [[PBCH]] 페이로드 생성, 스크램블링, CRC 부착, 채널 코딩 및 레이트 매칭 절차

## 소스
- 3GPP TS 38.211 v19.0.0 (Release 19)
- 3GPP TS 38.212 v18.0.0 (Release 18)