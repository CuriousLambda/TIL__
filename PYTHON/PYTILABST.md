# **추상 클래스(abstract class)**
- 추상화 작업이 존재하는 클래스
  - 추상화작업 : 선조를 추상으로 만들고 후손이 재 정의(메소드 오버라이딩)된 메소드로 구현하거나 객체 호출을 할 수 있도록 구현된 것.
- 즉, 클래스 내부에 구현되지 않은 메소드를 한가지 이상 가지고 있는 클래스를 추상 클래스라고 한다.

### 특징
- 추상 클래스는 객체생성 불가능
- __상속받은 후손 클래스가 반드시 추상 메소드를 재 정의해야 한다.__
- 만일 후손이 추상 메소드를 재정의하지 않으면 후손이 추상 클래스가 되어야 한다.

<br/>

> 추상 클래스는 기획자가 꼭 구현이 필요한 메소드를 정의하고 이를 상속하게 하는 것이다.<br/>
> 선조 클래스(추상클래스)에서 꼭 만들었으면하는 메소드를 강제하기 위함이다.<br/>
> 즉, 추상화는 메소드 재 정의를 강하게 묶어놓는다고 생각할 수 있다.<br/>
> 그렇기 때문에 개발자들이 메소드를 놓치거나 오류를 발생시키는 것을 방지할 수 있다.

<br/>

  - 추상 클래스를 생성하기 위해서는 abc모듈을 import해주어야 한다.
  - 추상 클래스는 클래스의 괄호 안에 metaclass=ABCMeta로 지정한다.
  - 추상 메서드는 함수 위에 @abstractmethod라는 키워드를 적어주어 다른 메서드들과 구별한다. 

> abc는 abstract base class의 약자

<br/>

예시01
```python
# 오류발생을 통해 보는 추상 클래스 문법

from abc import abstractmethod, ABCMeta         # 추상 클래스 생성을 위해 abc모듈 import
                                                # abstractmethod : @와 함께 메소드 위에 선언하게 되면 추상 메소드로 사용
                                                # ABCMeta : 클래스 선조로 지정하게 되면 후손은 추상 클래스가 된다.


class Base(metaclass=ABCMeta):      # 추상 클래스 선언
    @abstractmethod                 # 추상 메소드 선언
    def prn(self):                  # 소문자 prn
        pass

class Cat(Base):
    def prn(self):                  # 소문자 prn
        print('Cat class')

class Puppy(Base):
    def Prn(self):                  # 대문자 Prn
        print('Puppy class')

# 부모 클래스인 Base의 메소드 prn이 자식 클래스인 Cat에는 재정의 되었지만,
# 또 다른 자식 클래스인 Puppy에는 재정의되지 않았다.


def My_Call(m):
    m.prn()

if __name__ == '__main__':

  My_Call(Cat())
  My_Call(Puppy())

# 선조의 prn을 재정의하지 않고, Prn으로 했을 경우 오류가 난다.
# <<__상속받은 후손 클래스가 반드시 추상 메소드를 재 정의해야 한다.__>>는 형식을 만족하지 않기 때문!
```
출력결과
```python
Cat class
Traceback (most recent call last):
  File "my_python_path", line 31, in <module>
    My_Call(Puppy())
TypeError: Can't instantiate abstract class Puppy with abstract method prn
```

> 위의 코드 내의 주석 상에 작성했듯이 <br/>
> 추상클래스인 선조의 __prn__ 메소드를 후손클래스 Puppy에서 재정의하지 않았기 때문에 오류가 발생한다.<br/>
> 따라서 후손클래스인 Puppy의 __Prn__ 메소드를 __prn__ 으로 바꾸어주면 정상 작동할 것이다.

<br/>

*__수정한 예시01__*
```python
... 생략

class Puppy(Base):
    def prn(self):   
        print('Puppy class')


def My_Call(m):
    m.prn()

if __name__ == '__main__':

  My_Call(Cat())
  My_Call(Puppy())
```
출력결과
```python
Cat class
Puppy class
```
<br/>

#### 비슷한 예시를 한 개 더 살펴보자.
<br/>

예시02
```python
from abc import abstractmethod, ABCMeta     #abstractmethod : @와 함께 메소드 위에 선언하게 되면 추상 메소드로 사용
                                            #ABCMeta : 클래스 선조로 지정하게 되면 후손은 추상 클래스가 된다.

class Base(metaclass=ABCMeta): # 추상 클래스 선언
    @abstractmethod            # 추상 메소드 선언
    def prn(self):             # prn을 추상 메소드로 선언했기 때문에 후손 클래스에서 prn을 재 정의하자
        print('Base class')

    def base_prn(self):
        print('base_prn')

class Cat(Base):
    def prn(self):
        Base.base_prn(self)
        Base.prn(self)
        print('Cat class')

class Puppy(Base):
    def Prn(self):
        print('Puppy class')

if __name__ == '__main__':
    b = Base() 
```
출력결과
```python
Traceback (most recent call last):
  File "my_python_path", line 23, in <module>
    b = Base()
TypeError: Can't instantiate abstract class Base with abstract method prn
```
> 오류가 나는 이유는<br/>
> 위에서 언급했듯이 추상 클래스는 객체 생성이 불가능하다.<br/>
> 하지만 `b = Base()`에서 `b`라는 객체를 생성했으므로 오류가 나게 된다.

<br/>

*__수정한예시02__*
```python
from abc import abstractmethod, ABCMeta     # abstractmethod : @와 함께 메소드 위에 선언하게 되면 추상 메소드로 사용
                                            # ABCMeta : 클래스 선조로 지정하게 되면 후손은 추상 클래스가 된다.

class Base(metaclass=ABCMeta): # 추상 클래스 선언
    @abstractmethod            # 추상 메소드 선언
    def prn(self):             # prn을 추상 메소드로 선언했기 때문에 후손 클래스에서 prn을 재 정의하자
        print('Base class')

    def base_prn(self):
        print('base_prn')

class Cat(Base):
    def prn(self):
        Base.base_prn(self)
        Base.prn(self)
        print('Cat class')

class Puppy(Base):
    def Prn(self):
        print('Puppy class')

if __name__ == '__main__':
    c = Cat()     # 선조 메소드를 출력해보자
    c.base_prn()
    c.prn()       # 후손의 주소로 찾아오면 됨
```
출력결과
```python
base_prn
base_prn
Base class
Cat class
```

