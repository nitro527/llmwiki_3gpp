# PBCH_Payload_Generation

## 정의
[[PBCH]] 페이로드 생성은 상위 계층으로부터 전달된 전송 블록(Transport Block)에 타이밍 정보 및 시스템 정보를 포함하는 비트들을 결합하여 물리 계층 전송을 위한 최종 페이로드를 구성하는 절차를 의미한다.

## 요약
[[PBCH]] 페이로드는 상위 계층에서 제공하는 정보 비트와 시스템 타이밍을 나타내는 추가 비트들로 구성된다. 이 과정에서 [[SFN]](System Frame Number), 반 프레임(Half-frame) 정보, 그리고 [[SS_PBCH_Block_Generation]] 과정에서 결정된 후보 SS/PBCH 블록 인덱스 정보가 특정 규칙에 따라 매핑된다. 최종적으로 인터리버 패턴을 적용하여 비트 순서를 재배치함으로써 물리 계층 전송 준비를 마친다.

## 상세 설명
[[PBCH]] 페이로드 생성은 상위 계층에서 전달된 $A$ 비트의 전송 블록으로 시작한다. 이때 최하위 정보 비트는 TS 38.321의 규정에 따라 전송 블록의 최상위 비트(MSB)에 매핑된다.

추가적인 타이밍 관련 페이로드 비트 $a_{A}, a_{A+1}, \dots, a_{A+23}$은 다음과 같이 생성된다:
- $a_{A}, a_{A+1}, a_{A+2}, a_{A+3}$: [[SFN]]의 4번째, 3번째, 2번째, 1번째 LSB(Least Significant Bit)
- $a_{A+4}$: 반 프레임(Half-frame) 지시자 비트
- 나머지 비트들은 후보 SS/PBCH 블록 인덱스 및 관련 파라미터에 따라 결정된다. TS 38.213의 Clause 4.1에 정의된 $L_{max}$ 값에 따라 SS/PBCH 블록 인덱스의 MSB 및 추가 비트들이 매핑되며, 일부 비트는 예약(Reserved) 상태로 남겨진다.

최종 페이로드 비트 시퀀스는 인터리버 패턴(Table 7.1.1-1)을 사용하여 재배치된다. 이 과정에서 [[SFN]] 비트, 반 프레임 비트, SS/PBCH 블록 인덱스 비트가 지정된 위치로 분산되어 전송 효율과 수신 성능을 최적화한다.

## 인과 관계
- [[PBCH_Payload_Generation]] depends_on [[SS_PBCH_Block_Generation]] (후보 SS/PBCH 블록 인덱스 정보 사용)
- [[PBCH_Payload_Generation]] triggers [[Channel_Coding]] (생성된 페이로드는 채널 코딩 단계로 전달)
- [[PBCH_Payload_Generation]] part_of [[PBCH]] (PBCH 전송을 위한 필수 구성 단계)

## 관련 개념
- [[SFN]] (affects)
- [[SS_PBCH_Block_Generation]] (depends_on)
- [[Channel_Coding]] (triggers)
- [[PBCH]] (part_of)

## 스펙 근거
- TS 38.212 §7.1.1: PBCH 페이로드 생성 절차 및 비트 매핑 규칙 정의
- TS 38.211 §7.4.3.1: SS/PBCH 블록 인덱스 및 관련 파라미터 정의
- TS 38.213 §4.1: SS/PBCH 블록 후보 및 타이밍 관련 파라미터 정의

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03)
- 3GPP TS 38.211 V18.0.0 (2024-03)
- 3GPP TS 38.213 V18.0.0 (2024-03)