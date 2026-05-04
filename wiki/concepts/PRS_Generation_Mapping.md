# PRS_Generation_Mapping

## 정의
[[PRS]] (Positioning Reference Signal)는 5G NR 시스템에서 UE의 위치 측정을 지원하기 위해 설계된 하향링크 [[Reference_Signals]]입니다. 네트워크는 PRS를 사용하여 [[RSTD]], [[RSRP]], [[RSRPP]] 및 UE Rx-Tx time difference와 같은 다양한 포지셔닝 측정을 수행합니다.

## 요약
PRS는 특정 시퀀스 생성 규칙에 따라 생성되며, 정의된 [[Physical_Resource_Grid]] 내의 자원 요소에 매핑됩니다. UE는 네트워크로부터 설정된 시간 윈도우 내에서 PRS를 측정하며, 관련 측정 보고 기능을 지원합니다. 주요 지원 기능은 다음과 같습니다.

* 41-2-9: Multi-RTT를 위한 특정 시간 윈도우 내 DL PRS-RSRP, DL PRS-RSRPP, UE Rx-Tx 측정 지원
* 13-11: Multi-RTT를 위한 UE Rx-Tx Measurement Report
* 41-2-8: DL TDoA를 위한 특정 시간 윈도우 내 DL PRS-RSRP, DL PRS-RSRPP, DL RSTD 측정 지원
* 41-1-7c/d: Tx time stamp 유무에 따른 SL PRS 측정
* 41-2-10: DL AoD를 위한 특정 시간 윈도우 내 DL PRS-RSRP, DL PRS-RSRPP 측정 지원
* 44-3: NTN 환경에서 단일 위성을 이용한 Multi-RTT 측정 및 보고
* 13-6: DL-TDOA를 위한 DL PRS Measurement Report
* 27-2-1: UE-assisted DL-AoD를 위한 첫 번째 경로의 DL PRS RSRPP 측정 보고
* 41-5-1: [[RedCap]] UE를 위한 MG 내 Rx frequency hopping 기반 PRS 측정 및 보고
* 13-5: DL-AoD를 위한 DL PRS Measurement Report
* 25-19a: RTT 기반 PDC 및 [[SRS]]를 위한 DL PRS 기반 전파 지연 보상

## 상세 설명
PRS 생성 및 매핑 절차는 TS 38.211에 정의되어 있습니다.

1. **Sequence Generation**: PRS 시퀀스는 골드 시퀀스(Gold sequence)를 기반으로 생성되며, 슬롯 번호, 심볼 인덱스, 그리고 상위 계층 파라미터에 의해 초기화됩니다.
2. **Mapping to Physical Resources**: 생성된 시퀀스는 DL PRS 자원 내의 특정 RE(Resource Element)에 매핑됩니다. 이때 주파수 도메인과 시간 도메인에서의 밀도(density)와 콤(comb) 패턴이 적용됩니다.
3. **Mapping to Slots**: PRS 자원 세트는 여러 슬롯에 걸쳐 구성될 수 있으며, 각 자원은 설정된 주기와 오프셋에 따라 반복적으로 전송됩니다.

## 인과 관계
- [[Frame_Structure_Numerology]] (depends_on): PRS의 시간/주파수 매핑은 설정된 뉴머롤로지에 의존합니다.
- [[PRS_Measurement_Procedures]] (triggers): PRS 전송은 UE의 포지셔닝 측정 절차를 유발합니다.

## 관련 개념
- [[Reference_Signals]] (part_of)
- [[PRS_Measurement_Procedures]] (affects)
- [[Frame_Structure_Numerology]] (depends_on)
- [[Physical_Resource_Grid]] (part_of)

## 스펙 근거
- TS 38.211 §7.4.1.7.1: PRS의 일반적인 정의 및 목적
- TS 38.211 §7.4.1.7.2: PRS 시퀀스 생성 알고리즘
- TS 38.211 §7.4.1.7.3: DL PRS 자원 내 물리 자원 매핑 규칙
- TS 38.211 §7.4.1.7.4: DL PRS 자원 세트 내 슬롯 매핑 규칙

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03)
- 3GPP TS 38.822 (UE Feature List)