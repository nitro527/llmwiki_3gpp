# Sidelink_Timing

## 정의
사이드링크 프레임 타이밍은 UE가 사이드링크 전송을 시작하는 시점과 참조 프레임 간의 관계를 정의하며, 자원 예약 주기(reservation period)를 논리 슬롯(logical slot) 단위로 변환하는 절차를 포함한다.

## 요약
사이드링크 전송은 참조 프레임 시작 시점보다 특정 시간만큼 앞서 시작된다. UE는 사이드링크 전송 종료 후 일정 시간 동안 사이드링크 또는 다운링크 수신을 요구받지 않는다. 또한, 밀리초 단위의 자원 예약 주기는 자원 풀 내의 논리 슬롯 개수를 기반으로 변환되어 사이드링크 자원 할당에 사용된다.

## 상세 설명
사이드링크 무선 프레임 번호의 전송은 UE의 해당 타이밍 참조 프레임 시작 시점보다 $T_{sl}$만큼 앞서 시작된다. TS 38.211 §8.5에 따르면, $T_{sl}$은 0으로 정의된다. UE는 사이드링크 전송이 종료된 후, TS 38.133에 명시된 시간 이후에 사이드링크 또는 다운링크 전송을 수신할 수 있다.

UE가 TS 38.304 §8.2의 S 기준을 만족하는 서빙 셀을 보유한 경우:
- 참조 무선 프레임의 타이밍은 사이드링크와 동일한 상향링크 반송파 주파수를 갖는 셀의 하향링크 무선 프레임 타이밍과 동일하다.
- 타이밍 오프셋 값은 TS 38.211 §4.3.1에 따라 결정된다.

서빙 셀이 없는 경우:
- 참조 무선 프레임의 타이밍 및 관련 값은 TS 38.133 §12.2.2, §12.2.3, §12.2.4 또는 §12.2.5에 따라 결정된다.

자원 예약 주기 변환 절차:
TS 38.214 §8.1.7에 따라, 밀리초 단위의 주어진 자원 예약 주기 $P_{rsvp}$는 논리 슬롯 단위의 주기 $P_{step}$으로 다음과 같이 변환된다.
$P_{step} = P_{rsvp} \cdot \frac{N_{slot}}{1000}$
여기서 $N_{slot}$은 TS 38.211 §8에 정의된 자원 풀에 속하는 슬롯의 개수이다.

## 인과 관계
- [[Sidelink_Resource_Selection]] depends_on [[Sidelink_Timing]] (예약 주기 변환을 통한 자원 선택 수행)
- [[Synchronization_Procedures]] affects [[Sidelink_Timing]] (참조 타이밍 소스 결정)

## 관련 개념
- [[Sidelink_Resource_Configuration]] (part_of)
- [[Synchronization_Procedures]] (affects)
- [[Sidelink_Resource_Selection]] (depends_on)

## 스펙 근거
- TS 38.211 §8.5: 사이드링크 타이밍 관계 및 참조 프레임 정의
- TS 38.214 §8.1.7: 자원 예약 주기의 논리 슬롯 변환 절차

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)
- 3GPP TS 38.214 V17.x.x (Physical layer procedures for data)
- 3GPP TS 38.133 V17.x.x (Requirements for support of radio resource management)
- 3GPP TS 38.304 V17.x.x (User Equipment (UE) procedures in idle mode and RRC inactive state)