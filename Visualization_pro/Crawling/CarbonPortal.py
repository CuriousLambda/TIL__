from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

url = "https://www.gihoo.or.kr/netzero/user/sttstprfsn/nv_easyStatistics.do"

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url)
sleep(3)

# emission = driver.find_element(By.ID, "greenGasVal")
# print(emission)



soup = BeautifulSoup(driver.page_source, "html.parser")

# chartdiv = soup.find_all("div", class_ = "chart_result_area")
# print(chartdiv)

emission = soup.select("path")
print(emission[0])

driver.find_element_by_xpath('//*[@id="highcharts-55lxiof-0"]/svg/g[6]/g[2]/path[1]').click()

chart = soup.find("p", class_ = "greenGasVal")
print(chart)

'''
for p in chartdiv:
    emission = p.find("p").get_text()
    print(emission)
'''
