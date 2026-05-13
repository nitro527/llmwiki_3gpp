# SRS_Generation

## 정의
[[SRS]] (Sounding Reference Signal) 시퀀스 생성은 상향링크 채널 품질 측정 및 빔 관리를 위해 [[UE]]가 기지국으로 전송하는 참조 신호의 시퀀스를 생성하고, 이를 시간-주파수 자원에 매핑하는 절차를 의미한다.

## 요약
[[SRS]]는 상위 계층 파라미터에 의해 설정된 시퀀스 ID, 순환 시프트(Cyclic Shift), 전송 콤(Transmission Comb) 등을 사용하여 생성된다. 시퀀스는 기본적으로 Zadoff-Chu 시퀀스를 기반으로 하며, 주파수 호핑, 콤 오프셋, 안테나 포트 매핑을 통해 다양한 채널 환경에 적응적으로 전송된다.

## 상세 설명
[[SRS]] 시퀀스 $r_{SRS}^{(p, l')}(n)$은 TS 38.211 §6.4.1.4.2에 따라 다음과 같이 정의된다.

$r_{SRS}^{(p, l')}(n) = r_{u,v}^{(\alpha_p, \delta)}(n)$

여기서 $r_{u,v}^{(\alpha_p, \delta)}(n)$은 기본 시퀀스에 순환 시프트 $\alpha_p$가 적용된 형태이다.

### 1. 시퀀스 생성 파라미터
- 순환 시프트 $\alpha_p$: 안테나 포트 $p$에 대해 $\alpha_p = 2\pi n_{shift}^{p} / n_{SRS}^{cs}$로 결정되며, $n_{shift}^{p}$는 상위 계층 파라미터 `transmissionComb` 및 `cyclicShift` 설정에 따라 결정된다.
- 시퀀스 그룹 호핑 및 시퀀스 호핑: 상위 계층 파라미터 `groupOrSequenceHopping` 설정에 따라 비활성화되거나, 의사 난수 시퀀스(Pseudo-random sequence) $c(i)$를 사용하여 매 슬롯마다 호핑이 수행된다.
- 시퀀스 ID: 상위 계층 파라미터 `sequenceId`를 통해 초기화된다.

### 2. 자원 매핑 및 설정
- 안테나 포트: `nrofSRS-Ports` 또는 `nrofSRS-Ports-n8` 파라미터에 의해 결정되며, `ports8tdm` 설정 시 2개의 심볼에 걸쳐 포트가 분산된다.
- 주파수 호핑: `numberOfHops` 및 `freqHopping` 파라미터에 의해 주파수 도메인 시작 위치가 호핑된다.
- 시간 도메인 매핑: `resourceMapping` 파라미터의 `nrofSymbols` 및 `startPosition`을 통해 슬롯 내 심볼 위치가 결정된다.
- 전송 콤(Transmission Comb): `transmissionComb` 파라미터는 2, 4, 8 중 하나로 설정되며, 이는 주파수 도메인에서 샘플링 간격을 결정한다.

### 3. 동작 모드
- 주기적(Periodic), 반-지속적(Semi-persistent), 비주기적(Aperiodic) 전송 모드를 지원하며, 비주기적 SRS는 [[DCI]]를 통해 트리거된다.
- 공간 관계(Spatial Relation): `spatialRelationInfo`를 통해 참조 신호([[SSB]], [[CSI_RS]], 또는 다른 [[SRS]])와 동일한 공간 필터를 사용하도록 설정할 수 있다.

## 인과 관계
- [[SRS_Generation]] depends_on [[Sequence_Generation]] (기본 시퀀스 생성 알고리즘 사용)
- [[SRS_Generation]] affects [[SRS_Mapping]] (생성된 시퀀스를 물리 자원에 매핑)
- [[SRS_Generation]] depends_on [[DCI_Field_Mapping]] (비주기적 SRS 트리거링)
- [[SRS_Generation]] affects [[SRS_Power_Control]] (전송 전력 결정)

## 관련 개념
- [[SRS]] (part_of)
- [[SRS_Mapping]] (affects)
- [[Sequence_Generation]] (depends_on)
- [[DCI_Field_Mapping]] (depends_on)
- [[SRS_Power_Control]] (affects)
- [[SRS_Spatial_Relation]] (implements)

## 스펙 근거
- TS 38.211 §6.4.1.4.1: SRS 자원 설정 및 안테나 포트/심볼 매핑
- TS 38.211 §6.4.1.4.2: SRS 시퀀스 생성 및 순환 시프트 호핑
- TS 38.214 §6.2.1: UE 사운딩 절차 및 트리거링 메커니즘

## 소스
- 3GPP TS 38.211 (Release 16/17/18)
- 3GPP TS 38.214 (Release 16/17/18)