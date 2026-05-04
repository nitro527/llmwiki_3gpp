# Sidelink_Timing_Procedures

## 정의
[[Sidelink]] 예약 주기(Reservation Period)를 물리적 시간 단위(ms)에서 [[Sidelink]] 자원 할당을 위한 논리 슬롯(Logical Slot) 단위로 변환하는 절차를 의미합니다.

## 요약
[[Sidelink]] 통신에서 자원 예약 주기는 상위 계층에 의해 ms 단위로 설정되지만, 실제 자원 할당 및 [[PSSCH]] 전송은 [[Sidelink]] 자원 풀 내의 논리 슬롯을 기준으로 수행됩니다. 따라서 UE는 설정된 예약 주기를 해당 자원 풀의 논리 슬롯 개수로 변환하여 자원 예약 정보를 결정합니다.

## 상세 설명
[[Sidelink]] 전송을 수행하는 UE는 상위 계층으로부터 자원 예약 주기(Reservation Period)를 ms 단위로 전달받습니다. 이 주기는 [[SCI]]를 통해 다른 UE들에게 전달되어 자원 예약 정보를 공유하는 데 사용됩니다. 

자원 풀 내에서 실제 전송이 가능한 슬롯들은 [[Sidelink]] 자원 풀 설정에 따라 결정되며, 이를 논리 슬롯(Logical Slot)이라고 합니다. 예약 주기를 논리 슬롯 단위로 변환하는 과정은 다음과 같습니다.

1. 상위 계층에서 제공된 ms 단위의 예약 주기 값을 확인합니다.
2. 해당 [[Sidelink]] 자원 풀의 슬롯 설정 정보를 기반으로, 주어진 ms 시간 동안 포함되는 논리 슬롯의 개수를 계산합니다.
3. 이 계산된 논리 슬롯 개수는 [[PSSCH]] 자원 예약 및 [[Sidelink]] 전송 절차에서 주기적인 자원 할당을 수행하는 기준으로 활용됩니다.

## 인과 관계
- [[Sidelink_Resource_Allocation_Procedures]] (depends_on): 자원 할당 절차는 예약 주기를 논리 슬롯 단위로 변환한 결과를 기반으로 주기적 자원 예약 위치를 결정합니다.
- [[Sidelink_Transmission_Procedures]] (affects): 변환된 논리 슬롯 단위의 주기는 실제 [[PSSCH]] 전송 타이밍을 결정하는 데 직접적인 영향을 미칩니다.

## 관련 개념
- [[Sidelink]] (part_of)
- [[PSSCH]] (depends_on)
- [[SCI]] (triggers)

## 스펙 근거
- TS 38.214 §8.1.7에 따르면, UE는 상위 계층에 의해 제공된 예약 주기(ms)를 해당 [[Sidelink]] 자원 풀의 논리 슬롯 단위로 변환하여 자원 예약 절차를 수행해야 합니다.

## 소스
- 3GPP TS 38.214 V17.x.x, "Physical layer procedures for data", Section 8.1.7.