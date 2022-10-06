# **For, While 문**

## _**for문**_
-----------------------
<br/>

###  **1. 단일 for문**

<br/>

형식
```python
for 변수 in 시퀀스(순서형 자료형):
    조건 Ture 명령
else:
    False 명령
```
<br/>

예시01
```python
# for문을 이용해서 1~10까지의 합을 출력 해보자.

su = [1,2,3,4,5,6,7,8,9,10]
m_sum = 0

for res in su:
    m_sum += res

else:
    print('The sum is = ', m_sum)
```
출력결과
```python
The sum is = 55
```
<br/>

예시02
```python
# enumerate를 사용하지 않은 경우

fruit = ['apple','watermelon', 'peach', 'pear', 'grape']

for i in range(len(fruit)):
    print(i+100, fruit[i])
```
출력결과
```python
100 apple
101 watermelon
102 peach
103 pear
104 grape
```

<br/>

예시03
```python
# for문과 enumerate를 함께 사용할 경우

fruit = ['apple','watermelon', 'peach', 'pear', 'grape']
for x,y in enumerate(fruit,100):
    print(x,y)
```
출력결과
```
100 apple
101 watermelon
102 peach
103 pear
104 grape
```
> enumerate는 Python 내장함수이다.<br/>
> list가 있는 경우, 순서와 리스트의 값을 전달하는 기능<br/>
> 즉, 리스트의 원소에 순서 값을 부여해주는 함수<br/>
> 함수 형식은 `enumerate(list, start = any integer)`

<br/>

예시04
```python
# for문과 zip을 함께 사용하는 경우

a01=[1,2,3,4]
a02=['a','b']

for res in zip(a01,a02, strict=False):
    print(res)
```
출력결과
```python
(1, 'a')
(2, 'b')
```
> zip은 Python 내장함수이다.<br/>
> 각 객체가 담고 있는 원소를 tuple의 형태로 반환한다.<br/>
> 함수 형식은 `zip(*iterables, strict = True/False)` -> * 있으면 여러개를 컴마로 나열할 수 있다는 뜻<br/>
> `strict = False`가 디폴트 값이며, 이 경우 iterable들의 길이가 다르다면 짧은 객체를 기준으로 tuple을 생성한다.<br/>
> `strict = Ture`로 해주면 iterable들의 길이가 다를 경우 오류가 발생할 수 있다.

<br/>

### **2. 중첩 for문**
<br/>

형식
```python
    for 변수 in 시퀀스 :
        for 변수 in 시퀀스 :
            명령
```
<br/>

예시
```python
# 중첩 for를 이용해서 구구단을 출력 해보자.

for i in range(2,10):
    print(f'{i} 단')
    for j in range(1,10):
        print(" %d  * %d = %d " %(i, j , (i*j)))
        # 정수자리 정수자리 정수자리 '%(값, 값, 값)
    print('-----------')
```
출력결과
```python
2 단
 2  * 1 = 2 
 2  * 2 = 4 
 2  * 3 = 6 
 2  * 4 = 8 
 2  * 5 = 10 
 2  * 6 = 12 
 2  * 7 = 14 
 2  * 8 = 16 
 2  * 9 = 18 
-----------
3 단
 3  * 1 = 3 
 3  * 2 = 6 
 3  * 3 = 9 
 3  * 4 = 12 
 3  * 5 = 15 
 3  * 6 = 18 
 3  * 7 = 21 
 3  * 8 = 24 
 3  * 9 = 27 
-----------
---이하생략---
```

## _**while문**_
--------------------
<br/>

형식
```python
while 조건문 :
        True 반복할 명령
    else:
        False 명령
```
<br/>

예시01
```python
# 10에서 1까지 출력해보자. (즉, 역순으로 출력)

su=10

while su>=1:
    print(su, end='\t')
    su-=1
else:
    pass
```
출력결과
```python
10	9	8	7	6	5	4	3	2	1	
```
<br/>

예시02
```python
# 1부터 10까지의 합을 출력해보자.

su =1
sum = 0

while su <=10:
    print(su, end='+\t')
    sum +=su
    su += 1
else:
    print("=",sum)
```
출력결과
```python
1+	2+	3+	4+	5+	6+	7+	8+	9+	10+	= 55
```
<br/>

## Practice
```python
#exam04 : 1~100까지 출력을 하되 홀수만 출력을 하고 갯수를 구하자.

su = 1
cnt = 0

while su <= 100:
    if su % 2 == 1:
        cnt += 1
        print(su, end='\t')
    su += 1
else:
    print(' = 1부터 100까지의 홀수')
    print('cnt = ', cnt)
```
출력결과
```python
1	3	5	7	9	11	13	15	17	19	21	23	25	27	29	31	33	35	37	39	41	43	45	47	49	51	53	55	57	59	61	63	65	67	69	71	73	75	77	79	81	83	85	87	89	91	93	95	97	99	 = 1부터 100까지의 홀수
cnt =  50
```


