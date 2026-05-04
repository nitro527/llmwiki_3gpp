# PUSCH Transform Precoding

## 정의
[[PUSCH]] 전송 시 파형(waveform)을 CP-OFDM에서 DFT-s-OFDM으로 전환하여 전송하는 기술을 의미한다. 주로 단말의 송신 전력 효율을 높이고 PAPR(Peak-to-Average Power Ratio)을 낮추기 위해 사용된다.

## 요약
[[PUSCH]] Transform Precoding은 상위 계층 파라미터인 `transformPrecoder`에 의해 활성화 여부가 결정된다. 이 기능이 활성화되면 단말은 DFT-s-OFDM 파형을 사용하여 데이터를 전송하며, 이는 MCS 테이블 선택, 변조 차수 결정, 그리고 [[DMRS]] 구성 방식에 직접적인 영향을 미친다.

## 상세 설명
1. **활성화 결정**: 상위 계층 파라미터 `transformPrecoder`가 'enabled'로 설정된 경우, 단말은 해당 [[BWP]] 내의 [[PUSCH]] 전송에 대해 Transform Precoding을 적용한다.
2. **파형 전환**: Transform Precoding이 활성화되면 [[PUSCH]] 전송은 CP-OFDM 대신 DFT-s-OFDM 파형을 사용한다.
3. **MCS 테이블 연동**: Transform Precoding 적용 여부에 따라 사용할 수 있는 MCS 테이블이 달라진다. 예를 들어, 특정 테이블은 Transform Precoding이 활성화된 경우에만 사용 가능하며, 이는 [[PUSCH_Modulation]] 및 코드 레이트 결정에 영향을 준다.
4. **DMRS 영향**: Transform Precoding 적용 시, 낮은 PAPR 특성을 유지하기 위해 전용 [[DMRS]] 시퀀스 생성 및 매핑 방식이 적용된다.

## 인과 관계
- `transformPrecoder` (RRC) triggers [[PUSCH]] 파형 결정 (CP-OFDM vs DFT-s-OFDM)
- Transform Precoding 활성화 depends_on [[PUSCH]] MCS 테이블 선택
- Transform Precoding 활성화 affects [[DMRS]] 시퀀스 생성 및 PAPR 최적화

## 관련 개념
- [[PUSCH]] (part_of)
- [[DMRS]] (affects)
- [[PUSCH_Modulation]] (depends_on)
- [[BWP]] (part_of)
- [[PTRS_Generation_Mapping]] (affects)
- [[PUCCH_Format_Processing]] (affects)
- [[PUSCH_Layer_Mapping]] (affects)
- [[PUSCH_PTRS_Transmission]] (affects)

## 스펙 근거
- TS 38.211 §6.3.1.4: Transform precoding 적용 시의 DFT-s-OFDM 신호 생성 절차 정의
- TS 38.214 §6.1.3: 단말의 Transform precoding 적용 절차 및 RRC 파라미터 연동 규정
- TS 38.214 §6.1.4.1: Transform precoding 활성화 여부에 따른 변조 차수 및 타겟 코드 레이트 결정 방식
- TS 38.214 §6.1.4.2: Transform precoding 활성화 시의 TB(Transport Block) 크기 결정 절차

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03)
- 3GPP TS 38.214 V16.9.0 (2022-03)

## 이 페이지를 링크하는 페이지들 (inbound links)
- concepts/PTRS_Generation_Mapping.md
- concepts/PUCCH_Format_Processing.md
- concepts/PUSCH_Layer_Mapping.md
- concepts/PUSCH_PTRS_Transmission.md
- entities/PUSCH.md