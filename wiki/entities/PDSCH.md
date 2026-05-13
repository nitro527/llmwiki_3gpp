# PDSCH

## 정의
PDSCH(Physical Downlink Shared Channel)는 5G NR에서 사용자 데이터 및 상위 계층 시그널링을 전송하기 위한 핵심 하향링크 물리 채널입니다.

## 요약
PDSCH는 기지국(gNB)으로부터 단말(UE)로 데이터를 전달하며, [[HARQ]] 프로세스를 통해 신뢰성 있는 전송을 지원합니다. 채널 코딩 과정에서 [[CRC_Calculation]], [[Code_Block_Segmentation]], [[Channel_Coding]], [[Rate_Matching]], [[Code_Block_Concatenation]] 단계를 거치며, [[PDCCH]]를 통해 스케줄링 정보를 수신하여 복조 및 복호화를 수행합니다.

## 상세 설명
PDSCH의 전송 및 수신 절차는 TS 38.211 §7.3.1 및 TS 38.214 §5.1에 정의되어 있습니다.

1. 채널 코딩 및 처리:
   - 전송 블록(TB)은 [[CRC_Calculation]]을 거쳐 오류 검출 비트가 추가됩니다.
   - 데이터 크기에 따라 [[Code_Block_Segmentation]]이 수행되며, 각 코드 블록은 [[Channel_Coding]](LDPC)을 통해 부호화됩니다.
   - [[Rate_Matching]]을 통해 할당된 자원 요소(RE) 수에 맞게 비트가 조정되며, 최종적으로 [[Code_Block_Concatenation]]을 통해 하나의 전송 스트림으로 결합됩니다.

2. 수신 절차:
   - UE는 [[PDCCH]]를 통해 DCI format 1_0, 1_1, 1_2, 1_3, 4_0, 4_1, 4_2를 수신하여 PDSCH 스케줄링 정보를 획득합니다.
   - [[HARQ]] 프로세스는 셀당 최대 16개(능력에 따라 32개)가 지원되며, 상위 계층 파라미터 nrofHARQ-ProcessesForPDSCH에 의해 설정됩니다.
   - PDSCH 수신 시 [[DMRS]]를 사용하여 채널 추정을 수행하며, [[PDSCH_Scrambling]], [[PDSCH_Layer_Mapping]], [[PDSCH_Resource_Mapping]] 과정을 통해 물리 자원에 매핑된 데이터를 복원합니다.

3. 특수 동작:
   - 반복 전송(Repetition): repetitionScheme이 'tdmSchemeA', 'fdmSchemeA', 'fdmSchemeB' 등으로 설정된 경우, 동일한 TB에 대해 다중 전송 기회를 가집니다.
   - QCL(Quasi-Co-Location): UE는 DMRS 포트와 SS/PBCH 블록 또는 CSI-RS 간의 QCL 관계를 가정하여 채널을 추정합니다.
   - 다중 PDSCH 수신: UE 능력에 따라 FDMed 또는 TDMed 방식으로 다중 PDSCH를 동시에 수신할 수 있습니다.

## 인과 관계
- [[PDCCH]] triggers [[PDSCH]] (DCI를 통한 PDSCH 스케줄링)
- [[PDSCH]] depends_on [[CRC_Calculation]] (데이터 무결성 검증)
- [[PDSCH]] depends_on [[Channel_Coding]] (LDPC 기반 오류 정정)
- [[PDSCH]] depends_on [[Rate_Matching]] (자원 할당에 따른 비트 매핑)
- [[PDSCH]] depends_on [[DMRS]] (채널 추정 및 복조)
- [[PDSCH]] affects [[HARQ_ACK_Reporting]] (수신 성공 여부 피드백)

## 관련 개념
- [[HARQ]] (affects)
- [[PDCCH]] (triggers)
- [[DMRS]] (depends_on)
- [[CRC_Calculation]] (part_of)
- [[Channel_Coding]] (part_of)
- [[Rate_Matching]] (part_of)
- [[PDSCH_Scrambling]] (part_of)
- [[PDSCH_Layer_Mapping]] (part_of)
- [[PDSCH_Resource_Mapping]] (part_of)

## 스펙 근거
- TS 38.211 §7.3.1: Physical downlink shared channel 물리적 특성 정의
- TS 38.212 §7.2: Downlink shared channel 채널 코딩 및 처리 절차
- TS 38.214 §5.1: UE의 PDSCH 수신 절차 및 HARQ 프로세스 관리

## 소스
- 3GPP TS 38.211 V17.9.0 (Physical channels and modulation)
- 3GPP TS 38.212 V17.8.0 (Multiplexing and channel coding)
- 3GPP TS 38.214 V17.9.0 (Physical layer procedures for data)