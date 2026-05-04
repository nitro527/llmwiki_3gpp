# PDSCH_CBG_Transmission

## 정의
[[PDSCH]] [[CBG]] (Code Block Group) 기반 전송은 하나의 [[Transport_Block]] (TB)를 다수의 코드 블록 그룹으로 분할하여, 전체 TB가 아닌 특정 CBG 단위로 [[HARQ]] 재전송을 수행하는 기술입니다.

## 요약
본 기능은 [[UE]]가 [[PDSCH]] 수신 시 전체 TB를 재전송받는 대신, 오류가 발생한 특정 CBG만을 선택적으로 재전송받아 효율적인 자원 활용과 [[Latency]] 감소를 달성합니다. 이는 [[DCI]] 필드를 통해 제어되며, [[UE]]의 능력(Capability)에 따라 슬롯당 처리 가능한 [[PDSCH]] 개수와 [[Processing_Time]]이 결정됩니다.

## 상세 설명
[[PDSCH]] [[CBG]] 기반 전송은 다음과 같은 절차로 이루어집니다.

1. **CBG 그룹화**: 상위 계층 파라미터 `maxCodeBlockGroupsPerTransportBlock`에 의해 설정된 값에 따라 하나의 [[Transport_Block]] 내의 코드 블록들이 그룹화됩니다.
2. **DCI 해석**: [[PDCCH]]를 통해 전달되는 [[DCI]] 내의 'CBG Transmission Information' (CBGTI) 필드는 어떤 CBG가 전송되는지를 나타내며, 'CBG Flushing Out Information' (CBGFI) 필드는 이전 수신 데이터의 버퍼를 비울지 여부를 결정합니다.
3. **재전송 처리**: [[UE]]는 수신된 CBGTI 필드를 바탕으로 해당 [[PDSCH]]가 새로운 전송인지 혹은 특정 CBG에 대한 재전송인지를 판단합니다. 재전송의 경우, 이전에 성공적으로 수신된 CBG와 새로 수신된 CBG를 결합하여 [[Transport_Block]]을 복구합니다.

## 인과 관계
- [[PDSCH]] 수신 시 [[HARQ]] 프로세스는 [[CBG]] 기반 전송 설정 여부에 따라 [[HARQ_ACK_Codebook_Determination]]에 영향을 미칩니다.
- [[DCI_Formats_Processing]] 단계에서 CBGTI 필드 해석 결과가 재전송을 위한 [[PDSCH_Resource_Allocation]]을 결정합니다.

## 관련 개념
- [[PDSCH]] (part_of)
- [[HARQ]] (affects)
- [[DCI_Formats_Processing]] (depends_on)
- [[Transport_Block]] (part_of)

## 스펙 근거
- TS 38.214 §5.1.7.1: UE procedure for grouping of code blocks to code block groups
- TS 38.214 §5.1.7.2: UE procedure for receiving code block group based transmissions

## 소스
- 3GPP TS 38.214 V17.9.0 (2024-03)