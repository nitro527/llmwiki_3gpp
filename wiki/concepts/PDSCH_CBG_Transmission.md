# PDSCH_CBG_Transmission

## 정의
[[PDSCH]] 코드 블록 그룹(CBG, Code Block Group) 기반 전송은 하나의 전송 블록(TB, Transport Block)을 여러 개의 CBG로 분할하여, 전체 TB가 아닌 특정 CBG 단위로 재전송을 수행함으로써 효율적인 오류 정정 및 자원 활용을 가능하게 하는 전송 방식이다.

## 요약
상위 계층 파라미터인 PDSCH-CodeBlockGroupTransmission이 설정된 경우, [[UE]]는 TB를 구성하는 코드 블록(CB)들을 정해진 규칙에 따라 그룹화한다. [[DCI]] format 1_1의 CBGTI(CBG Transmission Information) 필드를 통해 전송되는 CBG를 식별하며, CBGFI(CBG Flushing Out Information) 필드를 통해 이전 수신 데이터와의 결합 여부를 결정한다.

## 상세 설명
### CBG 분할 절차
TB 내의 CB들을 CBG로 그룹화하는 과정은 다음과 같다.
1. TB 내의 총 CB 개수 $C$를 결정한다.
2. 최대 CBG 개수 $N$은 상위 계층 파라미터 maxCodeBlockGroupsPerTransportBlock에 의해 설정된다.
3. $M = \min(C, N)$으로 정의하며, $K = \lfloor C/M \rfloor$, $K_1 = \lfloor C/M \rfloor + 1$, $M_1 = C \pmod M$으로 계산한다.
4. $m < M_1$인 경우, CBG $m$은 $K_1$개의 CB를 포함하며, $m \ge M_1$인 경우 CBG $m$은 $K$개의 CB를 포함한다.

### DCI 기반 제어
- CBGTI 필드: DCI format 1_1 내에서 $N$ 비트 크기를 가지며, 각 비트는 특정 CBG의 전송 여부를 나타낸다. MSB는 CBG#0에 대응하며, '1'은 해당 CBG가 전송됨을, '0'은 전송되지 않음을 의미한다.
- CBGFI 필드: 재전송 시 이전 수신 인스턴스와의 결합 여부를 제어한다. '0'은 이전 인스턴스가 손상되었을 가능성이 있어 폐기(flushing)할 수 있음을 의미하며, '1'은 이전 인스턴스와 결합 가능함을 의미한다.
- 초기 전송 시에는 모든 CBG가 포함된 것으로 간주하며, 재전송 시에는 CBGTI에 명시된 CBG만 전송된다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_CBG_Transmission]] (CBG 기반 전송 설정 시 동작 방식 결정)
- [[DCI_Field_Mapping]] implements [[PDSCH_CBG_Transmission]] (CBGTI 및 CBGFI 필드 매핑)
- [[Code_Block_Segmentation]] affects [[PDSCH_CBG_Transmission]] (CBG 분할을 위한 기초 데이터 제공)

## 관련 개념
- [[PDSCH]] (part_of)
- [[DCI_Field_Mapping]] (implements)
- [[Code_Block_Segmentation]] (affects)
- [[HARQ_ACK_Reporting]] (depends_on)

## 스펙 근거
- TS 38.214 §5.1.7.1: CBG 분할 절차 및 파라미터 계산식 정의
- TS 38.214 §5.1.7.2: CBGTI 및 CBGFI 필드 해석 및 재전송 절차 정의

## 소스
- 3GPP TS 38.214 V16.9.0 (2022-03) "Physical layer procedures for data"