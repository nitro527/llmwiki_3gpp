# Sidelink_HARQ_ACK_Reporting_on_UL

## 정의
사이드링크 HARQ-ACK 정보를 상향링크 채널인 [[PUCCH]] 또는 [[PUSCH]]를 통해 기지국으로 보고하는 절차를 의미한다. 이는 사이드링크 [[PSFCH]] 수신 결과 또는 수신 부재를 기반으로 생성된 HARQ-ACK 정보를 상위 계층 설정 및 [[DCI]] 포맷 3_0에 따라 전송하는 과정을 포함한다.

## 요약
UE는 사이드링크 [[PSSCH]] 전송에 대한 응답으로 수신한 [[PSFCH]] 정보를 취합하여 HARQ-ACK 비트를 생성한다. 생성된 정보는 [[DCI]] 포맷 3_0에 의해 트리거되거나 설정된 상향링크 자원(PUCCH/PUSCH)을 통해 보고된다. 이때 보고 타이밍, 자원 선택, 우선순위 처리는 TS 38.213 §16.5에 정의된 규칙을 따른다.

## 상세 설명
사이드링크 HARQ-ACK 보고 절차는 다음과 같은 단계로 구성된다.

1. **HARQ-ACK 정보 생성**:
   - UE는 [[SCI]] 포맷 2-A/2-B의 Cast type indicator 및 PSFCH 수신 여부에 따라 ACK/NACK을 결정한다.
   - 우선순위 처리(TS 38.213 §16.2.4)로 인해 PSFCH를 수신하지 못하거나 PSSCH를 전송하지 못한 경우, UE는 NACK을 생성하며 이때의 우선순위 값은 해당 PSSCH 전송의 우선순위와 동일하다.
   - PSSCH 전송이 없는 경우에도 특정 조건(설정된 자원 내 전송 부재 등)에 따라 ACK을 생성할 수 있다.

2. **보고 타이밍**:
   - HARQ-ACK 보고는 PSFCH 수신이 종료된 후 일정 시간 이후에 수행되어야 한다.
   - 최소 지연 시간은 TS 38.211의 슬롯 구조 및 SCS(Subcarrier Spacing) 설정에 따라 결정된다.
   - [[DCI]] 포맷 3_0의 'PSFCH-to-HARQ feedback timing indicator' 필드는 보고가 수행될 슬롯을 지시하며, 이는 상위 계층에서 제공하는 `sl-PSFCH-ToPUCCH` 값과 매핑된다.

3. **자원 선택 및 전송**:
   - UE는 `sl-PUCCH-Config`를 통해 제공된 PUCCH 자원 세트 중 하나를 선택한다.
   - [[DCI]] 포맷 3_0 내의 'PUCCH resource indicator' 필드를 통해 실제 사용할 PUCCH 자원이 결정된다.
   - HARQ-ACK 정보는 [[PUCCH]] 포맷 0, 1, 2, 3, 4 중 하나를 사용하여 전송된다.
   - 동일한 슬롯 내에서 여러 HARQ-ACK 정보가 다중화될 수 있으며, 이때 전송되는 PUCCH의 우선순위 값은 포함된 HARQ-ACK 비트들의 우선순위 값 중 가장 작은 값(가장 높은 우선순위)을 따른다.

4. **특수 케이스**:
   - SL Configured Grant Type 1의 경우 `sl-PSFCH-ToPUCCH-CG-Type1`을 통해 자원이 제공된다.
   - DCI 포맷 3_0에서 PUCCH 자원 지시자가 0이고 타이밍 지시자가 0인 경우, PUCCH 자원이 제공되지 않은 것으로 간주하여 보고를 수행하지 않는다.

## 인과 관계
- [[DCI]] 포맷 3_0 (triggers) [[PUCCH]] 자원 할당 및 HARQ-ACK 보고 타이밍 결정
- [[PSFCH]] (depends_on) HARQ-ACK 정보 생성의 기초 데이터 제공
- [[PUCCH]] (implements) 사이드링크 HARQ-ACK 정보의 상향링크 전송
- [[PUSCH]] (implements) HARQ-ACK 정보의 피기백(piggyback) 전송

## 관련 개념
- [[PSFCH]] (depends_on)
- [[DCI]] (triggers)
- [[PUCCH]] (implements)
- [[PUSCH]] (implements)
- [[SCI]] (depends_on)
- [[Sidelink_Resource_Configuration]] (depends_on)

## 스펙 근거
- TS 38.213 §16.5: UE procedure for reporting HARQ-ACK on uplink
- TS 38.211 §4: Frame structure and physical resources
- TS 38.212 §7.3.1: DCI formats for sidelink

## 소스
- 3GPP TS 38.213 V18.0.0 (2024-03) "NR; Physical layer procedures for control"
- 3GPP TS 38.211 V18.0.0 (2024-03) "NR; Physical channels and modulation"
- 3GPP TS 38.212 V18.0.0 (2024-03) "NR; Multiplexing and channel coding"