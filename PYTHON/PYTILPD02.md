# 판다스(pandas)_02

### 예시01 - range로 Series 생성
```python
import pandas as pd

data = range(1, 10, 2)
d = pd.Series(data, index = range(1, len(data)+1))
print(d)
```
출력결과
```
1    1
2    3
3    5
4    7
5    9
dtype: int64
```

<br/>

### 예시02 - 벡터화 연산
```python
import pandas as pd

r = pd.Series([1,2,3])

print(r + 4)
print('\n\n')

print(r*3)
print('\n\n')

print(r/100)
```
출력결과
```
0    5
1    6
2    7
dtype: int64



0    3
1    6
2    9
dtype: int64



0    0.01
1    0.02
2    0.03
dtype: float64
```
- 인덱스는 연산하지 않고, 값들만 연산된다.

<br/>

### 예시03 - Series[조건식]
```python
# 값이 10보다 큰 애들만 추출해보자.

import pandas as pd

s1 = pd.Series(range(1,20))

print(s1[s1>10])
```
출력결과
```
10    11
11    12
12    13
13    14
14    15
15    16
16    17
17    18
18    19
dtype: int64
```

<br/>

### 예시04 - [ ] 없이 조건식만 작성했을 경우
```python
import pandas as pd

s1 = pd.Series(range(1,20))

print(s1>10)
```
출력결과
```
0     False
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9     False
10     True
11     True
12     True
13     True
14     True
15     True
16     True
17     True
18     True
dtype: bool
```

### 예시05 - Series[ 조건식 여러개 ] - OR (`|`)
```python
import pandas as pd

s1 = pd.Series(range(1,20))

print(s1[(s1 % 2 == 0) | (s1 % 3 == 0)])
```
출력결과
```
1      2
2      3
3      4
5      6
7      8
8      9
9     10
11    12
13    14
14    15
15    16
17    18
dtype: int64
```
- `|` 를 사용하면 OR 연산이 가능하다.

<br/>

### 예시06 - Series[ 조건식 여러개 ] - AND(`&`)
```python
import pandas as pd

s1 = pd.Series(range(1,20))

print(s1[(s1 % 2 == 0) & (s1 % 3 == 0)])
```
출력결과
```
5      6
11    12
17    18
dtype: int64
```
- `&` 를 사용하면 AND 연산이 가능하다.

<br/>

### 예시07 - index로 연산 수행
```python
import pandas as pd

s1 = pd.Series(range(1,20))

print(s1[s1.index>15])
```
출력결과
```
16    17
17    18
18    19
dtype: int64
```
- 인덱스가 15보다 큰 배열들을 나타낸다.

<br/>

### 예시08 - Series 간의 연산 _ Index가 없을 때
```python
import pandas as pd

a1 = pd.Series([11,2,3,4])
b1 = pd.Series([11,2,3,4])

print(a1 + b1)

print('\n\n')

print(a1 * b1)
```
출력결과
```
0    22
1     4
2     6
3     8
dtype: int64



0    121
1      4
2      9
3     16
dtype: int64
```

<br/>

### 예시09 - Series 간의 연산 _ Index가 있을 때
```python
import pandas as pd

a1 = pd.Series([11,2,3,4], index = ['a', 'b', 'c', 'd'])
b1 = pd.Series([11,2,3,4],index = ['a', 'b', 'c', 'd'])

print(a1 + b1)
```
출력결과
```
a    22
b     4
c     6
d     8
dtype: int64
```

<br/>


### 예시10 - Series 간의 연산 _ Index가 다를 때
```python
import pandas as pd

a1 = pd.Series([11,2,3,4], index = ['a', 'b', 'c', 'd'])
b1 = pd.Series([11,2,3,4],index = ['aa', 'bb', 'c', 'd'])

print(a1 + b1)
```
출력결과
```
a     NaN
aa    NaN
b     NaN
bb    NaN
c     6.0
d     8.0
dtype: float64
```
- Series 간의 연산은 인덱스 이름이 같아야한다.
- 인덱스 이름이 같은 열들은 연산이 됐지만 인덱스 이름이 다른 열들은 NaN으로 출력됐다.
- 인덱싱이 다를 때는 가장 큰 datatype으로 리턴된다.
- 이 경우, NaN(Not a Number) 때문에 수치에서 가장 큰 데이터 타입인 float64 type으로 리턴됐다.

<br/>

### 예시11 - dict 타입으로 Series만들기
```python
import pandas as pd

d = {'a': 1, 'b': 2, 'c': 3}

ser = pd.Series(data=d)

print(ser)
```
출력결과
```
a    1
b    2
c    3
dtype: int64
```
- dict의 key값이 인덱스로 설정된다.

<br/>

### 예시12 - array.keys()로 인덱스 설정하기
```python
import pandas as pd

city = {'서울' : 9904312, '부산' : 3448737, '인천' : 289045, '대구' : 2466052}

r = pd.Series(data = city, index = city.keys())

print(r)
```
출력결과
```
서울    9904312
부산    3448737
인천     289045
대구    2466052
dtype: int64
```
- dict의 key값을 인덱스로 그대로 사용할 경우, dict요소 자체가 순서를 갖고 있지 않아서 인덱스 순서가 바뀌어 나올 수도 있다.
- `array.keys()`를 사용하게 되면 순서가 배열 그대로 고정된다.

<br/>

### 예시13 - del로 Series 요소 지우기
```python
import pandas as pd

city = {'서울' : 9904312, '부산' : 3448737, '인천' : 289045, '대구' : 2466052}
r = pd.Series(data = city, index = city.keys())

del r['부산']

print(r)
```
출력결과
```
서울    9904312
인천     289045
대구    2466052
dtype: int64
```
