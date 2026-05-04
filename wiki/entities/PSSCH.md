# PSSCH

## 정의
[[PSSCH]]는 [[Sidelink]] 통신에서 데이터 전송을 담당하는 물리 채널로, [[UE]] 간의 직접적인 데이터 공유를 위해 사용되는 물리 계층 채널이다.

## 요약
[[PSSCH]]는 [[Sidelink]] 자원 풀 내에서 데이터를 전송하며, [[SCI]]를 통해 제어 정보를 전달받아 자원 할당 및 복조를 수행한다. 본 채널은 [[Scrambling]], [[Modulation]], [[Layer mapping]], [[Precoding]] 과정을 거쳐 물리 자원에 매핑되며, [[HARQ]] 피드백 및 [[CSI]] 보고 절차와 연동된다.

## 상세 설명
[[PSSCH]]의 물리 계층 처리는 다음과 같은 단계로 구성된다.

1. **데이터 및 제어 다중화**: [[TS 38.212 §8.2]]에 따라 [[PSSCH]]는 데이터와 [[SCI]] format 2-A, 2-B, 2-C, 2-D와 같은 2nd-stage [[SCI]] 정보를 다중화하여 전송한다.
2. **신호 처리**: [[TS 38.211 §8.3.1]]에 정의된 바와 같이 [[Scrambling]], [[Modulation]], [[Layer mapping]], [[Precoding]] 과정을 거친다.
3. **자원 매핑**: 가상 자원 블록(VRB)에서 물리 자원 블록(PRB)으로의 매핑이 수행된다.
4. **전송 절차**: [[TS 38.214 §8]]에 따라 [[UE]]는 자원 풀 내에서 시간 및 주파수 영역의 자원을 할당받으며, [[Modulation order]], [[Target code rate]], [[Redundancy version]], [[Transport block size]]를 결정한다.
5. **참조 신호**: [[PSSCH]] 전송과 함께 [[DMRS]], [[PT-RS]], [[CSI-RS]] 등이 전송되어 채널 추정 및 측정에 활용된다.

## 인과 관계
- [[SCI]] (triggers) [[PSSCH]] 자원 할당 및 복조 파라미터 결정
- [[Sidelink]] 자원 풀 구성 (affects) [[PSSCH]] 자원 선택 범위
- [[PSSCH]] (depends_on) [[PSCCH]]를 통한 1st-stage [[SCI]] 정보
- [[PSSCH]] (triggers) [[PSFCH]]를 통한 [[HARQ]] 피드백 전송

## 관련 개념
- [[Sidelink]] (part_of)
- [[PSCCH]] (depends_on)
- [[PSFCH]] (triggers)
- [[SCI]] (depends_on)
- [[DMRS]] (part_of)
- [[CSI-RS]] (part_of)

## 스펙 근거
- [[TS 38.211 §8.3.1]]: [[PSSCH]] 물리 계층 신호 처리 절차
- [[TS 38.212 §8.2]]: [[PSSCH]] 데이터 및 제어 정보 다중화
- [[TS 38.212 §8.4]]: [[PSSCH]] 상의 [[SCI]] 포맷 및 채널 코딩
- [[TS 38.213 §16.2.1]]: [[PSSCH]] 전송 관련 절차
- [[TS 38.214 §8]]: [[PSSCH]] 자원 할당 및 전송 파라미터 결정

## 소스
- 3GPP TS 38.211 V16.9.0 (Physical channels and modulation)
- 3GPP TS 38.212 V16.9.0 (Multiplexing and channel coding)
- 3GPP TS 38.213 V16.9.0 (Physical layer procedures for control)
- 3GPP TS 38.214 V16.9.0 (Physical layer procedures for data)