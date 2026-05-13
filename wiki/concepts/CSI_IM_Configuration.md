# CSI_IM_Configuration

## 정의
CSI-IM(Channel State Information – Interference Measurement)은 UE가 하향링크 채널 품질을 정확하게 측정하기 위해 간섭 신호를 측정하도록 설정된 자원 구성입니다.

## 요약
CSI-IM은 네트워크가 UE에게 간섭 환경을 측정할 수 있는 특정 자원 요소(Resource Element)를 할당하는 메커니즘입니다. UE는 상위 계층 파라미터인 CSI-IM-ResourceSet을 통해 하나 이상의 자원 집합을 설정받으며, 각 자원은 시간 및 주파수 도메인에서의 특정 패턴에 따라 매핑됩니다.

## 상세 설명
CSI-IM 자원 설정은 상위 계층 파라미터인 CSI-IM-Resource를 통해 이루어지며, 주요 구성 요소는 다음과 같습니다.

1. 자원 식별 및 위치 설정:
   - csi-IM-ResourceId: 각 CSI-IM 자원 구성을 식별하는 고유 ID입니다.
   - subcarrierLocation-p0/p1: csi-IM-ResourceElementPattern이 'pattern0' 또는 'pattern1'으로 설정된 경우, 슬롯 내에서 CSI-IM 자원이 점유하는 부반송파 위치를 정의합니다.
   - symbolLocation-p0/p1: 동일한 패턴 설정에 따라 슬롯 내에서 CSI-IM 자원이 위치하는 OFDM 심볼 위치를 정의합니다.

2. 주기 및 주파수 점유:
   - periodicityAndOffset: 주기적(Periodic) 또는 반-지속적(Semi-persistent) CSI-IM을 위한 주기와 슬롯 오프셋을 결정합니다.
   - freqBand: CSI-IM이 점유할 주파수 대역을 설정합니다.

3. 자원 요소 매핑:
   - 'pattern0'으로 설정된 경우, UE는 해당 PRB 내에서 4개의 자원 요소(k, l), (k+1, l), (k, l+1), (k+1, l+1)을 간섭 측정 자원으로 간주합니다.
   - 'pattern1'으로 설정된 경우, UE는 (k, l), (k+1, l), (k+2, l), (k+3, l) 위치의 자원 요소를 간섭 측정 자원으로 간주합니다.
   - 여기서 k와 l은 각각 상위 계층 파라미터로 설정된 주파수 도메인 및 시간 도메인 위치를 의미합니다.

## 인과 관계
- [[CSI_Reporting_Procedure]] depends_on [[CSI_IM_Configuration]] (간섭 측정을 통한 채널 품질 보고 전제)
- [[CSI_RS_Generation]] implements [[CSI_IM_Configuration]] (간섭 측정을 위한 자원 요소 할당 및 비워두기 동작)

## 관련 개념
- [[CSI_RS_Generation]] (implements)
- [[CSI_Reporting_Procedure]] (depends_on)

## 스펙 근거
- TS 38.214 §5.2.2.4에 따르면, UE는 상위 계층 파라미터 CSI-IM-ResourceSet을 통해 하나 이상의 CSI-IM 자원 집합을 설정받습니다.
- TS 38.214 §5.2.2.4에 따르면, 'pattern0' 및 'pattern1'에 따른 자원 요소 매핑 규칙이 정의되어 있습니다.

## 소스
- 3GPP TS 38.214 v19.0.0, "Physical layer procedures for data"