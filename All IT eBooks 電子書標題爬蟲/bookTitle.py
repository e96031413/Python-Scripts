import requests
from bs4 import BeautifulSoup
import concurrent.futures

import requests
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

info_urls = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

for i in range(1,2): #第1頁
    i=str(i)           #轉成字串
    url="https://allitbooks.net/page-"+i +".html"
    info_urls.append(url)

def crawler(url):
    global text
    text =''
    resp = requests.get(url,headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    titles = soup.find_all('h2')
    for t in titles:
        # print(t.string)
        text += t.string+'\n'

with concurrent.futures.ThreadPoolExecutor() as executor:
    for url in info_urls:
        executor.submit(crawler,url)

def send_ifttt(v1):   # 定義函式來向 IFTTT 發送 HTTP 要求
    url = ('https://maker.ifttt.com/trigger/PM2.5_Crawler/with/' +
          'key/OCLxwpzP2IgEnJ7pYrYbD' +
          '?value1='+str(v1))
    r = requests.get(url)      # 送出 HTTP GET 並取得網站的回應資料
    if r.text[:5] == 'Congr':  # 回應的文字若以 Congr 開頭就表示成功了
        print('已傳送 ('+str(v1)+') 到 Line')
    return r.text

ret = send_ifttt(text)  #傳送 HTTP 請求到 IFTTT
print('IFTTT 的回應訊息：',ret)     # 輸出 IFTTT 回應的文字