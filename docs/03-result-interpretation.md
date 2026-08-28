# Result Interpretation Guide

## PASS
평가가 정상 실행되었고 기준 충족.

## FAIL
평가는 정상 실행되었지만 해당 evaluator 기준 미충족.

## ERROR
평가 자체가 정상 실행되지 못함.

대표 Error:
- 429 Rate Limit
- Judge 호출 실패
- 인증/배포 문제
- Dataset 매핑 문제

## 분석 순서
1. 치명적 위험이 있는가?
2. 어떤 evaluator가 실패시켰는가?
3. 실제 response는 무엇인가?
4. reason은 무엇인가?
5. Instruction 문제인가?
6. Dataset 문제인가?
7. Evaluator/Rubric 문제인가?
8. 다음 버전에서 어떤 한 가지 변수를 바꿀 것인가?
