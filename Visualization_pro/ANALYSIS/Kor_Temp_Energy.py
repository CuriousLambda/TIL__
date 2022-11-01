import pandas as pd
import numpy as np
import matplotlib.pyplot as plt




##### (1990 ~ 2019) 우리나라 에너지 탄소배출량과 평균 기온 관계 #####



## csv 파일 불러오기
df_ems = pd.read_csv('../CSV/Kor_emission.csv')
df_temp = pd.read_csv('../CSV/Kor_Temp.csv')[17:47]

## csv파일 컬럼, 데이터타입 등 정보확인
df_ems.info()
df_temp.info()



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



## 피어슨 상관계수로 상관성 파악하기

# 0.39 - 양의 선형관계
print(np.corrcoef(Avg_Temp, Energy_Ems))
# 0.41 - 양의 선형관계
print(np.corrcoef(Spring_Temp, Energy_Ems))
# 0.46 - 양의 선형관계
print(np.corrcoef(Summer_Temp, Energy_Ems))
# 0.28 - 약한 양의 선형관계
print(np.corrcoef(Fall_Temp, Energy_Ems))
# -0.007 - 선형관계 모호함
print(np.corrcoef(Winter_Temp, Energy_Ems))





fig = plt.figure(figsize=(20, 10))
plt.rcParams["font.family"] = "Malgun Gothic"


ax01 = fig.add_subplot(1, 2, 1)

line = np.polyfit(Energy_Ems, Avg_Temp, 1)
p = np.poly1d(line)

ax01.scatter(energy, avg, color = 'red')
ax01.plot(Energy_Ems, p(Energy_Ems), "m:*")
ax01.set_xticks(list(range(200, 800, 100)))
ax01.set_xlim(200, 650)
plt.xlabel('탄소 배출량')
plt.ylabel('평균 기온')
plt.title("에너지 탄소 배출량과 평균 기온 추세선", fontsize = 20)




ax02 = fig.add_subplot(2, 4, 3)

line02 = np.polyfit(Energy_Ems, Spring_Temp, 1)
p = np.poly1d(line02)

ax02.scatter(energy, spring, color = 'violet')
ax02.plot(Energy_Ems, p(Energy_Ems), "m:*")
ax02.set_xticks(list(range(200, 800, 100)))
ax02.set_xlim(200, 650)
plt.xlabel('탄소 배출량')
plt.ylabel('봄 평균 기온')
plt.title("(에너지 탄소배출, 봄)", fontsize = 13)




ax03 = fig.add_subplot(2, 4, 4)

line03 = np.polyfit(Energy_Ems, Summer_Temp, 1)
p = np.poly1d(line03)

ax03.scatter(energy, summer, color = 'limegreen')
ax03.plot(Energy_Ems, p(Energy_Ems), "m:*")
ax03.set_xticks(list(range(200, 800, 100)))
ax03.set_xlim(200, 650)
plt.xlabel('탄소 배출량')
plt.ylabel('여름 평균 기온')
plt.title("(에너지 탄소배출, 여름)", fontsize = 13)




ax04 = fig.add_subplot(2, 4, 7)

line04 = np.polyfit(Energy_Ems, Fall_Temp, 1)
p = np.poly1d(line04)

ax04.scatter(energy, fall, color = 'brown')
ax04.plot(Energy_Ems, p(Energy_Ems), "m:*")
ax04.set_xticks(list(range(200, 800, 100)))
ax04.set_xlim(200, 650)
plt.xlabel('탄소 배출량')
plt.ylabel('가을 평균 기온')
plt.title("(에너지 탄소배출, 가을)", fontsize = 13)




ax05 = fig.add_subplot(2, 4, 8)

line05 = np.polyfit(Energy_Ems, Winter_Temp, 1)
p = np.poly1d(line05)

ax05.scatter(energy, winter, color = 'dodgerblue')
ax05.plot(Energy_Ems, p(Energy_Ems), "m:*")
ax05.set_xticks(list(range(200, 800, 100)))
ax05.set_xlim(200, 650)
plt.xlabel('탄소 배출량')
plt.ylabel('겨울 평균 기온')
plt.title("(에너지 탄소배출, 겨울)", fontsize = 13)



plt.show()
