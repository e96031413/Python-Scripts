# -*- coding: UTF-8 -*-
import requests
import twder
USD=twder.now('USD')
EUR=twder.now('EUR')
CNY=twder.now('CNY')
JPY=twder.now('JPY')
KRW=twder.now('KRW')

def send_ifttt(v1,v2,v3):   # 定義函式來向 IFTTT 發送 HTTP 要求
    url = ('https://maker.ifttt.com/trigger/currency/with/' +
          'key/OCLxwpzP2IgEnJ7pYrYbD' +
          '?value1='+str(v1)+
          '&value2='+str(v2)+
          '&value3='+str(v3))
    r = requests.get(url)      # 送出 HTTP GET 並取得網站的回應資料
    if r.text[:5] == 'Congr':  # 回應的文字若以 Congr 開頭就表示成功了
        print('已傳送 ('+str(v1)+','+str(v2)+','+str(v3)+') 到 Line')
    return r.text

ret = send_ifttt(USD,EUR,CNY)  #傳送 HTTP 請求到 IFTTT
print('IFTTT 的回應訊息：',ret)     # 輸出 IFTTT 回應的文字