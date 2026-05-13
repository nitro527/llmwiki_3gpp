# PUSCH_UTO_UCI_Reporting

## 정의
UTO-UCI(Uplink Transmission Opportunity Uplink Control Information) 보고는 [[PUSCH]]의 [[PUSCH_Configured_Grant_Operation]] 환경에서 UE가 향후 발생할 CG-PUSCH 전송 기회(TO, Transmission Occasion)의 사용 여부를 gNB에 알리기 위해 수행하는 UCI 보고 절차를 의미한다.

## 요약
UE는 설정된 CG-PUSCH 구성 내에서 nrofBitsInUTO-UCI 파라미터가 제공될 경우, 각 CG-PUSCH 전송 시 비트맵 형태의 UTO-UCI를 다중화하여 보고한다. 이 비트맵은 시간 순서대로 정렬된 이후의 CG-PUSCH TO들에 대한 전송 가능 여부를 나타내며, 특정 TO에 대해 '1'로 보고된 경우 해당 TO에서는 전송을 수행하지 않는다.

## 상세 설명
UE는 gNB로부터 configuredGrantConfig 내에 nrofBitsInUTO-UCI 값을 할당받으면, 해당 CG-PUSCH 구성의 각 전송 시 UTO-UCI를 포함한다. UTO-UCI는 비트맵 형태로 구성되며, 각 비트는 시작 시간 기준 오름차순으로 정렬된 이후의 CG-PUSCH TO들과 일대일로 매핑된다.

비트맵의 각 비트 값에 따른 동작은 다음과 같다:
- '0': UE가 해당 CG-PUSCH TO에서 전송을 수행할 수 있음을 의미한다.
- '1': UE가 해당 CG-PUSCH TO에서 전송을 수행하지 않음을 의미한다.

비쌍방향(unpaired) 스펙트럼 동작의 경우, 비트맵 매핑 대상이 되는 CG-PUSCH TO에서 유효하지 않은 TO는 제외된다. 유효하지 않은 TO는 다음의 경우를 포함한다:
- tdd-UL-DL-ConfigurationCommon 또는 tdd-UL-DL-ConfigurationDedicated에 의해 지시된 DL 심볼과 충돌하는 경우
- ssb-PositionsInBurst에 의해 제공된 SS/PBCH 블록 인덱스의 심볼과 충돌하는 경우

UE가 특정 CG-PUSCH TO에 대해 UTO-UCI를 통해 '1'을 보고한 경우, 해당 TO에 대해서는 실제 전송을 수행하지 않으며, 이후의 CG-PUSCH 전송 시에도 해당 TO에 대해 지속적으로 '1'을 보고하여 상태를 유지해야 한다.

## 인과 관계
- [[PUSCH_Configured_Grant_Operation]] depends_on [[PUSCH_UTO_UCI_Reporting]] (CG-PUSCH 전송 기회 관리 및 보고 절차)
- [[UCI_Multiplexing]] implements [[PUSCH_UTO_UCI_Reporting]] (UTO-UCI 비트맵의 PUSCH 다중화)

## 관련 개념
- [[PUSCH]] (part_of)
- [[PUSCH_Configured_Grant_Operation]] (depends_on)
- [[UCI_Multiplexing]] (implements)

## 스펙 근거
- TS 38.213 §9.3.1에 따르면, UE는 nrofBitsInUTO-UCI가 제공될 경우 CG-PUSCH 전송 시 UTO-UCI를 다중화한다.
- TS 38.213 §9.3.1에 따르면, UTO-UCI 비트맵은 이후의 CG-PUSCH TO들과 일대일로 매핑되며, 비트 값 '1'은 해당 TO에서의 전송 생략을 의미한다.
- TS 38.213 §9.3.1에 따르면, 비쌍방향 스펙트럼 동작 시 DL 심볼 또는 SS/PBCH 블록과 충돌하는 TO는 UTO-UCI 매핑 대상에서 제외된다.

## 소스
- 3GPP TS 38.213 v18.0.0 §9.3.1