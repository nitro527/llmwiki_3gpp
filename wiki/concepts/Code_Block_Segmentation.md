# Code_Block_Segmentation

## 정의
Code_Block_Segmentation은 전송 블록(Transport Block)을 채널 코딩 효율을 최적화하기 위해 더 작은 단위인 코드 블록(Code Block)으로 나누고, 각 코드 블록마다 오류 검출을 위한 [[CRC_Calculation]]을 수행하는 물리 계층 절차를 의미한다.

## 요약
전송 블록에 CRC가 부착된 비트열을 입력받아, LDPC(Low-Density Parity-Check) 코드의 블록 크기 제한에 맞춰 여러 개의 코드 블록으로 분할한다. 분할된 각 코드 블록에는 독립적인 CRC가 추가되어 수신단에서 코드 블록 단위의 오류 검출 및 [[HARQ]] 재전송 판단을 가능하게 한다.

## 상세 설명
전송 블록의 비트열을 $b_0, b_1, \dots, b_{B-1}$이라 할 때, 여기서 $B$는 CRC가 포함된 전송 블록의 총 비트 수이다. 이 비트열은 TS 38.212 §5.2.2에 정의된 절차에 따라 코드 블록으로 분할된다.

1. 코드 블록 분할: 입력된 비트열은 LDPC 부호화기의 최대 코드 블록 크기 제한에 따라 분할된다. 분할된 각 코드 블록은 $c_{r,0}, c_{r,1}, \dots, c_{r,K_r-1}$로 표기되며, 여기서 $r$은 코드 블록 번호, $K_r$은 해당 코드 블록의 비트 수를 나타낸다.
2. 코드 블록 CRC 부착: 각 코드 블록에 대해 별도의 CRC가 계산되어 부착된다. 이는 전체 전송 블록에 대한 CRC와는 별개로 동작하며, 채널 디코딩 과정에서 코드 블록 단위의 성공 여부를 판별하는 데 사용된다.
3. 제약 조건: DCI 내의 Time domain resource assignment 필드에 의해 지시된 numberOfSlotsTBoMS 값이 1보다 큰 경우, 코드 블록 크기 $B$에 대한 제한이 적용된다. 이때 부호화율(coding rate)은 TS 38.214 §6.1.4.1에 따라 MCS 인덱스로부터 결정된다.
   - 부호화율 $R \le 0.25$인 경우: $B \le 3840$
   - 그 외의 경우: $B \le 8448$

## 인과 관계
- [[Channel_Coding]] depends_on [[Code_Block_Segmentation]] (분할된 코드 블록 단위로 채널 부호화 수행)
- [[Code_Block_Segmentation]] triggers [[CRC_Calculation]] (각 코드 블록별 CRC 생성 및 부착)
- [[Code_Block_Concatenation]] depends_on [[Code_Block_Segmentation]] (분할된 코드 블록들을 다시 결합하여 전송 준비)

## 관련 개념
- [[CRC_Calculation]] (implements)
- [[Channel_Coding]] (depends_on)
- [[Code_Block_Concatenation]] (depends_on)

## 스펙 근거
- TS 38.212 §5.2: Code block segmentation and code block CRC attachment 일반 절차
- TS 38.212 §6.2.3: PUSCH 전송을 위한 코드 블록 분할 및 CRC 부착 상세 규격

## 소스
- 3GPP TS 38.212 V18.0.0, "Multiplexing and channel coding"