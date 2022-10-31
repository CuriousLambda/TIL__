import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## csv 파일 불러오기
df_death = pd.read_csv('./Disaster_Death.csv')
df_WorEms = pd.read_csv('./World-Carbon-Emission.csv')


## 사용할 데이터 만들기
year = df_death[['Year']]
drought = df_death[['Number of deaths from drought']]
earthquake = df_death[['Number of deaths from earthquakes']]
disaster = df_death[['Number of deaths from disasters']]
volcanic = df_death[['Number of deaths from volcanic activity']]
flood = df_death[['Number of deaths from floods']]
storm = df_death[['Number of deaths from storms']]
wildfire = df_death[['Number of deaths from wildfires']]
ex_temp = df_death[['Number of deaths from extreme temperatures']]
total_death = df_death[['Total_Death']]


Year = df_death['Year']
Drought = df_death['Number of deaths from drought']
Earthquake = df_death['Number of deaths from earthquakes']
Disaster = df_death['Number of deaths from disasters']
Volcanic = df_death['Number of deaths from volcanic activity']
Flood = df_death['Number of deaths from floods']
Storm = df_death['Number of deaths from storms']
Wildfire = df_death['Number of deaths from wildfires']
Ex_temp = df_death['Number of deaths from extreme temperatures']
Totla_Death = df_death['Total_Death']



year_ems = df_WorEms[['Year']]
total_ems = df_WorEms[['Total_Emission']]

Year_Ems = df_WorEms['Year']
Total_Ems = df_WorEms['Total_Emission']


## 재해로 인한 사망자 수는 줄어드는데 재해로 인한 피해는 더 크다?



## 피어슨 상관계수로 상관성 파악하기
# -0.01 - 선형관계 모호함
print(np.corrcoef(Totla_Death, Total_Ems))
# 0.11 - 선형관계 모호함
print(np.corrcoef(Drought, Total_Ems))
# 0.06 - 선형관계 모호함
print(np.corrcoef(Earthquake, Total_Ems))
# 0.07 - 선형관계 모호함
print(np.corrcoef(Volcanic, Total_Ems))
# -0.26 - 약한 음의 선형관계
print(np.corrcoef(Flood, Total_Ems))
# -0.13 - 선형관계 모호함
print(np.corrcoef(Storm, Total_Ems))
# 0.14 - 선형관계 모호함
print(np.corrcoef(Wildfire, Total_Ems))
# 0.06 - 선형관계 모호함
print(np.corrcoef(Ex_temp, Total_Ems))




fig = plt.figure(figsize=(24, 10))
plt.rcParams["font.family"] = "Malgun Gothic"


ax01 = fig.add_subplot(2, 2, 1)

line = np.polyfit(Total_Ems, Totla_Death, 1)
p = np.poly1d(line)

ax01.scatter(total_ems, total_death, color = 'red')
ax01.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("총 탄소 배출량과 자연재해로 인한 사망자 수 추세선", fontsize = 20)




ax02 = fig.add_subplot(2, 4, 3)

line02 = np.polyfit(Total_Ems, Drought, 1)
p = np.poly1d(line02)

ax02.scatter(total_ems, drought, color = 'tan')
ax02.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 가뭄 사망자)", fontsize = 10)




ax03 = fig.add_subplot(2, 4, 4)

line03 = np.polyfit(Total_Ems, Earthquake, 1)
p = np.poly1d(line03)

ax03.scatter(total_ems, earthquake, color = 'saddlebrown')
ax03.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 지진 사망자)", fontsize = 10)




ax04 = fig.add_subplot(2, 4, 5)

line04 = np.polyfit(Total_Ems, Flood, 1)
p = np.poly1d(line04)

ax04.scatter(total_ems, flood, color = 'deepskyblue')
ax04.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 홍수 사망자)", fontsize = 10)




ax05 = fig.add_subplot(2, 4, 6)

line05 = np.polyfit(Total_Ems, Storm, 1)
p = np.poly1d(line05)

ax05.scatter(total_ems, storm, color = 'turquoise')
ax05.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 폭풍 사망자)", fontsize = 10)




ax06 = fig.add_subplot(2, 4, 7)

line06 = np.polyfit(Total_Ems, Wildfire, 1)
p = np.poly1d(line06)

ax06.scatter(total_ems, wildfire, color = 'limegreen')
ax06.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 산불 사망자)", fontsize = 10)




ax07 = fig.add_subplot(2, 4, 8)

line07 = np.polyfit(Total_Ems, Ex_temp, 1)
p = np.poly1d(line07)

ax07.scatter(total_ems, ex_temp, color = 'mediumvioletred')
ax07.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 한파/폭염 사망자)", fontsize = 10)


plt.show()