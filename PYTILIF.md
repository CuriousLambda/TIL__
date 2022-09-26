# **if, match문**

## _**if문**_
> 조건문 (만일에 ~하면) <br/>
> if, if~else, 다중 if~else<br/>

<br/>

### **1. 단일 if 문**
- 단일 if문은 조건문이 True일 경우만 명령문이 실행되고 False일 경우는 실행되지 않는다.

```python
# my_var이 'a1234'이면 '비번이 맞아'라고 출력하자.

my_var = 'a1234'

if my_var == 'a1234':
    print('비번이 맞아')
```
출력결과<br/>
```python
비번이 맞아
```
<br/>

### **2. if~else문**
- if~else문은 조건문이 True일 경우만 True 명령문이 실행되고 나머지 경우는 else 구문을 실행한다. 

형식
```python
 if 조건문 :
    True 명령문
else:
    False 명령문
```

예시
```python
# my_var을 입력을 받아서 'a1234'이면 비번이 맞아 라고 출력하고
#아니면 '아니잖아!!!'라고 출력하자.

my_var = input('input id :')

if my_var == 'a1234': #Ture
    print('비번이 맞아') #True 명령 실행
else:
    print('아니잖아!!!') #False 명령 실행
```

출력결과
```python
input id : aaaa
아니잖아!!!
```
```python
input id : a1234
비번이 맞아
```
<br/>

### **3. 다중 if~else문**
- 다중 if~else문은 if~else문을 여러개 구현해서 선택적으로 조건문이 True일 경우만 True 명령문이 실행되고 나머지 경우는 else 구문을 실행한다.
- 순차적으로 조건식을 평가해서 수행하고 모든 조건식이 Fasle일 경우에는 else의 명령문을 실행하게 된다. else구문은 생략해도 된다.

형식
```python
if 조건문01:
    True 명령문01
elif 조건문02:
    True 명령문02   #elif의 갯수는 상관 없음
else:
    False 명령문
```

예시
```python
# 숫자를 받아서 숫자가 양수인지 음수인지 0인지 판별해보자.

su = int(input('input su:'))

if su > 0:
    print('양수')
elif su < 0:
    print('음수')
else:
    print('0')
```

출력결과
```python
input su:1
양수
```
```python
input su:0
0
```
```python
input su:-1
음수
```
<br/>

## _**match문**_
> 선택문 <br/>
> 조건이 여러개인 경우를 단일화 시키기 위해 사용

<br/>

### **match~case구문**

형식
```python
match 객체변수
    case value1 :명령문
    case value2 :명령문
    case _: 명령문
```
<br/>

예시01
```python
# su라는 변수값이 1,2,3일때 선택적으로 출력하는 구문을 만들어 보자.

su = 5

match su:
    case 1: print('1이야')
    case 2: print('2야')
    case 3: print('3이야')
    case _: print('이도저도 아니야')
```
출력결과
```python
이도저도 아니야
```
<br/>

예시02
```python
# my_list라는 변수값이 시퀀스 값일 때 선택적으로 출력하는 구문을 만들어 보자.

my_list = 1,[3,(1,2,3)]

match my_list:
    case [1,2,3] : print('맞을까?')
    case (1,2,3,4): print('어떤 것 같아?')
    case 3: print('3이야')
    case 1,[x,others]: print(f'1이랑 또다른 값이랑 {x} {others}')
#others는 아무 변수y,z,t,o등등 아무 변수나 주면 됨
```
출력결과
```python
1이랑 또다른 값이랑 3 (1, 2, 3)
```

<br/>

## Practice

```python
'''
if문을 사용하여 아래와 같은 조건을 만족하도록 프로그램을 작성해보자.
조건 1 : 문자열을 my_str이라는 변수로 입력 받는다.
조건 2 : 첫 글자가 소문자 이면 전체를 대문자로 바꾼다.
조건 3 : 첫 글자가 대문자이면 전체를 소문자로 바꾼다.
Hint : my_str[0]를 사용하고 str객체의 메소드를 사용한다.

'''

my_str = input('문자를 입력하세요 :')

if my_str[0].islower():
    print(my_str.upper())
elif my_str[0].isupper():
    print(my_str.lower())
else:
    pass
```
출력결과
```python
문자를 입력하세요 :RiGhT
right
```
```python
문자를 입력하세요 :riGhT
RIGHT
```

<br/>

### 주석
> `pass`는 문법상 코드가 필요하지만 아무 작업도 하고 싶지 않을 때 사용<br/>
> <br/>위의 예시 중 match문 예제02에서,<br/>
> `print(f'1이랑 또다른 값이랑 {x} {others}')`에서 `f'`는 f-string이라고 한다.<br/>
> f-string을 사용하면 문자열 안에 python의 표현식을 삽입할 수 있다.
> <br/>(문자열 안에 변수 값을 삽입하는 용도로 사용된다.)