from selenium import webdriver
import time
url='https://search.books.com.tw/search/query/cat/1/qsub/001/key/python/sort/5/c/0'

browser = webdriver.Firefox()
browser.set_window_size(1200,4500)
browser.get(url) # Load page
browser.save_screenshot('books.png')
browser.close()
