import pandas as pd
import matplotlib.pyplot as plt



##### (1990 ~ 2019) 계절별 평균 기온 변화와 우리나라 탄소배출량 현황 #####



## csv 파일 불러오기
df_ems = pd.read_csv('../CSV/Kor_emission.csv')
df_temp = pd.read_csv('../CSV/Kor_Temp.csv')[17:47]

## csv파일 컬럼, 데이터타입 등 정보확인
df_ems.info()
df_temp.info()


## 각 데이터프레임의 기술통계 확인
print(df_ems.describe())
print(df_temp.describe())


## 사용할 데이터 만들기

## -1 기온데이터
year = df_temp[['year']]
avg = df_temp[['avg_temp']]
spring = df_temp[['spr_temp']]
summer = df_temp[['sum_temp']]
fall = df_temp[['fall_temp']]
winter = df_temp[['win_temp']]

Year = df_temp['year']
Avg_Temp = df_temp['avg_temp']
Spring_Temp = df_temp['spr_temp']
Summer_Temp = df_temp['sum_temp']
Fall_Temp = df_temp['fall_temp']
Winter_Temp = df_temp['win_temp']

avg_mean = df_temp['avg_temp'].mean()
year_min = df_temp['year'].min()
year_max = df_temp['year'].max()


## -2 탄소배출량 데이터
year_ems = df_ems[['year']]
total = df_ems[['total_ems']]
net = df_ems[['net_ems']]
energy = df_ems[['energy_ems']]
industry = df_ems[['indus_ems']]
agriculture = df_ems[['agri_ems']]
lulucf = df_ems[['lulu_ems']]
waste = df_ems[['waste_ems']]
incdec = df_ems[['ems_incdec']]

Total_Ems = df_ems['total_ems']
Net_Ems = df_ems['net_ems']
Energy_Ems = df_ems['energy_ems']
Industry_Ems = df_ems['indus_ems']
Agriculture_Ems = df_ems['agri_ems']
LULUCF_Ems = df_ems['lulu_ems']
Waste_Ems = df_ems['waste_ems']
Ems_Incdec = df_ems['ems_incdec']



fig = plt.figure(figsize=(15, 10))
plt.rcParams["font.family"] = "Malgun Gothic"


ax01 = fig.add_subplot(1, 2, 1)

ax01.plot(year, avg, color = 'red', marker = 'o')
ax01.plot(year, spring, color = 'violet', marker = 'o')
ax01.plot(year, summer, color = 'limegreen', marker = 'o')
ax01.plot(year, fall, color = 'brown', marker = 'o')
ax01.plot(year, winter, color = 'dodgerblue', marker = 'o')

plt.legend(('AVERAGE', 'SPRING', 'SUMMER', 'FALL', 'WINTER'), bbox_to_anchor = (1.0, 0.82))
plt.title("계절별 평균 기온 변화", fontsize = 20)





ax02 = fig.add_subplot(1, 2, 2)


ax02.plot(year_ems, total, color = "red", marker = 'o')
ax02.plot(year_ems, net, color = "mediumspringgreen", marker = 'o')
ax02.plot(year_ems, energy, color = "cornflowerblue", marker = 'o')
ax02.plot(year_ems, industry, color = "dimgrey", marker = 'o')
ax02.plot(year_ems, agriculture, color = "gold", marker = 'o')
ax02.plot(year_ems, lulucf, color = "darkorchid", marker = 'o')
ax02.plot(year_ems, waste, color = "peru", marker = 'o')
ax02.plot(year_ems, incdec, color = "lightcoral", marker = 'o')

plt.legend(('TOTAL', 'NET', 'ENERGY', 'INDUSTRY', 'AGRICULTURE', 'LULUCF', 'WASTE', 'INCDEC'), loc = 'best', ncol = 2)
plt.title("분야별 탄소배출량 추이", fontsize = 20)



plt.show()
