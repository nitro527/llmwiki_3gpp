# PSCCH_Resource_Mapping

## 정의
[[PSCCH]] 물리 자원 매핑은 복소수 변조 심볼을 사이드링크 자원 풀 내의 물리적 자원 요소(Resource Element, RE)에 할당하는 물리 계층 절차를 의미한다.

## 요약
[[PSCCH]] 전송을 위해 변조된 심볼은 전력 제어를 위한 진폭 스케일링을 거친 후, 할당된 자원 내에서 [[DMRS]], [[PTRS]], [[CSI_RS]] 등 참조 신호가 점유하지 않는 RE에 순차적으로 매핑된다. 첫 번째 OFDM 심볼에 매핑되는 자원(참조 신호 포함)은 직전 OFDM 심볼에 복제되어 전송된다.

## 상세 설명
TS 38.211 §8.3.2.3에 따라 [[PSCCH]]의 물리 자원 매핑은 다음과 같이 수행된다.

1. 진폭 스케일링: 복소수 변조 심볼 집합은 TS 38.213의 16.4절에 명시된 전송 전력을 준수하기 위해 진폭 스케일링 계수와 곱해진다.
2. RE 매핑 순서: 스케일링된 심볼은 할당된 자원 내의 RE에 매핑된다. 이때 매핑 순서는 다음 규칙을 따른다.
   - 할당된 물리 자원 내에서 주파수 인덱스(k)가 증가하는 순서대로 매핑한다.
   - 이후 안테나 포트 인덱스 순서대로 매핑을 진행한다.
3. 제외 대상: [[PSCCH]]와 관련된 [[DMRS]]가 점유하는 RE는 매핑 대상에서 제외된다.
4. 심볼 복제: 매핑 절차 중 첫 번째 OFDM 심볼에 위치하는 RE(해당 심볼에 포함된 [[DMRS]], [[PTRS]], [[CSI_RS]] 포함)는 직전 OFDM 심볼에 동일하게 복제되어 전송된다.

## 인과 관계
- [[PSCCH_Resource_Mapping]] depends_on [[PSCCH_DMRS_Mapping]] (DMRS 점유 RE 제외 필요)
- [[PSCCH_Resource_Mapping]] depends_on [[PSCCH_Modulation]] (변조 심볼 입력)

## 관련 개념
- [[PSCCH]] (part_of)
- [[DMRS]] (affects)
- [[PTRS]] (affects)
- [[CSI_RS]] (affects)

## 스펙 근거
- TS 38.211 §8.3.2.3: Mapping to physical resources 절차 정의
- TS 38.213 §16.4: 사이드링크 전송 전력 및 자원 할당 관련 규정

## 소스
- 3GPP TS 38.211 V16.9.0 (Release 16) Physical channels and modulation