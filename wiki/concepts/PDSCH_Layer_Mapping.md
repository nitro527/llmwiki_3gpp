# PDSCH_Layer_Mapping

## 정의
[[PDSCH]] 레이어 매핑은 [[Modulation_Mapper]]로부터 출력된 복소수 심볼들을 하나 이상의 전송 레이어로 분배하는 물리 계층 처리 과정입니다.

## 요약
본 절차는 [[PDSCH]] 전송을 위해 변조된 심볼들을 MIMO(Multiple-Input Multiple-Output) 전송을 위한 다중 레이어로 매핑합니다. UE는 [[PDSCH]] 수신을 위한 기본 기능(2-1) 및 MIMO 레이어 지원(2-3)을 필수적으로 갖추어야 하며, 다양한 매핑 패턴(2-33a)과 매핑 타입(5-6, 5-6a), 스케줄링 오프셋(5-30, 5-30a) 및 인터리빙(5-7) 기능을 지원합니다. 또한 선택적으로 특정 심볼 길이의 타입 B 매핑(14-2), 다중 DCI 기반 mTRP를 위한 레이어 해석(16-2a-9), 멀티캐스트 전송을 위한 레이어(33-2g) 등을 지원할 수 있습니다.

## 상세 설명
[[PDSCH]] 레이어 매핑은 입력된 심볼 시퀀스를 안테나 포트 수와 전송 랭크에 따라 레이어로 분할합니다. 
- 단일 레이어 전송의 경우, 입력 심볼 시퀀스가 그대로 단일 레이어로 매핑됩니다.
- 다중 레이어 전송의 경우, 입력 심볼들은 각 레이어에 순차적으로 분배됩니다.
이 과정은 [[Physical_Resource_Grid]]에 매핑되기 전 단계로, 공간 다중화를 가능하게 하여 전송 효율을 극대화합니다.

## 인과 관계
- [[Modulation_Mapper]] (depends_on) → [[PDSCH_Layer_Mapping]]
- [[PDSCH_Layer_Mapping]] (affects) → [[PDSCH_Precoding]]
- [[PDSCH_Layer_Mapping]] (part_of) → [[PDSCH]]

## 관련 개념
- [[PDSCH]] (part_of)
- [[Modulation_Mapper]] (depends_on)
- [[PDSCH_Precoding]] (affects)

## 스펙 근거
- TS 38.211 §7.3.1.3에 따르면, PDSCH에 대한 레이어 매핑은 변조된 심볼들을 1개에서 8개까지의 레이어로 매핑하도록 정의되어 있습니다.

## 소스
- 3GPP TS 38.211 v16.9.0, "Physical channels and modulation", Section 7.3.1.3.