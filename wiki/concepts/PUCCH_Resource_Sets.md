# PUCCH_Resource_Sets

## 정의
[[PUCCH]] Resource Set은 [[UE]]가 상향링크 제어 정보([[UCI]])를 전송하기 위해 사용할 수 있는 [[PUCCH]] 자원들의 집합을 의미하며, 전송할 [[UCI]] 비트 수에 따라 동적으로 선택되는 자원 풀을 정의합니다.

## 요약
[[PUCCH]] Resource Set은 상위 계층 시그널링을 통해 설정되며, [[UCI]] 페이로드 크기에 따라 적절한 자원 세트가 선택됩니다. 각 세트는 다수의 [[PUCCH]] 자원들로 구성되며, [[DCI]] 내의 PUCCH resource indicator 필드를 통해 최종 자원이 결정됩니다.

## 상세 설명
TS 38.213 §9.2.1에 따라 [[PUCCH]] 자원 구성은 다음과 같은 메커니즘을 따릅니다.

1. 자원 세트 설정: [[UE]]는 상위 계층 파라미터인 PUCCH-ResourceSet을 통해 최대 4개의 자원 세트를 설정받을 수 있습니다.
2. 세트 선택: 전송할 [[UCI]]의 총 비트 수(SR, [[HARQ]]-ACK, [[CSI]] 포함)에 따라 적절한 자원 세트가 선택됩니다.
   - 첫 번째 자원 세트(index 0)는 2비트 이하의 [[UCI]]를 지원하며, 설정된 경우 최대 32개의 자원을 포함합니다.
   - 나머지 자원 세트(index 1~3)는 2비트를 초과하는 [[UCI]]를 지원하며, 설정된 경우 최대 8개의 자원을 포함합니다.
3. 자원 선택: 선택된 자원 세트 내에서, [[PDCCH]]의 DCI format 1_0 또는 1_1에 포함된 'PUCCH resource indicator' 필드 값이 특정 자원을 지시합니다.
4. 기능적 요구사항:
   - [[TRS]] (CSI-RS for tracking) 지원은 [[UE]]의 필수 기능입니다.
   - [[SR]], [[HARQ]]-ACK, [[CSI]]의 다중화와 관련하여, 동일 슬롯 내 동일 시작 심볼에서의 다중화(4-19), 서로 다른 시작 심볼에서의 다중화(4-19a, 4-19c), 그리고 슬롯 내 다중 전송(4-19b) 기능이 지원됩니다.
   - [[Multi-TRP]] 환경에서의 [[PUCCH]] 반복 전송(23-3-2, 23-3-3) 및 공간 관계(Spatial relation) 업데이트(23-3-2d) 기능이 선택적으로 지원됩니다.
   - 상향링크 빔 관리(2-30) 및 경로 손실 추정 유지(13-9e, 13-9f) 기능이 지원됩니다.

## 인과 관계
- [[UCI_PUCCH_Multiplexing]] (depends_on): [[UCI]] 비트 수에 따라 적절한 [[PUCCH]] 자원 세트가 결정됨.
- [[PUCCH_Resource_Determination]] (affects): [[DCI]] 필드 값에 따라 최종적으로 사용할 자원이 결정됨.
- [[PUCCH_Spatial_Setting]] (depends_on): 선택된 자원에 설정된 공간적 파라미터가 전송 빔포밍에 영향을 미침.

## 관련 개념
- [[PUCCH]] (part_of)
- [[UCI]] (depends_on)
- [[DCI]] (triggers)
- [[PUCCH_Repetition]] (affects)

## 스펙 근거
- TS 38.213 §9.2.1: [[PUCCH]] Resource Set 설정 및 선택 절차 정의
- TS 38.822: 관련 [[UE]] 기능(Feature) 정의

## 소스
- 3GPP TS 38.213 Release 18, "NR; Physical layer procedures for control"
- 3GPP TS 38.822, "Study on NR feature evolution"