# PUSCH_Scrambling

## 정의

[[PUSCH]] 전송 전에 비트 시퀀스를 Gold 시퀀스와 XOR하여 무작위화하는 절차.
[[DMRS]] 와는 독립적으로 데이터 비트에만 적용된다.

## 요약

[[PUSCH]] Scrambling은 [[PUSCH]] 데이터 비트 시퀀스 b(0)...b(M_bit-1)에
스크램블링 시퀀스 c(i)를 XOR하여 b_tilde(i) = (b(i) + c(i)) mod 2 를 생성한다.
스크램블링 시퀀스는 [[RNTI]], 코드워드 인덱스, n_ID로 초기화된다.

## 상세 설명

TS 38.211 §6.3.1에 따르면, 물리 계층에 전달된 비트 시퀀스
b(0), ..., b(M_bit - 1)는 변조 이전에 스크램블링된다.

스크램블링 공식:
```
b_tilde(i) = (b(i) + c(i)) mod 2
```

스크램블링 시퀀스 c(i)는 TS 38.211 §5.2.1의 length-31 Gold 시퀀스이며,
초기화 값은 다음과 같다:
```
c_init = n_RNTI × 2^15 + q × 2^14 + n_ID
```
- n_RNTI: C-RNTI (Cell Radio Network Temporary Identifier)
- q: 코드워드 인덱스 (0 또는 1)
- n_ID: RRC 상위 계층에서 설정, 범위 [0, 1023]

n_ID가 설정되지 않은 경우 n_ID = n_cell_ID (물리 셀 ID) 를 사용한다.

## 인과 관계

- n_RNTI가 변경되면(예: RRC 재설정) c_init이 변경되어 스크램블링 패턴이 달라진다.
- 동일 슬롯 내 두 UE의 n_RNTI가 다르면 스크램블링 시퀀스가 달라져 간섭이 무작위화된다.
- [[HARQ]] 재전송 시 RV(Redundancy Version)가 바뀌어도 n_RNTI는 동일하므로
  스크램블링 시퀀스는 변하지 않는다.

## 관련 개념

- [[PUSCH]] (part_of)
- [[DMRS]] (similar_to)
- [[HARQ]] (affects)
- [[BWP]] (depends_on)
- [[Gold_Sequence]] (depends_on)

## 스펙 근거

- TS 38.211 §6.3.1: PUSCH 스크램블링 공식 및 c_init 정의
- TS 38.211 §5.2.1: Gold 시퀀스 생성 방법
- TS 38.211 §6.3.1.1: c_init 파라미터 상세

## 소스

- 3gpp/38211-i90.docx §6.3.1
- 3gpp/38211-i90.docx §6.3.1.1
