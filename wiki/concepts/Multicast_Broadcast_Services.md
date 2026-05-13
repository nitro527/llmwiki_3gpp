# Multicast_Broadcast_Services

## 정의
[[Multicast_Broadcast_Services]] (MBS)는 5G NR에서 다수의 사용자에게 동일한 데이터를 효율적으로 전송하기 위한 기술로, [[PDCCH]] 및 [[PDSCH]]를 통한 브로드캐스트(Broadcast) 및 멀티캐스트(Multicast) 수신과 이에 따른 [[HARQ_ACK_Reporting]] 절차를 포함합니다.

## 요약
MBS는 [[G-RNTI]] 또는 [[G-CS-RNTI]]를 사용하여 멀티캐스트 데이터를 스케줄링하며, UE는 설정된 HARQ-ACK 보고 모드에 따라 ACK/NACK 또는 NACK-only 피드백을 수행합니다. RRC_CONNECTED 상태에서의 멀티캐스트 HARQ-ACK 정보는 전용 코드북 생성 규칙을 따르며, 특정 조건에서 유니캐스트(Unicast) HARQ-ACK 정보와 다중화(Multiplexing)될 수 있습니다.

## 상세 설명
MBS를 위한 데이터 수신 및 피드백 절차는 TS 38.213 §18에 정의되어 있습니다.

1. **식별자 및 스케줄링**:
   - 멀티캐스트 PDSCH 수신은 [[G-RNTI]]로 CRC가 스크램블된 멀티캐스트 DCI 포맷에 의해 스케줄링됩니다.
   - SPS(Semi-Persistent Scheduling) PDSCH 수신은 [[G-CS-RNTI]]를 사용하여 활성화, 해제 또는 재전송이 스케줄링됩니다.
   - 브로드캐스트 수신은 MCCH-RNTI 또는 G-RNTI를 사용합니다.

2. **HARQ-ACK 보고 모드**:
   - `harq-FeedbackOptionMulticast` 파라미터에 의해 두 가지 모드가 설정됩니다.
   - **첫 번째 모드 (ack-nack)**: UE가 TB를 올바르게 복호화하면 ACK, 그렇지 않으면 NACK을 생성합니다.
   - **두 번째 모드 (nack-only)**: UE는 ACK만 포함하는 [[PUCCH]]를 전송하지 않습니다. NACK 발생 시에만 PUCCH를 전송하며, 비트 수가 1개인 경우 NACK일 때만 전송합니다. 이 모드는 SPS PDSCH 활성화 후 첫 번째 수신에는 적용되지 않습니다.

3. **코드북 및 자원 할당**:
   - `pdsch-HARQ-ACK-Codebook` 설정에 따라 [[HARQ_ACK_Codebook_Determination]]이 수행됩니다. 'semi-static'인 경우 Type-1, 'dynamic'인 경우 Type-2 코드북을 생성합니다.
   - 멀티캐스트 HARQ-ACK 정보와 유니캐스트 HARQ-ACK 정보가 동일한 우선순위(Priority)를 가질 경우, 코드북을 결합하여 동일한 PUCCH 또는 [[PUSCH]]에서 전송할 수 있습니다.
   - PUCCH 자원 결정은 마지막 DCI 포맷이나 설정된 리스트(pucch-ConfigurationListMulticast 등)를 참조하여 수행됩니다.

4. **재전송**:
   - 초기 전송은 멀티캐스트 DCI 포맷으로만 스케줄링됩니다.
   - 첫 번째 보고 모드에서 재전송은 동일한 G-RNTI를 사용하는 멀티캐스트 DCI 또는 C-RNTI를 사용하는 유니캐스트 DCI로 스케줄링될 수 있습니다.

## 인과 관계
- [[PDCCH]] depends_on [[G-RNTI]] (멀티캐스트 DCI 수신을 위한 CRC 스크램블링)
- [[PDSCH]] depends_on [[G-CS-RNTI]] (SPS PDSCH 활성화 및 재전송 스케줄링)
- [[HARQ_ACK_Reporting]] depends_on [[Multicast_Broadcast_Services]] (멀티캐스트 HARQ-ACK 피드백 모드 결정)
- [[HARQ_ACK_Codebook_Determination]] depends_on [[Multicast_Broadcast_Services]] (멀티캐스트 HARQ-ACK 코드북 생성 규칙 적용)

## 관련 개념
- [[PDCCH]] (depends_on)
- [[PDSCH]] (depends_on)
- [[HARQ_ACK_Reporting]] (affects)
- [[HARQ_ACK_Codebook_Determination]] (affects)
- [[PUCCH]] (implements)

## 스펙 근거
- TS 38.213 §18: Multicast Broadcast Services 전반적인 절차 및 HARQ-ACK 보고 모드 정의
- TS 38.213 §18.1: HARQ-ACK 정보 생성 및 PUCCH 자원 매핑 규칙
- TS 38.213 §18.2: 유니캐스트 및 멀티캐스트 HARQ-ACK 다중화 규칙

## 소스
- 3GPP TS 38.213 Release 18 (v18.0.0) §18