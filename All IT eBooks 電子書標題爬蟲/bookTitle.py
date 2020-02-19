import requests
from bs4 import BeautifulSoup
import concurrent.futures

def crawler():
    for i in range(1,5): #第1頁到第831頁
        i=str(i)           #轉成字串
        url="http://www.allitebooks.org/page/"+i
        #print(url)
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'lxml')
        titles = soup.find_all('h2')
        for t in titles:
            print(t.string)

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.submit(crawler)