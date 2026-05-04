# PDSCH_Transmission_Parameters

## 정의
[[PDSCH]] 전송을 위해 필요한 변조 차수(Modulation order), 타겟 코드 레이트(Target code rate), 리던던시 버전(Redundancy version, RV), 그리고 전송 블록 사이즈(Transport block size, TBS)를 결정하는 물리 계층 절차를 의미합니다.

## 요약
[[PDSCH]] 전송 파라미터 결정은 [[DCI]]를 통해 전달된 정보와 상위 계층 설정(RRC)을 기반으로 수행됩니다. 변조 및 코딩 방식(MCS) 인덱스를 통해 변조 차수와 코드 레이트가 결정되며, 할당된 자원과 레이어 수 등을 고려하여 최종적인 TBS가 산출됩니다.

## 상세 설명
[[PDSCH]] 전송 파라미터 결정 절차는 크게 두 단계로 나뉩니다.

1. 변조 차수 및 타겟 코드 레이트 결정:
   - [[DCI]] 내의 MCS 필드 값을 사용하여 테이블을 참조함으로써 변조 차수와 타겟 코드 레이트를 결정합니다.
   - 이때 사용되는 테이블은 RRC 설정에 따라 결정되며, [[PDSCH]] 전송 모드 및 서비스 요구사항에 따라 달라질 수 있습니다.

2. 전송 블록 사이즈(TBS) 결정:
   - 할당된 물리 자원 블록(PRB)의 수, 레이어 수, 그리고 결정된 변조 차수 및 코드 레이트를 입력값으로 사용합니다.
   - 중간 단계의 정보량(N_info)을 계산한 후, 스펙에 정의된 TBS 테이블 및 매핑 규칙을 적용하여 최종 TBS를 도출합니다.
   - RV는 [[DCI]]의 RV 필드로부터 직접 결정되며, 이는 [[HARQ]] 프로세스 내에서 데이터 재전송 시 사용되는 패턴을 정의합니다.

## 인과 관계
- [[DCI]] (depends_on) [[PDSCH_Transmission_Parameters]]
- [[PDSCH_Transmission_Parameters]] (affects) [[PDSCH_Resource_Mapping]]
- [[PDSCH_Transmission_Parameters]] (affects) [[PDSCH_Modulation]]

## 관련 개념
- [[PDSCH]] (part_of)
- [[HARQ]] (depends_on)
- [[DCI]] (triggers)
- [[MCS]] (depends_on)

## 스펙 근거
- TS 38.214 §5.1.3에 따르면, [[PDSCH]]의 변조 차수, 타겟 코드 레이트, RV 및 TBS 결정 절차가 정의되어 있습니다.
- TS 38.214 §5.1.3.1에 따르면, MCS 인덱스를 통한 변조 차수 및 타겟 코드 레이트 결정 방식이 명시되어 있습니다.
- TS 38.214 §5.1.3.2에 따르면, 할당된 자원과 MCS 정보를 결합하여 TBS를 산출하는 알고리즘이 기술되어 있습니다.

## 소스
- 3GPP TS 38.214 v19.0.0 (Release 19) §5.1.3, §5.1.3.1, §5.1.3.2