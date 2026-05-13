# PUSCH_Transform_Precoding

## 정의
[[PUSCH]] 전송 시 신호의 PAPR(Peak-to-Average Power Ratio)을 낮추기 위해 DFT(Discrete Fourier Transform) 기반의 프리코딩을 적용하는 물리 계층 절차를 의미한다.

## 요약
[[PUSCH]] 전송에서 변환 프리코딩은 상위 계층 파라미터 및 [[DCI]] 필드에 의해 활성화 여부가 결정된다. 활성화 시, 변조 심볼은 DFT 연산을 거쳐 주파수 도메인에서 확산되며, 이는 [[OFDM_Baseband_Signal_Generation]] 과정의 일부로 수행된다.

## 상세 설명
변환 프리코딩이 활성화되면, 단일 레이어에 대한 복소수 심볼 블록은 각 [[OFDM]] 심볼에 대응하는 세트로 분할된다. 

1. **변환 프리코딩 적용**: 복소수 심볼 블록 $d(0), \dots, d(M_{symb}^{ap}-1)$에 대해 다음 식을 적용한다.
   $z(l \cdot M_{sc}^{PUSCH} + k) = \frac{1}{\sqrt{M_{sc}^{PUSCH}}} \sum_{m=0}^{M_{sc}^{PUSCH}-1} d(l \cdot M_{sc}^{PUSCH} + m) e^{-j \frac{2\pi km}{M_{sc}^{PUSCH}}}$
   여기서 $k = 0, \dots, M_{sc}^{PUSCH}-1$이며, $M_{sc}^{PUSCH}$는 자원 블록 단위의 [[PUSCH]] 대역폭에 대응하는 서브캐리어 수이다.

2. **[[PUSCH_PTRS_Generation]] 연동**: 
   - [[PUSCH_PTRS_Generation]]이 사용되지 않는 경우, 심볼 블록은 각 [[OFDM]] 심볼에 대응하는 세트로 나뉜다.
   - [[PUSCH_PTRS_Generation]]이 사용되는 경우, 심볼 블록은 [[OFDM]] 심볼별 세트로 나뉘며, 각 세트는 [[PUSCH_PTRS_Generation]] 샘플을 포함하거나 제외하여 구성된다.

3. **활성화 결정 로직**:
   - **RAR/Fallback RAR/TC-RNTI**: 상위 계층 파라미터 `msg3-transformPrecoder`에 따름.
   - **MsgA PUSCH**: `msgA-TransformPrecoder`가 설정된 경우 이를 따르고, 미설정 시 `msg3-transformPrecoder`를 따름.
   - **C-RNTI/MCS-C-RNTI/CS-RNTI**: 
     - [[DCI]] format 0_0 사용 시 `msg3-transformPrecoder`에 따름.
     - [[DCI]] format 0_1/0_2 사용 시, `dynamicTransformPrecoderFieldPresenceDCI-0-1` 또는 `dynamicTransformPrecoderFieldPresenceDCI-0-2`가 'enabled'이면 [[DCI]] 내 Transform precoder indicator 필드에 따름.
     - 그 외의 경우 `transformPrecoder` 파라미터 설정에 따르며, 미설정 시 `msg3-transformPrecoder`를 따름.
   - **Configured Grant**: `transformPrecoder` 파라미터 설정에 따르며, 미설정 시 `msg3-transformPrecoder`를 따름.

## 인과 관계
- [[PUSCH_Transform_Precoding]] affects [[OFDM_Baseband_Signal_Generation]] (DFT 연산 후 신호 생성)
- [[PUSCH_Transform_Precoding]] depends_on [[PUSCH_PTRS_Generation]] (PT-RS 샘플 포함 여부에 따른 심볼 분할)
- [[PUSCH_Transform_Precoding]] depends_on [[DCI_Field_Mapping]] (동적 활성화 여부 결정)

## 관련 개념
- [[PUSCH]] (part_of)
- [[OFDM_Baseband_Signal_Generation]] (implements)
- [[PUSCH_PTRS_Generation]] (affects)
- [[DCI_Field_Mapping]] (affects)

## 스펙 근거
- TS 38.211 §6.3.1.4: 변환 프리코딩 수식 및 심볼 매핑 정의
- TS 38.214 §6.1.3: UE의 변환 프리코딩 적용 절차 및 활성화 결정 조건

## 소스
- 3GPP TS 38.211 V17.x.x (Physical channels and modulation)
- 3GPP TS 38.214 V17.x.x (Physical layer procedures for data)