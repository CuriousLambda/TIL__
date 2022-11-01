import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


##### 2015년 이후 자연재해 종류별 사망자 수와 탄소배출량 관계 #####



## csv 파일 불러오기
df_death = pd.read_csv('../CSV/Disaster_Death.csv')
df_WorEms = pd.read_csv('../CSV/World-Carbon-Emission.csv')


## 사용할 데이터 만들기
year = df_death[['Year']].loc[25:]
drought = df_death[['Number of deaths from drought']].loc[25:]
earthquake = df_death[['Number of deaths from earthquakes']].loc[25:]
disaster = df_death[['Number of deaths from disasters']].loc[25:]
volcanic = df_death[['Number of deaths from volcanic activity']].loc[25:]
flood = df_death[['Number of deaths from floods']].loc[25:]
storm = df_death[['Number of deaths from storms']].loc[25:]
wildfire = df_death[['Number of deaths from wildfires']].loc[25:]
ex_temp = df_death[['Number of deaths from extreme temperatures']].loc[25:]
total_death = df_death[['Total_Death']].loc[25:]
print(flood)

Year = df_death['Year'].loc[25:]
Drought = df_death['Number of deaths from drought'].loc[25:]
Earthquake = df_death['Number of deaths from earthquakes'].loc[25:]
Disaster = df_death['Number of deaths from disasters'].loc[25:]
Volcanic = df_death['Number of deaths from volcanic activity'].loc[25:]
Flood = df_death['Number of deaths from floods'].loc[25:]
Storm = df_death['Number of deaths from storms'].loc[25:]
Wildfire = df_death['Number of deaths from wildfires'].loc[25:]
Ex_temp = df_death['Number of deaths from extreme temperatures'].loc[25:]
Totla_Death = df_death['Total_Death'].loc[25:]
print(Storm)



year_ems = df_WorEms[['Year']].loc[25:]
total_ems = df_WorEms[['Total_Emission']].loc[25:]

Year_Ems = df_WorEms['Year'].loc[25:]
Total_Ems = df_WorEms['Total_Emission'].loc[25:]




## 피어슨 상관계수로 상관성 파악하기
# -0.24 - 약한 음의 선형관계
print(np.corrcoef(Totla_Death, Total_Ems))
# 0.42 - 양의 선형관계
print(np.corrcoef(Drought, Total_Ems))
# 0.29 - 약한 양의 선형관계
print(np.corrcoef(Earthquake, Total_Ems))
# 0.57 - 양의 선형관계
print(np.corrcoef(Volcanic, Total_Ems))
# 0.10 - 약한 양의 선형관계 ** 음에서 양으로 바뀜
print(np.corrcoef(Flood, Total_Ems))
# 0.45 - 양의 선형관계
print(np.corrcoef(Storm, Total_Ems))
# 0.67 - 양의 선형관계
print(np.corrcoef(Wildfire, Total_Ems))
# -0.26 - 음의 선형관계 ** 양에서 음으로 바뀜
print(np.corrcoef(Ex_temp, Total_Ems))




fig = plt.figure(figsize=(20, 12))
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
plt.title("(총 탄소배출, 가뭄 사망자)", fontsize = 15)




ax03 = fig.add_subplot(2, 4, 4)

line03 = np.polyfit(Total_Ems, Earthquake, 1)
p = np.poly1d(line03)

ax03.scatter(total_ems, earthquake, color = 'saddlebrown')
ax03.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 지진 사망자)", fontsize = 15)




ax04 = fig.add_subplot(2, 4, 5)

line04 = np.polyfit(Total_Ems, Flood, 1)
p = np.poly1d(line04)

ax04.scatter(total_ems, flood, color = 'deepskyblue')
ax04.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 홍수 사망자)", fontsize = 15)




ax05 = fig.add_subplot(2, 4, 6)

line05 = np.polyfit(Total_Ems, Storm, 1)
p = np.poly1d(line05)

ax05.scatter(total_ems, storm, color = 'turquoise')
ax05.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 폭풍 사망자)", fontsize = 15)




ax06 = fig.add_subplot(2, 4, 7)

line06 = np.polyfit(Total_Ems, Wildfire, 1)
p = np.poly1d(line06)

ax06.scatter(total_ems, wildfire, color = 'limegreen')
ax06.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 산불 사망자)", fontsize = 15)




ax07 = fig.add_subplot(2, 4, 8)

line07 = np.polyfit(Total_Ems, Ex_temp, 1)
p = np.poly1d(line07)

ax07.scatter(total_ems, ex_temp, color = 'mediumvioletred')
ax07.plot(Total_Ems, p(Total_Ems), "m:*")
plt.xlabel('탄소 배출량')
plt.ylabel('사망자 수')
plt.title("(총 탄소배출, 한파/폭염 사망자)", fontsize = 15)


plt.show()