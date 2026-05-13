# CSI_Processing_Criteria

## 정의
CSI_Processing_Criteria는 [[UE]]가 [[CSI_Reporting_Procedure]]를 수행할 때 필요한 연산 자원(CPU)을 관리하고, 동시에 처리 가능한 [[CSI_RS]] 계산량 및 보고 제약 조건을 정의하는 규격입니다.

## 요약
[[UE]]는 [[CSI_ReportConfig]]에 따라 [[CSI_RS]] 기반의 측정 및 보고를 수행하며, 이때 소요되는 연산 자원인 CPU를 점유합니다. 특정 OFDM 심볼에서 가용 CPU를 초과하는 요청이 발생할 경우, [[UE]]는 우선순위가 낮은 [[CSI_Reporting_Procedure]]를 생략하거나 업데이트하지 않을 수 있습니다.

## 상세 설명
[[UE]]는 [[simultaneousCSI-ReportsPerCC]] 또는 [[simultaneousCSI-SubReportsPerCC-r18]] 파라미터를 통해 컴포넌트 캐리어(CC) 내에서, 그리고 [[simultaneousCSI-ReportsAllCC]] 또는 [[simultaneousCSI-SubReportsAllCC-r18]]을 통해 전체 CC에 걸쳐 동시에 계산 가능한 [[CSI_Reporting_Procedure]]의 수를 보고합니다.

1. **CPU 점유 및 우선순위**:
   - 특정 OFDM 심볼에서 L개의 CPU가 점유 중일 때, 새로운 N개의 [[CSI_Reporting_Procedure]]가 시작되면, [[UE]]는 우선순위가 낮은 보고부터 제외합니다.
   - [[CSI_ReportConfig]]의 [[reportQuantity]] 설정에 따라 CPU 점유 심볼 수와 연산량이 결정됩니다.
   - 예를 들어, [[reportQuantity]]가 'none'이고 [[trs-Info]]가 설정된 경우, 또는 'cri-RSRP', 'cri-SINR' 등 특정 측정값인 경우 TS 38.214 §5.2.1.6에 정의된 수식에 따라 CPU 점유가 발생합니다.

2. **CPU 점유 기간**:
   - 주기적/반주기적 [[CSI_Reporting_Procedure]]는 측정 자원(CSI-RS/CSI-IM/SSB)의 첫 심볼부터 보고를 운반하는 [[PUSCH]]/[[PUCCH]]의 마지막 심볼까지 CPU를 점유합니다.
   - 비주기적(Aperiodic) 보고는 [[PDCCH]] 트리거 이후부터 [[PUSCH]] 전송 종료 시점까지 점유합니다.

3. **CSI-RS 자원 카운팅**:
   - [[CSI_RS]] 자원이 여러 보고 설정에서 참조될 경우, 참조 횟수(N)만큼 자원 및 포트가 카운트됩니다.
   - [[csi-ReportSubConfigToAddModList]]가 설정된 경우, 트리거된 서브 설정 수(M)에 따라 자원 카운팅이 수행됩니다.

## 인과 관계
- [[CSI_Reporting_Procedure]] depends_on [[CSI_Processing_Criteria]] (CSI 계산 자원 제약 준수 필요)
- [[CSI_RS]] depends_on [[CSI_Processing_Criteria]] (자원 활성 기간 및 포트 카운팅 규칙 적용)
- [[PUSCH]] depends_on [[CSI_Processing_Criteria]] (비주기적 CSI 보고 시 CPU 점유 종료 시점 결정)
- [[PDCCH]] triggers [[CSI_Processing_Criteria]] (비주기적 CSI 보고 트리거 시 CPU 점유 시작)

## 관련 개념
- [[CSI_Reporting_Procedure]] (depends_on)
- [[CSI_RS]] (depends_on)
- [[PUSCH]] (depends_on)
- [[PDCCH]] (triggers)

## 스펙 근거
- TS 38.214 §5.2.1.6: CSI processing criteria 정의 및 CPU 점유 수식, 자원 카운팅 규칙 명시
- TS 38.214 §5.2.5: CSI 보고 우선순위 결정 규칙

## 소스
- 3GPP TS 38.214 V18.0.0 (2024-03) §5.2.1.6