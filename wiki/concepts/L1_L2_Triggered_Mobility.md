# L1/L2-Triggered Mobility

## 정의
[[L1/L2-Triggered Mobility]] (LTM)은 [[UE]]가 [[RRC]] 시그널링의 개입을 최소화하면서, [[L1]] 및 [[L2]] 계층의 제어 정보를 통해 셀 간 이동성(Cell Switch)을 수행하는 절차를 의미합니다. 특히 [[RACH]] 절차를 생략하거나 최적화하여 핸드오버 지연 시간을 단축하는 RACH-less 핸드오버를 포함합니다.

## 요약
LTM은 고속 이동성 환경이나 빈번한 셀 변경이 필요한 상황에서 핸드오버 중단 시간을 줄이기 위해 설계되었습니다. 주요 메커니즘은 [[Configured Grant]] 또는 [[Dynamic Grant]]를 활용한 [[PUSCH]] 전송을 통해 타겟 셀로의 접속을 즉각적으로 수행하는 것입니다.

## 상세 설명
LTM 절차는 크게 측정 보고, 타겟 셀로의 스위칭, 그리고 데이터 전송 단계로 나뉩니다.

1. **측정 및 보고**: [[UE]]는 [[Intra-frequency]] 또는 [[Inter-frequency]] [[L1]] 측정을 수행하고 이를 네트워크에 보고합니다. 이는 LTM 트리거를 위한 기초 데이터로 사용됩니다.
2. **셀 스위칭**: 네트워크는 [[MAC-CE]] 또는 [[DCI]]를 통해 타겟 셀의 [[TCI]] 상태를 활성화하고, [[UE]]가 타겟 셀로 즉시 이동할 수 있도록 준비시킵니다.
3. **RACH-less 핸드오버**:
   - **Configured Grant PUSCH**: [[UE]]는 사전에 설정된 [[Configured Grant]] 자원을 사용하여 타겟 셀에서 [[PUSCH]] 전송을 수행합니다. 이는 [[RACH]] 절차를 거치지 않고 업링크 동기를 맞추거나 데이터를 전송할 때 사용됩니다.
   - **Dynamic Grant PUSCH**: 네트워크는 [[DCI]]를 통해 동적으로 [[PUSCH]] 자원을 할당하며, [[UE]]는 이를 수신하여 타겟 셀에서 즉시 전송을 시작합니다.

## 인과 관계
- [[L1/L2-Triggered Mobility]] (depends_on) [[Basic initial access channels and procedures]]
- [[L1/L2-Triggered Mobility]] (affects) [[PUSCH]]
- [[L1/L2-Triggered Mobility]] (triggers) [[RACH-less handover]]

## 관련 개념
- [[PUSCH]] (part_of)
- [[RACH]] (similar_to)
- [[TCI]] (depends_on)
- [[MAC-CE]] (affects)
- [[DCI]] (affects)

## 스펙 근거
- [[TS 38.213]] §21: L1/L2-triggered mobility procedures에 대한 전반적인 절차 정의
- [[TS 38.213]] §21.1: RACH-less LTM 셀 스위치에서의 Configured-grant PUSCH 전송 규정
- [[TS 38.213]] §22: RACH-less 핸드오버에서의 PUSCH 전송 절차
- [[TS 38.213]] §22.1: Configured-grant PUSCH 전송 상세
- [[TS 38.213]] §22.2: Dynamic-grant PUSCH 전송 상세

## 소스
- 3GPP TS 38.213 Release 18 (i80)