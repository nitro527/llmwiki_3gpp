# PSSCH_Scrambling

## 정의
[[PSSCH]] 데이터 스크램블링은 물리 계층에서 전송되는 데이터 비트 시퀀스에 의사 난수 시퀀스를 곱하여 데이터의 무작위성을 부여하고, 셀 간 또는 단말 간 간섭을 완화하기 위한 물리 계층 처리 절차입니다.

## 요약
- [선택] 15-1: Receiving NR sidelink
- [선택] 15-2: Transmitting NR sidelink mode 1 scheduled by NR Uu
- [선택] 15-3: Transmitting NR sidelink mode 2
- [선택] 15-10: 256QAM sidelink transmission
- [선택] 15-12: Low-spectral efficiency 64QAM MCS table
- [선택] 15-18: Support of rank 2 transmission
- [선택] 15-19: Support of rank 2 reception
- [선택] 16-2a-0: Overlapping PDSCHs in time and fully overlapping in frequency and time
- [선택] 19-1: DRX Adaptation
- [선택] 20-1: RACH reporting
- [선택] 20-2: Immediate Measurement – WLAN measurement
- [선택] 20-5: Logged Measurement – Bluetooth measurement

[[PSSCH]]의 전송을 위해 입력된 비트 시퀀스 $b(0), \dots, b(M_{bit}-1)$은 스크램블링 과정을 거쳐 $b^{(q)}(0), \dots, b^{(q)}(M_{bit}-1)$로 변환됩니다.

## 상세 설명
[[PSSCH]] 스크램블링은 코드워드 $q$에 대해 수행되며, 입력 비트 시퀀스에 스크램블링 시퀀스 $c^{(q)}(i)$를 적용합니다. 스크램블링된 출력 비트 $b^{(q)}(i)$는 다음과 같이 정의됩니다.

$b^{(q)}(i) = (b^{(q)}(i) + c^{(q)}(i)) \mod 2$

여기서 $c^{(q)}(i)$는 [[Sequence_Generation]]에서 정의된 Gold 시퀀스를 기반으로 생성됩니다. 스크램블링 시퀀스 생성기는 초기값 $c_{init}$에 의해 결정되며, 이는 상위 계층 파라미터 및 [[Sidelink]] 전송 환경에 따라 설정됩니다.

## 인과 관계
- [[Sidelink_Channel_Processing]] (depends_on): [[PSSCH]] 데이터 처리는 스크램블링을 포함한 물리 계층 채널 처리 과정을 거칩니다.
- [[PSSCH_Modulation]] (triggers): 스크램블링된 비트 시퀀스는 이후 [[Modulation_Mapper]]를 통해 변조 심볼로 매핑됩니다.

## 관련 개념
- [[PSSCH]] (part_of)
- [[Sequence_Generation]] (depends_on)
- [[Modulation_Mapper]] (affects)

## 스펙 근거
- TS 38.211 §8.3.1.1에 따르면, [[PSSCH]]의 스크램블링은 코드워드 $q$에 대해 수행되며, 스크램블링 시퀀스 생성 및 적용 방식이 정의되어 있습니다.

## 소스
- 3GPP TS 38.211 V17.x.x (Release 17) "Physical channels and modulation"