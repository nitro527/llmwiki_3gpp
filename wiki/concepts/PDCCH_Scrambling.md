# PDCCH_Scrambling

## 정의
[[PDCCH]] 전송을 위해 채널 코딩된 비트 시퀀스에 대해 물리 계층에서 수행하는 비트 단위의 스크램블링 절차를 의미합니다.

## 요약
[[PDCCH]]의 스크램블링은 [[RNTI]] 및 [[DMRS_Generation_Mapping]]에서 사용되는 [[ScramblingID]]를 기반으로 초기화된 의사 난수 시퀀스를 사용하여 수행됩니다. 이는 데이터의 보안성을 높이고 셀 간 간섭을 무작위화하기 위한 필수적인 물리 계층 절차입니다.

## 상세 설명
[[PDCCH]] 스크램블링 과정은 다음과 같은 단계로 진행됩니다.
1. 입력된 비트 시퀀스 $b(0), b(1), \dots, b(M_{bit}-1)$에 대해 스크램블링이 적용됩니다.
2. 스크램블링 시퀀스 $c(i)$는 [[TS_38_211]] §7.3.2.3에 정의된 골드 시퀀스 생성기를 통해 생성됩니다.
3. 시퀀스 생성기의 초기값 $c_{init}$은 다음과 같이 결정됩니다.
   - $c_{init} = n_{RNTI} \cdot 2^{16} + n_{ID}$
   - 여기서 $n_{RNTI}$는 해당 [[PDCCH]] 전송과 관련된 [[RNTI]] 값입니다.
   - $n_{ID}$는 상위 계층 파라미터인 [[pdcch_DMRS_ScramblingID]]에 의해 결정되며, 만약 해당 파라미터가 설정되지 않은 경우 셀 ID인 $N_{ID}^{cell}$이 사용됩니다.
4. 출력 비트 시퀀스 $\tilde{b}(i)$는 입력 비트 $b(i)$와 스크램블링 시퀀스 $c(i)$의 모듈로-2 합으로 계산됩니다: $\tilde{b}(i) = (b(i) + c(i)) \mod 2$.

## 인과 관계
- [[PDCCH_Scrambling]] depends_on [[RNTI]]
- [[PDCCH_Scrambling]] depends_on [[DMRS_Generation_Mapping]]
- [[PDCCH_Scrambling]] affects [[PDCCH_Modulation]]

## 관련 개념
- [[PDCCH]] (part_of)
- [[RNTI]] (depends_on)
- [[DMRS_Generation_Mapping]] (depends_on)
- [[PDCCH_Modulation]] (affects)
- [[Beam_failure_recovery]] (triggers)

## 스펙 근거
- [[TS_38_211]] §7.3.2.3: PDCCH 스크램블링 시퀀스 생성 및 초기화 공식 정의.
- [[TS_38_822]] (UE Feature 2-31): [[Beam_failure_recovery]] 관련 PDCCH 모니터링 및 스크램블링 요구사항 명시.

## 소스
- [[TS_38_211]] v19.0.0
- [[TS_38_822]] v17.0.0