# PDCCH_Resource_Mapping

## 정의
[[PDCCH_Resource_Mapping]]은 [[PDCCH]] 전송을 위해 상위 계층에서 설정된 [[CORESET]] 내의 [[CCE]]를 물리 자원 요소인 [[REG]]에 매핑하고, 이를 최종적으로 물리 자원 블록(PRB) 및 OFDM 심볼에 할당하는 절차를 의미한다.

## 요약
[[PDCCH]]는 [[CORESET]] 내에서 [[CCE]] 단위로 구성되며, 각 [[CCE]]는 6개의 [[REG]]로 이루어진다. [[CCE]]-to-[[REG]] 매핑은 비인터리빙(non-interleaved) 또는 인터리빙(interleaved) 방식으로 설정될 수 있다. 인터리빙 방식의 경우 [[REG]] 번들(bundle) 단위로 자원을 분산시켜 주파수 다이버시티 이득을 얻으며, 비인터리빙 방식은 [[CCE]]가 연속적인 [[REG]]들로 구성된다.

## 상세 설명
[[CORESET]]은 주파수 도메인의 자원 블록과 시간 도메인의 심볼로 정의된다. [[CCE]]는 6개의 [[REG]]로 구성되며, 여기서 1개의 [[REG]]는 1개의 OFDM 심볼 내 1개의 자원 블록(RB)에 대응한다.

1. [[REG]] 번호 매핑: [[CORESET]] 내의 [[REG]]들은 시간 우선(time-first) 방식으로 번호가 매겨지며, 첫 번째 OFDM 심볼의 가장 낮은 RB 인덱스부터 0으로 시작한다.
2. [[CCE]]-to-[[REG]] 매핑 방식:
   - 비인터리빙(non-interleaved): [[REG]] 번들 크기 $L=6$이며, [[CCE]] $i$는 [[REG]] 번들 $i$로 구성된다.
   - 인터리빙(interleaved): [[REG]] 번들 크기 $L \in \{2, 3, 6\}$으로 설정 가능하며, 인터리버(interleaver)를 통해 [[REG]] 번들이 분산된다. 인터리버는 TS 38.211 §7.3.2.2에 정의된 수식에 따라 [[REG]] 번들을 섞는다.
3. 물리 자원 매핑: 복소 심볼 블록은 [[PDCCH]] [[DMRS]]가 사용하지 않는 자원 요소(RE)에 매핑된다. 매핑 순서는 주파수 도메인(RB 인덱스)을 먼저 채우고 시간 도메인(심볼 인덱스)을 채우는 방식이다.
4. [[CORESET]] 0: [[MIB]] 또는 [[SIB1]]을 통해 설정되는 [[CORESET]] 0은 특정 규칙에 따라 [[CCE]]-to-[[REG]] 매핑이 결정되며, 일부 대역폭에서는 특정 RB를 펑처링(puncturing)하여 자원을 구성한다.

## 인과 관계
- [[PDCCH_Resource_Mapping]] depends_on [[CORESET_Configuration]] (매핑 파라미터 및 자원 범위 결정)
- [[PDCCH_Resource_Mapping]] affects [[PDCCH_Search_Space_Configuration]] (CCE 인덱싱에 따른 후보 위치 결정)
- [[PDCCH_Resource_Mapping]] implements [[DMRS_Resource_Mapping]] (DMRS 위치를 제외한 RE 매핑)

## 관련 개념
- [[CORESET]] (part_of)
- [[CCE]] (part_of)
- [[REG]] (part_of)
- [[PDCCH]] (depends_on)
- [[DMRS]] (affects)

## 스펙 근거
- TS 38.211 §7.3.2.2: [[CORESET]] 정의 및 [[CCE]]-to-[[REG]] 매핑 절차
- TS 38.211 §7.3.2.5: 물리 자원 요소 매핑 규칙
- TS 38.213 §10.1: [[PDCCH]] 후보 결정 및 [[CCE]] 인덱싱 절차

## 소스
- 3GPP TS 38.211 (Physical channels and modulation)
- 3GPP TS 38.213 (Physical layer procedures for control)