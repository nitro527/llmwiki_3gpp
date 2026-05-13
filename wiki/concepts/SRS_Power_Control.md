# SRS_Power_Control

## 정의
[[SRS]] 전송 시 [[UE]]가 적용해야 하는 송신 전력 결정 절차를 의미하며, 상향링크 대역폭 부분([[Bandwidth_Part_Operation]]) 내에서 설정된 전력 제어 파라미터와 경로 손실 추정치를 기반으로 계산된다.

## 요약
[[SRS]] 전송 전력은 [[UE]]가 서빙 셀의 활성 상향링크 대역폭 부분에서 결정한 선형 전력 값을 기반으로 한다. 이 전력은 [[SRS]] 리소스 내의 포트 수와 설정된 모드(codebook 또는 antennaSwitching)에 따라 각 심볼에서 균등하게 분배된다.

## 상세 설명
[[UE]]는 [[SRS]] 전송을 위해 다음과 같은 전력 분배 규칙을 따른다.

TS 38.213 §7.3에 따라, [[SRS]] 리소스 세트의 용도가 'codebook' 또는 'antennaSwitching'으로 설정되고, 8개 포트를 가진 [[SRS]] 리소스에 대해 nrofSRS-Ports-n8이 'ports8tdm'으로 제공된 경우, [[UE]]는 활성 상향링크 대역폭 부분의 선형 송신 전력 값을 해당 [[SRS]] 리소스의 각 심볼 내 [[SRS]] 포트들에 균등하게 분배한다.

그 외의 경우, [[UE]]는 활성 상향링크 대역폭 부분의 선형 송신 전력 값을 각 심볼 내 [[SRS]] 리소스 세트에 포함된 각 [[SRS]] 리소스의 포트들에 균등하게 분배한다.

전력 제어 상태는 상위 계층에서 제공하는 파라미터와 [[TPC]] 커맨드에 의해 관리되며, 이는 [[Pathloss_Estimation]] 및 폐루프 전력 제어 루프를 통해 최종 송신 전력으로 결정된다.

## 인과 관계
- [[SRS]] depends_on [[SRS_Power_Control]] (전송 전력 결정 필수)
- [[SRS_Power_Control]] depends_on [[Pathloss_Estimation]] (경로 손실 보상값 산출)
- [[SRS_Power_Control]] depends_on [[Bandwidth_Part_Operation]] (활성 상향링크 대역폭 부분 기준 전력 결정)

## 관련 개념
- [[SRS]] (part_of)
- [[Pathloss_Estimation]] (depends_on)
- [[Bandwidth_Part_Operation]] (depends_on)

## 스펙 근거
- TS 38.213 §7.3: [[SRS]] 전송 전력 분배 및 포트별 할당 규칙 정의

## 소스
- 3GPP TS 38.213 v18.0.0 (2024-03)