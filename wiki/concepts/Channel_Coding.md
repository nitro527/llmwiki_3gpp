# Channel_Coding

## 정의
5G NR에서 전송 채널(TrCH) 및 제어 정보의 신뢰성 있는 전송을 위해 데이터 비트에 오류 정정 부호를 적용하는 물리 계층 절차를 의미한다.

## 요약
5G NR은 데이터 채널과 제어 채널의 특성에 따라 서로 다른 채널 코딩 방식을 사용한다. 데이터 채널인 [[UL-SCH]] 및 [[PDSCH]]에는 [[LDPC]] 코드가 사용되며, 제어 정보에는 [[Polar]] 코드가 주로 사용된다. 채널 코딩은 [[Code_Block_Segmentation]] 이후 단계에서 수행되며, 인코딩된 비트는 이후 [[Rate_Matching]] 과정을 거친다.

## 상세 설명
채널 코딩은 전송되는 정보의 종류에 따라 TS 38.212 §5.3에 정의된 표에 따라 결정된다.

1. 데이터 채널 코딩:
   - [[UL-SCH]]와 같은 전송 채널은 [[Code_Block_Segmentation]]을 통해 분할된 각 코드 블록 단위로 처리된다.
   - 각 코드 블록은 [[LDPC]] 인코딩을 수행하며, 이때 사용되는 베이스 그래프(Base Graph)는 [[LDPC_Base_Graph_Selection]]에 의해 결정된다.
   - TS 38.212 §6.2.4에 따르면, 코드 블록의 비트 시퀀스를 $c_r$이라 할 때, 각 코드 블록은 개별적으로 인코딩되어 출력 비트 시퀀스를 생성한다.

2. 제어 정보 코딩:
   - 제어 정보의 유형에 따라 [[Polar]] 코딩이 적용된다. 이는 작은 블록 길이에서도 우수한 성능을 제공하며, 제어 채널의 신뢰성을 보장한다.

3. 절차적 흐름:
   - 상위 계층으로부터 전달된 데이터는 먼저 [[CRC_Calculation]]을 거친다.
   - 이후 [[Code_Block_Segmentation]]을 통해 적절한 크기로 분할된다.
   - 분할된 블록은 각 채널 코딩 방식에 따라 인코딩된다.
   - 인코딩된 비트는 전송 자원에 맞추기 위해 [[Rate_Matching]] 과정을 수행한다.

## 인과 관계
- [[Code_Block_Segmentation]] triggers [[Channel_Coding]] (분할된 코드 블록이 인코딩 입력으로 전달)
- [[Channel_Coding]] triggers [[Rate_Matching]] (인코딩된 비트가 전송 자원에 맞게 조정됨)
- [[LDPC_Base_Graph_Selection]] affects [[Channel_Coding]] (LDPC 인코딩 시 사용할 베이스 그래프 결정)

## 관련 개념
- [[LDPC]] (implements)
- [[Polar]] (implements)
- [[Code_Block_Segmentation]] (depends_on)
- [[Rate_Matching]] (affects)
- [[CRC_Calculation]] (depends_on)

## 스펙 근거
- TS 38.212 §5.3: 채널 코딩 방식의 선택 및 적용 범위 정의
- TS 38.212 §6.2.4: [[UL-SCH]]에 대한 [[LDPC]] 인코딩 절차 상세

## 소스
- 3GPP TS 38.212 V18.0.0, "Multiplexing and channel coding"