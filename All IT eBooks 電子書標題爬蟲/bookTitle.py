import requests
from bs4 import BeautifulSoup
import concurrent.futures

info_urls = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

for i in range(1,5): #第1頁到第831頁
    i=str(i)           #轉成字串
    url="http://www.allitebooks.org/page/"+i
    info_urls.append(url)


def crawler(url):
    resp = requests.get(url,headers=headers)
    soup = BeautifulSoup(resp.text, 'lxml')
    titles = soup.find_all('h2')
    for t in titles:
        print(t.string)


with concurrent.futures.ThreadPoolExecutor() as executor:
    for url in info_urls:
        executor.submit(crawler,url)