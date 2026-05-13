# PSCCH

## 정의
[[PSCCH]]는 5G NR 사이드링크 통신에서 제어 정보를 전달하기 위해 정의된 물리 채널로, [[SCI]]를 전송하여 [[PSSCH]]의 복조 및 디코딩에 필요한 정보를 수신 단말에 제공한다.

## 요약
[[PSCCH]]는 사이드링크 자원 풀 내에서 [[PSSCH]]와 함께 전송되며, 전송 전력은 자원 블록 수와 설정된 전력 제어 파라미터에 의해 결정된다. E-UTRA와 NR 간의 사이드링크 공존 환경에서는 슬롯 간 전력 우선순위 규칙이 적용된다.

## 상세 설명
[[PSCCH]]는 사이드링크 통신에서 제어 정보를 전달하는 물리 채널로, TS 38.211 §8.3.2에 따라 정의된다.

전송 전력 결정:
[[PSCCH]] 전송 전력은 TS 38.213 §16.2.2에 따라 다음과 같이 결정된다.
- 기본 전력 식: P_PSCCH = min(P_CMAX, P_O_PSCCH + 10log10(M_PSCCH) + alpha * PL) [dBm]
- 여기서 M_PSCCH는 [[PSCCH]] 전송을 위한 자원 블록(RB)의 수이며, P_O_PSCCH 및 alpha는 상위 계층에 의해 설정된다.
- 전용 SL PRS 자원 풀에서 전송되는 경우, 해당 슬롯의 SL PRS 전송 전력과 동일하게 설정된다.

공존 환경에서의 전력 제어:
E-UTRA와 NR 사이드링크가 공존하는 환경에서, NR [[PSCCH]]/[[PSSCH]] 전송 슬롯이 E-UTRA 서브프레임과 중첩되는 경우, 시간적으로 앞선 슬롯의 전송 전력은 뒤에 오는 슬롯의 전송 전력보다 크거나 같아야 한다.

## 인과 관계
- [[PSCCH]] depends_on [[Sidelink_Resource_Configuration]] (자원 풀 설정 기반 전송)
- [[PSCCH]] triggers [[PSSCH]] (제어 정보 전달을 통한 데이터 채널 복조 지원)
- [[PSCCH]] depends_on [[Sidelink_Power_Control]] (전송 전력 결정 메커니즘 적용)

## 관련 개념
- [[PSSCH]] (affects)
- [[SCI]] (implements)
- [[Sidelink_Power_Control]] (implements)
- [[Sidelink_Resource_Configuration]] (depends_on)

## 스펙 근거
- TS 38.211 §8.3.2: Physical sidelink control channel 정의
- TS 38.213 §16.2.2: PSCCH 전송 전력 결정 및 공존 환경 규칙

## 소스
- 3GPP TS 38.211 Physical channels and modulation
- 3GPP TS 38.213 Physical layer procedures for control