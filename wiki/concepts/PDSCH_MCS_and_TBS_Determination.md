# PDSCH_MCS_and_TBS_Determination

## 정의
[[PDSCH]] 전송을 위해 [[DCI]] 내의 MCS(Modulation and Coding Scheme) 필드와 RV(Redundancy Version) 필드를 해석하고, 할당된 자원 정보를 바탕으로 전송 블록 사이즈(TBS, Transport Block Size)를 산출하며, UE의 처리 능력에 따른 수신 제약 조건을 검증하는 절차를 의미한다.

## 요약
UE는 [[DCI]]의 5비트 MCS 필드를 통해 변조 차수(Qm)와 타겟 코드 레이트(R)를 결정하고, RV 필드를 통해 재전송 정보를 확인한다. 이후 할당된 레이어 수(ʋ)와 PRB(Physical Resource Block) 수를 사용하여 TBS를 결정한다. 또한, UE는 특정 시간 구간 내의 처리 부하가 자신의 처리 능력(Capability)을 초과하지 않는지 검증하여, 조건 미충족 시 해당 [[PDSCH]] 수신을 수행하지 않을 수 있다.

## 상세 설명
1. **MCS 및 RV 결정**:
   - UE는 [[DCI]] 내 5비트 MCS 필드($I_{MCS}$)를 읽어 TS 38.214 §5.1.3.1에 정의된 절차에 따라 변조 차수($Q_m$)와 타겟 코드 레이트($R$)를 결정한다.
   - [[DCI]] 내 RV 필드를 통해 해당 전송의 재전송 버퍼 상태를 결정한다.
   - 유효 채널 코드 레이트가 0.95를 초과하는 경우, UE는 초기 전송에 대한 디코딩을 생략할 수 있다.

2. **TBS 결정**:
   - UE는 레이어 수($\nu$), 레이트 매칭 전 총 PRB 수($n_{PRB}$)를 사용하여 TS 38.214 §5.1.3.2에 정의된 절차에 따라 TBS를 산출한다.
   - 다중 [[PDSCH]]가 스케줄링된 경우, [[DCI]]의 RV 및 NDI(New Data Indicator) 필드 비트는 스케줄링 순서에 따라 각 [[PDSCH]]에 1:1 매핑된다.

3. **UE 처리 능력 기반 수신 제약**:
   - **14 심볼 구간 제약**: 특정 14 심볼(Normal CP 기준) 구간 내에서 처리해야 할 코드 블록(CB)의 총합이 정의된 임계치를 초과할 경우, UE는 해당 [[PDSCH]] 수신을 기대하지 않는다. 이는 서브캐리어 스페이싱($\mu, \mu'$), 코드 블록 수($C_i'$), 심볼 할당 정보($L_i, x_i$) 등을 고려하여 계산된다.
   - **슬롯 기반 제약**: 셀 그룹 내에서 슬롯 $s_j$에 할당된 모든 TB의 처리 부하가 해당 주파수 대역의 최대 데이터 레이트($R_{LBRM}$)를 초과하는 경우, UE는 해당 슬롯의 [[PDSCH]] 수신을 수행하지 않는다.
   - **처리 타입 2 및 고속 MCS 제약**: `processingType2Enabled`가 활성화되었거나 특정 MCS 임계치($W$)를 초과하는 경우, 더 엄격한 처리 능력 검증 공식이 적용된다.

## 인과 관계
- [[PDSCH]] depends_on [[PDSCH_MCS_and_TBS_Determination]] (데이터 수신을 위한 파라미터 결정)
- [[PDSCH_MCS_and_TBS_Determination]] depends_on [[DCI_Field_Mapping]] (MCS 및 RV 정보 획득)
- [[PDSCH_MCS_and_TBS_Determination]] depends_on [[Rate_Matching]] (TBS 산출 시 레이트 매칭 정보 활용)
- [[PDSCH_MCS_and_TBS_Determination]] depends_on [[Code_Block_Segmentation]] (CB 수 기반 처리 능력 검증)

## 관련 개념
- [[PDSCH]] (part_of)
- [[DCI]] (depends_on)
- [[Rate_Matching]] (depends_on)
- [[Code_Block_Segmentation]] (depends_on)

## 스펙 근거
- TS 38.214 §5.1.3: 변조 차수, 타겟 코드 레이트, RV 및 TBS 결정 절차
- TS 38.214 §5.1.3.1: MCS 테이블 기반 변조 및 코드 레이트 결정
- TS 38.214 §5.1.3.2: TBS 결정 절차
- TS 38.212 §5.4.2.1: 코드 블록 및 레이트 매칭 관련 파라미터 정의

## 소스
- 3GPP TS 38.214 v16.9.0 (Release 16)