# Interrupted_Transmission_Indication

## 정의
[[Interrupted_Transmission_Indication]]은 네트워크가 [[PDCCH]]를 통해 전송하는 [[DCI]] 포맷 2_1을 사용하여, 특정 시간-주파수 자원에서 [[UE]]의 하향링크 데이터 전송이 중단되었음을 알리는 메커니즘이다.

## 요약
[[UE]]는 [[DownlinkPreemption]]이 설정된 경우 [[INT-RNTI]]를 사용하여 [[DCI]] 포맷 2_1을 모니터링한다. 해당 [[DCI]]를 수신하면, 지시된 자원 내에서 데이터 전송이 발생하지 않는 것으로 간주하여 자원 효율성을 높인다. 이 지시는 [[SS/PBCH_Block_Generation]] 수신에는 적용되지 않는다.

## 상세 설명
[[UE]]는 상위 계층 파라미터인 [[DownlinkPreemption]]을 통해 [[INT-RNTI]]를 할당받고, [[DCI]] 포맷 2_1을 모니터링한다. TS 38.213 §11.2에 따라 다음 정보가 설정된다.

- [[int-ConfigurationPerServingCell]]: 서빙 셀 인덱스 및 [[DCI]] 내 필드 위치 정보
- [[dci-PayloadSize]]: [[DCI]] 포맷 2_1의 페이로드 크기
- [[timeFrequencySet]]: 시간-주파수 자원 지시 단위(Granularity)

[[UE]]가 [[DCI]] 포맷 2_1을 검출하면, 마지막 모니터링 주기 내의 특정 [[PRB]]와 심볼 집합에서 전송이 없음을 가정한다.
- 시간 자원: [[monitoringSlotPeriodicityAndOffset]]에 의해 결정된 마지막 모니터링 주기 내의 심볼들. 단, [[tdd-UL-DL-ConfigurationCommon]]에 의해 상향링크로 설정된 심볼은 제외된다.
- 주파수 자원: 활성 [[DL_BWP]] 내의 [[PRB]] 집합.

[[timeFrequencySet]] 설정에 따른 매핑 방식:
- 'set0': 14비트가 14개의 연속적인 심볼 그룹에 매핑되며, 각 비트가 0이면 전송 존재, 1이면 전송 없음을 의미한다.
- 'set1': 7쌍의 비트가 7개의 심볼 그룹에 매핑되며, 각 쌍의 비트는 [[PRB]]의 부분 집합(첫 번째 절반, 두 번째 절반)에 각각 적용된다.

## 인과 관계
- [[PDCCH]] depends_on [[Interrupted_Transmission_Indication]] (DCI 포맷 2_1 수신을 위한 물리 채널)
- [[PDSCH]] affects [[Interrupted_Transmission_Indication]] (지시된 자원 내 PDSCH 수신 여부 결정)

## 관련 개념
- [[DCI]] (implements)
- [[PDCCH]] (implements)
- [[PRB]] (affects)
- [[DL_BWP]] (affects)
- [[SS/PBCH_Block_Generation]] (affects)

## 스펙 근거
- TS 38.213 §11.2: Interrupted transmission indication 절차 정의
- TS 38.212: DCI 포맷 2_1 구조 정의
- TS 38.214: 자원 할당 및 PDSCH 수신 관련 상세

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) §11.2