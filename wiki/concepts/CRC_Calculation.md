# CRC_Calculation

## 정의
CRC_Calculation은 물리 계층에서 전송되는 데이터 블록의 무결성을 검증하기 위해 순환 중복 검사(Cyclic Redundancy Check) 비트를 생성하고 부착하는 절차를 의미합니다.

## 요약
CRC_Calculation은 입력 비트 시퀀스에 대해 특정 생성 다항식(Generator Polynomial)을 사용하여 패리티 비트를 산출합니다. 이 과정은 GF(2) 연산을 기반으로 하며, 시스템적(Systematic) 형태로 인코딩되어 데이터 비트 뒤에 패리티 비트가 추가됩니다. UL-SCH 전송 블록의 경우, 페이로드 크기에 따라 16비트 또는 24비트 CRC가 선택적으로 적용됩니다.

## 상세 설명
CRC 생성은 입력 비트 시퀀스 $a_0, a_1, \dots, a_{A-1}$에 대해 $L$개의 패리티 비트 $p_0, p_1, \dots, p_{L-1}$를 생성하는 과정입니다.

1. 생성 다항식 선택: TS 38.212 §5.1에 명시된 6가지 다항식 중 CRC 길이에 맞는 다항식을 사용합니다.
   - $g_{CRC24A}(D) = D^{24} + D^{23} + D^{18} + D^{17} + D^{14} + D^{11} + D^{10} + D^7 + D^6 + D^5 + D^4 + D^3 + D + 1$
   - $g_{CRC24B}(D) = D^{24} + D^{23} + D^6 + D^5 + D + 1$
   - $g_{CRC24C}(D) = D^{24} + D^{23} + D^{21} + D^{20} + D^{17} + D^{15} + D^{11} + D^9 + D^8 + D^7 + D^5 + D^3 + D + 1$
   - $g_{CRC16}(D) = D^{16} + D^{12} + D^5 + 1$
   - $g_{CRC11}(D) = D^{11} + D^{10} + D^9 + D^5 + 4 + 1$
   - $g_{CRC6}(D) = D^6 + D^5 + 1$

2. 인코딩: 시스템적 형태를 유지하며, 다항식 $a_0 D^{A+L-1} + \dots + a_{A-1} D^L + p_0 D^{L-1} + \dots + p_{L-1}$을 생성 다항식으로 나누었을 때 나머지가 0이 되도록 패리티 비트를 결정합니다.

3. UL-SCH 전송 블록 적용: TS 38.212 §6.2.1에 따라 전송 블록의 페이로드 크기가 결정되면 CRC를 부착합니다.
   - 페이로드 크기가 3824비트를 초과하거나, 코드 블록 세그먼트화가 필요한 경우 $L=24$비트 CRC를 사용합니다.
   - 그 외의 경우 $L=16$비트 CRC를 사용합니다.
   - 생성된 비트 시퀀스 $b_k$는 $k=0, \dots, A-1$에 대해 $b_k = a_k$이며, $k=A, \dots, A+L-1$에 대해 $b_k = p_{k-A}$로 정의됩니다.

## 인과 관계
- [[Code_Block_Segmentation]] depends_on [[CRC_Calculation]] (전송 블록 CRC 부착 후 코드 블록 단위로 분할)
- [[Channel_Coding]] depends_on [[CRC_Calculation]] (채널 코딩 수행 전 오류 검출을 위한 CRC 부착 필수)

## 관련 개념
- [[Code_Block_Segmentation]] (depends_on)
- [[Channel_Coding]] (depends_on)

## 스펙 근거
- TS 38.212 §5.1: CRC calculation 절차 및 생성 다항식 정의
- TS 38.212 §6.2.1: UL-SCH 전송 블록에 대한 CRC 부착 규칙 및 비트 매핑

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03) "Multiplexing and channel coding"