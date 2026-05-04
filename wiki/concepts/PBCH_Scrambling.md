# PBCH_Scrambling

## 정의
[[PBCH]] 전송을 위해 인코딩된 비트 시퀀스에 대해 물리 계층에서 수행하는 스크램블링 절차를 의미하며, 이는 [[SS_PBCH_Block]] 인덱스 정보를 포함하여 초기화됩니다.

## 요약
[[PBCH]] 데이터는 전송 전 스크램블링 과정을 거치며, 이 과정은 [[SS_PBCH_Block]] 내의 인덱스 정보를 활용하여 초기화된 시퀀스를 사용합니다. 이는 [[UE]]가 [[SS_PBCH_Block]]의 인덱스를 식별하고 셀 동기를 획득하는 데 필수적인 과정입니다.

## 상세 설명
[[PBCH]]의 스크램블링은 TS 38.211 §7.3.3.1에 정의된 절차를 따릅니다. 
- 스크램블링 시퀀스 생성은 [[Sequence_Generation]]의 골드 시퀀스 생성 방식을 따르며, 초기값 $c_{init}$은 [[SS_PBCH_Block]] 인덱스($\bar{i}_{SSB}$)와 셀 식별자($N_{ID}^{cell}$)에 의해 결정됩니다.
- 구체적으로 $c_{init} = N_{ID}^{cell}$로 설정되며, 이는 [[PBCH]] 페이로드의 일부인 [[SS_PBCH_Block]] 인덱스 정보와 결합되어 스크램블링 시퀀스를 생성합니다.
- 스크램블링된 비트 $\tilde{b}(i)$는 인코딩된 비트 $b(i)$와 스크램블링 시퀀스 $c(i)$의 모듈로-2 합산($\tilde{b}(i) = (b(i) + c(i)) \mod 2$)을 통해 생성됩니다.
- 이 과정은 [[Channel_Coding_General]] 이후에 수행되어 물리 채널 매핑 전의 최종 비트 단계를 구성합니다.

## 인과 관계
- [[SS_PBCH_Block]] (part_of)
- [[Channel_Coding_General]] (depends_on)
- [[PBCH_Modulation]] (affects)

## 관련 개념
- [[SS_PBCH_Block]] (part_of)
- [[Channel_Coding_General]] (depends_on)
- [[PBCH_Modulation]] (affects)

## 스펙 근거
- TS 38.211 §7.3.3.1: [[PBCH]] 스크램블링 시퀀스 생성 및 초기화 절차 정의
- TS 38.212 §7.1.2: [[PBCH]] 채널 코딩 후 스크램블링 적용 단계 명시

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)
- 3GPP TS 38.212 V17.x.x (Multiplexing and channel coding)