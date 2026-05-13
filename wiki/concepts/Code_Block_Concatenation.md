# Code_Block_Concatenation

## 정의
Code_Block_Concatenation은 [[Rate_Matching]]을 거친 다수의 코드 블록(Code Block) 출력 비트 시퀀스들을 하나의 연속적인 비트 스트림으로 결합하는 물리 계층 처리 절차를 의미합니다.

## 요약
이 절차는 전송 채널 또는 제어 채널의 인코딩 과정에서 생성된 개별 코드 블록들의 레이트 매칭 결과물을 순차적으로 이어 붙여, 최종적으로 물리 채널 전송을 위한 단일 비트 시퀀스를 생성합니다. TS 38.212 §5.5 및 §6.2.6에 정의된 알고리즘을 따릅니다.

## 상세 설명
Code_Block_Concatenation은 다음과 같은 단계로 수행됩니다.

1. 입력 시퀀스: $C$개의 코드 블록에 대해 각각 레이트 매칭된 비트 시퀀스 $f_{r,0}, f_{r,1}, \dots, f_{r,E_r-1}$이 입력됩니다. 여기서 $r$은 코드 블록 인덱스($r = 0, 1, \dots, C-1$)이며, $E_r$은 $r$번째 코드 블록의 레이트 매칭된 비트 수입니다.
2. 결합 알고리즘:
   - 초기화: $k = 0$ 및 $r = 0$으로 설정합니다.
   - 루프 수행: $r < C$인 동안 다음을 반복합니다.
     - $j = 0$으로 설정합니다.
     - $j < E_r$인 동안 다음을 반복합니다.
       - 출력 시퀀스 $g_k = f_{r,j}$를 할당합니다.
       - $k = k + 1$, $j = j + 1$로 증가시킵니다.
     - $r = r + 1$로 증가시킵니다.
3. 출력 시퀀스: 최종적으로 생성된 비트 시퀀스 $g_0, g_1, \dots, g_{G-1}$은 물리 채널 전송을 위한 총 비트 수 $G$를 가지며, 이는 $\sum_{r=0}^{C-1} E_r$과 같습니다.

이 절차는 [[PUSCH]] 및 [[PDSCH]]와 같은 데이터 채널뿐만 아니라, 제어 정보의 인코딩 과정에서도 동일하게 적용됩니다.

## 인과 관계
- [[Rate_Matching]] depends_on [[Code_Block_Concatenation]] (레이트 매칭된 비트들을 결합하여 전송 준비)
- [[Code_Block_Concatenation]] triggers [[PUSCH_Scrambling]] (결합된 비트 시퀀스가 스크램블링 단계로 전달)

## 관련 개념
- [[Code_Block_Segmentation]] (part_of)
- [[Channel_Coding]] (part_of)
- [[Rate_Matching]] (part_of)
- [[PUSCH_Scrambling]] (affects)
- [[PDSCH_Scrambling]] (affects)

## 스펙 근거
- TS 38.212 §5.5: Code block concatenation 일반 절차 정의
- TS 38.212 §6.2.6: PUSCH 전송을 위한 코드 블록 결합 절차 명시

## 소스
- 3GPP TS 38.212 V18.0.0 (2023-12) "Multiplexing and channel coding"