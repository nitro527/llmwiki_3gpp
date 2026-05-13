# Sidelink_Resource_Configuration

## 정의
[[Sidelink_Resource_Configuration]]은 [[NR]] [[Sidelink]] 통신을 위해 [[UE]]가 사용하는 물리적 자원 그리드, [[BWP]], 자원 풀(Resource Pool), 그리고 시간-주파수 자원 할당 규칙을 정의하는 설정 체계입니다.

## 요약
[[Sidelink]] 통신을 수행하는 [[UE]]는 상위 계층으로부터 [[SL-BWP-Config]] 또는 [[SL-BWP-ConfigCommon]]을 통해 [[SL_BWP]]를 제공받습니다. 자원 풀 내의 자원 할당은 주파수 도메인에서의 서브채널(Sub-channel) 구성과 시간 도메인에서의 슬롯(Slot) 선택 메커니즘을 통해 이루어지며, 이는 [[PSSCH]], [[PSCCH]], [[PSFCH]], 그리고 [[SL_PRS]] 전송을 지원합니다.

## 상세 설명
[[Sidelink]] 자원 설정은 TS 38.213 §16 및 TS 38.214 §8에 따라 다음과 같이 구성됩니다.

### 주파수 도메인 설정
- [[SL_BWP]] 내의 자원 풀은 주파수 도메인에서 서브채널 단위로 할당됩니다.
- 공유 스펙트럼 채널 접근(Shared spectrum channel access)을 사용하지 않거나, 'contiguousRB' 모드인 경우:
  - [[sl-NumSubchannel]]을 통해 서브채널 개수를, [[sl-SubchannelSize]]를 통해 각 서브채널의 연속적인 [[RB]] 개수를 설정합니다.
  - 첫 번째 서브채널의 시작 [[RB]]는 [[sl-StartRB-Subchannel]]로 지정됩니다.
- 'interlaceRB' 모드인 경우:
  - 각 [[RB_set]] 내의 서브채널 개수는 해당 RB 세트 내의 인터레이스(Interlace) 개수를 [[sl-NumInterlacePerSubchannel]]로 나눈 값으로 결정됩니다.

### 시간 도메인 설정
- 자원 풀에 사용 가능한 슬롯은 [[sl-TimeResource]] 파라미터와 10240 ms 주기를 기반으로 결정됩니다.
- 슬롯 선택 시 [[S-SSB]]가 설정된 슬롯이나, [[tdd-UL-DL-ConfigurationCommon]] 또는 [[sl-TDD-Configuration]]에 의해 UL로 설정되지 않은 심볼을 포함하는 슬롯은 제외됩니다.
- 비트맵(Bitmap) 기반의 논리적 슬롯 할당을 통해 최종 전송 가능한 슬롯 집합이 결정됩니다.
- 전송 시작 심볼은 [[sl-StartSymbol]] 또는 [[sl-StartingSymbolFirst]]/[[sl-StartingSymbolSecond]]에 의해 정의되며, 전송 길이는 [[sl-LengthSymbols]]에 의해 제한됩니다.

### 공유 스펙트럼 및 특수 설정
- 공유 스펙트럼 채널 접근 시, [[RB_set]] 간의 [[Intra_Cell_Guard_Band_Operation]] 내 [[RB]]는 특정 조건(채널 접근 성공 및 양쪽 RB 세트 사용) 하에서만 [[PSSCH]] 전송에 활용 가능합니다.
- [[SL_PRS]] 전송을 위한 전용 자원 풀(Dedicated SL PRS resource pool)이 설정될 수 있으며, 이는 [[PSSCH]] 전송 가능 여부에 따라 공유 또는 전용 풀로 구분됩니다.

## 인과 관계
- [[SL_BWP]] depends_on [[Frame_Structure]] (뉴머롤로지 및 자원 그리드 결정 전제)
- [[PSSCH]] depends_on [[Sidelink_Resource_Configuration]] (자원 풀 내 서브채널 및 슬롯 할당 기반 전송)
- [[PSCCH]] depends_on [[Sidelink_Resource_Configuration]] (자원 풀 내 자원 매핑 및 전송 구조 결정)
- [[PSFCH]] depends_on [[Sidelink_Resource_Configuration]] (자원 풀 내 자원 할당 및 우선순위 결정)
- [[SL_PRS]] depends_on [[Sidelink_Resource_Configuration]] (전용 또는 공유 자원 풀 설정 기반 전송)
- [[Intra_Cell_Guard_Band_Operation]] affects [[Sidelink_Resource_Configuration]] (가드 밴드 내 자원 활용 가능 여부 결정)

## 관련 개념
- [[SL_BWP]] (part_of)
- [[PSSCH]] (implements)
- [[PSCCH]] (implements)
- [[PSFCH]] (implements)
- [[SL_PRS]] (implements)
- [[Intra_Cell_Guard_Band_Operation]] (affects)
- [[Frame_Structure]] (depends_on)

## 스펙 근거
- TS 38.211 §8.1, §8.2: Sidelink 물리 자원 및 개요
- TS 38.213 §16: Sidelink 자원 풀 설정 및 슬롯/서브채널 결정 절차
- TS 38.214 §8: Sidelink 자원 풀 구성 및 공유 스펙트럼 채널 접근 관련 규칙

## 소스
- 3GPP TS 38.211 V17.9.0 (2024-03)
- 3GPP TS 38.213 V17.9.0 (2024-03)
- 3GPP TS 38.214 V17.9.0 (2024-03)