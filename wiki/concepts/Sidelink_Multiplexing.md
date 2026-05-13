# Sidelink_Multiplexing

## 정의
Sidelink_Multiplexing은 SL-SCH(Sidelink Shared Channel)을 통해 전송되는 데이터 비트와 2nd-stage SCI(Sidelink Control Information) 비트를 하나의 전송 블록으로 결합하여 PSSCH(Physical Sidelink Shared Channel)에 매핑하기 위한 비트 수준의 다중화 절차를 의미한다.

## 요약
Sidelink_Multiplexing은 SL-SCH의 부호화된 비트와 2nd-stage SCI의 부호화된 비트를 결합하여 총 전송 비트 수 G를 구성한다. 이 과정에서 2nd-stage SCI는 데이터와 함께 PSSCH 자원에 매핑되며, 전송 계층(layer) 수에 따라 비트 인터리빙 및 다중화 알고리즘이 적용된다.

## 상세 설명
TS 38.212 §8.2.1에 따라 SL-SCH의 부호화된 비트 시퀀스와 2nd-stage SCI의 부호화된 비트 시퀀스를 다중화하는 절차는 다음과 같다.

1. 변수 정의:
   - SL-SCH의 부호화된 비트 시퀀스를 f로 정의한다.
   - 2nd-stage SCI의 부호화된 비트 시퀀스를 b로 정의한다.
   - 다중화된 비트 시퀀스를 g로 정의하며, G는 총 전송 비트 수이다.
   - SL-SCH가 매핑되는 계층(layer) 수를 M_layer로 정의한다.

2. 다중화 알고리즘:
   - M_layer = 1인 경우:
     - 2nd-stage SCI의 변조 차수(modulation order)를 Q_m_SCI로 정의한다.
     - 2nd-stage SCI 비트가 데이터 비트와 교차하여 배치되도록 루프를 수행하며, 특정 조건에 따라 비트를 할당한다.
   - M_layer > 1인 경우:
     - 다중화된 비트 시퀀스를 생성하기 위해 계층별로 비트를 분배한다.
     - 각 계층에 대해 2nd-stage SCI 비트를 배치하고, 데이터 비트를 채우며, 필요 시 placeholder 비트를 삽입하여 자원을 정렬한다.

3. PSSCH 매핑:
   - TS 38.212 §8.4.5에 따라, 위 절차를 통해 생성된 2nd-stage SCI 비트는 PSSCH의 물리 자원 요소(Resource Element)에 매핑된다.

## 인과 관계
- [[PSSCH]] depends_on [[Sidelink_Multiplexing]] (PSSCH 전송을 위한 데이터 및 제어 정보 결합)
- [[Sidelink_Multiplexing]] implements [[PSSCH_Resource_Mapping]] (다중화된 비트의 물리 자원 매핑 수행)

## 관련 개념
- [[SL-SCH]] (depends_on)
- [[PSSCH]] (affects)
- [[2nd-stage_SCI]] (part_of)
- [[PSSCH_Resource_Mapping]] (implements)

## 스펙 근거
- TS 38.212 §8.2.1: Data and control multiplexing 절차 정의
- TS 38.212 §8.4.5: Multiplexing of coded 2nd-stage SCI bits to PSSCH 절차 정의

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03) "Multiplexing and channel coding"