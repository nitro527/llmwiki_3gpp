# Frame_Structure

## 정의
5G NR에서 시간 및 주파수 영역의 물리 자원을 체계적으로 관리하기 위한 계층적 구조를 의미하며, 프레임, 서브프레임, 슬롯 및 자원 그리드(Resource Grid)로 구성된다.

## 요약
5G NR은 다양한 서비스 요구사항을 충족하기 위해 가변적인 [[OFDM]] 뉴머롤로지(Numerology)를 지원한다. 시간 영역은 10ms 프레임 내에 서브프레임과 슬롯이 정의되며, 주파수 영역은 [[Bandwidth_Part_Operation]]을 통해 동적으로 자원을 할당한다. 모든 물리 자원은 시간 단위 $T_c$를 기준으로 정의된다.

## 상세 설명
### 시간 영역 구조
- 프레임(Frame): 10ms의 길이를 가지며, 10개의 서브프레임으로 구성된다.
- 서브프레임(Subframe): 1ms의 길이를 가지며, 슬롯의 개수는 뉴머롤로지 $\mu$에 따라 결정된다.
- 슬롯(Slot): $\mu$에 따라 한 서브프레임 내 슬롯 개수($N_{slot}^{subframe, \mu}$)와 슬롯당 OFDM 심볼 개수가 결정된다.
- 시간 단위: $T_c = 1 / (\Delta f_{max} \cdot N_f)$로 정의되며, 여기서 $\Delta f_{max} = 480 \cdot 10^3$ Hz, $N_f = 4096$이다.

### 뉴머롤로지(Numerology)
서브캐리어 간격(Subcarrier Spacing, SCS)은 $\Delta f = 2^\mu \cdot 15$ kHz로 정의된다. $\mu$ 값에 따라 슬롯의 길이와 심볼의 지속 시간이 달라지며, 이는 고주파수 대역과 저주파수 대역의 유연한 운용을 가능하게 한다.

### 물리 자원(Physical Resources)
- 자원 그리드(Resource Grid): 특정 뉴머롤로지 $\mu$와 캐리어에 대해 $N_{grid, x}^{size, \mu} \cdot N_{sc}^{RB}$개의 서브캐리어와 $N_{symb}^{subframe, \mu}$개의 OFDM 심볼로 구성된다.
- 자원 블록(Resource Block, RB): 주파수 영역에서 12개의 연속적인 서브캐리어로 정의된다.
- [[Bandwidth_Part_Operation]]: 전체 캐리어 대역폭 내에서 UE가 실제 데이터를 송수신하는 주파수 영역의 부분 집합을 설정하여 전력 소모를 최적화한다.

## 인과 관계
- [[OFDM_Baseband_Signal_Generation]] depends_on [[Frame_Structure]] (물리 자원 그리드 기반 신호 생성)
- [[Bandwidth_Part_Operation]] affects [[Frame_Structure]] (활성 BWP 내 자원 그리드 범위 결정)
- [[Slot_Format_Configuration]] affects [[Frame_Structure]] (슬롯 내 심볼의 방향성 결정)

## 관련 개념
- [[OFDM_Baseband_Signal_Generation]] (implements)
- [[Bandwidth_Part_Operation]] (affects)
- [[Slot_Format_Configuration]] (affects)

## 스펙 근거
- TS 38.211 §4.1: 시간 단위 $T_c$ 정의 및 상수 값 명시
- TS 38.211 §4.2: 뉴머롤로지 $\mu$ 및 서브캐리어 간격 정의
- TS 38.211 §4.3: 프레임, 서브프레임, 슬롯 구조 정의
- TS 38.211 §4.4: 자원 그리드 및 자원 블록 정의

## 소스
- 3GPP TS 38.211 V17.9.0 (2023-12) Physical channels and modulation