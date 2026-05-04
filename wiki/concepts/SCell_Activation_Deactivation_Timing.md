# SCell_Activation_Deactivation_Timing

## 정의
[[SCell]] Activation/Deactivation Timing은 [[MAC]] 계층에서 수신한 [[MAC CE]] 명령을 기반으로, [[UE]]가 특정 [[Secondary Cell]]을 활성화하거나 비활성화할 때 적용해야 하는 시간적 제약 및 절차를 의미합니다.

## 요약
[[UE]]는 [[SCell]] 활성화 명령을 수신한 후, [[CSI]] 보고, [[PDCCH]] 모니터링, [[SRS]] 전송 등을 수행하기 위해 필요한 준비 시간을 준수해야 합니다. 이 과정에서 [[Beam reporting timing]]과 같은 필수 기능이 적용되며, 다양한 보조 기능들이 활성화 속도와 효율을 최적화합니다.

## 상세 설명
[[SCell]] 활성화 명령이 포함된 [[MAC CE]]를 수신하면, [[UE]]는 해당 [[SCell]]에 대한 동작을 시작합니다. 
- [[Beam reporting timing]] (필수(cap)): [[SCell]] 활성화 후 빔 관련 보고를 수행하기 위한 타이밍 요구사항을 준수해야 합니다.
- [[Aperiodic CSI-RS for tracking for fast SCell activation]] (선택): 빠른 활성화를 위해 [[CSI-RS]]를 활용한 트래킹을 수행합니다.
- [[CSI reporting cross PUCCH group]] (선택): 활성화된 [[SCell]]의 [[CSI]] 보고를 다른 [[PUCCH]] 그룹을 통해 수행할 수 있습니다.
- [[UE-specific K_offset]] (선택): 활성화 시점과 관련된 오프셋을 조정하여 유연한 타이밍을 확보합니다.
- [[Aperiodic CSI-RS bandwidth for tracking for fast SCell activation for 10MHz UE channel bandwidth]] (선택): 10MHz 대역폭 환경에서 트래킹 성능을 최적화합니다.
- [[Support of CSI-RS RRM measurement for SCell without SS/PBCH block]] (선택): [[SS/PBCH Block]]이 없는 환경에서도 [[RRM]] 측정을 지원합니다.
- [[A-CSI-RS beam switching timing]] (선택): [[Aperiodic CSI-RS]] 기반의 빔 스위칭 타이밍을 제어합니다.
- [[New capability for beamSwitchTiming values of 224 and 336]] (선택): 특정 빔 스위칭 타이밍 값을 지원하여 고속 활성화를 지원합니다.
- [[Mulit-CC simultaneous TCI activation with multi-TRP]] (선택): 여러 [[TRP]] 환경에서 다중 [[CC]]에 대한 [[TCI]] 상태를 동시에 활성화합니다.
- [[Support of UL MAC CE based MG activation request for PRS measurements]] (선택): [[PRS]] 측정을 위한 [[Measurement Gap]] 활성화를 [[MAC CE]] 기반으로 요청합니다.
- [[Activation/Deactivation of SCG]] (선택): [[SCG]] 수준의 활성화/비활성화 절차를 수행합니다.

## 인과 관계
- [[MAC CE]] 수신 (triggers) -> [[SCell]] 활성화 절차
- [[SCell]] 활성화 (affects) -> [[CSI]] 보고 타이밍
- [[Beam reporting timing]] (depends_on) -> [[SCell]] 활성화 성공 여부

## 관련 개념
- [[MAC]] (part_of)
- [[CSI]] (affects)
- [[PDCCH]] (affects)
- [[SRS]] (affects)
- [[Beam reporting timing]] (depends_on)

## 스펙 근거
- TS 38.213 §4.3에 따르면, [[SCell]] 활성화/비활성화 명령에 따른 [[UE]]의 타이밍 요구사항 및 [[CSI]] 보고 절차가 정의되어 있습니다.

## 소스
- 3GPP TS 38.213 v18.0.0 (Release 18) §4.3