# SRS_CLI_Measurement

## 정의
SRS_CLI_Measurement는 기지국 간 간섭인 CLI(Cross-Link Interference)를 측정하기 위해 [[SRS]] 자원을 활용하여 RSRP(Reference Signal Received Power)를 측정하는 절차를 의미합니다.

## 요약
본 절차는 네트워크가 설정한 [[SRS]] 자원을 사용하여 UE가 CLI 환경에서의 신호 세기를 측정하는 메커니즘입니다. UE는 설정된 BWP(Bandwidth Part) 내에서 SRS-RSRP를 측정하며, 측정 자원의 개수 및 슬롯당 수신 자원 수에 대한 제한 사항을 준수해야 합니다.

## 상세 설명
CLI 측정을 위한 SRS 수신 절차는 다음과 같은 기술적 요구사항을 따릅니다.

1. 자원 설정: CLI 측정을 위한 SRS 자원은 TS 38.211 §6.4.1.4에 정의된 자원 구성을 따르며, TS 38.215 §5.1.19에 명시된 SRS-RSRP 측정 절차를 수행합니다.
2. BWP 제약 사항:
   - UE는 활성 BWP에 설정된 Subcarrier Spacing과 동일한 환경에서만 SRS-RSRP를 측정합니다.
   - 측정에 사용되는 SRS-RSRP 자원은 반드시 DL 활성 BWP 내에 완전히 포함되어야 합니다.
3. 측정 용량 제한:
   - UE는 최대 32개의 SRS 자원에 대해 측정을 수행할 수 있습니다.
   - UE는 하나의 슬롯 내에서 최대 8개의 SRS 자원을 수신하여 측정할 수 있습니다.

## 인과 관계
- [[SRS]] depends_on [[SRS_CLI_Measurement]] (CLI 측정을 위한 자원 구성 및 수신 절차 수행)
- [[SRS_CLI_Measurement]] depends_on [[Bandwidth_Part_Operation]] (측정 자원이 활성 BWP 내에 존재해야 함)

## 관련 개념
- [[SRS]] (part_of)
- [[Bandwidth_Part_Operation]] (depends_on)

## 스펙 근거
- TS 38.214 §5.1.6.4: SRS reception procedure for CLI
- TS 38.211 §6.4.1.4: SRS 자원 정의
- TS 38.215 §5.1.19: SRS-RSRP 측정 정의

## 소스
- 3GPP TS 38.214 V17.9.0 (2024-03)
- 3GPP TS 38.211 V17.9.0 (2024-03)
- 3GPP TS 38.215 V17.7.0 (2024-03)