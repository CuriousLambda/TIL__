# Referenceable Note For Crawling

## 1. 정적 크롤링 (Selenium X)
- static webpage 크롤링
- selenium을 사용하지 않고 html문서 상 필요 내용 크롤링
- 한 페이지 안에서 원하는 정보가 모두 드러나는 경우 정적크롤링을 사용할 수 있다.

<br/>

### 형식
``` python
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "url 주소"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

cdata = soup.select("Crawling할 태그의 선택자")
```

- 정적 크롤링은 위와 같은 방법을 반복해서 크롤링 데이터를 수집한 후 딕셔너리(Dictionary) 타입 또는 제이슨(json) 타입으로 만들어주면 된다.
- pandas는 dataframe을 만들기 위해 import


<br/>

## 2. 동적 크롤링 (Selenium O)
- selenium과 browser driver를 사용하여 크롤링
- 크롤링을 위해 Action을 취해야하는 경우 사용할 수 있다.
- url 주소는 바뀌지 않았는데 페이지의 내용이 바뀌는 경우 동적 크롤링을 사용해야 한다.
  - (예 : 스크롤 시 url이 바뀌지 않아도 웹 페이지에 추가 내용이 업로드 된다.)

<br/>

### 형식
```python
from selenium import webdriver # (*)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


url = "url 주소"
driver = webdriver.Chrome("chromedriver경로 또는 주소")
driver.get(url) # 브라우저 열기

time.sleep(5) # 5초 뒤 아래 코드 실행

cdata = driver.find_element(By.CLASS_NAME, "클래스명")
```
- (*) 표시 외의 라이브러리들은 사용자 편의에 따라서 더 추가하거나 제외시킬 수도 있다.
- chormedriver.exe 설치가 필요하다. 단, 현재 자신의 chromebrowser의 버전과 맞아야한다.
- 다른 webdriver를 사용하고 싶다면 다른 webdriver를 이용할 수도 있다.


<br/>
<br/>
<br/>


> 아래부터는 편의에 따라 사용하는 Selenium라이브러리의 몇가지 모듈 사용법을 소개해보려고 한다.

<br/>
<br/>

### 2-1. By 모듈
- 특정한 속성으로 element를 찾아오기 위해 사용

<br/>

형식
```python
cdata = driver.find_element(By.CLASS_NAME, "클래스명")
```
- `By.` 뒤에 들어갈 수 있는 속성들
    - CLASS_NAME : `cdata = driver.find_element(By.CLASS_NAME, "클래스명")`
    - CSS_SELECTOR : `cdata = driver.find_element(By.CSS_SELECTOR, "css selector")`
    - ID : `cdata = driver.find_element(By.ID, "ID명")`
    - LINK_TEXT : `cdata = driver.find_element(By.LINK_TEXT, "link text")`
    - NAME : `cdata = driver.find_element(By.NAME, "name")`
    - PARTIAL_LINK_TEXT = `cdata = driver.find_element(By.PARTIAL_LINK_TEXT, "partial link text")`
    - TAG_NAME = `cdata = driver.find_element(By.TAG_NAME, "tag 명")`
    - XPATH = `cdata = driver.find_element(By.XPATH, "xpath")`

<br/>

### 2-2. Keys 모듈
- 컴퓨터의 키보드 액션을 키값으로 보내주는 역할
- 유니코드로 키값이 지정되어 있다.

<br/>

형식
```python
element.send_keys(Keys.ENTER)
```
- `Keys`에 사용가능한 KeyBoard Action과 Uni Code

|Key|Uni Code||Key|Uni Code||Key|Uni Code|
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|ADD|\ue025||ALT|\ue00a||ARROW_DOWN|\ue015|
|ARROW_LEFT|\ue012||ARROW_RIGHT|\ue014||ARROW_UP|\ue013|
|BACKSPACE|\ue003||BACK_SPACE|\ue003||CANCEL|\ue001|
|CLEAR|\ue005||COMMAND|\ue03d||CONTROL|\ue009|
|DECIMAL|\ue028||DELETE|\ue017||DIVIDE|\ue029|
|DOWN|\ue015||END|\ue010||ENTER|\ue007|
|EQUALS|\ue019||ESCAPE|\ue00c||||
|||||||||
|F1|\ue031||F10|\ue03a||F11|\ue03b|
|F12|\ue03c||F2|\ue032||F3||\ue033|
|F4|\ue034||F5|\ue035||F6|\ue036|
|F7|\ue037||F8|\ue038||F9|\ue039|
|||||||||
|HELP|\ue002||HOME|\ue011||INSERT|\ue016|
|LEFT|\ue012||LEFT_ALT|\ue00a||LEFT_CONTROL|\ue009|
|LEFT_SHIFT|\ue008|||||||
|||||||||
|META|\ue03d||MULTIPLY|\ue024||NULL|\ue000|
|NUMPAD0|\ue01a||NUMPAD1|\ue01b||NUMPAD2|\ue01c|
|NUMPAD3|\ue01d||NUMPAD4|\ue01e||NUMPAD5|\ue01f|
|NUMPAD6|\ue020||NUMPAD7|\ue021||NUMPAD8|\ue022|
|NUMPAD9|\ue023|||||||
|||||||||
|PAGE_DOWN|\ue00f||PAGE_UP|\ue00e||PAUSE|\ue00b|
|RETURN|\ue006||RIGHT|\ue014||SEMICOLON|\ue018|
|SEPARATOR|\ue026||SHIFT|\ue008||SPACE|\ue00d|
|SUBTRACT|\ue027||TAB|\ue004||UP|\ue013|
|ZENKAKU_HANKAKU|\ue040|||||||
|||||||||

<br/>
<br/>

## 2-3. WebDriverWait모듈, expected_conditions모듈
- 득정 조건에 맞는 element가 존재할 때까지 기다리는 모듈
- 보통 WebDriverWait모듈을 사용할 대 expected_conditions모듈을 함께 사용한다.
- expected_conditions모듈은 관습적으로 EC로 사용하는 편인것 같다.

<br/>

형식
```python
element = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, 'id명')))
```
- `WebDriverWait(driver, 10)` : __최대__ 10초까지 기다린다.
- `until(EC.presence_of_all_elements_located((By.ID, 'id명')))` : ID가 'id명'인 element가 나올 때까지, 해당 element가 존재하면 True를 반환한다.
- `WebDriverWait(driver, 10)` VS `time.sleep(10)`
  - `WebDriverWait(driver, 10)` : 최대 10초까지 기다린다.
  - `time.sleep(10)` : 10초 후 다음 코드를 실행한다.

<br/>

## 2-4. ActionChains 모듈
- 브라우저 상에서 상호작용 후 크롤링 가능한 동적사이트가 있을 때 사용한다.
- 마우스 이동, 마우스 버튼 클릭, 버튼 클릭, 메뉴 인터렉션과 같은 낮은 수준의 상호작용을 자동화하는 모듈

<br/>

형식
```python
ActionChains(driver).context_click(element).perform()
```
- `ActionChains(driver)` : ActionChains 클래스를 호출하여 드라이버를 매개 변수로 전송
- `perform()` : 모든 ActionChains에 저장된 행동을 실행 후 전체 작업에 대한 제출
- `context_click(element)` : element 오른쪽 클릭하기

<br/>

- ActionChains에 사용 가능한 상호작용들

<br/>

  - lick( on_element = None )	: 요소를 클릭
    - on_element : 클릭 할 요소. None이면 현재 마우스 위치를 클릭

<br/>

  - click_and_hold( on_element = None ) :	요소를 마우스 왼쪽버튼으로 누르고 있음
    - on_element : 클릭 후 고정할 요소. None이면 현재 마우스 위치를 클릭

<br/>

  - context_click( on_element = None ) : 요소에서 컨텍스트 클릭 (오른쪽 클릭)을 수행
    - on_element : 컨텍스트 클릭 할 요소. None이면 현재 마우스 위치를 클릭

<br/>

  - double_click( on_element = None ) :	요소를 두 번 클릭
    - on_element : 더블 클릭 할 요소. None이면 현재 마우스 위치를 클릭

<br/>

 
  - drag_and_drop( source  , target ) :	source 요소를 클릭한 뒤, target으로 이동하고 마우스 버튼을 놓음
    - source : 마우스를 내리는 요소 / target : 마우스를 올릴 요소

<br/>

 
  - drag_and_drop_by_offset( source  , xoffset, yoffset ) :	source 요소를 클릭한 뒤, target으로 이동하고 마우스 버튼을 놓음
    - source : 마우스를 내리는 요소 / xoffset : 이동할 X 오프셋 / yoffset : 이동할 Y 오프셋

<br/>

 
  - key_down(value, element=None) :	key를 누르기만 함.
    - value : 보낼 key / element : key를 보낼 요소

<br/>

 
  - key_up(value, element=None) :	key를 놓음
    - value : 보낼 key / element : key를 보낼 요소

<br/>

 
  - move_by_offset(xoffset, yoffset) :	마우스를 현재 마우스 위치에서 오프셋으로 이동.
    - xoffset : 이동할 X 오프셋 / yoffset : 이동할 Y 오프셋

<br/>

 
  - move_to_element(to_element) :	마우스를 element 중앙으로 이동

 <br/>
 
  - to_element : 이동할 WebElement
    - move_to_element_with_offset(to_element, xoffset, yoffset)
      - 지정된 요소의 오프셋만큼 마우스를 이동
      - 오프셋은 요소의 왼쪽 위 모서리를 기준

<br/>

 
  - to_element : 이동할 WebElement / xoffset : 이동할 X 오프셋 / yoffset : 이동할 Y 오프셋
  - pause(seconds) :	지정된 기간 (seconds) 동안 모든 입력을 일시 중지
  - perform() :	저장된 모든 작업을 수행

<br/>

 
  - release(on_element=None) :	element에서 누른 상태의 마우스 버튼을 놓음
    - on_element : 마우스를 올릴 요소. None이면 현재 마우스 위치에서 놓음

<br/>

 
  - reset_actions() :	이미 로컬 및 원격 끝에 저장된 작업을 지움

<br/>

 
  - send_keys(*keys_to_send) :	현재 포커스 된 element에 키를 보냄
    - keys_to_send : 전송할 키

<br/>

 
  - send_keys_to_element(element, *keys_to_send) :	element에 키를 보냄
    - element : Key를 보낼 element / keys_to_send : 전송할 키