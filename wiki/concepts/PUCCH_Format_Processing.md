# PUCCH_Format_Processing

## 정의
[[PUCCH]] Format Processing은 상위 계층으로부터 전달된 [[UCI]] 정보를 물리 계층에서 전송하기 위해, 각 포맷(0, 1, 2, 3, 4)별로 정의된 시퀀스 생성, 변조, 확산, 그리고 물리 자원 매핑을 수행하는 일련의 절차를 의미합니다.

## 요약
[[PUCCH]]는 전송되는 정보량과 심볼 길이에 따라 5가지 포맷으로 구분됩니다. [필수(항상)]인 Basic UL control channel 및 Basic CSI feedback을 지원하며, [필수(cap)]로 지정된 다양한 포맷별 심볼 길이 및 주파수 호핑 기능을 통해 효율적인 제어 채널 전송을 수행합니다. 각 포맷은 고유한 처리 과정을 거쳐 [[Physical_Resource_Grid]]에 매핑됩니다.

## 상세 설명
[[PUCCH]] 포맷별 처리 절차는 다음과 같습니다.

* [[PUCCH]] Format 0: 1~2 심볼의 짧은 길이를 가지며, UCI 정보에 따라 시퀀스 순환 이동(cyclic shift)을 결정합니다. TS 38.211 §6.3.2.3에 따라 시퀀스 생성 및 물리 자원 매핑이 수행됩니다.
* [[PUCCH]] Format 1: 4~14 심볼의 긴 길이를 가지며, BPSK 또는 QPSK 변조 후 시간 영역의 직교 커버 코드(OCC)를 사용하여 확산합니다. TS 38.211 §6.3.2.4에 따라 시퀀스 변조 및 자원 매핑이 정의됩니다.
* [[PUCCH]] Format 2: 1~2 심볼의 짧은 길이를 가지며, [[Scrambling]], [[Modulation_Mapper]], 확산 과정을 거칩니다. TS 38.211 §6.3.2.5에 따라 처리됩니다.
* [[PUCCH]] Format 3 및 4: 4~14 심볼의 긴 길이를 가지며, [[Scrambling]], 변조, 블록 단위 확산(block-wise spreading), 그리고 [[PUSCH_Transform_Precoding]]과 유사한 DFT 기반 프리코딩을 수행합니다. Format 4는 추가적으로 직교 확산 코드를 사용합니다. TS 38.211 §6.3.2.6에 상세히 기술되어 있습니다.

## 인과 관계
* [[UCI_Bit_Sequence_Generation]] (triggers) [[PUCCH_Format_Processing]]
* [[PUCCH_Format_Processing]] (affects) [[Physical_Resource_Grid]]
* [[PUCCH_Resource_Determination]] (depends_on) [[PUCCH_Format_Processing]]

## 관련 개념
* [[PUCCH]] (part_of)
* [[UCI]] (depends_on)
* [[DMRS_Generation_Mapping]] (part_of)
* [[PUCCH_Frequency_Hopping]] (affects)
* [[PUCCH_Resource_Sets]] (depends_on)
* [[PUCCH_Repetition]] (affects)
* [[PUCCH_Sequence_Hopping]] (affects)
* [[Timing_Advance_Adjustment]] (affects)
* [[UCI_PUCCH_Multiplexing]] (affects)

## 스펙 근거
* TS 38.211 §6.3.2.3: PUCCH format 0 시퀀스 생성 및 자원 매핑
* TS 38.211 §6.3.2.4: PUCCH format 1 시퀀스 변조 및 자원 매핑
* TS 38.211 §6.3.2.5: PUCCH format 2 스크램블링, 변조, 확산 및 자원 매핑
* TS 38.211 §6.3.2.6: PUCCH formats 3, 4 스크램블링, 변조, 블록 확산, 프리코딩 및 자원 매핑
* TS 38.213 §9.2.2: UCI 전송을 위한 PUCCH 포맷 절차
* TS 38.213 §9.2.3: HARQ-ACK 보고 절차
* TS 38.213 §9.2.5.1: HARQ-ACK, CSI, SR 다중화 절차

## 소스
* 3GPP TS 38.211 V16.9.0 (2022-03)
* 3GPP TS 38.213 V16.9.0 (2022-03)

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/PUCCH_Format_Processing.md
- concepts/PUCCH_Repetition.md
- concepts/PUCCH_Sequence_Hopping.md
- concepts/Timing_Advance_Adjustment.md
- concepts/UCI_PUCCH_Multiplexing.md