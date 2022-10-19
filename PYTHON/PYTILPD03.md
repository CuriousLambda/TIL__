# 판다스(pandas)_03
> 판다스에서 사용되는 다양한 함수들 중 몇 가지를 소개하려고 한다.

<br/>

## 1. 함수 소개
- size : 개수 반환
- shape : 튜플형태로 shape반환
- unique: 유일한 값만 ndarray로 반환
- count : NaN을 제외한 개수를 반환
- mean: NaN을 제외한 평균
- value_counts: NaN을 제외하고 각 값들의 빈도를 반환

<br/>

## 2. 판다스 패키지의 date_range 함수 (날짜생성)
- `pd.date_range(start=None, end=None, periods=None, freq='D')`
- start : 시작날짜 / end= 끝날짜
- periods = 날짜 생성기간/ fref = 날짜 생성 주기
- start는 필수 옵션
- end나 periods는 둘 중 하나가 있어야 함
- freq는 설정하지 않으면 defalut값으로 Day로 설정

![date_attribute.PNG](https://user-images.githubusercontent.com/93986157/196703299-1c108615-d8d5-489d-adea-1eb93d570161.png)

<br/>

### 예제01 - mean, sum
```python
import pandas as pd

b= pd.Series([1, 3, 5, 7, 9])

print(b)
print('\n')

print('mena = ', b.mean())
print('sum = ', b.sum())
```
출력결과
```
0    1
1    3
2    5
3    7
4    9
dtype: int64


mena =  5.0
sum =  25
```

### 예제02 - value_counts()
```python
import pandas as pd

r = pd.Series([1,1,3,4,4]).value_counts()
print(r)
```
출력결과
```
1    2
4    2
3    1
dtype: int64
```
- `value_counts()`는 동일 값의 원소끼리 그룹핑하여 개수를 세서 반환하는 함수이다.

<br/>

### 예제03 - date_range _ Day
```python
import pandas as pd

r = pd.date_range(start = '2018-10-01', end = '2018-10-20')
print(r)
```
출력결과
```
DatetimeIndex(['2018-10-01', '2018-10-02', '2018-10-03', '2018-10-04',
               '2018-10-05', '2018-10-06', '2018-10-07', '2018-10-08',
               '2018-10-09', '2018-10-10', '2018-10-11', '2018-10-12',
               '2018-10-13', '2018-10-14', '2018-10-15', '2018-10-16',
               '2018-10-17', '2018-10-18', '2018-10-19', '2018-10-20'],
              dtype='datetime64[ns]', freq='D')
```
- DatetimeIndex로 반환된다.
- freq를 설정하지 않았을 때 기본값은 d (Day)이다.
- 인덱스이기 때문에 시리즈에 붙일 수 있다.
- dtype = 'datetime64[ns]'이다.

<br/>

### 예제04 - date_range _ Second
```python
import pandas as pd

r = pd.date_range(start = '2018-10-01', end = '2018-10-20', freq = 'S')
print(r)
```
출력결과
```
DatetimeIndex(['2018-10-01 00:00:00', '2018-10-01 00:00:01',
               '2018-10-01 00:00:02', '2018-10-01 00:00:03',
               '2018-10-01 00:00:04', '2018-10-01 00:00:05',
               '2018-10-01 00:00:06', '2018-10-01 00:00:07',
               '2018-10-01 00:00:08', '2018-10-01 00:00:09',
               ...
               '2018-10-19 23:59:51', '2018-10-19 23:59:52',
               '2018-10-19 23:59:53', '2018-10-19 23:59:54',
               '2018-10-19 23:59:55', '2018-10-19 23:59:56',
               '2018-10-19 23:59:57', '2018-10-19 23:59:58',
               '2018-10-19 23:59:59', '2018-10-20 00:00:00'],
              dtype='datetime64[ns]', length=1641601, freq='S')
```

<br/>

### 예제05 - date_range _ Week
```python
import pandas as pd

r = pd.date_range(start = '2018-10-01', end = '2018-10-20', freq = 'W')
print(r)
```
출력결과
```
DatetimeIndex(['2018-10-07', '2018-10-14'], dtype='datetime64[ns]', freq='W-SUN')
```

<br/>

### 예제06 - date_range _ 내가 원하는 간격 설정
```python
import pandas as pd

r = pd.date_range(start = '2018-10-01', end = '2018-10-20', freq = '3D')
print("3일 간격 출력('3D') : ", r)
print('\n')
print('\n')

s = pd.date_range(start = '2018-10-01', periods = 12, freq = '2BM')
print("2개월 간격으로 월말주기 12개 생성('2BM') : ", s)
print('\n')
print('\n')

w = pd.date_range(start = '2018-10-01', periods = 10, freq = '4BM')
print("4개월 간격으로 월말주기 10개 생성('4BM') : ", w)
print('\n')
print('\n')

y = pd.date_range(start = '2018-10-01', periods = 4, freq = 'QS')
print("분기별 생성('QS') : ", y)
```
출력결과
```
3일 간격 출력('3D') :  DatetimeIndex(['2018-10-01', '2018-10-04', '2018-10-07', '2018-10-10',
               '2018-10-13', '2018-10-16', '2018-10-19'],
              dtype='datetime64[ns]', freq='3D')




2개월 간격으로 월말주기 12개 생성('2BM') :  DatetimeIndex(['2018-10-31', '2018-12-31', '2019-02-28', '2019-04-30',
               '2019-06-28', '2019-08-30', '2019-10-31', '2019-12-31',
               '2020-02-28', '2020-04-30', '2020-06-30', '2020-08-31'],
              dtype='datetime64[ns]', freq='2BM')




4개월 간격으로 월말주기 10개 생성('4BM') :  DatetimeIndex(['2018-10-31', '2019-02-28', '2019-06-28', '2019-10-31',
               '2020-02-28', '2020-06-30', '2020-10-30', '2021-02-26',
               '2021-06-30', '2021-10-29'],
              dtype='datetime64[ns]', freq='4BM')




분기별 생성('QS') :  DatetimeIndex(['2018-10-01', '2019-01-01', '2019-04-01', '2019-07-01'], dtype='datetime64[ns]', freq='QS-JAN')
```