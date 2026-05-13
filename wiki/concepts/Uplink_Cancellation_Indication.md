# Uplink_Cancellation_Indication

## 정의
[[Uplink_Cancellation_Indication]]은 네트워크가 [[DCI]] 포맷 2_4를 사용하여 특정 서빙 셀의 [[PUSCH]] 또는 [[SRS]] 전송을 동적으로 취소하도록 지시하는 물리 계층 메커니즘입니다.

## 요약
네트워크는 [[CI-RNTI]]로 스크램블된 [[DCI]] 포맷 2_4를 통해 특정 시간-주파수 자원 영역에 대한 취소 정보를 전송합니다. [[UE]]는 이 정보를 수신하면 해당 자원과 겹치는 [[PUSCH]] 또는 [[SRS]] 전송을 즉시 중단해야 합니다. 이는 주로 동적 자원 재할당이나 간섭 제어를 위해 사용됩니다.

## 상세 설명
[[Uplink_Cancellation_Indication]]을 지원하기 위해 [[UE]]는 상위 계층 파라미터인 UplinkCancellation을 설정받아야 합니다.

1. DCI 포맷 2_4 구성:
   - [[UE]]는 [[CI-RNTI]]를 사용하여 [[DCI]] 포맷 2_4를 모니터링합니다.
   - 각 서빙 셀에 대해 시간-주파수 자원 영역(timeFrequencyRegion)이 정의되며, 이는 심볼 그룹과 PRB 그룹으로 나뉩니다.
   - 심볼 그룹은 timeDurationforCI와 timeGranularityforCI에 의해 결정되며, PRB 그룹은 frequencyRegionforCI에 의해 결정됩니다.

2. 취소 절차:
   - [[DCI]] 포맷 2_4의 비트맵은 특정 심볼 그룹과 PRB 그룹의 조합에 대응합니다.
   - 비트 값이 '1'인 경우, 해당 자원 영역과 겹치는 [[PUSCH]] 또는 [[SRS]] 전송을 취소합니다.
   - [[PUSCH]]의 경우, 취소는 해당 비트가 '1'인 가장 이른 심볼부터 시작하여 해당 전송의 모든 심볼을 포함합니다.
   - [[SRS]]의 경우, 비트가 '1'인 그룹에 포함된 심볼들만 취소됩니다.

3. 타이밍 제약:
   - [[DCI]] 포맷 2_4를 수신한 [[PDCCH]]의 마지막 심볼과 취소 대상 전송 사이에는 최소 처리 시간($T_{proc,2}$)이 보장되어야 합니다.
   - [[UE]]는 취소 지시를 받은 후, 해당 자원 영역을 포함하는 새로운 [[DCI]]에 의해 다시 스케줄링되지 않을 것으로 기대합니다.

## 인과 관계
- [[DCI]] 포맷 2_4 (triggers) [[Uplink_Cancellation_Indication]] (취소 지시를 위한 제어 정보 전달)
- [[Uplink_Cancellation_Indication]] (affects) [[PUSCH]] (해당 자원 영역과 겹치는 전송 중단)
- [[Uplink_Cancellation_Indication]] (affects) [[SRS]] (해당 자원 영역과 겹치는 전송 중단)
- [[PDCCH]] (depends_on) [[Uplink_Cancellation_Indication]] (DCI 포맷 2_4 수신을 위한 물리 채널)

## 관련 개념
- [[DCI]] (depends_on)
- [[PUSCH]] (affects)
- [[SRS]] (affects)
- [[PDCCH]] (depends_on)
- [[CI-RNTI]] (depends_on)

## 스펙 근거
- TS 38.213 §11.2A: UplinkCancellation 설정 및 DCI 포맷 2_4 모니터링 절차 정의
- TS 38.213 §11.2A: 취소 대상 자원 결정 및 비트맵 매핑 규칙
- TS 38.213 §11.2A: PUSCH 및 SRS 취소 조건 및 처리 시간 제약

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) §11.2A