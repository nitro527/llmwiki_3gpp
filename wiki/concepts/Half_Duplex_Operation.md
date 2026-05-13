# Half_Duplex_Operation

## 정의
페어드 스펙트럼(paired spectrum)을 사용하는 서빙 셀에서 동일한 시간 자원 내에 송신과 수신을 동시에 수행할 수 없는 UE의 동작 방식을 의미한다.

## 요약
Half-Duplex UE는 페어드 스펙트럼 내에서 상향링크와 하향링크의 동시 전송 및 수신이 불가능하다. 따라서 상향링크 전송과 하향링크 수신이 시간적으로 겹칠 경우, 스펙에 정의된 우선순위 규칙에 따라 특정 동작을 취소하거나 선택적으로 수행해야 한다. 또한, SS/PBCH 블록과의 시간적 충돌을 방지하기 위한 보호 구간 및 전송 제한 규칙을 준수해야 한다.

## 상세 설명
Half-Duplex UE는 페어드 스펙트럼 내에서 상향링크와 하향링크의 동시 동작을 지원하지 않는다.

1. 충돌 해결 메커니즘:
- UE는 하향링크 수신(PDCCH, PDSCH, CSI-RS, DL PRS)을 위한 DCI 포맷과 상향링크 전송(PUSCH, PUCCH, PRACH, SRS)을 위한 DCI 포맷을 동일한 심볼 세트 내에서 동시에 검출하지 않는다.
- 상위 계층에 의해 하향링크 수신이 설정된 심볼 세트에서, UE가 상향링크 전송을 지시하는 DCI를 검출하지 못한 경우에만 하향링크 수신을 수행한다.
- 상향링크 전송이 설정된 심볼 세트에서 하향링크 수신 DCI가 검출될 경우, UE는 PUSCH/PUCCH 전송을 취소할 수 있다. 단, 해당 DCI를 수신한 PDCCH의 마지막 심볼로부터 PUSCH 준비 시간(N2) 이내에 첫 심볼이 위치하는 경우 전송 취소를 기대하지 않는다. SRS의 경우, DCI 수신 PDCCH의 마지막 심볼로부터 N2 이내에 위치하는 심볼은 취소하지 않으며, 그 외의 심볼은 취소한다.

2. SS/PBCH 블록 연동:
- UE는 활성 DL BWP 내에 SS/PBCH 블록이 존재함을 인지할 경우, SS/PBCH 블록의 전후로 특정 시간 간격(N_gap)을 유지해야 한다.
- PUSCH, PUCCH, SRS 전송은 SS/PBCH 블록의 첫 심볼 이전 또는 마지막 심볼 이후에 N_gap 이상의 간격을 두지 못할 경우 전송이 제한된다.
- PRACH 또는 MsgA PUSCH가 상위 계층에 의해 트리거된 경우, SS/PBCH 블록과의 충돌 시 구현에 따라 전송 또는 수신 중 하나를 선택할 수 있다.

## 인과 관계
- [[PDCCH]] depends_on [[Half_Duplex_Operation]] (HD-UE의 수신 동작 제약)
- [[PUSCH]] depends_on [[Half_Duplex_Operation]] (HD-UE의 전송 취소 및 SS/PBCH 블록 보호 규칙)
- [[PUCCH]] depends_on [[Half_Duplex_Operation]] (HD-UE의 전송 취소 및 SS/PBCH 블록 보호 규칙)
- [[SRS]] depends_on [[Half_Duplex_Operation]] (HD-UE의 전송 취소 및 SS/PBCH 블록 보호 규칙)
- [[PRACH]] depends_on [[Half_Duplex_Operation]] (HD-UE의 전송 선택 규칙)
- [[SS_PBCH_Block_Generation]] affects [[Half_Duplex_Operation]] (SS/PBCH 블록 위치에 따른 전송 제한)

## 관련 개념
- [[PDCCH]] (depends_on)
- [[PUSCH]] (depends_on)
- [[PUCCH]] (depends_on)
- [[SRS]] (depends_on)
- [[PRACH]] (depends_on)
- [[SS_PBCH_Block_Generation]] (affects)

## 스펙 근거
- TS 38.213 §17.2: 페어드 스펙트럼 내 HD-UE의 동작 정의 및 충돌 해결 절차
- TS 38.211 §4: SS/PBCH 블록 관련 시간 간격 및 심볼 정의

## 소스
- 3GPP TS 38.213 v18.0.0 (2024-03) §17.2