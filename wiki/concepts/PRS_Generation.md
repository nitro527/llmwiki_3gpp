# PRS_Generation

## 정의
Positioning Reference Signal(PRS)은 네트워크가 UE의 위치를 추정할 수 있도록 기지국에서 하향링크로 전송하는 참조 신호이다.

## 요약
PRS는 특정 시퀀스 생성 규칙에 따라 생성되며, 시간 및 주파수 자원에 매핑되어 전송된다. UE는 이 신호를 수신하여 도달 시간 차이(TDOA), 도달 각도(AoD), 왕복 시간(RTT) 등을 측정함으로써 위치 기반 서비스를 수행한다.

## 상세 설명
PRS 시퀀스 $r_{l, n_s^f, \mu}(m)$은 다음과 같은 의사 난수 시퀀스(pseudo-random sequence) 생성기를 기반으로 정의된다.

$r_{l, n_s^f, \mu}(m) = \frac{1}{\sqrt{2}}(1 - 2 \cdot c(2m)) + j \frac{1}{\sqrt{2}}(1 - 2 \cdot c(2m + 1))$

여기서 $c(i)$는 Gold 시퀀스이며, 초기값 $c_{init}$은 슬롯 번호, 심볼 번호, 그리고 상위 계층에서 설정된 파라미터들에 의해 결정된다.

PRS 자원 매핑은 다음과 같은 규칙을 따른다.
1. 주파수 도메인에서 PRS는 서브캐리어 간격(SCS)에 따라 정의된 오프셋과 콤(comb) 구조를 사용하여 매핑된다.
2. 시간 도메인에서 PRS는 설정된 슬롯 내의 특정 OFDM 심볼에 위치한다.
3. PRS 자원 요소(RE)는 해당 자원 내에서 주파수 홉핑 및 콤 패턴에 따라 분산 배치되어 다중 셀 환경에서의 간섭을 최소화한다.

UE는 DL PRS를 사용하여 DL-TDOA, DL AoD, Multi-RTT 측정을 수행하며, 이를 위해 서빙 셀 및 인접 셀로부터의 PRS를 처리한다. 또한, SRS for positioning과 연동하여 공간적 관계(spatial relation)를 설정하거나, OLPC(Outer Loop Power Control)를 통해 상향링크 위치 측정 신호의 전송 전력을 제어한다.

## 인과 관계
- [[PRS_Generation]] depends_on [[Sequence_Generation]] (Gold 시퀀스 생성 알고리즘 사용)
- [[PRS_Generation]] affects [[PRS_Measurement_Procedure]] (측정 대상 신호 제공)
- [[PRS_Generation]] triggers [[SRS_Positioning_Procedure]] (측정된 PRS 기반의 상향링크 위치 측정 절차 개시)

## 관련 개념
- [[Sequence_Generation]] (depends_on)
- [[PRS_Measurement_Procedure]] (affects)
- [[SRS_Positioning_Procedure]] (triggers)
- [[Frame_Structure]] (part_of)

## 스펙 근거
TS 38.211 §7.4.1.7에 따르면, 하향링크 PRS는 위치 측정 목적을 위해 정의되며, 시퀀스 생성 및 자원 요소 매핑 규칙은 해당 섹션의 수식 및 파라미터 정의를 따른다.

## 소스
- 3GPP TS 38.211 V17.9.0, "NR; Physical channels and modulation"