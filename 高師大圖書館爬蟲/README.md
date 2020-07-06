# **爬取高師大108年度購買的新書**

## **2020/07/01已失效**
目前學校已禁止校外人士使用查詢系統，必須搭配校內VPN使用，故此爬蟲已無作用

需在list.txt中存入網址

```python
import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

with open('list.txt') as url:
    for urls in url:
        resp = requests.get(urls, headers=headers).text 
        soup = BeautifulSoup(resp, 'lxml')
        try:
        	for i in range(0,50):
        		bookName=soup.find_all(class_="briefcitTitle")[i]
        		content=bookName.text
        		print(content)
        except:
        	pass
```