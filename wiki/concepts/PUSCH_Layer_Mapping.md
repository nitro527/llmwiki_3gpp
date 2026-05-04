# PUSCH_Layer_Mapping

## 정의
[[PUSCH]] Layer Mapping은 변조된 심볼들을 하나 이상의 전송 레이어로 분배하여 공간 다중화(Spatial Multiplexing)를 가능하게 하는 물리 계층 처리 절차입니다.

## 요약
본 절차는 UE의 전송 능력에 따라 필수적으로 수행되는 기본 기능이며, MIMO 전송을 위한 다중 레이어 구성 및 단일 레이어 전송을 지원합니다. 
- [필수(항상)]: [[PUSCH]] 기본 전송, [[DFT-S-OFDM]] 파형, [[PDSCH]] 기본 수신
- [선택]: Codebook/Non-codebook 기반 MIMO 전송, Multi-TRP 반복 전송, CG [[PUSCH]] 전송, PRB interlace 매핑, UL 다중화 및 우선순위 처리

## 상세 설명
[[PUSCH]] Layer Mapping은 [[Modulation_Mapper]]로부터 출력된 복소수 심볼 블록 $d(0), \dots, d(M_{symb}^{ap}-1)$을 입력으로 받습니다. 

1. **레이어 수 결정**: 상위 계층 파라미터 및 DCI(Downlink Control Information)를 통해 결정된 레이어 수 $\nu$에 따라 심볼이 분배됩니다.
2. **매핑 규칙**: 
   - 단일 레이어 전송($\nu=1$)의 경우, 입력 심볼은 그대로 하나의 레이어 $x^{(0)}(i) = d(i)$로 매핑됩니다.
   - 다중 레이어 전송($\nu > 1$)의 경우, TS 38.211 §6.3.1.3에 정의된 매핑 방식에 따라 심볼이 각 레이어 $x^{(0)}(i), \dots, x^{(\nu-1)}(i)$로 순차적으로 분배됩니다.
3. **데이터 처리**: 각 레이어는 이후 [[PUSCH_Precoding]] 단계로 전달되어 안테나 포트로 매핑됩니다.

## 인과 관계
- [[Modulation_Mapper]] (depends_on): 변조된 심볼을 입력으로 받음
- [[PUSCH_Precoding]] (triggers): 매핑된 레이어 데이터를 프리코딩 단계로 전달
- [[PUSCH_Transform_Precoding]] (affects): [[DFT-S-OFDM]] 파형 사용 시 레이어 매핑 이후 변환 프리코딩이 적용됨

## 관련 개념
- [[PUSCH]] (part_of)
- [[PUSCH_Precoding]] (triggers)
- [[Modulation_Mapper]] (depends_on)
- [[DFT-S-OFDM]] (depends_on)
- [[PUSCH_Modulation]] (affects)
- [[PUSCH_Resource_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §6.3.1.3: PUSCH Layer Mapping 절차 및 심볼 분배 규칙 정의
- TS 38.822: PUSCH 관련 UE Feature Priority 및 필수/선택 기능 명시

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03), "Physical channels and modulation"
- 3GPP TS 38.822 V17.0.0 (2022-03), "UE radio access capabilities"

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/PUSCH_Modulation.md
- concepts/PUSCH_Resource_Mapping.md
- entities/PUSCH.md