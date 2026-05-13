# CSI_RS_Generation

## 정의
CSI-RS(Channel State Information Reference Signal)는 5G NR 시스템에서 채널 상태 측정, 빔 관리, 시간/주파수 추적 및 이동성 측정을 위해 하향링크로 전송되는 참조 신호이다.

## 요약
CSI-RS는 TS 38.211 §7.4.1.5에 정의된 시퀀스 생성 규칙에 따라 생성되며, NZP(Non-Zero Power) CSI-RS와 ZP(Zero Power) CSI-RS로 구분된다. UE는 이를 활용하여 CSI 피드백, L1-RSRP/SINR 측정, 그리고 TRS(Tracking Reference Signal)를 통한 시간 및 주파수 오프셋 추적을 수행한다.

## 상세 설명
CSI-RS 시퀀스는 의사 난수 생성기(pseudo-random sequence generator)를 기반으로 생성되며, 슬롯 내의 OFDM 심볼 인덱스, 슬롯 인덱스, 그리고 상위 계층 파라미터에 의해 초기화된다.

1. 시퀀스 생성:
   CSI-RS 시퀀스 $r_{l,n_s^f}(m)$은 TS 38.211 §7.4.1.5.2에 따라 생성된다. 시퀀스 생성기의 초기값 $c_{init}$은 슬롯 번호, OFDM 심볼 번호, 그리고 상위 계층에서 설정된 스크램블링 ID($n_{ID}$)를 포함한다.

2. 자원 매핑:
   CSI-RS 자원은 주파수 도메인에서 RE(Resource Element) 단위로 매핑되며, 설정된 밀도(density)와 빗살(comb) 구조에 따라 배치된다. 특정 PRB 내에서 PDSCH나 CORESET과 중첩되는 경우, 상위 계층 설정에 따라 레이트 매칭(rate matching) 또는 펑처링(puncturing)이 수행된다.

3. 추적용 자원(TRS) 설정:
   TRS는 시간 및 주파수 추적을 위해 사용되는 NZP-CSI-RS 자원 세트이다. 상위 계층 파라미터 `repetition`이 'on'으로 설정된 경우, UE는 해당 자원 세트 내의 CSI-RS가 동일한 공간적 필터(spatial filter)를 사용하여 전송됨을 가정할 수 있다.

4. 수신 절차 및 QCL(Quasi-Co-Location):
   UE는 CSI-RS 수신 시 설정된 QCL 정보를 바탕으로 채널을 추정한다. CORESET과 동일한 OFDM 심볼에서 CSI-RS를 수신할 경우, 'typeD' QCL 가정이 적용 가능하다면 UE는 이를 동일한 공간적 특성을 가진 것으로 간주한다. 단, CORESET이 두 개의 TCI 상태로 활성화된 경우, 첫 번째 TCI 상태를 기본 QCL 가정으로 사용한다.

5. DRX 및 DTX 동작:
   UE가 DRX 모드인 경우, CSI 보고를 위한 측정 시점은 DRX active time 또는 `drx-onDurationTimer` 구간 내로 제한된다. Cell DTX가 활성화된 경우, RI(Rank Indicator)를 포함하는 CSI 보고를 위한 주기적/반영구적 CSI-RS 수신은 DTX active period 내에서만 기대된다.

## 인과 관계
- [[CSI_RS_Generation]] depends_on [[OFDM_Baseband_Signal_Generation]] (기저대역 신호 생성 절차 활용)
- [[CSI_RS_Generation]] affects [[CSI_Reporting_Procedure]] (측정된 채널 정보를 기반으로 보고 수행)
- [[CSI_RS_Generation]] affects [[PDSCH_Reception_Procedure]] (TCI 상태 및 QCL 가정을 통한 수신 성능 최적화)
- [[CSI_RS_Generation]] depends_on [[CORESET_Configuration]] (중첩 자원 회피 및 QCL 가정 설정)

## 관련 개념
- [[CSI_Reporting_Procedure]] (affects)
- [[PDSCH_Reception_Procedure]] (affects)
- [[CORESET_Configuration]] (depends_on)
- [[OFDM_Baseband_Signal_Generation]] (depends_on)

## 스펙 근거
- TS 38.211 §7.4.1.5: CSI reference signals 시퀀스 생성 및 자원 매핑 정의
- TS 38.214 §5.1.6.1: CSI-RS 수신 절차, QCL 가정, DRX/DTX 동작 및 자원 중첩 처리 규칙

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03)
- 3GPP TS 38.214 V16.9.0 (2022-03)