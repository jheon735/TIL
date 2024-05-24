import requests
from bs4 import BeautifulSoup
import json

url = 'https://restcountries.com/v3/all'
response = requests.get(url).text
# soup = BeautifulSoup(response, 'html.parser')
# print(soup.find_all("name"))
data = json.loads(response)
print(data[0]["name"]["official"], data[0]["population"], data[0]["area"])

"""
["name"]["official"]
["population"]
["area"]
"""