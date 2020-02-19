import requests
from bs4 import BeautifulSoup
import concurrent.futures

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

with open('list.txt','r') as url:
    info_urls = [str(line) for line in url.readlines() if line[-2] != 'f']

def bookInfo(info_url):
    resp = requests.get(info_url, headers=headers).text
    soup = BeautifulSoup(resp, 'lxml')
    try:
        for i in range(0, 50):
            bookName = soup.find_all(class_="briefcitTitle")[i]
            content = bookName.text
            print(content)
    except:
        pass

with concurrent.futures.ThreadPoolExecutor() as executor:
    for url in info_urls:
        executor.submit(bookInfo,url)
