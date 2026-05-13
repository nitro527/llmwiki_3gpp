# PSSCH_DMRS_Mapping

## 정의
[[PSSCH]] 전송을 위해 생성된 [[DMRS]] 시퀀스를 물리 자원 요소(Resource Element, RE)에 배치하고, 프리코딩을 적용하여 안테나 포트로 매핑하는 물리 계층 절차를 의미한다.

## 요약
[[PSSCH_DMRS_Generation]]을 통해 생성된 시퀀스는 설정된 구성 타입에 따라 중간 양으로 매핑된 후, [[SCI]]를 통해 지시된 패턴에 따라 물리 자원에 배치된다. 이 과정에서 프리코딩 행렬과 진폭 스케일링 인자가 적용되며, 전송 자원의 시간 및 주파수 도메인 위치에 따라 최종 RE 매핑이 결정된다.

## 상세 설명
[[PSSCH]] [[DMRS]]의 물리 자원 매핑은 TS 38.211 §8.4.1.1.2에 따라 다음과 같이 수행된다.

1. 시퀀스 매핑: 생성된 시퀀스는 [[DMRS_Resource_Mapping]]의 구성 타입 1(configuration type 1)을 사용하여 중간 양으로 매핑된다. 이때 변환 프리코딩(transform precoding)은 적용되지 않는다.
2. 패턴 지시: [[DMRS]] 심볼의 시간 도메인 위치는 [[SCI]]를 통해 지시되며, TS 38.211 Table 8.4.1.1.2-1에 정의된 패턴을 따른다.
3. 프리코딩 및 스케일링: 중간 양은 프리코딩 행렬과 진폭 스케일링 인자($\beta_{PSSCH, DMRS}$)가 곱해진 후 물리 자원에 매핑된다.
   - 프리코딩 행렬은 TS 38.211 §8.3.1.4에 정의된 바를 따른다.
   - 안테나 포트 세트는 TS 38.214에 명시된 규격을 따른다.
4. 자원 매핑 조건: 매핑되는 자원 요소는 [[PSSCH]] 전송을 위해 할당된 공통 자원 블록(Common Resource Blocks) 내에 위치해야 한다.
5. 위치 정의: 
   - 주파수 도메인 위치는 공통 자원 블록 0의 서브캐리어 0을 기준으로 정의된다.
   - 시간 도메인 위치는 [[PSCCH]]를 포함한 [[PSSCH]] 전송을 위해 스케줄링된 자원의 시작점을 기준으로 정의되며, 중복된 OFDM 심볼을 포함한다.

## 인과 관계
- [[PSSCH_DMRS_Generation]] depends_on [[PSSCH_DMRS_Mapping]] (DMRS 시퀀스 생성 결과가 매핑의 입력으로 사용됨)
- [[PSSCH_DMRS_Mapping]] affects [[PSSCH_Transmission_Procedure]] (DMRS 매핑 결과가 최종 물리 채널 전송에 반영됨)

## 관련 개념
- [[PSSCH]] (part_of)
- [[DMRS]] (part_of)
- [[SCI]] (affects)
- [[PSSCH_DMRS_Generation]] (depends_on)

## 스펙 근거
- TS 38.211 §8.4.1.1.2: PSSCH DM-RS의 물리 자원 매핑 절차 및 파라미터 정의
- TS 38.212 §8.3.1.1: SCI를 통한 DM-RS 패턴 지시
- TS 38.214 §8.1.2.1: PSSCH 전송 자원 및 안테나 포트 관련 규격

## 소스
- 3GPP TS 38.211 V18.0.0 (2023-12) Physical channels and modulation