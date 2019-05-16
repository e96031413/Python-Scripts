import requests
from bs4 import BeautifulSoup
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}

with open('list.txt') as url:
	for urls in url:
		resp = requests.get(urls, headers=headers) 
		resp.encoding = 'utf8'
		soup = BeautifulSoup(resp.text, 'lxml')
		bookName=soup.find_all(class_="briefcitTitle")
		print(bookName)