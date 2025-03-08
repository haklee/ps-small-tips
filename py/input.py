"""이 파일에서는 다음의 내용을 다룬다.

1. 기본적인 형태의 입출력
2. 빠른 입출력
3. 공백, 줄바꿈으로 구분된 입력 받는 방법
"""

# 1. 기본적인 형태의 입출력

# 다음과 같은 방식으로 입력을 받을 수 있다.
# 줄바꿈으로 구분된 문자열이 변수에 저장된다.
a = input()

# 혹시 input 함수를 여러 번 사용해야 할 경우 다음과 같이 함수 이름을
# 변수에 넣어 코드 길이를 줄이는 것도 가능하다.
i = input  # 이제 i에 input함수 자체가 들어갔다.
a = i()  # input함수를 호출할때 i를 쓰자.
b = i()
c = i()

# 출력도 입력과 비슷한 방식으로 사용할 수 있다.
print("hello")

p = print
p("hello")
p("world")


# 2. 빠른 입출력
# [빠른 A+B](https://www.acmicpc.net/problem/15552) 문제를 통해서 테스트 가능하다.

# 1) sys의 stdin, stdout 활용
import sys  # 먼저 sys를 import한다.

# 한 줄을 읽어오자.
a = sys.stdin.readline()
# 위의 코드를 통해 a에 줄바꿈으로 구분된 문자열을 받아올 수 있다.
# 이때, a는 '\n' 문자로 끝나므로 이를 유의해야 한다.

# 읽은 줄을 출력하자.
sys.stdout.write(a)
# 이때, 위의 write함수를 사용해서 출력하면 기존의 print()를 사용할 때와 다르게
# 뒤에 '\n'문자가 없는 상태로 출력한다. 즉, 여러 줄을 출력하고 싶으면 아래와 같이
# 코드를 작성해야 한다.
for i in range(10):
    sys.stdout.write(str(i)+'\n')

# 그리고 무조건 string을 사용해야 한다.
# 아래와 같이 int값을 출력하려고 하면 에러가 발생한다.
for i in range(10):
    sys.stdout.write(i)  # TypeError: write() argument must be str, not int

# 2) open 활용
# open함수는 파이썬 내장 함수로, 파일을 열때 사용한다. 이를 값을 받을 때도 사용할 수
# 있는데, 설명은 아래의 링크를 참조하자.
# https://www.acmicpc.net/board/view/80013

# 예시 입력:
# 1
# 2 3
# 4 5 6

print(open(0).read())
# 출력:
# 1
# 2 3
# 4 5 6


# 3. 공백, 줄바꿈으로 구분된 입력 받는 방법

# split 함수를 써서 특정 문자열로 문자열을 자를 수 있다.

# 예시 입력:
# 1 2 3 4 5 6

# split 함수에 아무 인자도 안 넣으면 공백 문자를 기준으로 자른다.
print(input().split())
# 출력:
# ['1', '2', '3', '4', '5', '6']

# 예시 입력:
# baabbbaaabbabbaa

print(input().split('aa'))
# 출력:
# ['b', 'bbb', 'abbabb', '']
# 설명:
# 문자열 앞에부터 'aa'를 발견할때마다 자른다.
# baabbbaaabbabbaa
# b  bbb  abbabb  ^
# 마지막에 aa를 발견하고 문자열이 끝났는데, 이때 끝에 빈 문자열이 있는 걸로 친다.

# 많은 경우 숫자를 받아서 이를 정수로 변환하여 연산에 사용하고 싶을 것이다.
# 이때 map 함수를 사용하면 편하다.

# 예시 입력:
# 1 2 3 4 5 6

for i in map(int,input().split()):
    print(i)
# 출력:
# 1
# 2
# 3
# 4
# 5
# 6

print([*map(int,input().split())])
# 출력:
# [1, 2, 3, 4, 5, 6]


# 앞서 open함수를 통해 전체 인풋을 통째로 받아왔었다.
# 이를 숏코딩에 매우 유용하게 사용할 수 있는데, 예를 들어 아래와 같이 사용 가능하다.

# 예시 입력:
# 1
# 2 3
# 4 5 6

print(open(0).read().split())
# 출력:
# ['1', '2', '3', '4', '5', '6']

print([*open(0)])
# 출력:
# ['1\n', '2 3\n', '4 5 6\n']

print([sum(map(int,i.split())) for i in [*open(0)]])
# 출력:
# [1, 5, 15]


# 첫 줄이 아래 나올 인풋의 개수를 뜻하는 경우가 많은데, 이때 open함수를 다음과 같이
# 많이 활용한다.

# [A+B - 3](https://www.acmicpc.net/problem/10950)

# 첫 줄을 받아서 loop 횟수로 사용.
for _ in range(int(input())):
    a, b = map(int, input().split())
    print(a + b)

# slicing으로 첫 줄을 빼고 남은 줄들을 처리.
for i in[*open(0)][1:]:
    a, b = map(int, i.split())
    print(a + b)


# open함수 사용시 '\n'문자가 끝에 붙어있는 것을 출력에 활용할 수도 있다.

# [나이순 정렬](https://www.acmicpc.net/problem/10814)
print(*sorted([*open(0)][1:],key=lambda i:int(i.split()[0])),sep='')
# 어차피 모든 문자열 끝에 '\n'문자가 붙어있으니,
# string을 빈 문자열 seperator로 구분해서 출력.
