# Demo Overview

## 질문
Harness Engineering을 통해 Agent 행동을 설계했다면, 그 행동이 실제 사용자 요청에서도 그대로 나타나는가?

## 비교 원칙
- 같은 Agent model
- 같은 dataset
- 같은 Judge model
- 같은 evaluators
- Instruction만 변경

## 데모 성공 기준
V2의 모든 점수가 V1보다 높아지는 것이 목적이 아닙니다.

핵심은:
1. evaluator마다 다른 질문을 한다.
2. 지침 준수와 요청 완료는 충돌할 수 있다.
3. 제약 강화는 과도한 거절을 만들 수 있다.
4. aggregate score만으로 품질을 판단하지 않는다.
5. row-level response와 reason을 본다.
6. 업무 기준이 부족하면 custom rubric으로 보완한다.
