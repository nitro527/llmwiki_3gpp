# RIM_RS_Generation

## 정의
RIM-RS(Remote Interference Management Reference Signal)는 네트워크 노드 간의 원격 간섭을 관리하고 측정하기 위해 정의된 참조 신호이다.

## 요약
RIM-RS는 기지국 간의 간섭을 식별하고 완화하기 위한 목적으로 사용되는 신호이다. TS 38.211에 정의된 시퀀스 생성 규칙을 따르며, 특정 자원 구성에 따라 물리 계층에서 생성 및 매핑된다.

## 상세 설명
RIM-RS 시퀀스 $r_{l, n_s^\mu}(m)$은 다음과 같이 정의된다.

$r_{l, n_s^\mu}(m) = \frac{1}{\sqrt{2}}(1 - 2c(2m)) + j\frac{1}{\sqrt{2}}(1 - 2c(2m+1))$

여기서 $m = 0, 1, \dots, N_{RB}^{RIM, RS} \cdot N_{sc}^{RB} - 1$이며, $N_{RB}^{RIM, RS}$는 RIM-RS가 점유하는 자원 블록의 수이다.

1. 시퀀스 생성: 의사 난수 생성기(pseudo-random sequence generator) $c(i)$는 TS 38.211 §5.2.1에 정의된 Gold 시퀀스를 사용한다.
2. 초기화: 시퀀스 생성기의 초기값 $c_{init}$은 RIM-RS의 설정에 따라 결정되며, 이는 셀 ID 및 특정 파라미터에 의존한다.
3. 자원 매핑: 생성된 시퀀스는 시간 및 주파수 영역의 지정된 자원 요소(Resource Element)에 매핑된다. RIM-RS는 특정 심볼과 부반송파 위치에 배치되어 간섭 측정의 기준이 된다.

## 인과 관계
- [[Sequence_Generation]] implements [[RIM_RS_Generation]] (시퀀스 생성 알고리즘 활용)

## 관련 개념
- [[Sequence_Generation]] (depends_on)
- [[SRS_CLI_Measurement]] (affects)

## 스펙 근거
- TS 38.211 §7.4.1.6: RIM reference signals 정의 및 시퀀스 생성 공식

## 소스
- 3GPP TS 38.211 V17.0.0, "NR; Physical channels and modulation"