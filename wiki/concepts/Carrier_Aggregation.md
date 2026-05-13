# Carrier_Aggregation

## 정의
반송파 집성(Carrier Aggregation)은 다수의 서빙 셀(Serving Cell)을 결합하여 데이터 전송 대역폭을 확장하고 전송 효율을 높이는 기술로, 각 셀 간의 프레임 경계가 정렬되지 않은 경우 슬롯 오프셋을 통해 타이밍을 동기화하는 절차를 포함합니다.

## 요약
반송파 집성은 여러 셀에서의 동시 전송을 지원하며, 각 서빙 셀은 개별적인 물리 계층 파라미터를 가질 수 있습니다. 프레임 경계가 일치하지 않는 셀 간의 집성 시, 상위 계층 파라미터인 ca-SlotOffset을 사용하여 PCell/PSCell과 SCell 간의 슬롯 오프셋을 결정합니다. 이 오프셋은 각 셀의 서브캐리어 간격(Subcarrier Spacing, SCS) 설정에 따라 계산됩니다.

## 상세 설명
반송파 집성 환경에서 프레임 경계가 정렬되지 않은 경우, 슬롯 오프셋 결정은 다음과 같은 규칙을 따릅니다.

1. 슬롯 오프셋 계산 기준:
   - 각 셀의 scs-SpecificCarrierList에 의해 설정된 서브캐리어 간격 중 가장 낮은 SCS 설정을 기준으로 최대값을 산출합니다.

2. 슬롯 오프셋 결정 규칙:
   - 두 셀의 가장 낮은 SCS 설정이 동일한 경우:
     - PCell/PSCell의 Point A 주파수가 SCell의 Point A 주파수보다 낮으면, SCell의 슬롯 0 시작점은 PCell/PSCell의 슬롯 오프셋만큼 지연됩니다.
     - 반대의 경우, PCell/PSCell의 슬롯 0 시작점이 SCell의 슬롯 오프셋만큼 지연됩니다.
   - 두 셀의 가장 낮은 SCS 설정이 다른 경우:
     - 더 낮은 SCS를 가진 셀의 슬롯 0 시작점을 기준으로, 다른 셀의 슬롯 오프셋을 적용합니다.
     - PCell/PSCell의 가장 낮은 SCS 설정이 SCell보다 작거나 같으면, SCell의 슬롯 0 시작점이 PCell/PSCell의 슬롯 오프셋만큼 지연됩니다.
     - 그렇지 않은 경우, PCell/PSCell의 슬롯 0 시작점이 SCell의 슬롯 오프셋만큼 지연됩니다.

## 인과 관계
- [[Frame_Structure]] depends_on [[Carrier_Aggregation]] (프레임 경계 정렬 및 슬롯 오프셋 적용 시)
- [[Carrier_Aggregation]] affects [[SCell_Activation_Deactivation_Timing]] (셀 활성화 시 타이밍 기준 제공)

## 관련 개념
- [[Frame_Structure]] (part_of)
- [[SCell_Activation_Deactivation_Timing]] (affects)

## 스펙 근거
- TS 38.211 §4.5: 반송파 집성 정의 및 프레임 경계 정렬되지 않은 경우의 슬롯 오프셋 결정 규칙 명시

## 소스
- 3GPP TS 38.211 V17.x.x (Release 17) Physical channels and modulation