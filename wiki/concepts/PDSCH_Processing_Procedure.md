# PDSCH_Processing_Procedure

## 정의
[[PDSCH]] 수신 후 [[UE]]가 해당 [[HARQ-ACK]] 정보를 [[PUCCH]]를 통해 전송하기까지 요구되는 최소한의 시간적 여유를 의미하며, 이는 [[TS_38_214]] §5.3에 정의된 처리 능력(Capability) 및 물리 계층 파라미터에 의해 결정된다.

## 요약
[[UE]]는 [[PDSCH]]의 마지막 심볼 종료 시점으로부터 [[HARQ-ACK]]을 포함하는 [[PUCCH]]의 첫 번째 심볼 시작 시점까지의 시간 간격이 최소 처리 시간 $T_{proc,1}$ 이상일 때 유효한 [[HARQ-ACK]] 메시지를 생성한다. 이 시간은 [[UE]]의 처리 능력(Capability 1 또는 2), [[SCS]](Subcarrier Spacing), [[PDSCH]] 매핑 타입, 그리고 추가적인 지연 파라미터에 따라 계산된다.

## 상세 설명
[[UE]]의 [[PDSCH]] 처리 시간은 다음의 수식과 절차를 따른다.

1. **기본 처리 시간 계산**:
   - $T_{proc,1} = (N_1 \cdot d_{1,1} + d_2) \cdot (2048 + 144) \cdot \kappa \cdot 2^{-\mu} \cdot T_c$
   - $N_1$은 [[TS_38_214]] Table 5.3-1(Capability 1) 및 Table 5.3-2(Capability 2)에 정의된 값으로, [[PDCCH]], [[PDSCH]], [[PUCCH]]의 [[SCS]] 중 가장 큰 $T_{proc,1}$을 유발하는 $\mu$를 기준으로 결정된다.
   - $\kappa$는 [[TS_38_211]] §4.1에 정의된 상수이다.

2. **매핑 타입별 지연 파라미터 ($d_{1,1}$)**:
   - **Mapping Type A**: [[PDSCH]]의 마지막 심볼이 슬롯 내 $i$-번째 심볼이고 $i < 7$인 경우 $d_{1,1} = 7 - i$, 그 외에는 $0$이다.
   - **Mapping Type B**:
     - Capability 1: 할당된 심볼 수 $L \ge 7$이면 $0$, $4 \le L \le 6$이면 $7-L$, $L=3$이면 $3 + \min(d, 1)$, $L=2$이면 $3+d$이다. ($d$는 스케줄링 [[PDCCH]]와 [[PDSCH]] 간 중첩 심볼 수)
     - Capability 2: $L \ge 7$이면 $0$, $3 \le L \le 6$이면 중첩 심볼 수, $L=2$인 경우 특정 조건(3-심볼 [[CORESET]] 등)에 따라 $3$ 또는 중첩 심볼 수로 결정된다.

3. **Capability 2 특수 조건**:
   - [[PDSCH]]-ServingCellConfig의 higher layer 파라미터 processingType2Enabled가 'enable'로 설정된 경우 적용된다.
   - [[DCI]] format 4_0, 4_1, 4_2로 스케줄링된 [[PDSCH]]에는 적용되지 않는다.
   - 30kHz [[SCS]]에서 136 [[RB]]를 초과하는 할당 시 Capability 1로 폴백(fallback)된다.

4. **기타 고려 사항**:
   - [[PUCCH]] 우선순위가 다른 채널과 충돌하거나 [[UCI_Multiplexing]]이 발생하는 경우 $d_2$가 추가 지연으로 반영된다.
   - 공유 스펙 채널 접속(Shared spectrum channel access) 시 추가적인 지연이 발생할 수 있다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_Processing_Procedure]] (수신 후 HARQ-ACK 전송 가능 여부 결정)
- [[HARQ_ACK_Reporting]] depends_on [[PDSCH_Processing_Procedure]] (유효한 보고 시점 산출)
- [[PUCCH]] depends_on [[PDSCH_Processing_Procedure]] (HARQ-ACK 전송을 위한 자원 및 타이밍 결정)
- [[PDCCH]] triggers [[PDSCH_Processing_Procedure]] (스케줄링 DCI 수신 시점부터 처리 시간 계산 시작)

## 관련 개념
- [[PDSCH]] (affects)
- [[HARQ_ACK_Reporting]] (depends_on)
- [[PUCCH]] (depends_on)
- [[PDCCH]] (triggers)
- [[Slot_Format_Configuration]] (affects)

## 스펙 근거
- [[TS_38_214]] §5.3: UE PDSCH processing procedure time 정의 및 계산식
- [[TS_38_211]] §4.1: $\kappa$ 및 $T_c$ 상수 정의
- [[TS_38_211]] §7.4.1.1: PDSCH mapping type A/B 및 DMRS 위치 정의
- [[TS_38_213]] §9.2.5: HARQ-ACK 다중화 절차

## 소스
- 3GPP TS 38.214 V16.x.x (PDSCH processing procedure)
- 3GPP TS 38.211 V16.x.x (Physical channels and modulation)
- 3GPP TS 38.213 V16.x.x (Physical layer procedures for control)