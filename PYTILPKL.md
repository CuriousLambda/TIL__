# __피클(Pickle)__
- Python 내장 모듈
- 프로그램에서 코드 작성 시 객체를 파일로 저장할 때 사용하는 모듈
- 텍스트 상태의 데이터가 아닌 객체 자체를 바이너리(Binary) 파일로 저장한다.

### 장점
- 데이터를 전송에 걸리는 시간이 짧다.
- 피클은 바이너리(Binary) 파일로 저장한다. 바이너리 파일은 데이터 전송 시간이 상대적으로 적게 걸린다.
- 데이터가 방대해지고 양이 많아진다면 Pickle을 사용함으로써 시간을 절약할 수 있다.

<br/>

## 피클링을 작업하는 순서
1. import pickle
2. dump(출력할 객체, 파일객체)
    -  클래스 단위로 저장(출력)
3. load(파일객체)
    - 클래스 읽어옴

<br/>

## 예시
```python
import pickle, MyScore, zipfile

if __name__ == '__main__':
    f = open('pickle_01.txt', 'wb')
    s = [MyScore.Score('홍길동', 89, 75, 100),
         MyScore.Score('홍길동', 56, 100, 67),
         MyScore.Score('홍길동', 100, 78, 95)]
    pickle.dump(s,f)

    f = open('pickle_01.txt', 'rb')
    res = pickle.load(f)
    for r in range(len(res)) :
        print(res[r])

    #pickle_01.txt 파일을 zip파일로 인서트하자.
    with zipfile.ZipFile('B:/pythonPickle/com/test01/my_shutil.zip','a') as zf:
        zf.write('B:/pythonPickle/com/test01/pickle_01.txt')

    # zip파일 안에 a.txt 파일에 내용을 써보자.
    with zipfile.ZipFile('B:/pythonPickle/com/test01/my_shutil.zip','a') as zf:
        with zf.open('/a.txt','w') as f:
            f.write(b'abcdeg');

    with zipfile.ZipFile('B:/pythonPickle/com/test01/my_shutil.zip', 'a') as zf:
        print(zf.namelist())
```
출력결과
```python
홍길동	 89	 75	100	 26488.0	 학점 : B
홍길동	 56	 100	67	 22374.33333333333333	 학점 : C
홍길동	 100	 78	95	 27391.0	 학점 : A
['pythonPickle/com/test01/pickle_01.txt', '/a.txt']
```
- 먼저 실행 전과 실행 후의 차이를 그림으로 살펴보자<br/>

|실행전|실행후|
|:-----:|:------:|
|![실행전](https://user-images.githubusercontent.com/93986157/193457561-495e3e54-3928-4d2d-8a5f-5c45c8b4f527.png)|![실행후](https://user-images.githubusercontent.com/93986157/193457585-8428d186-dc67-4df8-8264-b10cd4287d80.png)|
||my_shutil.zip파일과 <br/>pickle_01.txt 파일 생성됨|

<br/>

- `pickle.dump(s,f)`로 list 객체를 파일에 저장했다.
- `for`문과 `print`를 활용하여 list객체를 순서대로 출력해보았다.
- 이전의 File Handling에서 다루었듯이, `with ~ as`문을 활용하여 자동 파일 닫기를 구현하며 _pickle.txt_ 파일을 zip파일로 인서트했다.
- zip파일 안에 _a.txt_ 파일을 만들고 내용을 작성했다.
- 이후 GUI의 폴더 안을 살펴보자.

|GUI상 txt파일 살펴보기|
|:-----:|
|![텍스트파일](https://user-images.githubusercontent.com/93986157/193458201-d8d3afd7-800f-4b6d-b99e-3972e17d531d.png)|

- 또한 __pickle__ 자체가 바이너리 상태로 데이터를 다루기 때문에 파일 오픈 시 `f = open('pickle_01.txt', 'rb')`와 같이 __`rb`__ 모드로 설정해주어야 한다.
- 마지막으로 `print(zf.namelist())`를 통해 zip파일 안의 모든 파일 리스틀 확인했다.