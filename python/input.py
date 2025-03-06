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

# TODO: 내용 작성


# 3. 공백, 줄바꿈으로 구분된 입력 받는 방법

# TODO: 내용 작성
