## DataFrame 기본
import pandas as pd
import numpy as np


## DataFrame 선언하기
dataset = np.array([['kor', 70], ['math', 80]])
df = pd.DataFrame(dataset, columns = ['class', 'score'])
print(df)



## DataFrame 읽고 저장하기
df.to_csv('./basic.csv', header = True, index = True, encoding = 'utf8')
data = pd.read_csv('./basic.csv', na_values = 'NA', encoding = 'utf8')
print(data) # 인덱스 명을 지정하지 않았기 때문에 index명 부분에 Unnamed가 나온다.

# header = True : 컬럼명을 함께 저장
# index = True : 인덱스명을 함께 저장
# na_values = 'NA' : null값이 빈칸이 아닌 string값으로 저장된 경우 인식을 위해 사용
# encoding = 'utf8' : 데이터에 한국어가 포함된 경우 utf9로 인코딩



## DataFrame의 인덱스 확인, 추가, 리셋
print(df.index)
print(list(df.index))

df.index = ['A', 'B']
print(df.index)

print(df)

df.set_index('class', drop = True, append = False, inplace = True)
print(df)

df.reset_index(drop = False, inplace = True)
print(df)

# drop : 인덱스로 세팅한 컬럼을 DataFrame에서 삭제할지 결정 -> True이면 인덱스 안나오고, False이면 인덱스 나온다.
# append : 기존에 존재하던 인덱스를 삭제할지, 컬럼으로 추가할지를 결정





## scikit-learn의 load_iris()
from sklearn.datasets import load_iris

iris = load_iris()
print(iris)
iris = pd.DataFrame(iris.data, columns = iris.feature_names)
print(iris)



## 앞, 뒤 5개 행 확인
print(iris.head())
print(iris.tail())


## 요약정보, 기술통계 확인
print(iris.info())
print(iris.describe())



