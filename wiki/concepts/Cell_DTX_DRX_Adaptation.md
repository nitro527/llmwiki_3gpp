# Cell_DTX_DRX_Adaptation

## 정의
[[Cell_DTX_DRX_Adaptation]]은 [[PDCCH]]를 통해 전송되는 [[DCI]] format 2_9를 사용하여 서빙 셀의 [[DTX]] 및 [[DRX]] 동작을 동적으로 활성화하거나 비활성화하고, PCell에 대한 NES-mode를 제어하는 L1 절차를 의미한다.

## 요약
[[UE]]는 상위 계층 설정에 따라 [[DCI]] format 2_9를 모니터링하며, 이를 통해 특정 서빙 셀의 [[DTX]]/[[DRX]] 상태를 변경하거나 NES-mode를 설정한다. 이 동작은 [[Active_Time]] 동안 수행되며, 설정된 타이밍 오프셋에 따라 새로운 동작 모드가 적용된다.

## 상세 설명
[[UE]]가 서빙 셀에 대해 [[DTX]] 또는 [[DRX]] 동작을 수행하도록 설정된 경우, [[DCI]] format 2_9를 수신하여 다음과 같은 제어를 수행한다.

1. DCI format 2_9 구성:
   - [[UE]]는 Type3-PDCCH CSS set을 통해 [[DCI]] format 2_9를 모니터링한다.
   - positionInDCI-cellDTRX 파라미터를 통해 [[DTX]]/[[DRX]] 표시 필드와 NES-mode 표시 필드의 위치를 확인한다.

2. DTX/DRX 표시 필드:
   - [[DTX]]와 [[DRX]]가 모두 설정된 경우 2비트를 사용하며, 첫 번째 비트는 [[DTX]], 두 번째 비트는 [[DRX]]를 나타낸다.
   - 하나만 설정된 경우 1비트를 사용하여 해당 동작을 나타낸다.
   - 비트 값이 '0'이면 비활성화, '1'이면 활성화를 의미한다.
   - SUL carrier가 설정된 경우, [[DRX]] 활성화/비활성화는 UL carrier와 SUL carrier 모두에 적용된다.

3. NES-mode 표시 필드:
   - nesEvent가 설정된 경우 1비트를 사용하여 NES-specific CHO 실행 조건을 제어한다.
   - '0'은 비활성화, '1'은 활성화를 의미한다.

4. 적용 타이밍:
   - [[cellSpecificKoffset]]이 제공되지 않은 경우: [[DCI]]를 수신한 슬롯 이후, 서빙 셀의 활성 BWP에서 해당 동작이 시작되는 첫 번째 슬롯부터 적용된다.
   - [[cellSpecificKoffset]]이 제공된 경우: [[DTX]]는 활성 DL BWP의 슬롯부터, [[DRX]]는 활성 UL BWP의 슬롯부터 적용되며, 이때 Table 11.5-1에 정의된 최소 시간 간격과 [[cellSpecificKoffset]]이 고려된다.

## 인과 관계
- [[DCI_Field_Mapping]] depends_on [[Cell_DTX_DRX_Adaptation]] (DCI format 2_9 필드 해석을 위한 매핑 정보 제공)
- [[PDCCH_Search_Space_Configuration]] depends_on [[Cell_DTX_DRX_Adaptation]] (Type3-PDCCH CSS set 설정 필요)
- [[Cell_DTX_DRX_Adaptation]] affects [[Bandwidth_Part_Operation]] (BWP 내 슬롯 동작 모드 변경)

## 관련 개념
- [[PDCCH]] (depends_on)
- [[DCI]] (depends_on)
- [[DRX]] (affects)
- [[Bandwidth_Part_Operation]] (affects)

## 스펙 근거
- TS 38.213 §11.5: [[DTX]]/[[DRX]] 적응을 위한 [[DCI]] format 2_9 동작 및 타이밍 정의
- TS 38.321: [[DTX]]/[[DRX]] 동작 및 [[Active_Time]] 정의
- TS 38.331: NES-specific CHO 실행 조건 정의

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §11.5