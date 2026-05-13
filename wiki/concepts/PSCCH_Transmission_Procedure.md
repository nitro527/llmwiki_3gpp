# PSCCH_Transmission_Procedure

## 정의
[[PSCCH]] 전송 절차는 사이드링크 통신에서 [[SCI]]를 전송하여 [[PSSCH]] 또는 [[SL_PRS]]의 자원 할당 및 제어 정보를 수신 UE에게 전달하는 물리 계층 동작을 의미한다.

## 요약
PSCCH 전송은 일반적인 사이드링크 자원 풀과 전용 [[SL_PRS]] 자원 풀에서 각각 다른 [[SCI_Format_Mapping]]을 사용하여 수행된다. UE는 상위 계층으로부터 제공받은 자원 할당 모드(모드 1 또는 모드 2)에 따라 시간 및 주파수 자원을 결정하며, 공유 스펙트럼 채널 접속 환경에서는 설정된 전송 구조에 따라 자원을 매핑한다.

## 상세 설명
PSCCH 전송 절차는 크게 일반 자원 풀에서의 동작과 전용 SL PRS 자원 풀에서의 동작으로 나뉜다.

1. 일반 자원 풀에서의 PSCCH 전송 (TS 38.213 §16.4)
- 시간 자원: sl-TimeResourcePSCCH에 의해 제공된 심볼 수만큼 할당되며, [[PSFCH]] 심볼 유무 및 SL-BWP 설정에 따라 시작 심볼이 결정된다.
- 주파수 자원: sl-FreqResourcePSCCH에 의해 제공된 PRB 수만큼 할당되며, 연관된 PSSCH의 최하위 서브채널 인덱스 및 RB-set 인덱스를 기준으로 시작한다.
- 공유 스펙트럼 동작: sl-TransmissionStructureForPSCCHandPSSCH 설정에 따라 interlaceRB 또는 contiguousRB 방식을 따르며, 인트라 셀 가드 밴드와 중첩되는 PRB는 사용하지 않는다.
- 모드 2 동작: 상위 계층이 선택한 자원 세트 중 가장 작은 슬롯 인덱스를 가진 자원을 선택하며, sl-ResourceReservePeriodList를 통해 자원 예약 주기를 설정한다.
- 모드 1 동작: 기지국으로부터 제공된 동적 그랜트 또는 SL 설정 그랜트(Configured Grant)에 따라 M개의 자원 중 특정 자원을 선택하여 전송한다.

2. 전용 SL PRS 자원 풀에서의 PSCCH 전송 (TS 38.213 §16.4A)
- 시간 자원: timeResourcePSCCH-DedicatedSL-PRS-RP에 의해 결정되며, 슬롯 내 SL 전송이 가능한 두 번째 심볼부터 시작한다.
- 주파수 자원: freqResourcePSCCH-DedicatedSL-PRS-RP에 의해 결정되며, 연관된 SL PRS 자원 인덱스에 따라 시작 PRB가 결정된다.
- SCI 포맷: [[SCI_Format_1-B]]를 사용하며, Source ID, Destination ID, Cast type indicator, SL PRS request 등을 포함한다.
- 모드 2 동작: sl-PRS-ResourceReservePeriodList를 사용하여 자원 예약 주기를 설정하고, sl-MaxNumPerReserveDedicatedSL-PRS-RP에 따라 자원을 선택한다.

## 인과 관계
- [[PSCCH]] depends_on [[Sidelink_Resource_Configuration]] (자원 풀 설정 및 파라미터 획득)
- [[PSCCH]] triggers [[PSSCH]] (제어 정보 전달을 통한 데이터 전송 개시)
- [[PSCCH]] triggers [[SL_PRS]] (전용 자원 풀에서의 측위 참조 신호 전송 개시)
- [[PSCCH]] implements [[SCI_Format_Mapping]] (제어 정보의 비트 필드 매핑)

## 관련 개념
- [[PSSCH]] (triggers)
- [[SL_PRS]] (triggers)
- [[Sidelink_Resource_Configuration]] (depends_on)
- [[SCI_Format_Mapping]] (implements)
- [[PSFCH]] (depends_on)

## 스펙 근거
- TS 38.213 §16.4: UE procedure for transmitting PSCCH
- TS 38.213 §16.4A: UE procedure for transmitting PSCCH in dedicated SL PRS resource pool
- TS 38.214: Sidelink resource allocation mode 1/2 및 자원 매핑 상세
- TS 38.321: 상위 계층의 자원 선택 및 예약 주기 제공 절차

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)