from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup


## 2012년부터 2019년까지 온실가스 배출량
## (년도, 배출량)


url = "https://www.index.go.kr/potal/main/EachDtlPageDetail.do?idx_cd=1464"

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url)
sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")

tdata = soup.select("#t_Table_146404 > tbody > tr:nth-child(1) > td")
# print(tdata)

# print("-------------------------------")

list1 = []

for i in tdata:
    emission = i.get_text()
    # print(emission)
    list1.append(emission)

print(list1)


yeardata = soup.select("#t_Table_146404 > thead > tr.bg > th")
# print(yeardata)

list2 = []

for i in yeardata:
    year = i.get_text()
    # print(year)
    list2.append(year)

del list2[0]

print(list2)


result =list(zip(list2, list1))
print(result)