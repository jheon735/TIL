import requests
from bs4 import BeautifulSoup
import time

"""
res = requests.get("http://www.example.com")

soup = BeautifulSoup(res.text, "html.parser")   #첫 파라미터는 html text, 두 번째는 어떤 형태를 parsing할 것인지 명시

# print(soup.prettify())  # 정리된 형태로 html을 출력해준다.

title = soup.title  #title
head = soup.head  #head
body = soup.body    #body

h1 = soup.find("h1")     #원하는 태그를 입력해서 가장 먼저 나오는 하나의 특정 태그를 찾아준다.
h1.name     #찾은 태그를 위의 형태로 저장하면 그 태그의 이름을 가져온다.
h1.text     #찾은 태그의 내용을 가져온다

#soup.find_all("p")  #원하는 태그를 입력해서 그 태그의 전체가 리스트 형태로 반환

res = requests.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
soup = BeautifulSoup(res.text, "html.parser")

#book = soup.find("h3")
h3_result = soup.find_all("h3")

# print(book.a.text) #find로 찾은 book은 객체이기 때문에 내부 태그를 검색해서 사용가능하다

for book in h3_result:
    print(book.a["title"])  #특정 속성을 가지고 오고 싶을 떈 dictionary처럼 사용

res = requests.get("https://programmers.co.kr/pages/data_engineering")
soup = BeautifulSoup(res.text, "html.parser")

#print(soup.find("div", id="results"))   #id를 찾을 땐 이런 형태로
find_result = soup.find("div", "page-header")  #class는 key없이 바로 두번째 항목에 입력

print(find_result.h1.text.strip())  #strip으로 공백 지우기
"""

user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

# res = requests.get("https://hashcode.co.kr/", user_agent)   #두번째 인자에 헤더를 넣어야하는데 헤더가 딕셔너리 형태이기 때문에 위의 정보로 요청을 보냄
# soup = BeautifulSoup(res.text, "html.parser")

# results = soup.find_all("li", "question-list-item")

# for result in results:
#     print(result.find("div", "question").find("div", "top").h4.text)

titles = []
for i in range(1, 6):
    res = requests.get(f"https://hashcode.co.kr/?page={i}", user_agent)     # 페이지네이션 된 사이트 스크래핑
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.find_all("li", "question-list-item")
    for result in results:
        titles.append(result.find("div", "question").find("div", "top").h4.text)
    time.sleep(0.1)

print(titles)