# Network_Controlled_Repeater_Operation

## 정의
[[Network_Controlled_Repeater_Operation]]은 기지국(gNB)이 제어 링크를 통해 [[Network_Controlled_Repeater]](NCR)의 동작을 직접 관리하고 최적화하는 무선 통신 기술을 의미합니다.

## 요약
[[Network_Controlled_Repeater]]는 gNB와 UE 사이에서 신호를 증폭하여 전달하는 장치로, gNB로부터 제어 정보를 수신하여 백홀 링크 및 액세스 링크의 전송/수신 타이밍, 빔 관리, 그리고 [[TCI_State]]를 동적으로 제어받습니다.

## 상세 설명
[[Network_Controlled_Repeater_Operation]]은 다음과 같은 핵심 기능을 포함합니다.

1. **제어 링크 및 백홀 링크**: gNB는 NCR에 대한 제어 정보를 전달하기 위해 별도의 제어 링크를 사용합니다. NCR은 gNB로부터 수신된 설정에 따라 백홀 링크(gNB-NCR 간)와 액세스 링크(NCR-UE 간)의 동작을 수행합니다.
2. **빔 관리**: NCR은 gNB의 지시에 따라 특정 빔 방향으로 신호를 송수신하며, 이를 위해 [[TCI_State]]를 활용하여 빔을 설정합니다.
3. **전송/수신 타이밍 제어**: NCR은 gNB로부터 전달받은 타이밍 정보를 바탕으로 신호의 증폭 및 전달 시점을 결정합니다. 이는 기지국과 UE 간의 [[Frame_Structure_Numerology]]를 유지하면서 신호 지연을 최소화하기 위함입니다.
4. **동적 설정**: gNB는 NCR의 동작 모드를 동적으로 변경할 수 있으며, 이를 통해 네트워크 환경 변화에 유연하게 대응합니다.

## 인과 관계
- [[Network_Controlled_Repeater]] (depends_on) [[Network_Controlled_Repeater_Operation]]
- [[TCI_State]] (affects) [[Network_Controlled_Repeater_Operation]]
- [[Frame_Structure_Numerology]] (affects) [[Network_Controlled_Repeater_Operation]]

## 관련 개념
- [[Network_Controlled_Repeater]] (part_of)
- [[TCI_State]] (depends_on)
- [[Frame_Structure_Numerology]] (depends_on)

## 스펙 근거
- TS 38.213 §20에 따르면, [[Network_Controlled_Repeater]]는 gNB에 의해 제어되며, 제어 링크를 통해 수신된 설정에 따라 동작해야 합니다.
- TS 38.213 §20은 NCR의 빔 관리 및 타이밍 제어 절차에 대한 요구사항을 정의합니다.

## 소스
- 3GPP TS 38.213 Release 18 (i80) §20