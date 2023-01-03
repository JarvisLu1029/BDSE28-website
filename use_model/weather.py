import requests
import json
from pprint import pprint # 不會只有一列，方便看
import statistics
import datetime
import pandas as pd
import openpyxl

# 取得當前日期
today = datetime.datetime.today().date()
print(today)

# 計算隔天日期
# tomorrow = today + datetime.timedelta(days=1)

def population(loc):
    df = pd.read_excel('C:/Users/student/Desktop/my_project/111年09月 ( 鄉鎮市區 )人口密度.xlsx')
    x = df.loc[df['地區']==f'{loc}',['人口密度'][0]]
    return x

# https://www.visualcrossing.com
def weatherAPI(a1):
    # 密鑰
    key = '4KD3GK5WQ8HX23YXVEVS3ZYPM'
    # 單位
    unitGroup = 'metric'
    # 語言
    lang = 'zh'
    # 需求資料
    include = 'hours'
    # 元素
    elements = 'datetime,pressure,humidity,temp,winddir,windspeed'

    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{a1}/{today}/{today}?key={key}&unitGroup={unitGroup}&lang={lang}&include={include}&elements={elements}"


    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = json.loads(response.text)
        pprint(f"查詢日期 = {data['days'][0]['datetime']}")
        pprint(f"濕度(%) = {data['days'][0]['humidity']}")
        pprint(f"大氣壓力(hPa) = {data['days'][0]['pressure']}")
        pprint(f"溫度(°C) = {data['days'][0]['temp']}")
        pprint(f"風向(°) = {data['days'][0]['winddir']}")
        pprint(f"風速(km/h) = {data['days'][0]['windspeed']}")
        print('-'*10)
