# PSCCH_Resource_Mapping

## 정의
[[PSCCH]] (Physical Sidelink Control Channel) 물리 자원 매핑은 [[Sidelink]] 통신에서 [[SCI]] (Sidelink Control Information)를 전송하기 위해 물리 자원 블록(PRB)과 OFDM 심볼에 신호를 배치하는 절차를 의미합니다.

## 요약
PSCCH는 [[PSSCH]]와 함께 전송되며, 특정 자원 풀 내에서 정의된 시간 및 주파수 자원에 매핑됩니다. UE는 상위 계층에서 설정된 자원 풀 내에서 SCI 포맷 1-A 또는 1-B를 포함하는 PSCCH를 전송하며, 이는 TS 38.211 및 TS 38.213에 정의된 절차를 따릅니다.

## 상세 설명
PSCCH의 물리 자원 매핑은 다음과 같은 과정을 포함합니다.

1. **자원 할당**: UE는 상위 계층으로부터 설정된 자원 풀 내에서 PSCCH 전송을 위한 자원을 선택합니다. 이때 [[Sidelink]] 모드 2 동작을 지원하는 UE는 자원 선택 절차를 수행합니다.
2. **매핑 규칙**: PSCCH는 PSSCH와 동일한 슬롯 내에서 전송됩니다. TS 38.211 §8.3.2.3에 따라, PSCCH에 매핑되는 복소 심볼은 해당 자원 풀에 대해 설정된 주파수 영역의 PRB와 시간 영역의 OFDM 심볼에 배치됩니다.
3. **SCI 전송**: PSCCH를 통해 전송되는 SCI 포맷 1-A 또는 1-B는 PSSCH의 자원 할당, [[HARQ]] 정보, 변조 및 코딩 방식(MCS) 등을 포함합니다.
4. **SL PRS 전송**: 전용 [[SL_PRS]] 자원 풀이 설정된 경우, UE는 TS 38.213 §16.4A에 정의된 절차에 따라 해당 풀 내에서 PSCCH를 전송합니다.

## 인과 관계
- [[Sidelink_Resource_Selection]] (triggers) PSCCH 자원 결정
- [[PSCCH_Modulation]] (depends_on) PSCCH 물리 자원 매핑의 심볼 배치
- [[PSSCH]] (part_of) PSCCH와 동일한 슬롯 내 전송

## 관련 개념
- [[PSCCH]] (part_of)
- [[PSSCH]] (affects)
- [[SCI]] (depends_on)
- [[SL_PRS]] (affects)

## 스펙 근거
- TS 38.211 §8.3.2.3: PSCCH의 물리 자원 매핑 규칙 정의
- TS 38.213 §16.4: PSCCH 전송을 위한 UE 절차
- TS 38.213 §16.4A: 전용 SL PRS 자원 풀에서의 PSCCH 전송 절차

## 소스
- 3GPP TS 38.211 V16.9.0, "Physical channels and modulation"
- 3GPP TS 38.213 V16.9.0, "Physical layer procedures for control"