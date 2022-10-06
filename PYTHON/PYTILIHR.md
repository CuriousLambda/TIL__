# **상속(inheritance)**
- 어떤 클래스의 기능을 그대로 물려받으면서 다른 기능을 더 추가할 수 있는 기능
- 상속을 해주는 클래스를 부모 클래스(parent class) 또는 선조 클래스라고 한다.
- 상속을 받는 클래스를 자식 클래스 (child class) 또는 후손 클래스라고 한다.
- 두 개의 클래스 사이에 재정의(re-define)된 메소드가 있다면 상속관계라고 할 수 있다.

<br/>

형식
```python
class AA:
    def getTot():
        ...
    def getPrn():
        ...

class BB(AA):
    def getTot():
        1)return AA.getTot() + 내용   # 선조 함수 호출 방법 1
        2)super().getTot() + 내용     # 선조 함수 호출 방법 2

class DD(BB):
    def getTot():
        ...
```
> 위의 형식은 다중 상속 형식을 나타내고 있는데, BB의 선조는 AA이고, DD의 선조는 BB이다.<br/>
> 이러한 경우, DD는 BB와 AA를 모두 부모(parent) 또는 super로 가진다고 한다.

<br/>

- 부모 클래스가 하나인 것은 단일 상속, 부모클래스가 두개 이상일 경우 다중 상속이라고 한다.
- Python은 다중 상속 구현이 가능하다.

<br/>

예시01
```python
# 번호는 실행 순서
# Person 클래스를 부모 클래스로, Student 클래스를 자식 클래스로 만들자.
# Person에서는 name, age를 사용하고 Student에서는 grade를 사용하여 이름, 나이, 성적을 출력해보자.

class Person:
    def __init__(self, name, age):          # 3)
        self.name = name
        self.age = age

    def PersonInfo(self):
        return self.name + " : (age : " + str(self.age) + ")"



class Student(Person):
    def __init__(self, name, age, grade):   # 1) 생성자 호출하면서 객체 생성
        Person.__init__(self, name, age)    # 2) 호출
        self.grade = grade                  # 4)

    def GetStudent(self):
        return self.PersonInfo() + ", grade : " + str(self.grade)



if __name__ == '__main__':
    y = Student("Ruri", 7, 3)               # 상속관계 테스트 
    print(y.PersonInfo())                   # Ruri, 7
    print(y.GetStudent())                   # Ruri, 7,3
```
출력결과
```python
Ruri : (age : 7)
Ruri : (age : 7), grade : 3
```
> Student 클래스는 후손 클래스로서, Person 클래스를 선조로 가진다.<br/>
> 따라서 Student는 Person의 메소드를 사용할 수 있다.<br/>
> `print(y.PersonInfo())`가 실행되는 것을 확인할 수 있다.

<br/>

## _**오버라이딩**_
- 메소드 재정의
- 상속받은 후손 클래스에서 상속해 준 선조 클래스에 이미 정의된 메소드 기능을 변경해서 새로 정의하는 것

   <br/>

    - 특징
      - 오버라이드 하고자 하는 메소드가 선조 클래스에 존재해야 한다.
      - 선조에서 선언한 메소드와 후손의 메소드 명이 반드시 같아야 한다.
      - 파이썬에서는 메소드의 리턴 형이 같지 않아도 된다.

<br/>

예시02
```python
class MyScore:

    def __init__(self,kor,eng):
        self.kor = kor
        self.eng = eng

    def getTot(self):
        return (self.kor + self.eng)



class MyScore_Sub(MyScore):                 #3과목의 총점을 구하자. - 선조 클래스에 2과목의 총점을 구하는 로직이 있다.

    def __init__(self, kor, eng, mat):
        self.mat = mat
        super().__init__(kor, eng)

    def getTot(self):
        return (str(super().getTot() + self.mat))



class MyScore_Sub02(MyScore):

    def __init__(self, kor, eng, mat, mus):
        self.mus = mus
        self.mat = mat
        super().__init__(kor, eng)

    def getTot(self):
        return (str(super().getTot() + self.mat + self.mus))


if __name__ == '__main__':

    m1 = MyScore_Sub(85,70,100)
    print(m1.getTot())

    m2 = MyScore_Sub02(100,90,60,85)
    print(m2.getTot())
```
출력결과
```python
255
335
```
> __MyScore__ 클래스는 __MyScore_Sub__ 클래스와 __MyScore_Sub02__ 클래스의 선조(부모) 클래스이다.<br/>
> __MyScore(선조)__ 에서 정의되어 있는 `getTot(self)` 메소드가 __MyScore_Sub(후손)__, __MyScore_Sub02__ 에서도 정의되어 있는 것을 확인 할 수 있다.<br/>
> `super.getTot()` 를 활용해 선조의 메소드 기능을 넘겨받는다. 


