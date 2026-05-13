# PSCCH_DMRS_Mapping

## 정의
[[PSCCH_DMRS_Mapping]]은 사이드링크 통신에서 [[PSCCH]] 복조를 위해 생성된 참조 신호 시퀀스를 물리 자원 요소(Resource Element)에 배치하는 절차를 의미한다.

## 요약
[[PSCCH]] 전송을 위한 [[DMRS]]는 특정 안테나 포트와 슬롯 내 OFDM 심볼에 매핑된다. 이 과정에서 시퀀스는 전송 전력 규정을 준수하기 위해 진폭 스케일링 계수가 곱해지며, [[PSCCH]]를 구성하는 자원 요소 내에 배치된다.

## 상세 설명
[[PSCCH]] [[DMRS]]의 물리 자원 매핑은 TS 38.211 §8.4.1.3.2에 따라 다음과 같이 수행된다.

1. 시퀀스 스케일링: 생성된 [[DMRS]] 시퀀스는 TS 38.213에 명시된 전송 전력을 준수하기 위해 진폭 스케일링 계수와 곱해진다.
2. 자원 매핑: 스케일링된 시퀀스는 안테나 포트 p에 대해 슬롯 내 자원 요소 (k, l)에 순차적으로 매핑된다.
3. 매핑 조건:
   - 매핑되는 자원 요소는 [[PSCCH]]를 구성하는 자원 요소 범위 내에 있어야 한다.
   - 기준점은 공통 자원 블록 0(Common Resource Block 0)의 부반송파 0이다.
   - l은 슬롯 내 OFDM 심볼 번호를 나타낸다.
4. 파라미터: 매핑에 사용되는 양은 TS 38.211 Table 8.4.1.3.2-1에 정의되어 있으며, UE는 이를 기반으로 자원을 선택한다.

## 인과 관계
- [[PSCCH_DMRS_Generation]] depends_on [[PSCCH_DMRS_Mapping]] (DMRS 시퀀스 생성 후 자원 매핑 수행)
- [[PSCCH_DMRS_Mapping]] affects [[PSCCH_Transmission_Procedure]] (PSCCH 복조를 위한 참조 신호 위치 결정)

## 관련 개념
- [[PSCCH]] (part_of)
- [[DMRS]] (part_of)
- [[PSCCH_DMRS_Generation]] (depends_on)
- [[PSCCH_Transmission_Procedure]] (affects)

## 스펙 근거
- TS 38.211 §8.4.1.3.2 Mapping to physical resources

## 소스
- 3GPP TS 38.211 V18.0.0 (2023-12) Physical channels and modulation