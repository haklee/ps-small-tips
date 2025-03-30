# 자주 사용하는 공식

문제 풀이에 유용한 공식들을 모아놓았다.

## 피보나치 수

피보나치 수는 다음을 만족한다.

``` text
1보다 큰 자연수 i에 대해 i번째 피보나치 수를 f(i)라고 한다면,
- f(0) = 0
- f(1) = 1
- f(i) = f(i-1) + f(i-2)
```

### 카시니 항등식 (Cassini’s identity)

``` text
f(i+1) + f(i-1) = f(i)^2 + (-1)^i
```

### 도가뉴 항등식 (d’Ocagne’s identity)

``` text
f(i+j) = f(i-1)*f(j) + f(i)*f(j+1)
```

i = n, j = n을 대입하면

``` text
f(2*n) = f(n-1)*f(n) + f(n)*f(n+1)
       = f(n) * (f(n+1) + f(n-1))
       = (f(n+1) - f(n-1)) * (f(n+1) + f(n-1))
       = f(n+1)^2 - f(n-1)^2
```

i = n, j = n-1을 대입하면

``` text
f(2*n-1) = f(n-1)*f(n-1) + f(n)*f(n)
         = f(n)^2 + f(n-1)^2
```

도가뉴 항등식을 활용하면 큰 n에 대해서 f(n)값을 log(n)의 SC와 log(n)의 TC로 구할 수 있다. 이는 [피보나치 수 6](https://www.acmicpc.net/problem/11444) 및 이와 유사한 문제를 풀때 유용하게 활용할 수 있다.
