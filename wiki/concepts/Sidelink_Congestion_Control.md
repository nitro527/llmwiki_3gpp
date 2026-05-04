# Sidelink Congestion Control

## 정의
[[Sidelink]] 리소스 할당 모드 2(Resource allocation mode 2)에서 무선 채널의 혼잡도를 관리하고, [[UE]] 간의 효율적인 자원 공유를 위해 전송 파라미터를 조정하는 메커니즘을 의미합니다.

## 요약
본 기능은 [[TS 38.822]]에 정의된 UE Feature 중 다음 항목들과 관련이 있습니다.
- [필수(항상)] 15-5: Sidelink congestion control
- [필수(항상)] 15-1: Receiving NR sidelink
- [선택] 41-1-5: SL-PRS congestion control in a dedicated resource pool
- [선택] 3-5a: For type 1 CSS with dedicated RRC configuration, type 3 CSS, and UE-SS, monitoring occasion can be any OFDM symbol(s) of a slot for Case 2 with a DCI gap
- [선택] 4-25: Parallel SRS and PUCCH/PUSCH transmission across CCs in inter-band CA
- [선택] 4-26: Parallel PRACH and SRS/PUCCH/PUSCH transmissions across CCs in inter-band CA
- [선택] 6-5: Basic DL NR-NR CA operation
- [선택] 6-6: Basic UL NR-NR CA operation
- [선택] 6-7: Two NR PUCCH group with same numerology
- [선택] 6-8: Different numerology across NR PUCCH groups
- [선택] 6-9: Different numerologies across NR carriers within the same NR PUCCH group, with PUCCH on a carrier of smaller SCS
- [선택] 6-9a: Different numerologies across NR carriers within the same NR PUCCH group, with PUCCH on a carrier of larger SCS

## 상세 설명
[[Sidelink]] 리소스 할당 모드 2에서 [[UE]]는 [[CBR]](Channel Busy Ratio)을 측정하여 현재 채널의 혼잡 상태를 파악합니다. 측정된 [[CBR]] 값에 따라 [[UE]]는 전송 파라미터를 조정하거나 리소스 선택 범위를 제한하여 시스템 전체의 성능을 유지합니다. 주요 제어 요소는 다음과 같습니다.

1. **CBR 측정**: [[UE]]는 설정된 리소스 풀 내에서 [[PSFCH]] 또는 [[PSSCH]]의 에너지 레벨을 기반으로 [[CBR]]을 계산합니다.
2. **CR(Channel occupancy Ratio) 제한**: [[UE]]는 특정 시간 윈도우 동안 점유하는 채널 자원의 비율인 [[CR]]이 상위 계층에서 설정한 임계치를 초과하지 않도록 제한합니다.
3. **전송 파라미터 조정**: 혼잡도가 높은 경우, [[UE]]는 패킷의 우선순위, 전송 전력, 또는 리소스 예약 간격을 조정하여 혼잡을 완화합니다.

## 인과 관계
- [[CBR]] 측정 (depends_on) [[Sidelink]] 리소스 풀 설정
- [[CR]] 제한 (affects) [[Sidelink]] 전송 절차
- [[Sidelink]] 혼잡 제어 (triggers) 전송 파라미터 재설정

## 관련 개념
- [[Sidelink]] (part_of)
- [[CBR]] (depends_on)
- [[CR]] (depends_on)
- [[Sidelink_Resource_Allocation_Procedures]] (affects)

## 스펙 근거
- [[TS 38.214]] §8.1.6에 따르면, 리소스 할당 모드 2에서 [[UE]]는 상위 계층으로부터 제공받은 [[CBR]] 임계치와 [[CR]] 제한 값을 사용하여 전송 자원을 선택해야 합니다.
- [[TS 38.214]] §8.1.6.1에서는 [[CBR]] 측정 절차와 [[CR]] 계산 방식을 정의하며, 이를 통해 [[UE]]가 자원 선택 시 준수해야 할 제약 조건을 명시하고 있습니다.

## 소스
- 3GPP TS 38.214 v19.0.0, "NR; Physical layer procedures for data", Section 8.1.6.