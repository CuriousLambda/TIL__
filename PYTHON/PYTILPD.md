# 판다스(pandas)_01
- series, DataFrame등의 자료구조를 활용한 데이터분석 기능을 제공해주는 라이브러리


<br/>

## Series
- pandas의 기본 객체 중 하나
- 자료구조는 순차 1차원 배열로, 인덱싱이 가능하다.
- numpy의 ndarray를 기반으로 인덱싱 기능을 추가하여 1차원 배열을 나타냄
- index를 지정하지 않을 시, 기본적으로 ndarray와 같이 0-based 인덱스 생성, 지정할 경우 명시적으로 지정된 index를 사용

<br/>

### 예시01 - Series 객체 생성
```python
import pandas as pd

s = pd.Series([1,2,3,4,5], index = ['AA', 'BB', 'CC', 'DD', 'EE'])
print(s)
```
출력결과
```python
AA    1
BB    2
CC    3
DD    4
EE    5
dtype: int64
```

<br/>

### 예시02 - index 이름 만들기
```python
import pandas as pd

s = pd.Series([1,2,3,4,5], index = ['AA', 'BB', 'CC', 'DD', 'EE'])

s.index.name = 'test'

print(s)
```
출력결과
```python
test
AA    1
BB    2
CC    3
DD    4
EE    5
dtype: int64
```

<br/>

### 예시03 - Series 이름 만들기
```python
import pandas as pd

s = pd.Series([1,2,3,4,5], index = ['AA', 'BB', 'CC', 'DD', 'EE'])
s.index.name = 'test'

s.name = "이름 컬럼"

print(s)
```
출력결과
```python
test
AA    1
BB    2
CC    3
DD    4
EE    5
Name: 이름 컬럼, dtype: int64
```
- name은 pd.Series의 속성으로 만들어 줄 수도 있다.
  - 예) `s = pd.Series([1,2,3,4,5], index = ['AA', 'BB', 'CC', 'DD', 'EE'], name = "이름 컬럼)`

<br/>

### 예시04 - Series의 원소추출 _1) 인덱스 번호로 추출
```python
import pandas as pd

s = pd.Series([1,2,3,4,5], index = ['AA', 'BB', 'CC', 'DD', 'EE'])
s.index.name = 'test'
s.name = "이름 컬럼"

print(s[2])
```
출력결과
```python
3
```

<br/>

### 예시05 - Series의 원소추출 _2) 인덱스 이름으로 추출
```python
import pandas as pd

s = pd.Series([1,2,3,4,5], index = ['AA', 'BB', 'CC', 'DD', 'EE'])
s.index.name = 'test'
s.name = "이름 컬럼"

print(s['CC'], s['EE'])
```
출력결과
```python
3 5
```

<br/>

### 예시06 - Series 원소 값 변경
```python
import pandas as pd

s = pd.Series([1,2,3,4,5], index = ['AA', 'BB', 'CC', 'DD', 'EE'])
s.index.name = 'test'
s.name = "이름 컬럼"

s['CC'] = 3000
s['EE'] = 5000

print(s)
```
출력결과
```python
test
AA       1
BB       2
CC    3000
DD       4
EE    5000
Name: 이름 컬럼, dtype: int64
```

<br/>

### 예시07 - Series 인덱스로 데이터 추출 ([ , ])
```python
import pandas as pd

s = pd.Series([1,[2,3],4,5], index = ['AA', 'BB', 'CC', 'DD'])

print(s[[1,3]])
```
출력결과
```python
BB    [2, 3]
DD         5
dtype: object
```
- 첫번째, 세번째 인덱스의 원소를 가져온다.
- 주의할 점은 `s[1, 3]`은 오류가 발생한다.

<br/>

### 예시08 - Series 인덱스로 데이터 추출 ( : )
```python
import pandas as pd

s = pd.Series([1,[2,3],4,5], index = ['AA', 'BB', 'CC', 'DD'])

print(s[1:3])
```
출력결과
```python
BB    [2, 3]
CC         4
dtype: object
```
- ` : `을 사용했을 경우에는 `1인덱스부터 3인덱스 전까지`의 의미를 갖는다.

<br/>

- 마찬가지로 인덱스명을 사용해도 같은 결과가 나온다.

<br/>

### 예시09 - Series 인덱스명으로 데이터 추출 ([ , ])
```python
import pandas as pd
s = pd.Series([1,[2,3],4,5], index = ['AA', 'BB', 'CC', 'DD'])

print(s[['BB','DD']])
```
출력결과
```python
BB    [2, 3]
DD         5
dtype: object
```

<br/>

### 예시10 - Series 인덱스명으로 데이터 추출 ( : )
```python
import pandas as pd
s = pd.Series([1,[2,3],4,5], index = ['AA', 'BB', 'CC', 'DD'])

print(s['BB':'CC'])
```
출력결과
```python
BB    [2, 3]
CC         4
dtype: object
```

<br/>

### 예시11 - 객체 인덱스로 추출
```python
import pandas as pd
s = pd.Series([1,[2,3],4,5], index = ['AA', 'BB', 'CC', 'DD'])

print(s.BB, s.AA, s[0], s['AA'])
```
출력결과
```python
[2, 3] 1 1 1
```

<br/>

### 예시12 - 간단한 Series를 만들어보자.
```python
# 문자 인덱스의 시리즈이다. 아래와 같은 결과를 출력할 수 있도록 코드를 작성해보자.

'''
도시
서울     9904312
부산     3448737
인천     289045
대구     2466052
Name : 인구, dtype : in64
'''

res = pd.Series([9904312, 3448737, 289045, 2466052], index = ['서울','부산', '인천', '대구'], name = '인구')
res.index.name = '도시'
print(res)
```
출력결과
```python
도시
서울    9904312
부산    3448737
인천     289045
대구    2466052
Name: 인구, dtype: int64
```