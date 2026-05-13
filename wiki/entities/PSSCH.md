# PSSCH

## 정의
[[PSSCH]]는 5G NR Sidelink 통신에서 사용자 데이터(SL-SCH)를 전송하기 위해 사용되는 물리 채널로, [[PSCCH]]와 함께 자원 풀 내에서 데이터 전송을 수행한다.

## 요약
[[PSSCH]]는 상위 계층에서 설정된 Sidelink 자원 풀 내에서 데이터를 전송하며, [[SL-SCH]] 전송 채널의 물리적 구현체이다. 자원 할당 방식에 따라 연속적인 RB(contiguousRB) 또는 인터레이스(interlaceRB) 구조를 가지며, [[Sidelink_Resource_Configuration]]에 따라 시간 및 주파수 자원이 결정된다.

## 상세 설명
[[PSSCH]]의 동작은 TS 38.213 §16 및 TS 38.214 §8에 정의되어 있다.

1. 자원 풀 설정:
   - 상위 계층 파라미터인 `sl-TransmissionStructureForPSCCHandPSSCH`에 따라 주파수 도메인 구조가 결정된다.
   - 'contiguousRB' 모드에서는 `sl-NumSubchannel`과 `sl-SubchannelSize`를 통해 서브채널이 구성된다.
   - 'interlaceRB' 모드에서는 RB 세트 내의 인터레이스 개수를 기반으로 서브채널이 구성된다.
   - 공유 스펙트럼 채널 액세스(shared spectrum channel access) 환경에서는 RB 세트 간의 가드 밴드(intra-cell guard bands)를 활용한 전송이 가능하다.

2. 시간 도메인 자원:
   - 가용한 슬롯은 `sl-TimeResource`에 의해 결정되며, 10240ms 주기로 반복된다.
   - 전송 시작 심볼은 `sl-StartSymbol` 또는 `sl-StartingSymbolFirst`/`sl-StartingSymbolSecond`에 의해 결정되며, `sl-LengthSymbols`에 정의된 연속 심볼 범위 내에서 전송된다.

3. 데이터 처리:
   - [[SL-SCH]]의 처리는 [[UL-SCH]]의 절차를 따르며, 레이트 매칭(rate matching)은 TS 38.212 §8.2에 명시된 규칙을 따른다.
   - [[PSSCH]]의 우선순위는 스케줄링 [[SCI]] 포맷의 우선순위 필드에 의해 지시된다.

4. 공유 스펙트럼 동작:
   - 채널 액세스 절차가 성공한 경우에만 전송이 가능하며, 인접한 RB 세트 간의 가드 밴드 PRB는 두 RB 세트 모두에서 채널 액세스에 성공한 경우에 한해 [[PSSCH]] 전송에 사용될 수 있다.

## 인과 관계
- [[PSSCH]] depends_on [[Sidelink_Resource_Configuration]] (자원 풀 및 서브채널 설정 전제)
- [[PSSCH]] depends_on [[PSCCH]] (데이터 전송을 위한 제어 정보 수신)
- [[PSSCH]] implements [[SL-SCH]] (전송 채널의 물리적 매핑)
- [[PSSCH]] affects [[Sidelink_Transmission_Procedure]] (데이터 전송 절차 수행)

## 관련 개념
- [[PSCCH]] (affects)
- [[SL-SCH]] (implements)
- [[Sidelink_Resource_Configuration]] (depends_on)
- [[Sidelink_Transmission_Procedure]] (affects)
- [[PSSCH_Resource_Mapping]] (part_of)
- [[PSSCH_DMRS_Mapping]] (part_of)

## 스펙 근거
- TS 38.211 §8.3.1: [[PSSCH]] 물리 채널 정의
- TS 38.212 §8.2: [[SL-SCH]] 처리 및 레이트 매칭 규칙
- TS 38.213 §16: Sidelink 자원 풀 설정 및 슬롯/심볼 결정 절차
- TS 38.214 §8: [[PSSCH]] 관련 자원 할당 및 공유 스펙트럼 동작 절차

## 소스
- 3GPP TS 38.211 V16.9.0 (2022-03)
- 3GPP TS 38.212 V16.8.0 (2022-03)
- 3GPP TS 38.213 V16.8.0 (2022-03)
- 3GPP TS 38.214 V16.9.0 (2022-03)