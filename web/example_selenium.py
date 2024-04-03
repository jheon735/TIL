from selenium import webdriver

driver = webdriver.Chrome()     # 사용할 브라우저 지정
driver.implicitly_wail(10)      # 응답 후 시간 지연
driver.get("http://www.example.com")

elem = driver.find_element_by_tag_name("hello-input")   # 특정 태그를 불러와
elem.send_keys("Hello!") # 문자 입력도 가능