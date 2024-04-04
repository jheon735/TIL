from selenium import webdriver
from selenium.webdriver.chrome.service import Service   #드라이버는 브라우저마다 다르다
from webdriver_manager.chrome import ChromeDriverManager    # pc에 설치된 크롬과 버전을 같게 하기 위해
from selenium.webdriver.common.by import By     # 응답 요소에서 특정 요소를 추출하는 메서드
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import keys, ActionChains     # 액션을 주는 메서드
from selenium.webdriver.common.actions.action_builder import ActionBuilder


#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))    # 크롬을 켜서 동작하게 드라이버라는 객체 생성
#driver.get("http://www.example.com")
#print(driver.page_source)

"""
# driver 객체도 닫아야 하기 때문에 with 문을 사용하는 것이 좋다
# tag이름으로 찾기
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("http://www.example.com")
    for element in driver.find_elements(By.TAG_NAME, "p"):
        print("Text:",element.text)

# implicit wait
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")    # 동적 웹사이트
    driver.implicitly_wait(10)  # 렌더링이 끝나면 바로 넘어오고 아닐 때 10초만 기다린다
    print(driver.find_element(By.XPATH, r'//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[1]/div/a/div[2]/p[1]').text)

# explicit wait
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")    # 동적 웹사이트
    #WebDriverWait의 인자 두개. driver와 최대 기다릴 시간. EC method 사용해서 target이라는 ID가 존재할 때 까지 기다려라. 그리고 특정 요소때문에 기다렸다면 그 요소를 객체로 받을 수 있다
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[1]/div/a/div[2]/p[1]')))    
    print(element.text)

# 제목 여러개 가져오기
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://indistreet.com/live?sortOption=startDate%3AASC")
    driver.implicitly_wait(10)
    
    for i in range(1, 11):
        element = driver.find_element(By.XPATH, f'//*[@id="__next"]/div/main/div[2]/div/div[4]/div[1]/div[{i}]/div/a/div[2]/p[1]')
        print(element.text)

#마우스 이벤트 처리하기
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://qna.programmers.co.kr/")
driver.implicitly_wait(0.5)

button = driver.find_element(By.CLASS_NAME, "UtilMenustyle__Link-sc-2sjysx-4.ewJwEL")
ActionChains(driver).click(button).perform()
"""

#키보드 이벤트 처리하기

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.naver.com/")
driver.implicitly_wait(1)

# 내비게이션 바에서 "로그인" 버튼을 찾아 눌러봅시다.
button = driver.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")
ActionChains(driver).click(button).perform()

# "아이디" input 요소에 여러분의 아이디를 입력합니다.
id_input = driver.find_element(By.ID, "id")
ActionChains(driver).send_keys_to_element(id_input, "ID").perform()

# "패스워드" input 요소에 여러분의 비밀번호를 입력합니다.
pw_input = driver.find_element(By.ID, "pw")
ActionChains(driver).send_keys_to_element(pw_input, "Password").perform()

# "로그인" 버튼을 눌러서 로그인을 완료합니다.
button = driver.find_element(By.CLASS_NAME, "btn_login")
ActionChains(driver).click(button).perform()



