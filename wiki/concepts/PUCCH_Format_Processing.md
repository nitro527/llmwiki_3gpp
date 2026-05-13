# PUCCH_Format_Processing

## 정의
[[PUCCH]]를 통해 상향링크 제어 정보([[UCI]])를 전송할 때, 전송 심볼 수와 UCI 비트 수에 따라 결정되는 물리 계층 전송 포맷(Format 0~4) 및 그에 따른 신호 처리 절차를 의미한다.

## 요약
[[PUCCH]] 포맷은 전송 심볼 길이와 UCI 비트 수에 따라 0에서 4까지 분류된다. 각 포맷은 고유한 변조 방식, [[DMRS]] 매핑, 그리고 자원 할당 규칙을 가지며, 상위 계층 설정 및 [[DCI]]를 통해 동적으로 제어된다.

## 상세 설명
[[PUCCH]] 포맷 선택은 전송 심볼 수와 UCI 비트 수에 따라 다음과 같이 결정된다.

- [[PUCCH]] Format 0: 1~2 심볼 전송, 1~2 비트의 [[HARQ-ACK]] 또는 [[SR]] 전송 시 사용.
- [[PUCCH]] Format 1: 4심볼 이상 전송, 1~2 비트의 [[HARQ-ACK]] 또는 [[SR]] 전송 시 사용.
- [[PUCCH]] Format 2: 1~2 심볼 전송, 2비트 초과의 [[UCI]] 전송 시 사용.
- [[PUCCH]] Format 3: 4심볼 이상 전송, 2비트 초과의 [[UCI]] 전송 시 사용. 직교 커버 코드([[OCC]])를 포함하지 않거나 interlace 기반 전송 시 사용.
- [[PUCCH]] Format 4: 4심볼 이상 전송, 2비트 초과의 [[UCI]] 전송 시 사용. [[OCC]]를 포함하는 경우 사용.

Format 3 및 4의 경우, 추가적인 [[DMRS]] 심볼 설정이 가능하며, 변조 방식은 기본적으로 QPSK를 사용하나, 상위 계층 파라미터 pi2BPSK 설정 시 π/2-BPSK를 적용할 수 있다.

공간적 설정([[PUCCH_Spatial_Setting]])은 [[TCI_State]], [[PUCCH_SpatialRelationInfo]], 또는 [[SRS]] 자원 인덱스를 통해 결정된다. 빔 대응(beam correspondence)이 지원되는 경우, UE는 설정된 공간적 관계 정보를 바탕으로 상향링크 빔을 결정한다.

## 인과 관계
- [[PUCCH_Format_Processing]] depends_on [[PUCCH_Sequence_Generation]] (UCI 전송을 위한 시퀀스 생성 전제)
- [[PUCCH_Format_Processing]] depends_on [[PUCCH_DMRS_Generation]] (제어 채널 복조를 위한 참조 신호 생성)
- [[PUCCH_Format_Processing]] depends_on [[PUCCH_Spatial_Setting]] (전송을 위한 공간적 필터 결정)
- [[PUCCH_Format_Processing]] triggers [[PUCCH_Power_Control]] (전송 포맷에 따른 전력 제어 수행)

## 관련 개념
- [[PUCCH]] (part_of)
- [[UCI]] (affects)
- [[DMRS]] (part_of)
- [[HARQ_ACK_Reporting]] (depends_on)
- [[SR_Reporting]] (depends_on)
- [[PUCCH_Spatial_Setting]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.2.3 (PUCCH format 0)
- TS 38.211 §6.3.2.4 (PUCCH format 1)
- TS 38.211 §6.3.2.5 (PUCCH format 2)
- TS 38.211 §6.3.2.6 (PUCCH formats 3 and 4)
- TS 38.213 §9.2.2 (PUCCH Formats for UCI transmission)

## 소스
- 3GPP TS 38.211 V17.0.0 (Physical channels and modulation)
- 3GPP TS 38.213 V17.0.0 (Physical layer procedures for control)