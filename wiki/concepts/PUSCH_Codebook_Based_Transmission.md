# PUSCH_Codebook_Based_Transmission

## 정의
[[PUSCH]] Codebook Based Transmission은 기지국(gNB)이 제공하는 [[DCI]] 내의 [[SRI]]와 [[TPMI]] 정보를 기반으로, [[UE]]가 사전에 정의된 코드북을 사용하여 [[Precoding]]을 수행하고 데이터를 전송하는 상향링크 전송 방식입니다.

## 요약
본 방식은 [[SRS]] 리소스 세트 설정을 통해 [[MIMO]] 전송을 지원하며, [[UE]]는 [[SRI]]를 통해 사용할 [[SRS]] 리소스를 선택하고, [[TPMI]]를 통해 해당 리소스에 적용할 프리코딩 행렬을 결정합니다. 또한, [[Full_Power_Transmission]] 모드를 지원하여 [[UE]]의 송신 전력을 효율적으로 활용할 수 있습니다.

## 상세 설명
- **기본 절차**: [[UE]]는 상위 계층 파라미터 `txConfig`가 'codebook'으로 설정된 경우 본 방식을 사용합니다. [[UE]]는 [[SRS]] 리소스 세트 내의 리소스들을 통해 채널 상태를 기지국에 보고하며, 기지국은 [[DCI]] 필드인 [[SRI]]와 [[TPMI]]를 통해 전송 파라미터를 지시합니다.
- **SRI 및 TPMI**: [[SRI]]는 [[SRS]] 리소스 세트 내에서 어떤 [[SRS]] 리소스가 사용될지 결정하며, [[TPMI]]는 선택된 [[SRS]] 리소스의 안테나 포트 수와 레이어 수에 대응하는 코드북 내의 프리코딩 행렬을 지정합니다.
- **Full Power Transmission**: [[UE]]는 [[Full_Power_Transmission]] 모드(mode 0, 1, 2)를 지원하여, 특정 조건에서 안테나 포트 간 전력을 재분배하거나 최대 송신 전력을 유지할 수 있습니다. 이는 [[UE]]의 하드웨어 능력에 따라 결정됩니다.
- **Codebook Subset Restriction**: 기지국은 상위 계층 시그널링을 통해 특정 프리코딩 행렬의 사용을 제한할 수 있습니다.

## 인과 관계
- [[SRS]] 리소스 설정 (triggers) [[SRI]] 기반 프리코더 선택
- [[SRI]] 및 [[TPMI]] 수신 (triggers) [[PUSCH]] [[Precoding]] 수행
- [[Full_Power_Transmission]] 모드 설정 (affects) [[TPMI]] 그룹 구성 및 전력 할당

## 관련 개념
- [[PUSCH]] (part_of)
- [[SRS]] (depends_on)
- [[DCI]] (depends_on)
- [[Precoding]] (affects)
- [[Full_Power_Transmission]] (similar_to)

## 스펙 근거
- TS 38.214 §6.1.1.1에 따르면, 코드북 기반 전송을 위해 [[UE]]는 `txConfig`가 'codebook'으로 설정되어야 하며, [[SRI]]를 통해 선택된 [[SRS]] 리소스와 [[TPMI]]를 통해 지시된 프리코딩 행렬을 사용하여 [[PUSCH]]를 전송합니다.
- TS 38.214 §6.1.1.1에 따르면, [[UE]]는 [[SRS]] 리소스 세트 내의 리소스들을 기반으로 코드북 서브셋 제한을 적용받습니다.

## 소스
- 3GPP TS 38.214 V17.9.0 (Release 17) §6.1.1.1