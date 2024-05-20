import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim

today = (datetime.now()+timedelta(hours=9)).strftime(r"%Y%m%d")
querydate = today[:6]

gu_code = {11110 : "종로구", 11140 : "중구", 11170 : "용산구", 11200 : "성동구", 11215 : "광진구", 11230 : "동대문구",
        11260 : "중랑구", 11290 : "성북구", 11305 : "강북구", 11320 : "도봉구", 11350 : "노원구", 11380 : "은평구",
        11410 : "서대문구", 11440 : "마포구", 11470 : "양천구", 11500 : "강서구", 11530 : "구로구", 11545 : "금천구",
        11560 : "영등포구", 11590 : "동작구", 11620 : "관악구", 11650 : "서초구", 11680 : "강남구", 11710 : "송파구",
        11740 : "강동구"}

def data_extract(url, key, dates, cols, save_fname, make_list):
    region = gu_code.keys()
    data = []
    for i in region:
        params ={'serviceKey' : f'{key}', 
                'LAWD_CD' : f'{i}', 
                'DEAL_YMD' : f'{dates}'}
        response = requests.get(url, params=params).content
        soup = BeautifulSoup(response, 'lxml-xml')
        rows = soup.find_all('item')
        make_list(data, rows, cols)

    df = pd.DataFrame(data, columns=cols, dtype = object) 
    df.to_csv(f'{save_fname}.csv') 

# 아파트매매
url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
cols = ['년','월', '일', '법정동', '아파트',  '전용면적', '거래금액', '건축년도',
        '지번', '지역코드', '층', '해제여부', '해제사유발생일', '거래유형', '중개사소재지', '등기일자', '매도자', '매수자','동']

# data_extract(url, key, dates, cols, "아파트매매", apartment_sell)

region = [11110, 11140, 11170, 11200, 11215, 11230, 11260, 11290, 11305, 11320, 11350, 11380, 11410, 11440, 11470, 11500, 11530, 11545,
            11560, 11590, 11620 ,11650, 11680, 11710, 11740]

key = "ZU3VKtV/cyVYqylBKhohTTGbwd5/hq0d4YDqWyHz9kODNZMljBKxidxikPm6J4uY7MTEGHQfT4+FuK/UEGmNkQ=="
params ={'serviceKey' : f'{key}', 
        'LAWD_CD' : f'{region[0]}', 
        'DEAL_YMD' : f'{querydate}'}
response = requests.get(url, params=params).content
soup = BeautifulSoup(response, 'lxml-xml')
rows = soup.find_all('item')
data = []
for row in rows:
    items = row.find_all()
    items_dict = {}
    for item in items:
        items_dict[item.name.strip()] = item.text.strip()
    data.append(items_dict)

df = pd.DataFrame(data)
df["계약일"] = df["년"].map(str) + df["월"].map(str) + df["일"].map(str)
df["주소"] = "서울특별시 "+ df[""] + " "

cols =['계약일', '자치구명', '법정동명', '주소', '건물명', '층', '위도', '경도', '물건금액(만원)', '건물면적(㎡)', '토지면적(㎡)', 
        '권리구분', '취소일', '건축년도', '건물용도', '신고구분']


def get_lat_lng(add):
    geolocator = Nominatim(user_agent='South Korea')  # Fix the typo here
    location = geolocator.geocode(add)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        print('지번 주소 문제')
        print(add)
        return None, None

trade = pd.read_csv('data/seoul_realestate.csv', header = 0, skipinitialspace=True)
trade = trade.drop(trade[trade['자치구코드'] > 20000].index)
trade = trade.drop(['접수연도', '신고한 개업공인중개사 시군구명', '자치구코드', '법정동코드', '지번구분', '지번구분명'], axis=1)
trade = trade.fillna(-9999)
tt = time.time()
newdata = []
for idx, row in trade.iterrows():
    if row['본번'] != -9999 and row['부번'] != 0:
        row['주소'] = "서울특별시 "+row["자치구명"]+" "+row["법정동명"] + " " + str(int(row["본번"])) + "-" + str(int(row["부번"]))
        lat, lon = get_lat_lng(row['주소'])
        row['위도'] = lat
        row['경도'] = lon
    elif row['본번'] != -9999 and row['부번'] == 0:
        row['주소'] = "서울특별시 "+row["자치구명"]+" "+row["법정동명"] + " " + str(int(row["본번"]))
        lat, lon = get_lat_lng(row['주소'])
        row['위도'] = lat
        row['경도'] = lon
    else:
        row['주소'] = "서울특별시 "+row["자치구명"]+" "+row["법정동명"]
        row['위도'] = -9999
        row['경도'] = -9999
    if idx == 10:
        print(idx, time.time()-tt)
        break
    newdata.append(row)

df = pd.DataFrame(newdata, dtype = object) 
df = df.replace({-9999: None})
df.to_csv(f'test.csv') 