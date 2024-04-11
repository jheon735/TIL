import seaborn as sns
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
from collections import Counter

"""
# seaborn 기초
plt.figure(figsize=(10, 5))
sns.lineplot(x = [1,3,2,4], y = [4, 3, 2, 1])
# sns.barplot(x=[1,2,3,4], y=[0.7, 0.2, 0.1, 0.05])
plt.title("bar plot")
plt.xlabel("x label")
plt.ylabel("y label")
plt.ylim(2, 3)
plt.show()

# 기상청에서 온도 자료 가져와서 그래프 그리기
with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get("https://www.weather.go.kr/w/weather/forecast/short-term.do")
    driver.implicitly_wait(1)
    temps = driver.find_element(By.ID, "my-tchart").text

temps = [int(i) for i in temps.replace("℃","").split("\n")]

sns.lineplot(
    x = range(len(temps)),
    y = temps
)
plt.ylim(min(temps)-2, max(temps)+2)
plt.show()
"""

# 프로그래머스 Q&A 질문태그 빈도 시각화
user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

freq = {}
for i in range(1,11):
    with requests.get(f"https://hashcode.co.kr/?page={i}", user_agent) as res:
        soup = BeautifulSoup(res.text, "html.parser")
        ul_tags = soup.find_all("ul", "question-tags")

    for ul in ul_tags:
        li_tags = ul.find_all("li")
        for li in li_tags:
            tag = li.text.strip()
            if tag not in freq:
                freq[tag] = 1
            else:
                freq[tag] += 1
        time.sleep(0.1)

counter = Counter(freq)
# counter.most_common(10) #상위 10개 보여주기

x = [elem[0] for elem in counter.most_common(10)]
y = [elem[1] for elem in counter.most_common(10)]

plt.figure(figsize=(20, 10))
plt.title("Frequency of quesion in Q&A")
plt.xlabel("Tag")
plt.ylabel("Frequency")
sns.barplot(x=x, y=y)
plt.show()