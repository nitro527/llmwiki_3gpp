# RedCap_UE_Operation

## 정의
RedCap(Reduced Capability) UE는 5G NR 시스템에서 특정 서비스(예: 웨어러블 기기, 산업용 센서, 영상 감시)를 위해 대역폭, 안테나 수, 처리 능력 등을 최적화하여 비용과 전력 소모를 줄인 단말을 의미한다.

## 요약
RedCap UE는 일반적인 5G NR 단말과 동일한 물리 계층 절차를 따르는 것을 원칙으로 한다. 다만, 하드웨어 제약 사항을 반영하여 특정 주파수 대역폭 내에서의 동작, 제한된 안테나 구성, 그리고 특정 기능에 대한 최적화된 처리를 수행한다. 별도의 명시가 없는 한, TS 38.213의 모든 절차는 RedCap UE에도 동일하게 적용된다.

## 상세 설명
RedCap UE는 표준 5G NR 단말이 지원하는 필수 물리 계층 기능을 모두 지원한다. 주요 동작 특성은 다음과 같다.

- 일반 동작: TS 38.213에 기술된 모든 물리 계층 절차는 별도의 언급이 없는 한 RedCap UE에 동일하게 적용된다.
- 기능 지원: RedCap UE는 기능 시그널링 없이도 필수적인 Layer-1 기능을 지원해야 한다.
- 대역폭 및 자원 제약: RedCap UE는 특정 주파수 대역에서 감소된 피크 데이터 레이트와 감소된 기저대역 대역폭을 지원하도록 구성될 수 있다. 이는 FR1 대역에서 특히 유효하며, 시스템은 이를 위해 전용 [[Bandwidth_Part_Operation]]을 설정할 수 있다.
- 처리 능력 최적화: 특정 시나리오에서 [[PDSCH]] 및 [[PUSCH]] 처리를 위한 Capability 2를 지원하며, 슬롯당 다중 TB 처리를 통해 지연 시간을 단축할 수 있다. 또한, 셀 스위칭 시 더 빠른 처리 시간을 지원하는 기능이 포함된다.

## 인과 관계
- [[Bandwidth_Part_Operation]] depends_on [[RedCap_UE_Operation]] (RedCap UE의 대역폭 제약 준수를 위한 BWP 설정)
- [[PDSCH_Processing_Procedure]] depends_on [[RedCap_UE_Operation]] (RedCap UE의 처리 능력에 따른 PDSCH 수신 절차 최적화)
- [[PUSCH_Transmission_Procedure]] depends_on [[RedCap_UE_Operation]] (RedCap UE의 처리 능력에 따른 PUSCH 전송 절차 최적화)

## 관련 개념
- [[Bandwidth_Part_Operation]] (implements)
- [[PDSCH_Processing_Procedure]] (implements)
- [[PUSCH_Transmission_Procedure]] (implements)

## 스펙 근거
- TS 38.213 §17: RedCap UE는 별도의 명시가 없는 한 일반 UE와 동일한 물리 계층 절차를 따르며, 필수적인 Layer-1 기능을 모두 지원함.

## 소스
- TS 38.213 v18.0.0 (5G NR; Physical layer procedures for control)