import requests
from bs4 import BeautifulSoup

# 사이트 안띄우고 바로 결과 출력


## 1990년부터 2019년까지 온실가스 배출량
## (년도, 배출량)


## 통계표가 게시되어 있는 국가지표통계 사이트
url = "https://www.index.go.kr//strata/jsp/showStblGams3.jsp?stts_cd=146404&idx_cd=1464&freq=Y&period=1990:2019"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")


## 배출량 텍스트가 있는 td 선택자 선택
tdata = soup.select("#tr_146404_1 > td")
# print(tdata)
# print("-------------------------------")


## 배출량을 리스트로 만들기
list_ems = []

for i in tdata:
    emission = i.get_text()
    # print(emission)
    list_ems.append(emission)

print(list_ems)




## 연도 텍스트가 있는 th 선택자 선택
yeardata = soup.select("#trHeader146404_1 > th")
# print(yeardata)



## 연도를 리스트로 만들기
list_year = []

for i in yeardata:
    year = i.get_text()
    # print(year)
    list_year.append(year)

## 첫번째 text는 공백으로 필요 없음
del list_year[0]

print(list_year)


result =list(zip(list_year, list_ems))
print(result)