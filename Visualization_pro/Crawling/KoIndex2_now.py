import requests
from bs4 import BeautifulSoup
import pandas as pd

# 사이트 안띄우고 바로 결과 출력


## 1990년부터 2019년까지 온실가스 배출량
## (년도, 배출량)


## 통계표가 게시되어 있는 국가지표통계 사이트
url = "https://www.index.go.kr//strata/jsp/showStblGams3.jsp?stts_cd=146404&idx_cd=1464&freq=Y&period=1990:2019"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")


## 배출량 텍스트가 있는 td 선택자 선택
tdata = soup.select("#tr_146404_1 > td")
# print(tdata)
# print("-------------------------------")


## 배출량을 리스트로 만들기
list_ems = []

for i in tdata:
    emission = i.get_text()
    # print(emission)
    list_ems.append(emission)

print('총 탄소배출량')
print(list_ems)
print('\n')


## 순배출량 리스트
net_ems = soup.select("#tr_146404_2 > td")

list_net = []

for i in net_ems:
    net = i.get_text()
    list_net.append(net)

print('순 탄소배출량')
print(list_net)
print('\n')


## 에너지 부분 탄소배출량
energy_ems = soup.select("#tr_146404_3 > td")

list_energy = []

for i in energy_ems:
    energy = i.get_text()
    list_energy.append(energy)

print('에너지 부분 탄소배출량')
print(list_energy)
print('\n')



## 산업공정 탄소배출량
indus_ems = soup.select("#tr_146404_4 > td")

list_indus = []

for i in indus_ems:
    indus = i.get_text()
    list_indus.append(indus)

print('산업공정 부분 탄소배출량')
print(list_indus)
print('\n')



## 농업 탄소배출량
agri_ems = soup.select("#tr_146404_5 > td")

list_agri = []

for i in agri_ems:
    agri = i.get_text()
    list_agri.append(agri)

print('농업 부분 탄소배출량')
print(list_agri)
print('\n')




## LULUCF 탄소배출량
lulu_ems = soup.select("#tr_146404_6 > td")

list_lulu = []

for i in lulu_ems:
    lulu = i.get_text()
    list_lulu.append(lulu)

print('LULUCF 부분 탄소배출량')
print(list_lulu)
print('\n')




## 폐기물 탄소배출량
waste_ems = soup.select("#tr_146404_7 > td")

list_waste = []

for i in waste_ems:
    waste = i.get_text()
    list_waste.append(waste)

print('폐기물 부분 탄소배출량')
print(list_waste)
print('\n')




## 총 배출량 증감율
ems_inde = soup.select("#tr_146404_8 > td")

list_incdec = []

for i in ems_inde:
    incdec = i.get_text()
    list_incdec.append(incdec)

print('총 탄소배출량 증감율')
print(list_incdec)
print('\n')








## 연도 텍스트가 있는 th 선택자 선택
yeardata = soup.select("#trHeader146404_1 > th")
# print(yeardata)



## 연도를 리스트로 만들기
list_year = []

for i in yeardata:
    year = i.get_text()
    # print(year)
    list_year.append(year)

## 첫번째 text는 공백으로 필요 없음
del list_year[0]

print(list_year)


year_ems =list(zip(list_year, list_ems))
print(year_ems)

year_net =list(zip(list_year, list_net))
print(year_net)

year_energy =list(zip(list_year, list_energy))
print(year_energy)

year_indus =list(zip(list_year, list_indus))
print(year_indus)

year_agri =list(zip(list_year, list_agri))
print(year_agri)

year_lulu =list(zip(list_year, list_lulu))
print(year_lulu)

year_waste =list(zip(list_year, list_waste))
print(year_waste)

year_incdec =list(zip(list_year, list_incdec))
print(year_incdec)



data = {'year' : list_year, 'total_ems' : list_ems, 'net_ems' : list_net, 'energy_ems' : list_energy, 'indus_ems' : list_indus, 'agri_ems' : list_agri, 'lulu_ems' : list_lulu, 'waste_ems' : list_waste, 'ems_incdec' : list_incdec}

df = pd.DataFrame(data)
df.set_index('year', inplace = True)
print(df)

df.to_csv("./Visualization_pro/ANALYSIS/Kor_emission.csv")