# PSBCH

## 정의
PSBCH(Physical Sidelink Broadcast Channel)는 사이드링크 통신에서 동기화 정보 및 시스템 정보를 인접 단말(UE)로 전달하기 위해 사용되는 물리 채널입니다.

## 요약
PSBCH는 S-PSS(Sidelink Primary Synchronization Signal) 및 S-SSS(Sidelink Secondary Synchronization Signal)와 함께 S-SS/PSBCH 블록을 구성합니다. 이 블록은 사이드링크 동기화 절차의 핵심 요소로, 단말 간의 시간 및 주파수 동기화를 맞추고 TDD 설정 정보를 공유하는 데 사용됩니다.

## 상세 설명
PSBCH는 SL-BCH(Sidelink Broadcast Channel) 전송 채널을 물리 계층에서 처리하며, 주요 동작은 다음과 같습니다.

1. **전송 채널 처리**: SL-BCH는 BCH의 절차를 따르되, 80ms 주기 제한이 없으며 PBCH 페이로드 생성 및 스크램블링 절차를 생략합니다. 레이트 매칭 출력 시퀀스 길이(E)는 cyclicPrefix 설정에 따라 1386(ECP) 또는 1782(NCP)로 결정됩니다.
2. **S-SS/PSBCH 블록 구성**: PSBCH는 S-PSS, S-SSS와 연속된 심볼에서 전송됩니다. 단말은 이 블록 내의 서브캐리어 인덱스 66을 기준으로 주파수 위치를 결정하며, 이는 anchor RB-set 또는 non-anchor RB-set 설정에 따라 달라집니다.
3. **동기화 및 TDD 설정**: 단말은 sl-NumSSB-WithinPeriod를 통해 16 프레임 주기 내의 S-SS/PSBCH 블록 수를 전달받습니다. 또한, PSBCH 페이로드 내의 비트 시퀀스를 통해 sl-TDD-Config를 전달하여 슬롯 포맷 정보를 공유합니다.
4. **전송 절차**: 공유 스펙트럼 채널 접속(Shared spectrum channel access) 환경에서는 anchor RB-set에서 전송을 시도하며, 실패 시 non-anchor RB-set을 사용할 수 있습니다. 전송 시 첫 심볼에 CP 확장을 적용하며, 인접 단말과의 우선순위 충돌 시 더 높은 우선순위의 신호를 전송합니다.

## 인과 관계
- [[Sidelink_Timing]] depends_on [[PSBCH]] (동기화 정보 획득을 위한 PSBCH 수신 전제)
- [[PSBCH]] implements [[SL-BCH]] (SL-BCH 전송 채널의 물리 계층 구현)
- [[PSBCH]] part_of [[S-SS/PSBCH_Block_Generation]] (S-SS/PSBCH 블록의 구성 요소)
- [[PSBCH_Scrambling]] affects [[PSBCH]] (물리 채널 데이터의 스크램블링 적용)
- [[PSBCH_DMRS_Generation]] affects [[PSBCH]] (채널 추정을 위한 참조 신호 생성)

## 관련 개념
- [[S-SS/PSBCH_Block_Generation]] (part_of)
- [[SL-BCH]] (implements)
- [[PSBCH_Scrambling]] (affects)
- [[PSBCH_DMRS_Generation]] (affects)
- [[Sidelink_Timing]] (depends_on)
- [[Synchronization_Procedures]] (implements)

## 스펙 근거
- TS 38.211 §8.3.3: PSBCH 물리 채널 정의 및 구성
- TS 38.212 §8.1: SL-BCH 전송 채널 처리 및 레이트 매칭
- TS 38.213 §16.1: 사이드링크 동기화 절차 및 PSBCH 전송/수신 파라미터

## 소스
- 3GPP TS 38.211 Physical channels and modulation
- 3GPP TS 38.212 Multiplexing and channel coding
- 3GPP TS 38.213 Sidelink synchronization procedures