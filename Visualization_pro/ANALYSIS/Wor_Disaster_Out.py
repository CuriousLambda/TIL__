import pandas as pd
import matplotlib.pyplot as plt


##### 재해별 사망자 수 이상값 확인을 위한 BoxPlot #####



## csv 파일 불러오기
df_death = pd.read_csv('../CSV/Disaster_Death.csv')
df_WorEms = pd.read_csv('../CSV/World-Carbon-Emission.csv')



## 데이터프레임 기술통계 확인하기
stat1 = df_death.describe()
stat2 = df_WorEms.describe()
print(stat1)
print(stat2)




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








fig = plt.figure(figsize=(20, 10))
plt.rcParams["font.family"] = "Malgun Gothic"



ax01 = fig.add_subplot(2, 2, 1)

ax01.boxplot(total_death)
plt.title("총 사망자 박스플롯", fontsize = 20)




ax02 = fig.add_subplot(2, 4, 3)

ax02.boxplot(drought)
plt.title("가뭄 사망자 박스플롯", fontsize = 15)




ax03 = fig.add_subplot(2, 4, 4)

ax03.boxplot(earthquake)
plt.title("지진 사망자 박스플롯", fontsize = 15)




ax04 = fig.add_subplot(2, 4, 5)

ax04.boxplot(flood)
plt.title("홍수 사망자 박스플롯", fontsize = 15)




ax05 = fig.add_subplot(2, 4, 6)

ax05.boxplot(storm)
plt.title("폭풍 사망자 박스플롯", fontsize = 15)




ax06 = fig.add_subplot(2, 4, 7)

ax06.boxplot(wildfire)
plt.title("산불 사망자 박스플롯", fontsize = 15)




ax07 = fig.add_subplot(2, 4, 8)

ax07.boxplot(ex_temp)
plt.title("폭염/한파 사망자 박스플롯", fontsize = 15)


plt.savefig('../Graph_Img/world_disa_outliers_check.png', dpi = 100)
plt.show()