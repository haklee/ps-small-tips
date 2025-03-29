# 런타임 전의 전처리

제목 그대로, 이 기법의 핵심은 코드가 돌기 전에 미리 계산된 값을 준비해두는 것이다. solved에는 [런타임 전의 전처리(precomputation)](https://solved.ac/problems/tags/precomputation)라는 이름의 태그로 소개되어 있다. 실제 문제를 통해 이 기법을 활용하는 방법을 설명하는 것이 더 이해가 쉬울 것이다.

## [N-Queen](https://www.acmicpc.net/problem/9663)

n-queen 문제는 n * n 크기의 체스판이 주어졌을때 퀸 n개를 서로 공격할 수 없도록 놓는 문제다. 이 문제를 코드를 통해 풀고자 하면 보통 백트래킹 기법을 활용하는데, n-queen의 경우의 수를 묻는 문제에 한정하여 [n-queen 수열을 설명하는 사이트](https://oeis.org/A000170)의 도움을 받을 수 있다. 위 문제를 파이썬으로 푼다면 아래와 같이 풀 수 있다.

``` python
print([1,1,0,0,2,10,4,40,92,352,724,2680,14200,73712,365596][int(input())])
```

앞서 언급한 [The On-Line Encyclopedia of Integer Sequences](https://oeis.org/)사이트는 이런 n-queen 수열 외에도 각종 유명한 정수 수열들이 많이 소개되어있으니 작은 n수에 대한 어떤 수열의 n번째 값을 묻는 문제를 풀때 유용하게 활용하도록 하자.
