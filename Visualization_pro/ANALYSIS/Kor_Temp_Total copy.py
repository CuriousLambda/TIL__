import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



## csv 파일 불러오기
df_ems = pd.read_csv('./Kor_emission.csv')
df_temp = pd.read_csv('./Kor_Temp.csv')[17:47]

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

# 0.38 - 양의 선형관계
print(np.corrcoef(Avg_Temp, Total_Ems))
# 0.41 - 양의 선형관계
print(np.corrcoef(Spring_Temp, Total_Ems))
# 0.44 - 양의 선형관계
print(np.corrcoef(Summer_Temp, Total_Ems))
# 0.27 - 약한 양의 선형관계
print(np.corrcoef(Fall_Temp, Total_Ems))
# -0.007 - 선형관계 모호함
print(np.corrcoef(Winter_Temp, Total_Ems))


# 0.38 - 양의 선형관계
print(np.corrcoef(Avg_Temp, Net_Ems))
# 0.40 - 양의 선형관계
print(np.corrcoef(Spring_Temp, Net_Ems))
# 0.46 - 양의 선형관계
print(np.corrcoef(Summer_Temp, Net_Ems))
# 0.26 - 약한 양의 선형관계
print(np.corrcoef(Fall_Temp, Net_Ems))
# -0.005 - 선형관계 모호함
print(np.corrcoef(Winter_Temp, Net_Ems))




fig = plt.figure(figsize=(15, 10))
plt.rcParams["font.family"] = "Malgun Gothic"


ax01 = fig.add_subplot(1, 2, 1)

ax01.plot(avg, total, color = 'red', marker = 'o')
ax01.plot(year, spring, color = 'violet', marker = 'o')
ax01.plot(year, summer, color = 'limegreen', marker = 'o')
ax01.plot(year, fall, color = 'brown', marker = 'o')
ax01.plot(year, winter, color = 'dodgerblue', marker = 'o')

plt.title("계절별 평균 기온 변화", fontsize = 20)





ax02 = fig.add_subplot(2, 2, 2)

ax02.axhline(avg_mean, color = "mediumspringgreen", linewidth = "5")
ax02.plot(year, avg, color = "red", marker = 'o')
plt.title("연도별 평균 기온변화", fontsize = 20)



line = np.polyfit(Avg_Temp, Total_Ems, 1)
p = np.poly1d(line)
print(line)

ax03 = fig.add_subplot(2, 2, 4)
ax03.scatter(Avg_Temp, Total_Ems)
ax03.plot(Avg_Temp, p(Avg_Temp), "m:*")
ax03.set_yticks(list(range(200, 900, 100)))
ax03.set_ylim(150, 800)
plt.title("평균 기온과 총 탄소 배출량 추세선", fontsize = 20)





plt.show()
