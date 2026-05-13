# PUCCH_DMRS_Mapping

## 정의
[[PUCCH]] 전송 시 채널 추정을 위해 사용되는 [[DMRS]] 시퀀스를 물리 자원 요소(Resource Element, RE)에 배치하는 절차를 의미한다.

## 요약
[[PUCCH]] 포맷에 따라 [[DMRS]] 시퀀스는 지정된 안테나 포트와 시간-주파수 자원 영역에 매핑된다. 전송 전 진폭 스케일링이 수행되며, 각 포맷별로 정의된 규칙에 따라 할당된 자원 블록(Resource Block, RB) 내의 RE에 시퀀스가 배치된다.

## 상세 설명
[[PUCCH]] 전송을 위한 [[DMRS]] 매핑은 각 포맷별로 다음과 같이 수행된다.

1. 공통 절차:
   - 생성된 [[DMRS]] 시퀀스는 [[TS 38.213]]에 명시된 송신 전력을 준수하기 위해 진폭 스케일링 계수와 곱해진다.
   - 시퀀스는 할당된 RB 내의 RE에 순차적으로 매핑된다.

2. [[PUCCH]] 포맷 0 및 1:
   - [[TS 38.211]] §6.4.1.3.1.2에 따라, 시퀀스는 안테나 포트 p에서 슬롯 내의 RE에 매핑된다.
   - 인터레이스(Interlace) 전송의 경우, [[TS 38.213]] §9.2.1에 따라 활성 대역폭 부분(Bandwidth Part, BWP) 내의 각 RB에 대해 매핑 동작이 반복된다.

3. [[PUCCH]] 포맷 2:
   - [[TS 38.211]] §6.4.1.3.2.2에 따라, RE 매핑은 공통 자원 블록 0의 서브캐리어 0을 기준으로 정의된다.
   - 매핑되는 RE는 [[TS 38.213]] §9.2.1에 따라 할당된 RB 범위 내에 위치해야 한다.

4. [[PUCCH]] 포맷 3 및 4:
   - [[TS 38.211]] §6.4.1.3.3.2에 따라, RE 매핑은 할당된 가장 낮은 번호의 RB 내 서브캐리어 0을 기준으로 정의된다.
   - [[DMRS]] 심볼 위치는 슬롯 내 주파수 호핑(Frequency Hopping) 여부 및 추가 [[DMRS]] 설정 여부에 따라 [[TS 38.211]] Table 6.4.1.3.3.2-1에 의해 결정된다.

## 인과 관계
- [[PUCCH_DMRS_Generation]] depends_on [[PUCCH_DMRS_Mapping]] (생성된 시퀀스의 물리적 배치 수행)
- [[PUCCH_DMRS_Mapping]] depends_on [[PUCCH]] (PUCCH 포맷별 자원 할당 규칙 적용)
- [[PUCCH_DMRS_Mapping]] affects [[DMRS]] (물리 자원 요소에 DMRS 시퀀스 배치)

## 관련 개념
- [[PUCCH]] (part_of)
- [[DMRS]] (part_of)
- [[PUCCH_DMRS_Generation]] (depends_on)
- [[Frame_Structure]] (depends_on)

## 스펙 근거
- TS 38.211 §6.4.1.3.1.2 (PUCCH 포맷 0, 1 매핑)
- TS 38.211 §6.4.1.3.2.2 (PUCCH 포맷 2 매핑)
- TS 38.211 §6.4.1.3.3.2 (PUCCH 포맷 3, 4 매핑)
- TS 38.213 §9.2.1 (자원 할당 및 인터레이스 관련)

## 소스
- 3GPP TS 38.211 V18.0.0 (Physical channels and modulation)