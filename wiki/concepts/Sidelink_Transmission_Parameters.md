# Sidelink_Transmission_Parameters

## 정의
[[Sidelink_Transmission_Parameters]]는 [[PSSCH]]를 통한 데이터 전송 시 필요한 변조 차수(Modulation order), 타겟 코드 레이트(Target code rate), 리던던시 버전(Redundancy version), 그리고 전송 블록 사이즈(Transport block size, TBS)를 결정하는 물리 계층 절차를 의미합니다.

## 요약
[[Sidelink]] 전송을 수행하는 [[UE]]는 상위 계층으로부터 제공받은 파라미터와 [[SCI]]를 통해 전달되는 정보를 바탕으로 전송 파라미터를 결정합니다. 이는 [[PSSCH]]의 효율적인 자원 활용과 신뢰성 있는 데이터 전송을 보장하기 위한 핵심 메커니즘입니다.

## 상세 설명
[[PSSCH]] 전송 파라미터 결정 절차는 크게 두 가지 영역으로 나뉩니다.

1. 변조 차수 및 타겟 코드 레이트 결정:
   [[UE]]는 상위 계층에서 설정된 값 또는 [[SCI]]를 통해 지시된 정보를 사용하여 변조 차수와 타겟 코드 레이트를 결정합니다. 이는 [[PSSCH]]의 링크 적응(Link adaptation)을 수행하는 과정입니다.

2. 전송 블록 사이즈(TBS) 결정:
   [[PSSCH]]를 통해 전송될 데이터의 크기인 TBS는 할당된 물리 자원의 양(Resource elements)과 결정된 변조 차수 및 타겟 코드 레이트를 기반으로 계산됩니다. 이 과정은 [[TS 38.214]]의 규정에 따라 수행되며, [[Sidelink]] 자원 풀 내에서 가용한 자원 블록(Resource blocks)의 수와 심볼의 수를 고려합니다.

3. 리던던시 버전(Redundancy version):
   [[HARQ]] 동작을 지원하기 위해 전송 시마다 리던던시 버전이 결정됩니다. 이는 데이터의 재전송 시 오류 정정 능력을 최적화하는 역할을 합니다.

## 인과 관계
- [[Sidelink_Resource_Allocation_Procedures]] (depends_on): 자원 할당 결과에 따라 가용 자원량이 결정되며, 이는 TBS 계산의 입력값이 됩니다.
- [[PSSCH_Modulation]] (affects): 결정된 변조 차수는 실제 [[PSSCH]]의 심볼 매핑 방식에 영향을 미칩니다.
- [[Sidelink_HARQ_Reporting]] (triggers): 리던던시 버전의 결정은 [[HARQ]] 재전송 시의 성능과 직결됩니다.

## 관련 개념
- [[PSSCH]] (part_of)
- [[SCI]] (depends_on)
- [[HARQ]] (affects)
- [[Sidelink_Resource_Allocation_Procedures]] (depends_on)

## 스펙 근거
- [[TS 38.214]] §8.1.3: Modulation order, target code rate, redundancy version and transport block size determination
- [[TS 38.214]] §8.1.3.1: Modulation order and target code rate determination
- [[TS 38.214]] §8.1.3.2: Transport block size determination

## 소스
- 3GPP TS 38.214 V16.9.0 (2022-03), "NR; Physical layer procedures for data"