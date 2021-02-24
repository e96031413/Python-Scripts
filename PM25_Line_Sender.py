# -*- coding: UTF-8 -*-
import requests      # 匯入 requests 套件
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://data.epa.gov.tw/api/v1/aqx_p_432?format=csv&limit=85&api_key=9b5bba60-4cfe-4167-8958-cc40337d7ffe'
df = pd.read_csv(url)

i = df[['County','SiteName','AQI']]
i = i.set_index(['County']).loc['臺南市']
print(i)

def send_ifttt(v1):   # 定義函式來向 IFTTT 發送 HTTP 要求
    url = ('https://maker.ifttt.com/trigger/PM2.5_Crawler/with/' +
          'key/OCLxwpzP2IgEnJ7pYrYbD' +
          '?value1='+str(v1))
    r = requests.get(url)      # 送出 HTTP GET 並取得網站的回應資料
    if r.text[:5] == 'Congr':  # 回應的文字若以 Congr 開頭就表示成功了
        print('已傳送 ('+str(v1)+') 到 Line')
    return r.text

ret = send_ifttt(i)  #傳送 HTTP 請求到 IFTTT
print('IFTTT 的回應訊息：',ret)     # 輸出 IFTTT 回應的文字