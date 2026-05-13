# LDPC_Base_Graph_Selection

## 정의
LDPC_Base_Graph_Selection은 [[Channel_Coding]] 과정에서 전송 블록(Transport Block)의 각 코드 블록(Code Block)을 인코딩하기 위해 두 가지 LDPC 베이스 그래프(Base Graph 1 또는 Base Graph 2) 중 하나를 결정하는 절차를 의미한다.

## 요약
5G NR 시스템에서 데이터 채널의 효율적인 오류 정정을 위해 코드 블록의 크기와 부호화율(Coding Rate)에 따라 적절한 LDPC 베이스 그래프를 선택한다. 초기 전송 및 재전송 시 동일한 베이스 그래프가 적용되며, 특정 조건에 따라 베이스 그래프 2를 사용하고, 그 외의 경우에는 베이스 그래프 1을 사용한다.

## 상세 설명
LDPC 베이스 그래프 선택은 전송 블록의 페이로드 크기(Payload Size, $K$)와 MCS 인덱스를 통해 결정된 부호화율($R$)을 기반으로 수행된다. TS 38.212 §7.2.2에 명시된 선택 조건은 다음과 같다.

베이스 그래프 2(Base Graph 2)가 선택되는 조건은 다음과 같다.
- $K \le 292$인 경우
- $K \le 3824$이고 $R \le 0.67$인 경우
- $R \le 0.25$인 경우

위의 조건 중 어느 하나라도 만족하지 않는 경우, 베이스 그래프 1(Base Graph 1)이 사용된다. 여기서 $K$는 [[Code_Block_Segmentation]] 이후의 페이로드 크기를 의미하며, 부호화율 $R$은 TS 38.214 §5.1.3.1에 정의된 MCS 인덱스에 의해 결정된다. 동일한 전송 블록에 대한 재전송 시에도 초기 전송 시 결정된 베이스 그래프를 동일하게 적용한다.

## 인과 관계
- [[Channel_Coding]] depends_on [[LDPC_Base_Graph_Selection]] (채널 코딩 수행을 위한 그래프 결정)
- [[Code_Block_Segmentation]] affects [[LDPC_Base_Graph_Selection]] (코드 블록 크기 K가 그래프 선택의 입력값으로 사용)

## 관련 개념
- [[Channel_Coding]] (depends_on)
- [[Code_Block_Segmentation]] (affects)

## 스펙 근거
- TS 38.212 §7.2.2 LDPC base graph selection

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03)