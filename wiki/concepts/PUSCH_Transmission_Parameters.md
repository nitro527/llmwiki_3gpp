# PUSCH_Transmission_Parameters

## 정의
[[PUSCH]] 전송을 위해 [[DCI]]를 통해 전달된 정보를 바탕으로 변조 차수(Modulation order), 타겟 코드 레이트(Target code rate), [[HARQ]] 프로세스에서 사용될 Redundancy Version(RV), 그리고 최종적인 Transport Block(TB) 사이즈를 결정하는 절차를 의미합니다.

## 요약
[[PUSCH]] 전송 파라미터 결정은 기지국이 전송한 [[DCI]] 포맷 내의 MCS 필드와 기타 제어 정보를 해석하여 수행됩니다. UE는 지정된 MCS 테이블을 참조하여 변조 방식과 코드 레이트를 도출하고, 할당된 자원 블록 수와 레이어 수에 기반하여 TB 사이즈를 계산합니다. 또한, [[CBG]] 기반 재전송이나 다중 슬롯 전송 시의 파라미터 처리 규칙을 따릅니다.

## 상세 설명
[[PUSCH]] 전송 파라미터 결정 과정은 크게 변조 및 코드 레이트 결정과 TB 사이즈 결정 단계로 나뉩니다.

1. **변조 차수 및 타겟 코드 레이트 결정**:
   - UE는 [[DCI]] 내의 MCS 필드 값을 사용하여 상위 계층에서 설정된 MCS 테이블을 참조합니다.
   - 이 테이블은 변조 차수($Q_m$)와 타겟 코드 레이트($R$)를 매핑합니다.
   - 만약 [[Transform_Precoding]]이 활성화된 경우와 비활성화된 경우에 따라 서로 다른 MCS 테이블이 적용될 수 있습니다.

2. **Transport Block Size(TBS) 결정**:
   - TBS는 할당된 자원의 수($N_{RE}$), 변조 차수($Q_m$), 타겟 코드 레이트($R$), 그리고 레이어 수($v$)를 기반으로 계산됩니다.
   - TS 38.214 §6.1.4.2에 명시된 수식에 따라 중간 값($N_{info}$)을 먼저 산출한 후, 이를 양자화하여 최종 TBS를 결정합니다.

3. **Redundancy Version(RV) 결정**:
   - [[DCI]] 내의 RV 필드는 [[HARQ]] 재전송 시 사용할 버퍼의 시작 위치를 지정합니다. 초기 전송과 재전송 간의 시퀀스에 따라 RV 값이 결정됩니다.

4. **다중 슬롯 및 CBG 기반 처리**:
   - [[CBG]] 기반 전송을 지원하는 UE는 특정 슬롯 내에서 여러 개의 TB를 처리할 수 있습니다.
   - UE Capability에 따라 슬롯당 최대 2개, 4개, 또는 7개의 유니캐스트 [[PUSCH]]를 처리할 수 있으며, 이는 [[CBGTI]] 필드를 통해 제어됩니다.

## 인과 관계
- [[DCI_Formats_Processing]] (triggers) -> [[PUSCH]] 파라미터 결정
- [[PUSCH_Resource_Allocation]] (depends_on) -> TBS 계산을 위한 자원 정보 제공
- [[PUSCH_HARQ_Feedback]] (affects) -> RV 값의 선택 및 재전송 시점 결정

## 관련 개념
- [[PUSCH]] (part_of)
- [[HARQ]] (affects)
- [[DCI]] (triggers)
- [[CBG]] (depends_on)
- [[Transform_Precoding]] (affects)

## 스펙 근거
- TS 38.214 §6.1.4: Modulation order, redundancy version and transport block size determination
- TS 38.214 §6.1.4.1: Modulation order and target code rate determination
- TS 38.214 §6.1.4.2: Transport block size determination

## 소스
- 3GPP TS 38.214 V17.x.x (Release 17)