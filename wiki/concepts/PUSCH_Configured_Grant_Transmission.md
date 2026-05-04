# PUSCH_Configured_Grant_Transmission

## 정의
[[PUSCH]] Configured Grant는 기지국(gNB)으로부터 동적인 DCI(Downlink Control Information) 할당 없이, 상위 계층(RRC) 설정에 의해 미리 정의된 자원을 사용하여 상향링크 데이터를 전송하는 방식입니다.

## 요약
Configured Grant는 Type 1과 Type 2로 구분되며, 각각 RRC 설정만으로 동작하거나 RRC 설정 후 DCI로 활성화되는 특징을 가집니다. 본 전송 방식은 지연 시간을 최소화하고 제어 채널 오버헤드를 줄이는 데 목적이 있습니다.

## 상세 설명
Configured Grant 기반의 [[PUSCH]] 전송은 다음과 같은 메커니즘을 포함합니다.

*   **Type 1**: RRC 설정만으로 전송 자원이 즉시 활성화됩니다.
*   **Type 2**: RRC 설정 후, PDCCH를 통한 DCI로 활성화/비활성화가 제어됩니다.
*   **반복 전송 (Repetition)**: TS 38.214 §6.1.2.3에 따라 PUSCH Repetition Type A 및 Type B를 지원하며, TB(Transport Block)를 여러 슬롯이나 심볼에 걸쳐 반복 전송하여 신뢰성을 높입니다.
*   **RV(Redundancy Version) 시퀀스**: 반복 전송 시 각 전송마다 정의된 RV 시퀀스를 순환하며 적용합니다.
*   **SRS 매핑**: Configured Grant 자원과 연계된 [[SRS]] 리소스 세트를 매핑하여 채널 상태 정보를 활용한 빔포밍을 수행할 수 있습니다.
*   **슬롯 카운팅**: 반복 전송 시 슬롯 경계를 고려한 카운팅 로직이 적용됩니다.
*   **공유 스펙트럼 동작**: 비면허 대역(Unlicensed band)에서의 동작을 위해 LBT(Listen-Before-Talk) 절차와 연동됩니다.

## 인과 관계
- [[PUSCH]] (depends_on) [[PUSCH_Configured_Grant_Transmission]]
- [[SRS]] (affects) [[PUSCH_Configured_Grant_Transmission]]
- [[HARQ]] (affects) [[PUSCH_Configured_Grant_Transmission]]
- [[DCI_Formats_Processing]] (triggers) [[PUSCH_Configured_Grant_Transmission]]

## 관련 개념
- [[PUSCH]] (part_of)
- [[SRS]] (depends_on)
- [[HARQ]] (affects)
- [[DCI_Formats_Processing]] (triggers)

## 스펙 근거
- TS 38.214 §6.1.2.3: Resource allocation for uplink transmission with configured grant
- TS 38.214 §6.1.2.3.1: Transport Block repetition for uplink transmissions of PUSCH repetition Type A with a configured grant
- TS 38.214 §6.1.2.3.2: Transport Block repetition for uplink transmissions of PUSCH repetition Type B with a configured grant
- TS 38.214 §6.1.2.3.3: Transport Block repetition for uplink transmissions of TB processing over multiple slots with a configured grant

## 소스
- 3GPP TS 38.214 V17.x.x (Physical layer procedures for data)