import pandas as pd
import matplotlib.pyplot as plt


##### 재해별 사망자 수 이상값과 탄소배출량 그래프 비교 #####



## csv 파일 불러오기
df_death = pd.read_csv('../CSV/Disaster_Death.csv')
df_WorEms = pd.read_csv('../CSV/World-Carbon-Emission.csv')





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



# print(df_death[Drought >= 511][['Number of deaths from drought']])
# print(df_death[Flood >= 25745][['Number of deaths from floods']])



fig = plt.figure(figsize=(20, 12))
plt.rcParams["font.family"] = "Malgun Gothic"


# 가뭄 이상값
ax01 = fig.add_subplot(3, 2, 2)
ax01.scatter(df_death[Drought >= 511][['Year']], df_death[Drought >= 511][['Number of deaths from drought']], color = 'tan')

ax02 = ax01.twinx()
ax02.plot(Year_Ems, Total_Ems, alpha = 0.5)

plt.title("가뭄 이상값", fontsize = 15)




# 지진 이상값
ax03 = fig.add_subplot(3, 2, 3)
ax03.scatter(df_death[Earthquake >= 102876][['Year']], df_death[Earthquake >= 102876][['Number of deaths from earthquakes']], color = 'saddlebrown')

ax04 = ax03.twinx()
ax04.plot(Year_Ems, Total_Ems, alpha = 0.5)

plt.title("지진 이상값", fontsize = 15)





# 홍수 이상값
ax05 = fig.add_subplot(3, 2, 4)
ax05.scatter(df_death[Flood >= 25745][['Year']], df_death[Flood >= 25745][['Number of deaths from floods']], color = 'deepskyblue')

ax06 = ax05.twinx()
ax06.plot(Year_Ems, Total_Ems, alpha = 0.5)

plt.title("홍수 이상값", fontsize = 15)




# 폭풍 이상값
ax07 = fig.add_subplot(3, 2, 5)
ax07.scatter(df_death[Storm >= 24034][['Year']], df_death[Storm >= 24034][['Number of deaths from storms']], color = 'turquoise')

ax08 = ax07.twinx()
ax08.plot(Year_Ems, Total_Ems, alpha = 0.5)

plt.title("폭풍 이상값", fontsize = 15)




# 폭염/한파 이상값
ax09 = fig.add_subplot(3, 2, 6)
ax09.scatter(df_death[Ex_temp >= 10650][['Year']], df_death[Ex_temp >= 10650][['Number of deaths from extreme temperatures']], color = 'mediumvioletred')

ax10 = ax09.twinx()
ax09.plot(Year_Ems, Total_Ems, alpha = 0.5)

plt.title("폭염/한파 이상값", fontsize = 15)




# 총 재해사망자 수 이상값
ax11 = fig.add_subplot(3, 2, 1)
ax11.scatter(df_death[Totla_Death > 434085][['Year']], df_death[Totla_Death > 434085][['Total_Death']], color = 'red')

ax12 = ax11.twinx()
ax12.plot(Year_Ems, Total_Ems, alpha = 0.5)

plt.title("총 재해사망자 수 이상값", fontsize = 20)




plt.show()