# Sidelink SCI Processing

## 정의
[[Sidelink]] Control Information(SCI)는 [[PSSCH]] 및 [[PSCCH]] 전송을 제어하기 위해 송신 [[UE]]가 수신 UE로 전달하는 제어 정보입니다. 이는 2단계(2-stage) 구조로 구성되어, 1st-stage SCI는 PSCCH를 통해 전송되고 2nd-stage SCI는 PSSCH와 함께 다중화되어 전송됩니다.

## 요약
SCI는 데이터 전송을 위한 자원 할당, 변조 및 코딩 방식(MCS), [[HARQ]] 관련 정보 등을 포함합니다. 1st-stage SCI는 [[SCI format 1-A]]와 [[SCI format 1-B]]로 정의되며, 2nd-stage SCI는 [[SCI format 2-A]], [[SCI format 2-B]], [[SCI format 2-C]], [[SCI format 2-D]]로 세분화되어 전송 데이터의 특성에 따라 선택적으로 사용됩니다.

## 상세 설명
SCI 처리는 크게 1st-stage와 2nd-stage로 구분됩니다.

1. **1st-stage SCI**: PSCCH를 통해 전송되며, 수신 UE가 PSSCH를 복조하기 위한 필수 정보를 제공합니다.
   - [[SCI format 1-A]]: 일반적인 PSSCH 스케줄링 정보를 포함합니다.
   - [[SCI format 1-B]]: 특정 제어 목적을 위해 정의됩니다.

2. **2nd-stage SCI**: PSSCH 내의 자원을 사용하여 전송됩니다. 이는 1st-stage SCI에서 지시된 정보를 보완하며, 구체적인 데이터 복조 및 디코딩 파라미터를 포함합니다.
   - [[SCI format 2-A]], [[SCI format 2-B]], [[SCI format 2-C]], [[SCI format 2-D]]: 각 포맷은 서로 다른 전송 요구사항(예: HARQ 프로세스 ID, NDI, RV, 소스 ID 등)을 지원합니다.

3. **UE 절차**:
   - 송신 UE는 상위 계층으로부터 전달받은 파라미터를 기반으로 자원 할당(시간 및 주파수 도메인)을 수행합니다.
   - [[TS 38.214 §8.1]]에 따라 MCS, [[Transport Block Size]], [[Redundancy Version]]을 결정합니다.
   - 모드 2(Mode 2) 자원 할당 시, UE는 혼잡 제어(Congestion Control) 절차를 수행하여 자원 선택을 최적화합니다.
   - [[Location reporting]]은 필수적으로 수행되어야 하며, 필요에 따라 [[256QAM]] 지원 및 [[PSFCH]] 수신 절차와 연동됩니다.

## 인과 관계
- [[SCI format 1-A]] (triggers) [[PSSCH]] 전송 파라미터 결정
- [[Sidelink Resource Allocation]] (affects) [[SCI]] 필드 설정
- [[Sidelink Congestion Control]] (affects) [[PSSCH]] 자원 선택

## 관련 개념
- [[PSSCH]] (depends_on)
- [[PSCCH]] (part_of)
- [[HARQ]] (depends_on)
- [[Sidelink Resource Allocation]] (affects)

## 스펙 근거
- TS 38.212 §8.3.1: 1st-stage SCI formats (1-A, 1-B) 정의
- TS 38.212 §8.4.1: 2nd-stage SCI formats (2-A, 2-B, 2-C, 2-D) 정의
- TS 38.214 §8.1: PSSCH 전송을 위한 UE 절차, 자원 할당, MCS 및 TBS 결정 절차

## 소스
- 3GPP TS 38.212 V18.0.0 (2024-03)
- 3GPP TS 38.214 V18.0.0 (2024-03)