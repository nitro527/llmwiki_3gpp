# Modulation_Mapper

## 정의
Modulation_Mapper는 입력된 이진 비트(binary digits)를 복소수 변조 심볼(complex-valued modulation symbols)로 변환하는 물리 계층의 신호 처리 기능을 의미한다.

## 요약
Modulation_Mapper는 전송 채널을 통해 전달된 비트 스트림을 특정 변조 방식에 따라 성상도(constellation) 상의 점으로 매핑한다. 지원되는 변조 방식은 π/2-BPSK, BPSK, QPSK, 16QAM, 64QAM, 256QAM, 1024QAM을 포함하며, 각 방식은 입력 비트 수와 출력 심볼의 복소수 값에 따라 결정된다.

## 상세 설명
Modulation_Mapper는 입력된 비트 시퀀스를 수신하여, 선택된 변조 차수(modulation order)에 따라 복소수 심볼을 생성한다. 

1. 입력: 이진 비트(0 또는 1)
2. 출력: 복소수 변조 심볼
3. 변조 방식별 매핑:
   - π/2-BPSK: 1비트를 입력받아 위상 회전이 적용된 BPSK 심볼로 변환한다.
   - BPSK: 1비트를 입력받아 성상도 상의 두 점 중 하나로 매핑한다.
   - QPSK: 2비트를 입력받아 4개의 성상도 점 중 하나로 매핑한다.
   - 16QAM: 4비트를 입력받아 16개의 성상도 점 중 하나로 매핑한다.
   - 64QAM: 6비트를 입력받아 64개의 성상도 점 중 하나로 매핑한다.
   - 256QAM: 8비트를 입력받아 256개의 성상도 점 중 하나로 매핑한다.
   - 1024QAM: 10비트를 입력받아 1024개의 성상도 점 중 하나로 매핑한다.

각 변조 방식은 TS 38.211 §5.1에 정의된 성상도 매핑 규칙을 따르며, 이는 채널 환경과 MCS(Modulation and Coding Scheme) 설정에 따라 동적으로 결정된다.

## 인과 관계
- [[PUSCH_Modulation]] depends_on [[Modulation_Mapper]] (변조 심볼 생성 절차 수행)
- [[PSSCH_Modulation]] depends_on [[Modulation_Mapper]] (사이드링크 데이터 변조 수행)

## 관련 개념
- [[PUSCH_Modulation]] (implements)
- [[PSSCH_Modulation]] (implements)
- [[Channel_Coding]] (depends_on)

## 스펙 근거
- TS 38.211 §5.1: Modulation mapper의 기본 정의 및 입력/출력 사양 명시

## 소스
- 3GPP TS 38.211 V17.0.0, "Physical channels and modulation"