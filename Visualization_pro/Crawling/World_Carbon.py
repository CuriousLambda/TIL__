import pandas as pd
import numpy as np


## csv 파일 불러오기
xlsx = pd.read_excel("./World_Carbon_Emiss.xlsx")
xlsx.to_csv("./World_Carbon.csv")

df = pd.read_csv("World_Carbon.csv")
df.info()

df_new = df.drop(0, axis = 0)

df_fill = df_new.fillna(0)
df_fill["Year"] = df_fill.iloc[:,1]
df_fill.to_csv("./Carbon_Year.csv")


df_carbon = pd.read_csv("Carbon_Year.csv")
print(df_carbon)

df_Glo_Ems = df_carbon.set_index(keys = "Year")
# print(df_Glo_Ems.columns)
df_Ems = df_Glo_Ems.drop(["Territorial emissions in MtCO₂", "Unnamed: 0.1", "Unnamed: 0"], axis = 'columns')
# print(df_Ems)
df_Ems.loc[:, "Total_Emission"] = df_Ems.loc[:, 'Unnamed: 1':'Unnamed: 221'].sum(axis = 1)

print(df_Ems)

df_Ems.to_csv("../ANALYSIS/World-Carbon-Emission.csv")