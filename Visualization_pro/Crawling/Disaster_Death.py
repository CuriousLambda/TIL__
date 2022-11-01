import pandas as pd
import numpy as np


## csv 파일 불러오기
df = pd.read_csv('./natural-disasters.csv')

## 필요한 컬럼만 가져오기
df_essential = df[['Number of deaths from drought', 'Number of deaths from earthquakes',
                    'Number of deaths from disasters', 'Number of deaths from volcanic activity',
                    'Number of deaths from floods', 'Number of deaths from storms',
                    'Number of deaths from wildfires', 'Number of deaths from extreme temperatures', 'Year']]


## 1990년부터 2019년 데이터만 가져오기
df_y = df_essential[(df_essential['Year'] >= 1990) & (df_essential['Year'] <= 2019)]

## NaN값 0으로 대체
df_year = df_y.fillna(0)
print(df_year)
df_set = df_year.set_index(keys = 'Year')
print(df_set)
df_death = df_set.groupby(['Year']).sum()
print(df_death)

df_death.loc[:, "Total_Death"] = df_death.loc[:, 'Number of deaths from drought':'Number of deaths from extreme temperatures'].sum(axis = 1)
# print(df_death)

df_death.to_csv("../CSV/Disaster_Death.csv")

'''
## 각 년도별 합계 구하기
for i in range(1990, 2000):
    globals()['sum_{}'.format(i-1990)] = df_year[df['Year'] == i].sum()
    # sum = df_year[df['Year'] == i].sum()
    # Year 컬럼 빼고 시리즈로 만들기
    print(globals()['sum_{}'.format(i-1990)][0 : 8])
    # df_sum0, df_sum1, ... 과 같은 dataframe만들기
    globals()['df_sum{}'.format(i-1990)] = pd.DataFrame(globals()['sum_{}'.format(i-1990)][0 : 8], columns = [i])
    # 인덱스로 년도를 사용할 수 있도록 행과 열을 바꿈
    globals()['df_tr{}'.format(i-1990)] = globals()['df_sum{}'.format(i-1990)].transpose()
    # print(globals()['df_tr{}'.format(i-1990)])

for j in range(0,9):
    df_fin = globals()['df_tr{}'.format(j)].append(globals()['df_tr{}'.format(j+1)])

print(df_fin)
'''


'''
for j in range(0, 8):
        globals()['df_cc{}'.format(j)] = pd.concat((globals()['df_tr{}'.format(j)], globals()['df_tr{}'.format(j+1)]))
        df_fin = pd.concat((globals()['df_cc{}'.format(j)],globals()['df_tr{}'.format(j+2)]))
        
print(df_fin)
'''