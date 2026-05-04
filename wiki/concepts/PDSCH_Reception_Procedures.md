# PDSCH_Reception_Procedures

## 정의
[[PDSCH]] 수신 절차는 [[UE]]가 [[PDCCH]]를 통해 스케줄링된 하향링크 데이터를 물리 계층에서 수신하고, [[HARQ]] 프로세스를 관리하며, 정해진 시간 내에 처리를 완료하기 위한 일련의 규정된 동작을 의미합니다.

## 요약
[[PDSCH]] 수신은 [[QCL]] 가정, [[Reference_Signals]] 수신, [[PDSCH_CBG_Transmission]] 처리 및 [[PDSCH_Reception_Preparation_Time]] 준수를 포함합니다. [[UE]]는 [[PDCCH]] 수신 후 데이터 복조를 위해 필요한 시간과 [[HARQ-ACK]] 피드백을 위한 준비 시간을 보장받아야 하며, 이는 [[UE]]의 처리 능력(Capability)에 따라 달라집니다.

## 상세 설명
[[PDSCH]] 수신 절차는 다음과 같은 핵심 요소로 구성됩니다.

1. **[[QCL]] 가정**: [[UE]]는 [[PDSCH]]의 [[DMRS]]와 [[Reference_Signals]] 간의 [[QCL]] 관계를 기반으로 채널 추정을 수행합니다. 이는 [[TS_38_214]] §5.1.5에 따라 안테나 포트 간의 공간적 특성을 파악하는 데 사용됩니다.
2. **[[Reference_Signals]] 수신**: [[CSI_RS]], [[DMRS]], [[PT_RS]] 및 [[PRS]] 수신 절차를 통해 채널 상태 정보 측정, 데이터 복조, 위상 추적 및 위치 측정 등을 수행합니다. 특히 [[CSI_RS]]는 트래킹, L1-RSRP/SINR 계산, 이동성 관리 등을 위해 사용됩니다(§5.1.6).
3. **[[PDSCH_CBG_Transmission]]**: [[Code_Block_Group]] 기반의 전송을 지원하여, 전체 전송 블록이 아닌 특정 그룹 단위의 재전송을 가능하게 함으로써 효율적인 [[HARQ]] 동작을 수행합니다(§5.1.7).
4. **[[PDSCH_Reception_Preparation_Time]]**: [[UE]]가 [[PDCCH]]를 수신한 후 [[PDSCH]]를 처리하기 위해 필요한 최소 시간을 정의합니다. 이는 [[Subcarrier_Spacing]]에 따라 달라지며, [[UE]]의 처리 능력(Capability #1 또는 #2)에 따라 다르게 적용됩니다(§5.3, §5.5).
5. **[[Scheduling_Offset_Restriction]]**: [[PDCCH]]와 [[PDSCH]] 사이의 최소 스케줄링 오프셋 제한에 대한 적용 지연 시간을 관리합니다(§5.3.1).

## 인과 관계
- [[PDCCH]] 수신 (triggers) [[PDSCH]] 수신 절차
- [[PDSCH_Reception_Preparation_Time]] (affects) [[PDSCH]] 스케줄링 오프셋
- [[QCL]] 설정 (depends_on) [[Reference_Signals]] 채널 추정 품질
- [[PDSCH_CBG_Transmission]] (affects) [[HARQ]] 재전송 효율성

## 관련 개념
- [[PDSCH]] (part_of)
- [[PDCCH]] (triggers)
- [[HARQ]] (part_of)
- [[Reference_Signals]] (depends_on)
- [[PDSCH_Reception_Preparation_Time]] (part_of)
- [[PDSCH_CBG_Transmission]] (similar_to)

## 스펙 근거
- [[TS_38_214]] §5.1.5: Antenna ports quasi co-location
- [[TS_38_214]] §5.1.6: UE procedure for receiving reference signals
- [[TS_38_214]] §5.1.7: Code block group based PDSCH transmission
- [[TS_38_214]] §5.3: UE PDSCH processing procedure time
- [[TS_38_214]] §5.3.1: Application delay of the minimum scheduling offset restriction
- [[TS_38_214]] §5.5: UE PDSCH reception preparation time with different subcarrier spacings

## 소스
- 3GPP TS 38.214 V17.9.0 (2024-03) "NR; Physical layer procedures for data"