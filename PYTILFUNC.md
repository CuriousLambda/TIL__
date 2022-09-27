# **함수**
<br/>

## _**함수(Function)**_
<br/>

형식
```python
def username(변수, *가변변수, **가변변수):
        명령
        return
```
> __*가변변수 = 가변인자__, 변수(인자)를 대입하면 튜플(tuple)형식으로 반환. <br/>
> __**가변변수  = 키워드 가변인자__, 변수(인자)를 대입하면 dictionary형식으로 반환. -- `keyword = value`형태로 함수 호출

<br/>

- 함수를 호출할 때 가변변수가 있을 경우, _**변수, 가변변수, 키워드 가변변수**_ 순으로 넣어줘야 정상작동한다.
- 함수 선언 시 일반변수는 초기값을 가질 수 있다.

<br/>

예시01
```python
# 매개인자 없는 리턴형 함수를 만들어 보자.

def getA():
    return 100

def getB():
    return (1,2,3,4)

def getC():
    return [1,2,3,4]

def getD():
    return "abcd"

def getE():
    return 'A'

def getF():
    return {'a' : ('a', 'b', 'c', 'd', 'e')}


if __name__ == '__main__':
    print(getA())     #100
    print(getB())       #(1,2,3,4)를 리턴 출력
    print(getC())       #[1,2,3,4]
    print(getD())       # "abcd"
    print(getE())       # 'A'
    print(getF())       # {'a' : ('a','b','c','d','e')}
```
출력결과
```python
100
(1, 2, 3, 4)
[1, 2, 3, 4]
abcd
A
{'a': ('a', 'b', 'c', 'd', 'e')}
```
<br/>

예시02
```python
# 매개인자 있는 리턴형 함수를 만들어 보자.

def getA(su):
    print(type(su), end = '\n-------------')
    return su


if __name__ == '__main__':
    print(getA(100))             #100
    print(getA((1,2,3,4)))       #(1,2,3,4)
    print(getA([1,2,3,4]))       #[1,2,3,4]
    print(getA("abcd"))          # "abcd"
    print(getA('A'))             # 'A'
    print(getA({'a' : ('a','b','c','d','e')}))       # {'a' : ('a','b','c','d','e')}
```
출력결과
```python
<class 'int'>
-------------100
<class 'tuple'>
-------------(1, 2, 3, 4)
<class 'list'>
-------------[1, 2, 3, 4]
<class 'str'>
-------------abcd
<class 'str'>
-------------A
<class 'dict'>
-------------{'a': ('a', 'b', 'c', 'd', 'e')}
```
<br/>

에시03
```python
# 리턴 타입과 매개인자 타입을 가변으로 설정을 해보자.
# 함수() 안에 가변인자를 지정할 수 있다.

def getTest01(*a):
    print(a, type(a))

def getTest02(**a):
    print(a)

# 만일에 가변 인자를 섞어서 쓰고 싶다. *, ** 순서 바뀌면 안됨
def getTest03(res, *a, **b):
    print(res, a,b)

if __name__ == '__main__':
    getTest01(1,2,3,4,5)
    getTest01(1,2,3)
    getTest02(a=1, b=2, c=3)
    getTest03(1,2,3,4,5, a=1, b=2)
```
출력결과
```python
(1, 2, 3, 4, 5) <class 'tuple'>
(1, 2, 3) <class 'tuple'>
{'a': 1, 'b': 2, 'c': 3}
1 (2, 3, 4, 5) {'a': 1, 'b': 2}
```
<br/><br/>


## Practice
<br/>

Pr01
```python
    # 이름 주소 전화번호를 input()으로 세 사람 입력 받아 출력해 보자.
    # while문 input()문 사용
    # 만일 지정된 세 사람의 이름이 아닌 다른 이름이 입력되면 다시 입력할 수 있도록 기회를 줘보자.

def person1(k):
    print(k, '의 주소 : 서울시 강남구', end='\n')
    print(k, '의 전화번호 : 111-1111', end='\n')

def person2(g):
    print(g, '의 주소 : 서울시 종로구', end='\n')
    print(g, '의 전화번호 : 222-2222', end='\n')

def person3(f):
    print(f, '의 주소 : 서울시 송파구', end='\n')
    print(f, '의 전화번호 : 333-3333', end='\n')


a = input('이름 : ')

while a == '길동' or a == '동백' or a == '영우':
    if a == '길동':
        person1(a)
        break
    elif a == '동백':
        person2(a)
        break
    else:
        person3(a)
        break
else:
    print('길동, 동백, 영우 중에 한 사람을 입력해주세요')
    a = input('이름 : ')
    while a == '길동' or a == '동백' or a == '영우':
        if a == '길동':
             person1(a)
             break
        elif a == '동백':
            person2(a)
            break
        elif a == '영우':
            person3(a)
            break
```
출력결과
```python
이름 : 마이클
길동, 동백, 영우 중에 한 사람을 입력해주세요
이름 : 동백
동백 의 주소 : 서울시 종로구
동백 의 전화번호 : 222-2222
```
<br/>

Pr02
```python
'''
이름, 국어, 영어, 수학을 main에서 입력 받아서
getTot(국어, 영어, 수학)로 총점을 리턴받고
getAvg(tot)를 통해 평균을,
getGrad(tot)를 통해 학점을 리턴받는 함수를 만들어보자.

==============================================================

출력예시
이름 : 홍길동
국어 : 84
영어 : 100
수학 : 90
총점 :
평균 :
학점 :

'''


def getTot(국어,영어,수학):
    return 국어+영어+수학
    #print('총점 :', 국어+영어+수학)

def getAvg(tot):
    return tot/3
    #print('평균 :', tot/3)

def getGrade(tot):
    if tot >= 270:
        return '학점 : A'
    elif tot >= 240 and tot < 270:
        return '학점 : B'
    elif tot >= 210 and tot < 240:
        return '학점 : C'
    else:
        return '학점 : D'

if __name__ == '__main__':
    a= input('이름 : ')
    국어 = int(input('국어 : '))
    영어 = int(input('영어 : '))
    수학 = int(input('수학 : '))
    tot = getTot(국어, 영어, 수학)
    print('평균 :', getAvg(tot))
    print(getGrade(tot))
```
출력결과
```python
이름 : 전과목에서 한개틀리는 사람
국어 : 100
영어 : 100
수학 : 90
평균 : 96.66666666666667
학점 : A
```
> 함수를 호출할 때 우리는 `if __name__ == '__main__':` 안에서 입력하게 된다. 이것의 의미는 따로 다루어보도록 하자.