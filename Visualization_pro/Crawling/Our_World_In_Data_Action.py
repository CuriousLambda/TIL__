from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time


### 세계 자연 재해로 인한 사망자 수 ###
## (* CSV 파일 다운받음 *)


url = "https://ourworldindata.org/natural-disasters"
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)

time.sleep(3)

table_button_check = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/main/article/div[2]/div[2]/div/div/section[2]/div[2]/div[2]/div/figure[1]/div/div/div/div[4]/div[2]/nav/ul/li[3]')))
table_button_class = driver.find_elements(By.XPATH, '/html/body/main/article/div[2]/div[2]/div/div/section[2]/div[2]/div[2]/div/figure[1]/div/div/div/div[4]/div[2]/nav/ul/li[3]')[0].get_attribute('class')

print(table_button_class)

while table_button_class == "tab clickable":
    table_button_check = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '/html/body/main/article/div[2]/div[2]/div/div/section[2]/div[2]/div[2]/div/figure[1]/div/div/div/div[4]/div[2]/nav/ul/li[3]')))
    table_button_class = driver.find_elements(By.XPATH, '/html/body/main/article/div[2]/div[2]/div/div/section[2]/div[2]/div[2]/div/figure[1]/div/div/div/div[4]/div[2]/nav/ul/li[3]')[0].get_attribute('class')
    print(table_button_class)

table_button = driver.find_elements(By.XPATH, '/html/body/main/article/div[2]/div[2]/div/div/section[2]/div[2]/div[2]/div/figure[1]/div/div/div/div[4]/div[2]/nav/ul/li[3]')[0]
driver.execute_script("arguments[0].click();", table_button)
