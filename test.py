import requests
import time
import pandas as pd

trade = pd.read_csv('data/seoul_realestate.csv', header = 0, skipinitialspace=True)
trade = trade.drop(trade[trade['자치구코드'] > 20000].index)
trade = trade.drop(['접수연도', '신고한 개업공인중개사 시군구명', '자치구코드', '법정동코드', '지번구분', '지번구분명'], axis=1)
trade = trade.fillna(-9999)
tt = time.time()

apiurl = "https://api.vworld.kr/req/address?"
for idx, row in trade.iterrows():
    if row['본번'] != -9999 and row['부번'] != 0:
        row['주소'] = "서울특별시 "+row["자치구명"]+" "+row["법정동명"] + " " + str(int(row["본번"])) + "-" + str(int(row["부번"]))
        params = {
            "service": "address",
            "request": "getcoord",
            "crs": "epsg:4326",
            f"address": "{addr}",
            "format": "json",
            "type": "road",
            "key": "28010AC2-7187-3642-BC8C-816A34DDF7CC"
        }
        response = requests.get(apiurl, params=params)
        if response.status_code == 200:
            print(response.json())
    if idx == 10:
        print(idx, time.time()-tt)
        break

