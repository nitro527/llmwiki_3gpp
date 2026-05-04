# Link_Recovery_Procedures

## 정의
[[Link_Recovery_Procedures]]는 [[UE]]가 서빙 셀의 [[Bandwidth_Part_Operation]]에서 빔 실패(Beam Failure)를 감지하고, 이를 복구하기 위해 후보 빔(Candidate Beam)을 측정하여 네트워크에 복구 요청을 전달하는 L1/L2 절차를 의미합니다.

## 요약
이 절차는 빔 기반 통신 환경에서 무선 링크 품질이 저하되었을 때, [[PDCCH]] 수신 실패를 방지하고 통신을 지속하기 위해 수행됩니다. [[UE]]는 빔 실패 감지(BFD, Beam Failure Detection), 후보 빔 식별, 그리고 [[PRACH]]를 이용한 링크 복구 요청(LRR, Link Recovery Request)의 과정을 거칩니다. 본 절차와 관련된 주요 기능 지원 사항은 다음과 같습니다.

- [필수(항상)] 3-0: Basic MAC procedures
- [필수(항상)] 20-16: Radio Link Failure Reporting
- [필수(항상)] 1-1: Basic initial access channels and procedures
- [필수(항상)] 2-5: Basic downlink DMRS for scheduling type A
- [필수(항상)] 2-6: Basic downlink DMRS for scheduling type B
- [필수(cap)] 2-6a: Support 1+2 DMRS (downlink)
- [선택] 20-14: Radio Link Failure Report for inter-RAT MRO EUTRA
- [선택] 57-3: Sidelink consistent LBT detection and recovery
- [선택] 2-7: Supported 2 symbols front-loaded DMRS (downlink)
- [선택] 2-8: Supported 2 symbols front-loaded +2 symbols additional DMRS (downlink)
- [선택] 2-9: Support 1+3 DMRS symbols(downlink)
- [조건부] 2-10: Support DMRS type (downlink)

## 상세 설명
[[Link_Recovery_Procedures]]는 TS 38.213 §6에 명시된 바와 같이 다음 단계로 구성됩니다.

1. **빔 실패 감지 (Beam Failure Detection)**: [[UE]]는 상위 계층에서 설정된 [[Reference_Signals]] (예: [[CSI_RS]] 또는 [[SS_PBCH_Block]])를 기반으로 빔 실패 인스턴스를 모니터링합니다. 설정된 임계값 이하로 품질이 떨어지면 빔 실패 인스턴스가 발생하며, 연속적인 인스턴스 수가 상위 계층 파라미터에 도달하면 빔 실패가 선언됩니다.
2. **후보 빔 식별**: 빔 실패가 감지되면, [[UE]]는 미리 설정된 후보 빔 리스트 중에서 품질이 양호한 빔을 측정하여 선택합니다.
3. **링크 복구 요청 (LRR)**: [[UE]]는 선택된 후보 빔에 대응하는 [[PRACH]] 자원을 사용하여 네트워크에 복구 요청을 전송합니다. 이후 네트워크로부터의 응답을 모니터링하여 복구 절차를 완료합니다.

## 인과 관계
- [[Radio_Link_Monitoring]] (depends_on): 빔 실패 감지는 무선 링크 모니터링의 확장된 개념으로, 특정 빔의 품질 저하를 감지하는 기초가 됩니다.
- [[PRACH]] (triggers): 빔 실패 감지 시, [[UE]]는 복구 요청을 위해 특정 [[PRACH]] 자원을 트리거합니다.
- [[Bandwidth_Part_Operation]] (part_of): 빔 실패 감지 및 복구는 특정 [[Bandwidth_Part_Operation]] 내에서 수행됩니다.

## 관련 개념
- [[Radio_Link_Monitoring]] (affects)
- [[PRACH]] (depends_on)
- [[Bandwidth_Part_Operation]] (part_of)
- [[CSI_RS]] (depends_on)
- [[SS_PBCH_Block]] (depends_on)

## 스펙 근거
- TS 38.213 §6: Link recovery procedures에 대한 전반적인 절차 및 빔 실패 감지 메커니즘 정의.
- TS 38.822: UE Feature Priority 관련 요구사항 명시.

## 소스
- 3GPP TS 38.213 "NR; Physical layer procedures for control"
- 3GPP TS 38.822 "NR; User Equipment (UE) radio access capabilities"