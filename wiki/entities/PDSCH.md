# PDSCH

## 정의
[[PDSCH]]는 5G NR에서 하향링크 데이터를 사용자 단말([[UE]])에게 전달하기 위해 사용하는 물리 채널입니다.

## 요약
[[PDSCH]]는 [[DL-SCH]]로부터 전달받은 데이터를 물리 계층에서 처리하여 전송하는 채널로, [[Scrambling]], [[Modulation]], [[Layer_Mapping]], [[Antenna_Port_Mapping]], [[PDSCH_Resource_Mapping]] 과정을 거칩니다. [[UE]]는 [[DCI]]를 통해 자원 할당 및 전송 파라미터를 수신하며, [[HARQ]] 절차를 통해 데이터 수신 성공 여부를 보고합니다.

## 상세 설명
[[PDSCH]]의 물리 계층 처리 과정은 다음과 같습니다.

* [[Scrambling]]: 전송되는 비트 시퀀스는 [[PDSCH_Scrambling]]을 통해 스크램블링됩니다 (TS 38.211 §7.3.1.1).
* [[Modulation]]: 스크램블링된 비트는 [[PDSCH_Modulation]]을 통해 복소 심볼로 변환됩니다 (TS 38.211 §7.3.1.2).
* [[Layer_Mapping]]: 변조된 심볼은 [[PDSCH_Layer_Mapping]]을 통해 하나 이상의 전송 레이어로 매핑됩니다 (TS 38.211 §7.3.1.3).
* [[Antenna_Port_Mapping]]: 레이어는 [[Antenna_Port_Mapping]]을 통해 물리적 안테나 포트로 매핑됩니다 (TS 38.211 §7.3.1.4).
* [[PDSCH_Resource_Mapping]]: 심볼은 [[PDSCH_Resource_Mapping]]을 통해 가상 자원 블록([[VRB]]) 및 물리 자원 블록([[PRB]])에 매핑됩니다 (TS 38.211 §7.3.1.5, §7.3.1.6).

[[UE]]는 [[PDSCH_Reception_Procedures]]에 따라 자원 할당을 결정하며, [[PDSCH_Resource_Allocation]]을 통해 시간 및 주파수 영역의 자원을 할당받습니다. 또한 [[PDSCH_CBG_Transmission]]을 통해 코드 블록 그룹 단위의 재전송을 지원합니다.

## 인과 관계
* [[DCI]] (triggers) [[PDSCH]] 수신 절차
* [[PDSCH]] (depends_on) [[PDSCH_Resource_Allocation]]
* [[PDSCH]] (affects) [[HARQ_ACK_Codebook_Determination]]
* [[PDSCH]] (part_of) [[DL-SCH]]

## 관련 개념
- [[PDSCH_Scrambling]] (part_of)
- [[PDSCH_Modulation]] (part_of)
- [[PDSCH_Layer_Mapping]] (part_of)
- [[PDSCH_Resource_Mapping]] (part_of)
- [[DMRS]] (depends_on)
- [[CSI_RS]] (depends_on)
- [[PT_RS]] (depends_on)
- [[HARQ]] (depends_on)

## 스펙 근거
* TS 38.211 §7.3.1: [[PDSCH]] 물리 채널 구조 및 매핑 절차
* TS 38.212 §7.2: [[DL-SCH]] 채널 코딩 및 레이트 매칭
* TS 38.214 §5.1: [[UE]]의 [[PDSCH]] 수신 절차 및 자원 할당

## 소스
* 3GPP TS 38.211 v17.9.0
* 3GPP TS 38.212 v17.9.0
* 3GPP TS 38.214 v17.9.0