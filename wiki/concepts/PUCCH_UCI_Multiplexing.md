# PUCCH_UCI_Multiplexing

## 정의
[[PUCCH]]_UCI_Multiplexing은 [[UE]]가 단일 [[Slot]] 내에서 [[HARQ-ACK]], [[SR]], 그리고 [[CSI]] 보고서를 하나의 [[PUCCH]] 자원에 결합하여 전송하는 물리 계층 절차를 의미한다.

## 요약
이 절차는 [[UE]]가 상향링크 제어 정보(UCI)를 효율적으로 전송하기 위해, 설정된 [[PUCCH]] 자원 내에서 정보의 우선순위에 따라 비트를 다중화하고, [[maxCodeRate]]를 준수하도록 자원 크기 및 전송할 정보량을 제어하는 메커니즘이다.

## 상세 설명
[[PUCCH]]를 통한 [[HARQ-ACK]], [[SR]], [[CSI]] 다중화는 다음과 같은 단계로 수행된다.

1. 자원 결정:
   - 단일 [[CSI]] 보고 시 [[pucch-CSI-ResourceList]]를 사용하며, 다중 보고 시 [[multi-CSI-PUCCH-ResourceList]]를 참조한다.
   - [[PUCCH]] 포맷 2, 3, 4를 사용하는 경우, [[maxCodeRate]] 파라미터를 통해 다중화된 UCI의 코드 레이트를 제어한다.

2. 파라미터 정의:
   - $O_{ACK}$: [[HARQ-ACK]] 비트 수
   - $O_{SR}$: [[SR]] 비트 수
   - $O_{CSI}$: [[CSI]] 보고서 비트 수 (Part 1 및 Part 2 포함)
   - $O_{CRC}$: 인코딩을 위한 [[CRC]] 비트 수

3. 자원 선택 및 코드 레이트 제어:
   - [[PUCCH]] 포맷 2, 3, 4에서 UCI 비트 수와 설정된 코드 레이트($R$)를 기반으로 필요한 PRB 수를 계산한다.
   - 가용 자원 내에서 전송 가능한 비트 수를 초과할 경우, [[CSI]] 보고서의 우선순위(Priority)에 따라 일부 보고서를 드롭하거나 Part 2 CSI 보고서를 제외하고 Part 1 CSI만 전송하는 방식으로 제어한다.
   - [[InterlaceAllocation]]이 설정된 경우, 첫 번째 및 두 번째 인터레이스를 사용하여 자원을 확장할 수 있다.

4. 특수 케이스:
   - [[PDSCH]] 수신 없이 [[HARQ-ACK]]를 전송하는 경우, 특정 조건에 따라 [[PUCCH]] 자원을 선택한다.
   - [[CSI]] 보고서가 중첩되는 경우, 우선순위가 낮은 보고서부터 순차적으로 제외하여 전송 가능한 자원 내에 맞춘다.

## 인과 관계
- [[PUCCH_Format_Processing]] depends_on [[PUCCH_UCI_Multiplexing]] (다중화된 UCI의 인코딩 및 변조 수행)
- [[UCI_Multiplexing]] implements [[PUCCH_UCI_Multiplexing]] (상위 계층 UCI 다중화 로직의 물리 계층 구현)
- [[PUCCH_Resource_Selection]] depends_on [[PUCCH_UCI_Multiplexing]] (다중화된 UCI 비트 수에 따른 자원 결정)

## 관련 개념
- [[HARQ-ACK]] (affects)
- [[SR]] (affects)
- [[CSI]] (affects)
- [[PUCCH]] (part_of)
- [[UCI_Multiplexing]] (implements)
- [[PUCCH_Resource_Selection]] (depends_on)

## 스펙 근거
- TS 38.213 §9.2.5.2: UE procedure for multiplexing HARQ-ACK/SR/CSI in a PUCCH
- TS 38.214 §5.2: CSI reporting procedures
- TS 38.211 §6.3.1: PUCCH transmission

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03)
- 3GPP TS 38.214 V18.0.0 (2024-03)
- 3GPP TS 38.211 V18.0.0 (2024-03)