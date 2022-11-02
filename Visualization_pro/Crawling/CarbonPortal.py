from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains


### 세계 탄소 배출량 데이터 ###
## (* csv 다운받음 *)

url = "https://www.gihoo.or.kr/netzero/user/sttstprfsn/nv_easyStatistics.do"

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

path = driver.find_element(By.CLASS_NAME, "highcharts-halo highcharts-color-0")
print(path)

# act = ActionChains(driver)
# act.move_to_element(path).perform()

sleep(3)


