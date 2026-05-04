# Radio_Link_Monitoring

## 정의
[[Radio_Link_Monitoring]] (RLM)은 [[UE]]가 서빙 셀의 하향링크 무선 링크 품질을 평가하고, 이를 바탕으로 [[Out_of_sync]] 또는 [[In_sync]] 상태를 상위 계층에 보고하여 무선 링크 실패 여부를 판단하는 물리 계층 절차를 의미합니다.

## 요약
RLM은 [[DL_BWP]]별로 설정된 [[Reference_Signals]]를 사용하여 수행됩니다. [[UE]]는 물리 계층에서 측정된 품질이 특정 임계값에 도달하는지 감시하며, 이 결과는 [[RRC]] 계층의 무선 링크 관리 절차에 활용됩니다. 본 절차는 [[DMRS]] 및 [[CSI_RS]]와 같은 참조 신호를 기반으로 하며, 다양한 [[UE]] 기능 지원 여부에 따라 유연하게 구성됩니다.

## 상세 설명
[[UE]]는 서빙 셀의 하향링크 품질을 모니터링하기 위해 다음의 절차를 수행합니다.

1. **RLM-RS 설정**: [[UE]]는 [[RRC]]를 통해 설정된 [[Reference_Signals]] (주로 [[SS_PBCH_Block]] 또는 [[CSI_RS]])를 사용하여 무선 링크 품질을 측정합니다.
2. **품질 평가**: 측정된 품질이 가상의 [[PDCCH]] 수신 성능을 기준으로 정의된 임계값(Q_out, Q_in)과 비교됩니다.
   - Q_out: [[Out_of_sync]] 상태를 결정하는 품질 임계값
   - Q_in: [[In_sync]] 상태를 결정하는 품질 임계값
3. **상태 보고**: 물리 계층은 측정 결과에 따라 상위 계층으로 [[Out_of_sync]] 또는 [[In_sync]] 표시를 전달합니다.
4. **UE Feature 지원**:
   - [필수(항상)] [[DMRS]] 기반의 하향링크 및 상향링크 스케줄링(Type A/B) 지원을 통해 기본적인 채널 추정 및 품질 평가를 수행합니다.
   - [필수(cap)] [[Active_spatial_relations]] 설정을 통해 빔 기반의 품질 모니터링을 지원합니다.
   - [선택] [[CSI_RS]] 기반의 RLM/BM/BFD 측정 지원: [[CD_SSB]]가 현재 활성화된 [[Bandwidth_Part_Operation]] 외부에 존재하더라도 [[CSI_RS]]를 활용하여 모니터링을 지속할 수 있습니다.
   - [선택] [[Dynamic_SFI_monitoring]] 및 비면허 대역에서의 SFI 모니터링 기능을 통해 동적인 환경에서의 링크 품질 평가를 최적화합니다.
   - [선택] [[One_slot_periodic_TRS_configuration_for_FR1]]을 통해 시간 및 주파수 추적 성능을 향상시켜 RLM의 정확도를 높입니다.

## 인과 관계
- [[Radio_Link_Monitoring]] (triggers) [[Radio_Link_Failure]] (상위 계층 판단 시)
- [[Bandwidth_Part_Operation]] (affects) [[Radio_Link_Monitoring]] (BWP별로 RLM-RS가 설정됨)
- [[Reference_Signals]] (depends_on) [[Radio_Link_Monitoring]] (품질 평가를 위한 측정 자원으로 사용됨)

## 관련 개념
- [[Bandwidth_Part_Operation]] (part_of)
- [[Reference_Signals]] (part_of)
- [[Radio_Link_Failure]] (triggers)
- [[PDCCH_Monitoring_Procedures]] (similar_to)

## 스펙 근거
- TS 38.213 §5에 따르면, [[UE]]는 상위 계층으로부터 설정된 [[Reference_Signals]] 자원 집합을 기반으로 하향링크 무선 링크 품질을 모니터링해야 합니다.
- TS 38.213 §5.1에 따르면, [[Out_of_sync]] 및 [[In_sync]] 평가를 위한 임계값은 가상의 [[PDCCH]] 블록 에러율을 기준으로 정의됩니다.

## 소스
- 3GPP TS 38.213 "NR; Physical layer procedures for control" (Release 18) §5