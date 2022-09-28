# **클래스(Class)**

## 객체와 클래스
- 객체
  - 서로 연관된 데이터와 그 데이터를 조작하기 위한 함수를 하나의 집합에 모아놓은 것
  - 이 때 집합의 원소가 되는 변수를 멤버(member) 또는 속성(attribute)이라고 한다.
  - 특히 함수는 메소드(method)라고 부르며 매개변수 self를 필수적으로 가진다.
  
- 클래스
  - 객체에서 사용될 속성과 메소드를 정의한 틀

<br/>

> 객체를 사용하여 데이터를 표현하는 프로그래밍 기법을 객체 지향 프로그래밍(Object-Oriented Programming, OOP)이라고 한다.<br/>
> 컴퓨터 프로그램을 여러개의 독립된 단위, 객체들의 모임으로 파악하는 것이다.<br/>
> 객체 지향 프로그래밍은 프로그램을 유연하고 변경이 쉽게 만들어 대규모 소프트웨어 개발에 많이 사용된다.<br/>
> 또한 소프트웨어 개발과 보수를 간편하게 하는 편리함이 있다.<br/>
> Python도 객체 지향 언어 중 하나이다.

<br/>

### 형식
```python
class User_Name:
      1) 변수 선언                  
      2) 생성자, 소멸자.
      3) def userName(self):        
      4) 기타 재정의 메소드
```
<br/>

## 생성자와 소멸자
- 생성자
  - `def __init__(self):`
  - 생성자는 `__init__` 메소드를 만들면 된다. 같은 클래스 내에서 오직 한번만 입력해야한다.
  - 초기화 메소드로, 객체가 생성된 후 가장 먼저 호출되며 자동으로 호출되는 메소드이다.
- 소멸자
  - `def  __del__(self):`
  - 소멸자는 `__del__` 메소드를 만들면 된다.
  - 객체가 소멸될 때 자동으로 호출되는 메소드.
  - self인자가 아닌 다른 매개변수를 받지 않는다.

<br/>

## Python `self`?
- 파이썬에서 메소드를 정의할 때 첫 번째 매개인자를 반드시 명시하게 되는데, 이것을 self인수라고 부른다.
- self인수의 의미는 객체자신의 참조이다.
- 모든 메소드는 최소한 self 인수는 가져야 한다. (@를 이용한 클래스 메소드 , 정적 메소드 등은 예외)
- 객체를 통해서 불려지는 메소드의 첫 번째 인수는 자동적으로 객체의 참조로 채워진다. 따라서 self 인수를 넘겨줄 필요는 없다.
- self를 통해서 클래스 내의 멤버나 메소드를 자유롭게 호출할 수 있다.

<br/>

예시01
```python

class Calc:
    def __init__(self,x, y):
        self.x = x      #Calc가 가진 멤버변수 x,y
        self.y = y      #객체를 통해 값이 전달되어 사용하려면 멤버변수로 대입해서 호출
        

    def getX(self):      # 멤버변수 self.x값을 리턴하는 메소드
        return self.x;

    def getY(self):      # 멤버변수 self.y값을 리턴하는 메소드
        return self.y;

    def setX(self, x):   # self.x 값 전달 및 변경
        self.x =x;

    def setY(self, y):   # self.y 값 전달 및 변경
        self.y =y;

    def getHap(self):
        return self.x + self.y

    def getSub(self):
        return self.x - self.y

    def getMul(self):
        return self.x * self.y

    def getDiv(self):
        return self.x / self.y
    
    #출력 메소드
    def my_prn(self):
        print("%5d %5d %5d %5d %5d %5d"%(
            self.getX(), self.getY(), self.getHap(),
            self.getSub(), self.getMul(), self.getDiv()
            )
              )
```
<br/>

함수호출
```python
from Calc import *


if __name__ == '__main__':
    c1 = Calc(100, 50) # c1객체 생성, Calc 클래스의 __init__
    c2 = Calc(80, 70)  # c2객체 생성, Calc 클래스의 __init__
    c1.my_prn()
    c2.my_prn()

    print('c1의 x 값을 2500 으로 변경 후 c1 전체 출력')
    c1.setX(2500)
    c1.my_prn()

    print('c2의 y 값을 10 으로 변경 후 c2 전체 출력')
    c1.setY(10)
    c2.my_prn()

    print('c1의 x 값과 c2의 y값의 합을 출력')
    print(c1.x + c2.y)
    tot = c1.getX() + c2.getY()
    print(f'{tot}')
```
출력결과
```python
  100    50   150    50  5000     2
   80    70   150    10  5600     1
c1의 x 값을 2500 으로 변경 후 c1 전체 출력
 2500    50  2550  2450 125000    50
 2500    50  2550  2450 125000    50
c2의 y 값을 10 으로 변경 후 c2 전체 출력
   80    10    90    70   800     8
   80    10    90    70   800     8
c1의 x 값과 c2의 y값의 합을 출력
2510
2510
```
출력결과를 풀어보자면,<br/><br/>
먼저 c1의 경우<br/>
100  = getX(), 50 = getY(), 150 = getHap(),<br/>
50 = getSub(), 5000 = getMul(), 2 = getDiv()의 결과로 나온 것이고,<br/><br/>
c2의 경우
80  = getX(), 70 = getY(), 150 = getHap(),<br/>
10 = getSub(), 5600 = getMul(), 1 = getDiv()의 결과로 나온 것이다.

<br/><br/>

## **Public** member / **Private** member
- public 멤버
  - 기본적으로 모든 클래스 멤버들은 public이며, 함수들은 동적 바인딩(C++에서의 virtual 함수)이다.
    > 동적바인딩 : 실행 시에만 메모리에 로드되어 코드 간결화, 실행 속도 단축, 비용 절감이 가능하다.<br/>
    > 정적바인딩 : 메모리에 로드해 놓고 호출되는 기법
- private 멤버
    - 기본적으로 파이썬은 private 함수나 변수를 키워드를 통해 명시적으로 지원하지 않지만
    - 관습적으로 (conventionally) 더블 언더스코어(__)로 시작하는 이름은 non-public으로 취급된다.
    - __로 시작하는 모든 이름들은 `__클래스명__.이름`의 형식으로 변환된다.

<br/>

형식
```python
class Test{
    public int a;       # (공개)
    protected int b;    # (상속시 후손 공개)
    private int c;      # (비공개)
        int d;          # (현재 패키지에서만 공개)
        }
```
<br/>

## Practice
```python
# MyScore는 세 과목을 관리하는 클래스, [총점, 평균, 학점]을 리턴한다.
# Score라는 클래스를 만들고 주어진 결과가 나오도록 호출해보자.

# 파일명은 <MyScroe.py>

class Score:

    #생성자에서 초기값 처리
    def __init__(self, name, 국어, 영어, 수학):
        self.__name = name
        self.__국어 = 국어
        self.__영어 = 영어
        self.__수학 = 수학

    def getTot(self):
        return self.__국어 + self.__영어 + self.__수학

    def getAvg(self):
        return self.getTot() / 3

    def getGrade(self):
        if self.getTot() >= 270:
            return '학점 : A'
        elif self.getTot() >= 240 and self.getTot() < 270:
            return '학점 : B'
        elif self.getTot() >= 210 and self.getTot() < 240:
            return '학점 : C'
        else:
            return '학점 : D'
    def my_prn(self):
        print(f'{self.__name}\t'
              f'{self.__국어}\t'
              f'{self.__영어}\t'
              f'{self.__수학}\t'
              f'{self.getTot()}\t'
              f'{self.getAvg()}\t'
              f'{self.getGrade()}')

    #객체를 호출하게 되면 자동 호출되는 메소드
    #선조가 가진 메소드를 재 정의 한다.
    def __str__(self):
        return (f'{self.__name}\t {self.__국어}\t {self.__영어}\t'
              f'{self.__수학}\t {self.getTot()}'
              f'{self.getAvg()}\t {self.getGrade()}')


    ##### 국어 수학 영어 과목을 값 전달 및 변경
    def setKor(self, 국어):
        self.__국어 = 국어
    def setMat(self, 수학):
        self.__수학 = 수학
    def setEng(self, 영어):
        self.__영어 = 영어
    def setName(self, name):
        self.__name = name

    #####국어, 수학, 영어 값을 리턴하는 메소드
    def getKor(self):
        return self.__국어
    def getMat(self):
        return self.__수학
    def getEng(self):
        return self.__영어
    def getName(self):
        return self.__name
```
함수호출
```python
from MyScore import *

if __name__ == '__main__':
    s1 = Score('홍길동', 70, 80, 90)
    s2 = Score('김동백', 80, 100, 100)
    s3 = Score('우영우', 100, 100, 100)

    print(s1)
    print(s2)
    print(s3)


    print('1) 홍길동을 정길동으로 바꾼다.')
    s1.setName('정길동')
    print(s1)

    print('2) 정길동의 국어점수를 30점으로 바꾼다.')
    s1.setKor(30)
    print(s1)

    print('3) 정길동의 수학점수를 50점으로 바꾼다.')
    s1.setMat(50)
    print(s1)

    print('4) 정길동 레코드를 출력한다.')
    print(s1)

    print('5) 김동백을 이길동으로 변환')
    s2.setName('이길동')
    print(s2)

    print('6) 우영우를 최길동으로 바꾼다.')
    s3.setName('최길동')
    print(s3)

    print('7) 이길동의 모든 점수를 100으로 바꾼다.')
    s2.setEng(100)
    s2.setKor(100)
    s2.setMat(100)
    print(s2)

    print('8) 최길동의 모든 점수를 50으로 바꾼다.')
    s3.setEng(50)
    s3.setKor(50)
    s3.setMat(50)
    print(s3)

    print('9) 전체 레코드 출력한다.')
    print(s1)
    print(s2)
    print(s3)

    print('10) 모든 레코드의 수학점수와 국어점수의 총 합계를 낸다.')
    x = s1.getMat() + s2.getMat() + s3.getMat()
    y = s1.getKor() + s2.getKor() + s3.getKor()
    print(x)
    print(y)
```
출력결과
```python
홍길동	 70	 80	90	 240    80.0	 학점 : B
김동백	 80	 100	100	 280    93.33333333333333	 학점 : A
우영우	 100	 100	100	 300    100.0	 학점 : A
1) 홍길동을 정길동으로 바꾼다.
정길동	 70	 80	90	 240    80.0	 학점 : B
2) 정길동의 국어점수를 30점으로 바꾼다.
정길동	 30	 80	90	 200    66.66666666666667	 학점 : D
3) 정길동의 수학점수를 50점으로 바꾼다.
정길동	 30	 80	50	 160    53.333333333333336	 학점 : D
4) 정길동 레코드를 출력한다.
정길동	 30	 80	50	 160    53.333333333333336	 학점 : D
5) 김동백을 이길동으로 변환
이길동	 80	 100	100	 280    93.33333333333333	 학점 : A
6) 우영우를 최길동으로 바꾼다.
최길동	 100	 100	100	 300    100.0	 학점 : A
7) 이길동의 모든 점수를 100으로 바꾼다.
이길동	 100	 100	100	 300    100.0	 학점 : A
8) 최길동의 모든 점수를 50으로 바꾼다.
최길동	 50	 50	50	 150    50.0	 학점 : D
9) 전체 레코드 출력한다.
정길동	 30	 80	50	 160    53.333333333333336	 학점 : D
이길동	 100	 100	100	 300    100.0	 학점 : A
최길동	 50	 50	50	 150    50.0	 학점 : D
10) 모든 레코드의 수학점수와 국어점수의 총 합계를 낸다.
200
180
```

