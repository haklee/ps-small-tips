/*이 파일에서는 다음의 내용을 다룬다.

1. 기본적인 형태의 입출력
2. 공백, 줄바꿈으로 구분된 입력 받는 방법
*/

// 1. 기본적인 형태의 입출력

// 아래의 입출력 방식은 빠른 입출력에 바로 사용할 수 있다.

// 다음과 같은 방식으로 입력을 받을 수 있다.
// 입력으로 들어온 문자열 전체를('\n'문자를 포함해서) 받아온다.
a = require('fs').readFileSync(0).toString()

// 다음과 같은 방식으로 출력이 가능하다.
console.log(a)


// 3. 공백, 줄바꿈으로 구분된 입력 받는 방법

// split 함수를 써서 특정 문자열로 문자열을 자를 수 있다.

// 예시 입력:
// 1 2 3 4 5 6

// split 함수에 아무 인자도 안 넣으면 공백 문자를 기준으로 자른다.
a = require('fs').readFileSync(0).toString()
console.log(a.split(' '))
// tagged template literal 문법을 활용하면 이를 좀 더 줄일 수도 있다.
console.log(a.split` `)

// 출력:
// ['1', '2', '3', '4', '5', '6']

// 예시 입력:
// baabbbaaabbabbaa

a = require('fs').readFileSync(0).toString()
console.log(a.split(' '))

// 출력:
// ['b', 'bbb', 'abbabb', '']
// 설명:
// 문자열 앞에부터 'aa'를 발견할때마다 자른다.
// baabbbaaabbabbaa
// b  bbb  abbabb  ^
// 마지막에 aa를 발견하고 문자열이 끝났는데, 이때 끝에 빈 문자열이 있는 걸로 친다.


// 많은 경우 숫자를 받아서 이를 정수로 변환하여 연산에 사용하고 싶을 것이다.
// 그런데 js에서의 아주 신기한 방식으로 형 변환을 할 수 있다.
// 구체적인 내용은 문서에서 다루고, 여기에서는 간단한 사용법만 언급하도록 하겠다.

// 예시 입력:
// 1 2 3 4 5 6

a = require('fs').readFileSync(0).toString()
// map 함수로 object 안에 있는 값을 변형한다.
// string 앞에 +기호를 붙이면 string을 number타입으로 형변환한다.
console.log(a.split` `.map(i=>+i))
// 출력:
// [ 1, 2, 3, 4, 5, 6 ]

for(n of a.split` `.map(i=>+i))console.log(n)
// 혹은, 아래와 같이 object 안에 있는 값을 순회하면서 받아온 값을 변환해서 출력해도 된다.
for(n of a.split` `)console.log(+n)

// 출력:
// 1
// 2
// 3
// 4
// 5
// 6


// 한 번에 인풋을 받아왔으니 아래와 같이 사용 가능하다.

// 예시 입력:
// 1
// 2 3
// 4 5 6

a = require('fs').readFileSync(0).toString()

// regex. 자세한 사용법은 다른 문서에서 다루도록 하겠다.
console.log(a.split(/\s+|\n/))
// 출력:
// ['1', '2', '3', '4', '5', '6']

// 다음과 같이 new line으로 split을 할 수도 있다.
console.log(a.split`
`)
// 출력:
// [ '1\r', '2 3\r', '4 5 6' ]

// reduce함수를 사용하여 다음과 같이 sum을 구현할 수 있다.
console.log(a.split`
`.map(i=>i.split` `.reduce((a,b)=>a+ +b,0)))
// 출력:
// [1, 5, 15]
