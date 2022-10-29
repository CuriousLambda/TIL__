import requests
from bs4 import BeautifulSoup
import pandas as pd

## 연도별 평균 기온( 연 전체, 봄, 여름, 가을, 겨울) 표 url
url = "https://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=140001&idx_cd=1400&freq=Y&period=1973:2021"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")



## 년도
yeardata = soup.select("#trHeader140001_1 > th")

list_year = []

for i in yeardata:
    year = i.get_text()
    list_year.append(year)

del list_year[0]

print(list_year)
## 17개 지우면 1990년부터



## 년 전체 평균 기온
tdata = soup.select("#tr_140001_1 > td")

list_avg = []

for i in tdata:
    avgtemp = i.get_text()
    list_avg.append(avgtemp)

print(list_avg)




## 봄 평균 기온
spring = soup.select("#tr_140001_2 > td")

list_spr = []

for i in spring:
    spr_data = i.get_text()
    list_spr.append(spr_data)

print(list_spr)




## 여름 평균 기온
summer = soup.select("#tr_140001_3 > td")

list_sum = []

for i in summer:
    sum_data = i.get_text()
    list_sum.append(sum_data)

print(list_sum)




## 가을 평균 기온
fall = soup.select("#tr_140001_4 > td")

list_fall = []

for i in fall:
    fall_data = i.get_text()
    list_fall.append(fall_data)

print(list_fall)





## 겨울 평균 기온
winter = soup.select("#tr_140001_5 > td")

list_win = []

for i in winter:
    win_data = i.get_text()
    list_win.append(win_data)

print(list_win)



## (년도, 년 전체 평균 기온)
result_avg = list(zip(list_year, list_avg))

## (년도, 봄 평균 기온)
result_spr = list(zip(list_year, list_spr))

## (년도, 여름 평균 기온)
result_sum = list(zip(list_year, list_sum))

## (년도, 가을 평균 기온)
result_fall = list(zip(list_year, list_fall))

## (년도, 겨울 평균 기온)
result_win = list(zip(list_year, list_win))


print("년도별 평균기온")
print(result_avg)
print("\n")

print("년도별 봄 평균 기온")
print(result_spr)
print("\n")

print("년도별 여름 평균 기온")
print(result_sum)
print("\n")

print("연도별 가을 평균 기온")
print(result_fall)
print("\n")

print("연도별 겨울 평균 기온")
print(result_win)

data = {'year' : list_year, 'avg_temp' : list_avg, 'spr_temp' :  list_spr, 'sum_temp' : list_sum, 'fall_temp' : list_fall, 'win_temp' : list_win}
df = pd.DataFrame(data)
df.set_index('year', inplace=True)
print(df)

df.to_csv("./Visualization_pro/ANALYSIS/Kor_Temp.csv")