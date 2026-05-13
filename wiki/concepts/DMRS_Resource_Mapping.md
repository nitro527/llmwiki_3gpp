# DMRS_Resource_Mapping

## 정의
[[DMRS_Resource_Mapping]]은 [[PUSCH]] 전송 시 채널 추정을 위해 사용되는 [[DMRS]] 심볼을 물리 자원 요소(RE)에 매핑하고, 안테나 포트를 할당하는 절차를 의미합니다.

## 요약
[[DMRS]]는 상위 계층 설정 및 [[DCI]] 정보에 따라 타입 1 또는 타입 2로 구성되며, [[PUSCH]] 매핑 타입(A 또는 B)과 [[Transform_Precoding]] 활성화 여부에 따라 시간 및 주파수 도메인 위치가 결정됩니다.

## 상세 설명
[[DMRS]] 시퀀스는 중간 양(intermediate quantity)을 거쳐 물리 자원에 매핑됩니다.

1. 시퀀스 매핑:
   - [[Transform_Precoding]]이 비활성화된 경우, [[DMRS_UplinkConfig]]의 설정에 따라 타입 1 또는 타입 2가 적용됩니다.
   - [[Transform_Precoding]]이 활성화된 경우, 특정 시퀀스 매핑 규칙이 적용됩니다.
   - 안테나 포트 할당은 [[PUSCH_Precoding]] 절차와 연계되어 수행됩니다.

2. 시간 도메인 위치:
   - [[PUSCH]] 매핑 타입 A: 슬롯 시작점 기준으로 [[dmrs-TypeA-Position]]에 의해 첫 번째 [[DMRS]] 심볼 위치가 결정됩니다.
   - [[PUSCH]] 매핑 타입 B: 스케줄링된 [[PUSCH]] 자원 시작점 기준으로 위치가 결정됩니다.
   - [[maxLength]] 파라미터가 'len2'로 설정된 경우, [[DCI]] 또는 설정된 그랜트(configured grant)에 따라 단일 심볼 또는 이중 심볼 [[DMRS]]가 사용됩니다.

3. 주파수 도메인 위치:
   - [[Transform_Precoding]] 비활성화 시, 공통 자원 블록(CRB) 0의 서브캐리어 0이 기준점이 됩니다.
   - [[Transform_Precoding]] 활성화 시, 스케줄링된 [[PUSCH]] 자원의 가장 낮은 번호 자원 블록의 서브캐리어 0이 기준점이 됩니다.

4. 특수 케이스:
   - [[msgA]] 전송 시, [[msgA-DMRS-Config]]의 설정이 우선하며, 타입 1만 지원됩니다.
   - 주파수 호핑(frequency hopping)이 활성화된 경우, 각 홉(hop)마다 [[DMRS]] 위치가 독립적으로 계산됩니다.

## 인과 관계
- [[DMRS_Resource_Mapping]] depends_on [[DMRS_Sequence_Generation]] (매핑할 시퀀스 생성 전제)
- [[DMRS_Resource_Mapping]] affects [[PUSCH_Precoding]] (안테나 포트 및 프리코딩 매트릭스 적용)
- [[DMRS_Resource_Mapping]] depends_on [[PUSCH_Transform_Precoding]] (매핑 기준점 및 시퀀스 매핑 방식 결정)

## 관련 개념
- [[PUSCH]] (part_of)
- [[DMRS]] (part_of)
- [[DMRS_Sequence_Generation]] (depends_on)
- [[PUSCH_Precoding]] (affects)
- [[PUSCH_Transform_Precoding]] (depends_on)

## 스펙 근거
- TS 38.211 §6.4.1.1.3: [[DMRS]] 시퀀스의 물리 자원 매핑 및 안테나 포트 할당 규칙
- TS 38.211 Table 6.4.1.1.3-1, 6.4.1.1.3-2: [[DMRS]] 설정 타입별 파라미터
- TS 38.211 Table 6.4.1.1.3-3 ~ 6.4.1.1.3-6: [[DMRS]] 시간 도메인 위치 및 인덱스

## 소스
- 3GPP TS 38.211 V16.9.0 (Release 16) §6.4.1.1.3