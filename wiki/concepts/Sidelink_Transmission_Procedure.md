# Sidelink_Transmission_Procedure

## 정의
사이드링크 전송 절차는 [[UE]]가 [[PSCCH]], [[PSSCH]], 또는 [[SL_PRS_Generation]]을 전송하기 위해 자원을 할당하고, [[SCI_Format_Mapping]]을 통해 제어 정보를 전달하며, 시간 및 주파수 영역에서 물리 자원을 매핑하는 일련의 과정을 의미한다.

## 요약
사이드링크 전송은 모드 1(네트워크 제어)과 모드 2(UE 자율 선택)로 구분된다. 모드 1에서는 [[DCI_Formats_Processing]]을 통해 자원이 할당되며, 모드 2에서는 [[Sidelink_Resource_Selection]]을 통해 자원을 결정한다. 전송되는 데이터와 제어 정보는 [[SCI_Format_Mapping]]에 정의된 필드에 따라 시간 및 주파수 자원이 결정되며, [[SL_PRS_Generation]]의 경우 전용 자원 풀 내에서 별도의 절차를 따른다.

## 상세 설명
사이드링크 전송 절차는 크게 자원 할당 방식과 전송 대상 채널에 따라 다음과 같이 구분된다.

### PSSCH 전송 절차 (SCI format 1-A 기반)
[[PSSCH]] 전송을 위한 시간 및 주파수 자원은 [[PSCCH]]에 포함된 [[SCI_Format_Mapping]]의 'Time resource assignment' 및 'Frequency resource assignment' 필드에 의해 결정된다.
- 시간 자원: 'Time resource assignment'는 TRIV(Time Resource Indicator Value)를 통해 N개의 자원 위치를 논리적 슬롯 오프셋으로 지시한다.
- 주파수 자원: 'Frequency resource assignment'는 FRIV(Frequency Resource Indicator Value)를 통해 시작 서브채널과 할당된 서브채널의 개수를 결정한다.
- 반복 전송: [[Sidelink_Resource_Selection]]에 의해 선택된 그랜트에 따라 동일한 자원 세트가 여러 슬롯에 걸쳐 반복될 수 있으며, 이는 [[SL_RESOURCE_RESELECTION_COUNTER]]에 의해 제어된다.

### SL PRS 전송 절차 (SCI format 1-B 기반)
전용 [[SL_PRS_Generation]] 자원 풀에서의 전송은 [[SCI_Format_Mapping]]의 SCI format 1-B를 사용한다.
- 자원 결정: 첫 번째 [[SL_PRS_Generation]] 자원은 [[PSCCH]] 전송에 사용된 서브채널 인덱스와 동일하게 설정된다.
- 추가 자원: 두 번째 및 세 번째 자원은 'Resource ID indication' 필드(PRIV)를 통해 결정된다.
- 모드 1 지원: [[SL_PRS_Generation]] 전송을 위해 다이내믹 그랜트 및 설정된 그랜트(Configured grant type 1/2)가 지원된다.

### LTE 사이드링크 SPS 활성화
[[DCI_Formats_Processing]]의 DCI format 3_1을 통해 LTE 사이드링크 SPS(Semi-Persistent Scheduling)가 활성화 또는 해제된다. 활성화 시, UE는 지정된 타이밍 오프셋 이후부터 [[PSCCH]] 및 [[PSSCH]] 전송을 시작한다.

## 인과 관계
- [[PSCCH]] depends_on [[SCI_Format_Mapping]] (제어 정보 전달을 위한 포맷 정의)
- [[PSSCH]] depends_on [[Sidelink_Resource_Selection]] (전송을 위한 자원 결정)
- [[SL_PRS_Generation]] depends_on [[SCI_Format_Mapping]] (SCI format 1-B를 통한 자원 지시)
- [[DCI_Formats_Processing]] triggers [[PSCCH]] (모드 1에서 전송 활성화)

## 관련 개념
- [[PSCCH]] (affects)
- [[PSSCH]] (affects)
- [[SL_PRS_Generation]] (affects)
- [[SCI_Format_Mapping]] (implements)
- [[Sidelink_Resource_Selection]] (depends_on)
- [[DCI_Formats_Processing]] (triggers)

## 스펙 근거
- TS 38.213 §16.6: LTE 사이드링크 SPS 활성화 및 전송 타이밍 절차
- TS 38.214 §8.1.5: SCI format 1-A 기반 PSSCH 자원 결정 절차
- TS 38.214 §8.1.5A: 선호/비선호 자원 세트 결정 절차
- TS 38.214 §8.2.4.1: 사이드링크 모드 1에서의 자원 할당
- TS 38.214 §8.2.4.2A: SCI format 1-B 기반 SL PRS 자원 결정 절차

## 소스
- 3GPP TS 38.213 (v18.0.0)
- 3GPP TS 38.214 (v19.0.0)