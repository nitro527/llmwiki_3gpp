# Rate_Matching

## 정의
[[Rate_Matching]]은 [[Channel_Coding]]을 거친 부호화된 비트(coded bits)를 물리 채널의 가용 자원 크기에 맞추어 선택, 인터리빙 및 조정하는 물리 계층 절차를 의미합니다.

## 요약
[[Rate_Matching]]은 전송 블록(TB)의 부호화된 비트를 물리적 자원 요소(RE)에 매핑하기 전, 가용 자원량에 따라 비트를 펑처링(puncturing)하거나 반복(repetition)하여 최종 전송 비트 수를 결정하는 과정입니다. 이는 [[LDPC]] 기반의 채널 코딩 이후 수행되며, 다중 슬롯 전송 시 슬롯별 자원 할당 상황에 따라 동적으로 수행됩니다.

## 상세 설명
[[Rate_Matching]] 절차는 TS 38.212 §5.4 및 §6.2.5에 정의되어 있습니다.

1. 기본 동작:
   각 코드 블록(CB)의 부호화된 비트 $d_{k}^{(r)}$은 레이트 매칭 블록으로 전달됩니다. 여기서 $r$은 코드 블록 번호, $K_{r}$은 해당 코드 블록의 부호화된 비트 수입니다.

2. 버퍼 관리:
   상위 계층 파라미터 `rateMatching`이 `limitedBufferRM`으로 설정된 경우, 제한된 버퍼 크기에 맞추어 레이트 매칭이 수행됩니다. 그렇지 않은 경우, 가용 자원에 따라 최적화된 매칭이 이루어집니다.

3. 다중 슬롯 전송 시의 동작:
   - DCI 내 `Time domain resource assignment` 필드에 의해 지시된 `numberOfSlotsTBoMS` 값이 1인 경우, 각 코드 블록은 슬롯 단위로 독립적으로 레이트 매칭됩니다.
   - `numberOfSlotsTBoMS` 값이 1보다 큰 경우, 각 슬롯은 전체 전송 블록의 가용 비트 수에 따라 레이트 매칭됩니다.
   - 첫 번째 슬롯이 아닌 경우, 이전 슬롯에서의 전송 상태(시작 비트 인덱스, 가용 비트 수, 스킵된 필러 비트 수 등)를 고려하여 TS 38.212 Table 5.4.2.1-2에 따라 레이트 매칭이 수행됩니다.

4. 자원 매핑:
   레이트 매칭이 완료된 비트 $f_{k}^{(r)}$은 물리 채널의 자원 요소에 매핑될 준비를 마칩니다. 이 과정에서 특정 신호(예: [[LTE_CRS]])가 점유한 자원을 회피하는 레이트 매칭 패턴이 적용될 수 있습니다.

## 인과 관계
- [[Channel_Coding]] depends_on [[Rate_Matching]] (채널 코딩 결과물이 레이트 매칭의 입력으로 사용됨)
- [[Rate_Matching]] affects [[PUSCH_Resource_Mapping]] (레이트 매칭된 비트가 물리 자원에 매핑됨)
- [[Rate_Matching]] affects [[PDSCH_Resource_Mapping]] (레이트 매칭된 비트가 물리 자원에 매핑됨)

## 관련 개념
- [[Channel_Coding]] (depends_on)
- [[PUSCH_Resource_Mapping]] (affects)
- [[PDSCH_Resource_Mapping]] (affects)
- [[LDPC]] (depends_on)

## 스펙 근거
- TS 38.212 §5.4: 레이트 매칭 일반 절차 및 알고리즘 정의
- TS 38.212 §6.2.5: PUSCH 및 다중 슬롯 전송 시의 레이트 매칭 상세 규칙

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03) "Multiplexing and channel coding"