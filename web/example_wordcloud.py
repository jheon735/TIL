import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from konlpy.tag import Hannanum
import time
import requests
from bs4 import BeautifulSoup

"""
national_anthem = 
동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
남산 위에 저 소나무 철갑을 두른 듯
바람 서리 불변함은 우리 기상일세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
가을 하늘 공활한데 높고 구름 없이
밝은 달은 우리 가슴 일편단심일세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세
이 기상과 이 맘으로 충성을 다하여
괴로우나 즐거우나 나라 사랑하세
무궁화 삼천리 화려 강산
대한 사람 대한으로 길이 보전하세


hannanum = Hannanum()
nouns = hannanum.nouns(national_anthem)     #명사들을 키워드로 나열
counter = Counter(nouns)

wordcloud = WordCloud(
    font_path=
    background_color='white',
    width = 1000,
    height = 1000,
)
img = wordcloud.generate_from_frequencies(counter)
plt.imshow(img)
plt.show()
"""

user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

questions = []
for i in range(1, 6):
    res = requests.get(f"https://hashcode.co.kr/?page={i}", user_agent)     # 페이지네이션 된 사이트 스크래핑
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("li", "question-list-item")

    for result in results:
        questions.append(result.h4.text.strip())

    time.sleep(0.1)

hannanum = Hannanum()
words = []
for question in questions:
    nouns = hannanum.nouns(question)
    words += nouns

counter = Counter(words)
wordcloud = WordCloud(
    font_path=r"C:\Users\l9305\OneDrive\문서\TIL\TIL\web\MALGUN.TTF",
    background_color='white',
    width = 1000,
    height = 1000,
)
img = wordcloud.generate_from_frequencies(counter)
plt.imshow(img)
plt.show()