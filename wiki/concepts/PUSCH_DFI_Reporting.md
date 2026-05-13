# PUSCH_DFI_Reporting

## 정의
[[PUSCH]] 전송에 대한 [[HARQ]]-ACK 정보를 [[DCI]] 포맷 0_1의 DFI(Downlink Feedback Information) 필드를 통해 전달받는 절차를 의미한다.

## 요약
[[UE]]는 [[CS-RNTI]]로 스크램블된 [[PDCCH]]를 통해 DFI 플래그가 설정된 [[DCI_Field_Mapping]]을 수신하여, 이전에 전송한 [[PUSCH]]의 성공 여부를 확인한다. 이 정보는 [[ConfiguredGrantConfig]] 또는 동적 스케줄링된 [[PUSCH]]의 [[HARQ]] 프로세스 상태를 결정하는 데 사용된다.

## 상세 설명
[[UE]]는 특정 서치 스페이스 세트를 모니터링하여 [[CS-RNTI]]로 CRC가 스크램블된 [[DCI]] 포맷 0_1을 검출한다. DFI 플래그 필드 값이 '1'로 설정된 경우, 해당 [[DCI]]는 [[PUSCH]] 전송에 대한 [[HARQ]]-ACK 정보를 포함한다.

1. HARQ-ACK 정보의 범위:
   - [[DCI]]를 수신한 서빙 셀의 모든 [[HARQ]] 프로세스에 대한 전송 블록 정보를 포함한다.
   - [[DCI]]에 [[Carrier_Aggregation]]을 위한 캐리어 지시자 필드가 포함된 경우, 해당 필드가 지시하는 서빙 셀의 정보를 포함한다.

2. 유효성 판단 (cg-minDFI-Delay):
   - [[ConfiguredGrantConfig]]에 의해 설정된 [[PUSCH]]의 경우, [[PDCCH]] 수신의 첫 번째 심볼이 [[PUSCH]] 전송(또는 반복 전송)의 마지막 심볼보다 cg-minDFI-Delay만큼 이후에 위치해야 정보가 유효하다.
   - 동적으로 스케줄링된 [[PUSCH]]의 경우, 단일 슬롯 전송 시 마지막 심볼 이후 cg-minDFI-Delay만큼 이후여야 한다.
   - 다중 슬롯 전송 시, [[HARQ]]-ACK 값이 ACK이면 첫 번째 슬롯의 마지막 심볼 이후, NACK이면 마지막 슬롯의 마지막 심볼 이후에 [[PDCCH]] 수신이 시작되어야 유효하다.

3. 디코딩 결과 해석:
   - [[UE]]는 수신된 [[HARQ]]-ACK 정보가 ACK이면 전송 블록이 성공적으로 디코딩된 것으로 간주하고, NACK이면 실패한 것으로 간주한다.
   - 동일한 BWP 내의 여러 [[ConfiguredGrantConfig]] 간에 서로 다른 cg-minDFI-Delay 값을 설정할 수 없다.

## 인과 관계
- [[PDCCH]] depends_on [[PUSCH_DFI_Reporting]] (DFI 정보 전달을 위한 제어 채널 수신)
- [[PUSCH]] affects [[PUSCH_DFI_Reporting]] (보고 대상이 되는 상향링크 데이터 전송)
- [[HARQ]] depends_on [[PUSCH_DFI_Reporting]] (DFI를 통한 전송 성공 여부 확인 및 재전송 결정)

## 관련 개념
- [[DCI]] (implements)
- [[PUSCH]] (affects)
- [[HARQ]] (depends_on)
- [[ConfiguredGrantConfig]] (depends_on)
- [[CS-RNTI]] (depends_on)

## 스펙 근거
- TS 38.213 §10.5에 따르면, [[UE]]는 [[CS-RNTI]]로 스크램블된 [[DCI]] 포맷 0_1을 통해 [[HARQ]]-ACK 정보를 수신하며, cg-minDFI-Delay 파라미터를 통해 정보의 유효성을 결정한다.

## 소스
- 3GPP TS 38.213 v18.0.0 §10.5