# CSI_RS

## 정의
[[CSI_RS]]는 5G NR 시스템에서 채널 상태 정보(CSI) 측정, 시간/주파수 추적, 이동성 관리 및 빔 관리를 위해 기지국이 하향링크로 전송하는 참조 신호이다.

## 요약
[[CSI_RS]]는 TS 38.211 §7.4.1.5에 정의된 신호로, 채널 품질 측정, L1-RSRP 및 L1-SINR 계산, RLM(Radio Link Monitoring), RRM(Radio Resource Management) 측정 등 다양한 목적으로 사용된다. 특히 추적용으로 사용되는 TRS(CSI-RS for tracking)와 고속 SCell 활성화를 위한 자원 설정이 포함되며, [[PDCCH]]의 [[CORESET]]과 [[QCL]] 관계를 설정하여 수신 성능을 최적화한다.

## 상세 설명
[[CSI_RS]] 수신 절차는 다음과 같다:

1. **QCL 및 자원 설정**: 
   - [[NZP-CSI-RS-ResourceSet]] 설정에서 `repetition` 파라미터가 'on'으로 설정된 경우, UE는 해당 [[CSI_RS]] 자원과 동일한 심볼에서 [[CORESET]] 모니터링을 수행하지 않는다.
   - 그 외의 경우, [[CSI_RS]]와 [[CORESET]]이 동일한 OFDM 심볼에서 전송되면, UE는 [[CSI_RS]]와 [[CORESET]]의 [[PDCCH]] [[DMRS]]가 'typeD' [[QCL]] 관계에 있다고 가정할 수 있다.
   - [[CORESET]]이 두 개의 TCI state로 활성화된 경우, 첫 번째 TCI state를 [[CSI_RS]]에 대한 기본 [[QCL]] 가정으로 사용한다. 이는 동일 대역 내의 다른 컴포넌트 캐리어 간에도 적용된다.
   - [[CSI_RS]]는 [[CORESET]]의 검색 공간(search space)이 점유하는 OFDM 심볼 내에서 해당 [[CORESET]]과 PRB가 중첩되도록 설정될 수 없다.

2. **DRX 및 DTX 동작**:
   - [[DRX]]가 설정된 경우, [[CSI_RS]] 측정 시점은 [[DRX]] 활성 시간(active time) 또는 `drx-onDurationTimer`가 동작 중인 시간 내에 발생해야 한다.
   - 셀 [[DTX]]가 활성화된 경우, RI(Rank Indicator)를 포함하는 CSI 보고 설정과 관련된 주기적 또는 반-지속적(semi-persistent) [[CSI_RS]]는 [[DTX]] 활성 기간 중에만 수신이 기대된다.

3. **기타 제약**:
   - [[SIB1]]이 전송되는 OFDM 심볼에서 [[SIB1]] 메시지와 중첩되는 PRB를 통해 [[CSI_RS]]를 수신하지 않는다.

## 인과 관계
- [[CSI_RS]] depends_on [[CSI_RS_Generation]] (신호 생성 절차 전제)
- [[CSI_RS]] affects [[CSI_Reporting_Procedure]] (측정 결과 기반 보고 수행)
- [[CSI_RS]] depends_on [[CORESET_Configuration]] (QCL 가정 및 자원 충돌 회피)

## 관련 개념
- [[CSI_RS_Generation]] (implements)
- [[CSI_Reporting_Procedure]] (affects)
- [[CORESET_Configuration]] (depends_on)
- [[QCL]] (implements)
- [[DRX]] (depends_on)

## 스펙 근거
- TS 38.214 §5.1.6.1: CSI-RS reception procedure
- TS 38.211 §7.4.1.5: CSI-RS sequence generation and mapping

## 소스
- 3GPP TS 38.214 v17.9.0 (Release 17)
- 3GPP TS 38.211 v17.9.0 (Release 17)