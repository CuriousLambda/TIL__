# File Handling

## 1. 파일 열기
<br/>

형식
```python
f = open('파일명' 또는 '파일경로', mode = '파일 열기 모드')

f.close()
```
- 파일을 다루기 위해 가장 먼저 해야할 것은 파일 열기이다.
- 파일 모드는 크게 'b'(바이너리 모드), 't'(텍스트 모드)가 있고 세부적으로 'r', 'w', 'a', 'x' 모드가 있다.
- 파일을 열었다면 반드시 파일을 닫아 주어야 한다.
- 파일을 닫지 않는다면 데이터가 없어지거나, 추가적인 작업이 불가할 수 있다.

<br/>

## 1-1) 파일 열기 모드
|파일 열기 모드|기능|
|:------------:|:---:|
|__r__|__Read__, 파일을 읽기 전용으로 연다|
|__w__|__Write__, 파일을 새로 쓴다 (즉, 덮어쓴다)<br/>만약 파일이 존재하지 않으면 새로운 파일을 생성한다|
|__a__|__Append__, 파일에 내용을 추가한다|
|__x__|__Create__, 파일을 생성한다<br/>이미 파일이 존재한다면 에러를 반환한다|

<br/>

|파일 열기 모드|기능|
|:--------:|:----:|
|__b__|__Binary__, 이진파일 모드<br/>ex) 이미지 파일은 'b' 모드로 오픈해야한다|
|__t__|__Text__, 기본 디폴트 모드|

<br/>

## 2. 파일 쓰기
<br/>

형식
```python
f.write('문자열')
f.writelines['list_01', 'list_02', 'list_03',,,,]
f.writelines('tuple_01', 'tuple_02', 'tuple_03',,,,)
```
- `.write`를 통해 파일에 내용을 쓰는 것이 가능하다.
- `.writelines`를 통해 튜플이나 리스트 자료형을 사용하여 여러 줄을 쓸 수도 있다.

<br/>

## 3. 파일 읽기
<br/>

형식
```python
f.read()
f.writelines()
```
- `read()`를 통해 파일 읽기가 가능하다.
- 더이상 읽을 자료가 없을 경우 마지막에 빈 문자열을 반환한다.
- `read()`, `readlines()`의 괄호`()`안에 숫자를 적어주면 그 바이트 수만큼 파일을 읽어온다.

<br/>

## 4. `with open() as`
- 파일을 오픈한 뒤에 반드시 `f.close()`를 통해 파일을 닫아주어야 한다.
- `with open() as`를 사용하면 열린 파일 객체가 자동으로 닫아진다.

<br/>

형식
```python
with open('파일명' 또는 '파일경로', '파일 열기 모드') as f
```

<br/>

### Practice
<br/>

### Pr01
```python
# 파일을 생성해서 데이터를 쓰고 읽어보자.

def file_Test():
    f = open('a.txt','w')   #파일 생성, 쓰기모드
    for i in range(65,91):
        f.write('%3s'%chr(i))
    f.close()

    f= open('a.txt','r')
    print(f.read(10))       # 괄호 안에는 바이트단위
    f.close()
    print('============================================')

    f = open('사과사진.jpg', 'r+b')     # 이미지는 그냥 r만 쓰면 못읽어와서 +binary해줘야 한다
    print(f.read())
    f.close()

if __name__ == '__main__':
    file_Test()
```
출력결과
```python
  A  B  C 
============================================
b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00\xff\xfe\x00;CREATOR: gd-jpeg v1.0 (using IJG JPEG v80), quality = 82\n\xff\xdb\x00C\x00\x06\x04\x04\x05\x04\x04\x06\x05\x05\x05\x06\x06\x06\x07\t\x0e\t\t\x08\x08\t\x12\r\r\n\x0e\x15\x12\x16\x16\x15\x12\x14\x14\x17\x1a!\x1c\x17\x18\x1f\x19\x14\x14\x1d\'\x1d\x1f"#%%%\x16\x1c),...생략'
```
- 먼저 파일 생성 결과를 이미지로 살펴보면,<br/>

|실행전|실행후|
|:----:|:---:|
|![실행전](https://user-images.githubusercontent.com/93986157/193412759-aff25887-2c2f-480d-82fc-599d3d01b506.png)|![실행후](https://user-images.githubusercontent.com/93986157/193412889-b9b7e716-9ef2-4f1d-8c4a-d6dc935044b3.png)|
||실행 후 a.txt 파일 생성됨|
<br/>

- 또한 a.txt에는<br/>
![a.txt](https://user-images.githubusercontent.com/93986157/193413053-31e19a62-b962-4b25-ba28-404ed4014f51.png)
- A~Z까지의 영문이 쓰여진 것을 확인할 수 있다.
- `print(f.read(10))`에서 10바이트를 읽어왔으므로, 출력결과는 _'빈칸2개'_ **'A'** _'빈칸2개'_ **'B'** _'빈칸2개'_ **'C'** _'빈칸'_ 이 출력된 것이다.
- 마지막 출력결과는 사과사진.jpg를 이진모드로 읽어온 결과다.

<br/>

### Pr02
```python
# 사과사진.jpg의 내용을 읽어서 apple02.png로 출력해보자.

def file_Test01():
    f = open('사과사진.jpg', 'r+b')
    f_o = open('apple02.png', 'w+b')
    f_o.write(f.read())
    f_o.close()
    f.close()



# 구구단을 출력하고 읽어오자. 편의상 2단만 하자.

def file_Test02():
    with open('gugu.txt', 'w') as f:
        for i in range(1,10):
            f.write('%3d * %3d = %3d\n'%(2,i,(2*i)))
    with open('gugu.txt', 'r') as f:
        print(f.read())


if __name__ == '__main__':
    file_Test01()
    file_Test02()
```
출력결과
```python
  2 *   1 =   2
  2 *   2 =   4
  2 *   3 =   6
  2 *   4 =   8
  2 *   5 =  10
  2 *   6 =  12
  2 *   7 =  14
  2 *   8 =  16
  2 *   9 =  18
```
- 파일 실행결과를 이미지로 살펴보면<br/>

|실행전|실행후|
|:----:|:---:|
|![실행전](https://user-images.githubusercontent.com/93986157/193413703-1d69f6c8-b612-4871-b805-faefbf8ad378.png)|![실행후](https://user-images.githubusercontent.com/93986157/193413726-075c47a3-c7ea-45e1-aabb-59f090ae7180.png)|
||실행 후 apple02.png, gugu.txt 파일 생성됨|
<br/>

- 또한 gugu.txt에는<br/>
![gugu.txt](https://user-images.githubusercontent.com/93986157/193413796-e8fe981c-3e8e-46dd-ac23-8553a73cd3b6.png)
- 구구단 2단이 쓰여진 것을 확인할 수 있다.
- `with open() as`를 활용하여 자동 파일 닫기를 구현했다.