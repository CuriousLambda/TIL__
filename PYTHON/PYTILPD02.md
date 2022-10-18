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