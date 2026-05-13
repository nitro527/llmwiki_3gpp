# CSI_CQI_Determination

## 정의
[[CSI_CQI_Determination]]은 [[UE]]가 하향링크 채널 품질을 평가하여 기지국에 보고하기 위한 CQI(Channel Quality Indicator) 인덱스를 결정하는 절차를 의미합니다.

## 요약
[[UE]]는 CSI reference resource 내에서 특정 변조 방식, 타겟 코드 레이트, 전송 블록 사이즈의 조합을 사용하여 [[PDSCH]]를 수신할 때, 정해진 블록 오류 확률(BLER)을 만족하는 가장 높은 CQI 인덱스를 산출합니다. 이 과정에서 채널 및 간섭 측정의 시간적 제한 조건이 적용될 수 있습니다.

## 상세 설명
[[UE]]는 상향링크 슬롯 n에서 보고할 각 CQI 값에 대해 다음 조건을 만족하는 가장 높은 CQI 인덱스를 도출합니다.

1. **성능 조건**: [[PDSCH]] 전송 블록이 CSI reference resource 내에서 수신될 때, 전송 블록 오류 확률이 다음을 초과하지 않아야 합니다.
   - 0.1: cqi-Table이 'table1', 'table2', 또는 'table4-r17'로 설정된 경우
   - 0.00001: cqi-Table이 'table3'으로 설정된 경우

2. **측정 제한**:
   - timeRestrictionForChannelMeasurements가 "notConfigured"인 경우, [[UE]]는 CSI reference resource 이전의 [[CSI_RS]]를 기반으로 채널을 측정합니다.
   - "Configured"인 경우, [[UE]]는 셀 DTX가 활성화된 경우 해당 활성 기간 내의 가장 최근 [[CSI_RS]]를 사용합니다.
   - 간섭 측정 역시 timeRestrictionForInterferenceMeasurements 설정에 따라 [[CSI_IM]] 또는 간섭 측정용 [[CSI_RS]]를 사용하여 동일한 시간적 제한을 적용합니다.

3. **CQI 인덱스 매핑**:
   - cqi-BitsPerSubband가 설정되지 않은 경우, 2비트 서브밴드 차분 CQI를 사용하여 wideband CQI와의 오프셋을 보고합니다.
   - cqi-BitsPerSubband가 설정된 경우, 각 서브밴드에 대해 4비트 CQI 인덱스를 직접 보고합니다.

4. **변조 및 TBS 결정**:
   - CQI 인덱스는 [[PDSCH]] 전송을 위한 변조 방식과 전송 블록 사이즈(TBS) 조합에 대응합니다.
   - 유효 채널 코드 레이트가 CQI 인덱스에서 지시하는 코드 레이트에 가장 근접한 조합을 선택하며, 동일한 근접도를 가진 경우 가장 작은 TBS를 선택합니다.

## 인과 관계
- [[CSI_Reporting_Procedure]] depends_on [[CSI_CQI_Determination]] (CQI 보고를 위한 인덱스 산출 필수)
- [[CSI_CQI_Determination]] depends_on [[CSI_RS]] (채널 측정의 기준 신호로 사용)
- [[CSI_CQI_Determination]] depends_on [[CSI_IM]] (간섭 측정의 기준 신호로 사용)
- [[CSI_CQI_Determination]] depends_on [[PDSCH]] (CQI 산출을 위한 가상의 전송 블록 수신 모델)

## 관련 개념
- [[CSI_Reporting_Procedure]] (depends_on)
- [[CSI_RS]] (depends_on)
- [[CSI_IM]] (depends_on)
- [[PDSCH]] (depends_on)

## 스펙 근거
- TS 38.214 §5.2.2.1: CQI 인덱스 정의 및 결정 조건, 측정 제한 파라미터, 서브밴드 CQI 보고 방식, TBS 및 변조 방식 매핑 규칙 명시.

## 소스
- 3GPP TS 38.214 v19.0.0 (Release 19) §5.2.2.1