# PUCCH

## 정의
PUCCH는 5G NR 시스템에서 상향링크 제어 정보(UCI, Uplink Control Information)를 기지국으로 전송하기 위해 사용되는 물리 채널입니다.

## 요약
PUCCH는 HARQ-ACK, SR(Scheduling Request), CSI(Channel State Information)와 같은 상향링크 제어 정보를 전송하며, 전송되는 정보의 양과 심볼 길이에 따라 5가지 포맷(Format 0, 1, 2, 3, 4)을 지원합니다. 각 포맷은 특정 자원 할당 및 시퀀스 생성 규칙을 따르며, 전력 제어 및 다중화 절차를 통해 효율적인 상향링크 통신을 수행합니다.

## 상세 설명
TS 38.211 §6.3.2.1에 따라 PUCCH는 다양한 페이로드 크기와 전송 심볼 길이를 수용하기 위해 다중 포맷을 지원합니다.

- 포맷 0: 1~2 심볼의 짧은 전송을 지원하며, 주로 HARQ-ACK 및 SR 전송에 사용됩니다.
- 포맷 1: 4~14 심볼의 긴 전송을 지원하며, HARQ-ACK 및 SR을 전송합니다.
- 포맷 2: 1~2 심볼의 짧은 전송을 지원하며, CSI 및 HARQ-ACK 전송에 사용됩니다.
- 포맷 3 및 4: 4~14 심볼의 긴 전송을 지원하며, 대용량 UCI 전송을 위해 설계되었습니다.

TS 38.211 §6.3.2.2에 따르면, 포맷 0, 1, 3, 4는 시퀀스 기반 전송을 수행하며, 시퀀스 그룹 및 시퀀스 번호는 시퀀스 호핑(Sequence Hopping) 규칙에 따라 결정됩니다. 또한, 순환 이동(Cyclic Shift) 호핑이 적용되어 다중 사용자 간의 직교성을 확보합니다.

TS 38.213 §7.2에 따라, UE는 MCG(Master Cell Group) 및 SCG(Secondary Cell Group) 각각에 대해 독립적인 PUCCH 전력 제어 절차를 수행합니다. PUCCH-SCell이 설정된 경우, Primary PUCCH 그룹과 Secondary PUCCH 그룹에 대해 별도의 전력 제어 및 HARQ-ACK 코드북 결정 절차가 적용됩니다.

## 인과 관계
- [[PUCCH_Sequence_Generation]] depends_on [[PUCCH]] (시퀀스 생성 시 필수)
- [[PUCCH_Format_Processing]] depends_on [[PUCCH]] (포맷별 데이터 처리 필수)
- [[PUCCH_Power_Control]] affects [[PUCCH]] (전송 전력 제어)
- [[PUCCH_DMRS_Generation]] depends_on [[PUCCH]] (복조 참조 신호 생성)
- [[PUCCH_DMRS_Mapping]] depends_on [[PUCCH]] (자원 매핑)
- [[UCI_Multiplexing]] triggers [[PUCCH]] (제어 정보 다중화 시 사용)
- [[HARQ_ACK_Reporting]] depends_on [[PUCCH]] (HARQ-ACK 피드백 전송)
- [[SR_Reporting]] depends_on [[PUCCH]] (스케줄링 요청 전송)
- [[CSI_Reporting_Procedure]] depends_on [[PUCCH]] (채널 상태 정보 보고)
- [[PUCCH_Resource_Selection]] depends_on [[PUCCH]] (자원 할당)

## 관련 개념
- [[PUCCH_Sequence_Generation]] (implements)
- [[PUCCH_Format_Processing]] (implements)
- [[PUCCH_Power_Control]] (affects)
- [[PUCCH_DMRS_Generation]] (part_of)
- [[PUCCH_DMRS_Mapping]] (part_of)
- [[UCI_Multiplexing]] (implements)
- [[HARQ_ACK_Reporting]] (implements)
- [[SR_Reporting]] (implements)
- [[CSI_Reporting_Procedure]] (implements)
- [[PUCCH_Resource_Selection]] (depends_on)

## 스펙 근거
- TS 38.211 §6.3.2.1: PUCCH 포맷 정의 및 주파수 호핑 규칙
- TS 38.211 §6.3.2.2: 시퀀스 생성 및 순환 이동 호핑
- TS 38.212 §4.1: 상향링크 제어 정보 매핑
- TS 38.212 §6.3.1: PUCCH 상의 UCI 절차
- TS 38.213 §7.2: PUCCH 전력 제어 및 셀 그룹 관리 절차

## 소스
- 3GPP TS 38.211 V16.9.0 (Physical channels and modulation)
- 3GPP TS 38.212 V16.9.0 (Multiplexing and channel coding)
- 3GPP TS 38.213 V16.9.0 (Physical layer procedures for control)