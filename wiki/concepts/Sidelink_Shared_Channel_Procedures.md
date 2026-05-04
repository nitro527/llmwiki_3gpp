# Sidelink Shared Channel Procedures

## 정의
[[Sidelink Shared Channel Procedures]]는 [[Sidelink]] 통신에서 [[PSSCH]]를 통해 데이터를 전송하고 수신하기 위한 물리 계층 절차를 의미합니다. 이는 자원 할당, 변조 및 코딩, 자원 선택, 혼잡 제어 등을 포함합니다.

## 요약
[[PSSCH]] 전송 절차는 [[Sidelink]] 자원 할당 모드에 따라 결정되며, 전송을 위한 자원 선택, [[SCI]]를 통한 제어 정보 전달, 그리고 [[HARQ]] 피드백을 포함한 데이터 전송 과정을 포함합니다. 수신 측은 [[PSCCH]]를 통해 전달된 [[SCI]]를 디코딩하여 [[PSSCH]]를 복조합니다.

## 상세 설명
- **전송 절차**: [[UE]]는 상위 계층으로부터 전달받은 정보를 바탕으로 [[PSSCH]] 전송을 수행합니다. 전송 방식은 [[TS 38.214]] §8.1.1에 정의된 전송 스킴을 따릅니다.
- **자원 할당**: 시간 및 주파수 영역에서의 자원 할당은 [[TS 38.214]] §8.1.2에 따라 수행됩니다. 이는 [[SCI]] 포맷 1-A를 통해 수신 측에 전달됩니다.
- **변조 및 코딩**: [[Transport Block]]의 크기, 변조 차수, 타겟 코드 레이트 및 [[Redundancy Version]] 결정은 [[TS 38.214]] §8.1.3에 명시된 절차를 따릅니다.
- **자원 선택 및 혼잡 제어**: [[Sidelink]] 자원 할당 모드 2에서 [[UE]]는 자원 선택을 위해 [[TS 38.214]] §8.1.4의 절차를 수행하며, [[TS 38.214]] §8.1.6에 따라 혼잡 제어 메커니즘을 적용합니다.
- **수신 절차**: [[UE]]는 [[TS 38.214]] §8.3에 따라 [[PSSCH]] 수신을 수행하며, 이는 [[PSCCH]]를 통해 획득한 제어 정보를 기반으로 합니다.

## 인과 관계
- [[Sidelink Resource Allocation Procedures]] (triggers) [[PSSCH]] 전송
- [[Sidelink Congestion Control]] (affects) [[PSSCH]] 자원 선택
- [[Sidelink SCI Processing]] (depends_on) [[PSSCH]] 수신 및 복조

## 관련 개념
- [[PSSCH]] (part_of)
- [[PSCCH]] (part_of)
- [[Sidelink Resource Allocation Procedures]] (depends_on)
- [[Sidelink Congestion Control]] (affects)
- [[Sidelink HARQ Reporting]] (part_of)

## 스펙 근거
- [[TS 38.214]] §8.1: [[UE]] procedure for transmitting the physical sidelink shared channel
- [[TS 38.214]] §8.1.1: Transmission schemes
- [[TS 38.214]] §8.1.2: Resource allocation
- [[TS 38.214]] §8.1.3: Modulation order, target code rate, redundancy version and transport block size determination
- [[TS 38.214]] §8.1.4: [[UE]] procedure for determining the subset of resources to be reported to higher layers in [[PSSCH]] resource selection in [[Sidelink]] resource allocation mode 2
- [[TS 38.214]] §8.1.6: [[Sidelink]] congestion control in [[Sidelink]] resource allocation mode 2
- [[TS 38.214]] §8.3: [[UE]] procedure for receiving the physical sidelink shared channel

## 소스
- 3GPP TS 38.214 V17.9.0 (2024-03) "NR; Physical layer procedures for data"