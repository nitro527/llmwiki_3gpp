# HARQ_ACK_Reporting

## 정의
HARQ_ACK_Reporting은 [[UE]]가 [[PDSCH]] 수신 또는 [[DCI]] 트리거에 대한 응답으로 [[HARQ]]-ACK 정보를 [[PUCCH]]를 통해 네트워크로 보고하는 상향링크 제어 절차를 의미한다.

## 요약
[[UE]]는 [[PDSCH]] 수신 완료 후 또는 [[DCI]]에 포함된 지시자에 따라 정해진 타이밍에 [[HARQ]]-ACK 정보를 전송한다. 전송을 위한 [[PUCCH]] 자원은 [[DCI]] 내의 [[PUCCH_Resource_Selection]] 필드 또는 상위 계층 설정에 의해 결정되며, 다중 [[PDSCH]] 수신에 대한 응답은 [[HARQ_ACK_Codebook_Determination]] 절차를 통해 구성된 코드북을 기반으로 수행된다.

## 상세 설명
[[UE]]의 [[HARQ]]-ACK 보고 절차는 TS 38.213 §9.2.3에 따라 다음과 같이 수행된다.

1. 타이밍 결정:
   - [[PDSCH]] 수신 종료 슬롯을 $n$이라 할 때, [[HARQ]]-ACK 정보는 슬롯 $n+k$에서 전송된다.
   - $k$ 값은 [[DCI]] 내의 PDSCH-to-HARQ_feedback timing indicator 필드에 의해 결정된다. 해당 필드가 없는 경우 상위 계층 파라미터(dl-DataToUL-ACK 등)를 사용한다.
   - [[SPS]] [[PDSCH]]의 경우, 활성화 [[DCI]]에 포함된 타이밍 지시자를 따른다.

2. [[PUCCH]] 자원 결정:
   - [[PUCCH]] 자원은 [[HARQ_ACK_Codebook_Determination]]을 통해 결정된 비트 수와 [[PUCCH_Resource_Selection]] 필드 값에 따라 선택된다.
   - 마지막 [[DCI]] 포맷(SPS 활성화 제외)에 포함된 [[PUCCH]] 자원 지시자 필드가 자원 세트 내의 인덱스를 결정한다.
   - 자원 지시자 필드가 없는 경우, 첫 번째 자원을 사용한다.
   - 자원 세트 크기가 8을 초과하는 경우, [[PDCCH]] 수신 시 사용된 첫 번째 [[CCE]] 인덱스($n_{CCE,0}$)와 [[CORESET]] 인덱스를 조합하여 자원 인덱스를 계산한다.

3. 전송 제한 및 다중화:
   - [[UE]]는 슬롯당 우선순위 인덱스별로 하나의 [[PUCCH]]만 전송하는 것을 원칙으로 한다.
   - [[PUCCH]] 포맷 0 또는 1 사용 시, [[PUCCH_Sequence_Generation]]을 통해 순환 이동(cyclic shift) 값을 결정한다.
   - [[PUCCH]] 포맷 2 또는 3 사용 시, 할당된 [[PRB]] 수와 인터레이스(interlace) 설정을 고려하여 전송한다.

## 인과 관계
- [[HARQ_ACK_Codebook_Determination]] depends_on [[HARQ_ACK_Reporting]] (보고할 비트 수 및 자원 세트 결정 전제)
- [[PUCCH_Resource_Selection]] depends_on [[HARQ_ACK_Reporting]] (DCI 필드 기반 자원 매핑 수행)
- [[PUCCH_Format_Processing]] depends_on [[HARQ_ACK_Reporting]] (결정된 포맷에 따른 신호 생성)
- [[UCI_Multiplexing]] depends_on [[HARQ_ACK_Reporting]] (다중 UCI 정보의 PUCCH 결합)

## 관련 개념
- [[PUCCH]] (part_of)
- [[PDSCH]] (affects)
- [[DCI_Field_Mapping]] (affects)
- [[HARQ_ACK_Codebook_Determination]] (depends_on)
- [[PUCCH_Resource_Selection]] (depends_on)
- [[PUCCH_Sequence_Generation]] (implements)

## 스펙 근거
- TS 38.213 §9.2.3: UE procedure for reporting HARQ-ACK
- TS 38.213 §9.2.1: PUCCH resource determination
- TS 38.211 §4.1: Frame structure and timing

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)
- 3GPP TS 38.211 V18.0.0 (2024-03)