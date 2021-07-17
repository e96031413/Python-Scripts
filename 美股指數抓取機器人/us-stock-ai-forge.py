# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests


# driver_path = r"C:\Users\e96031413\chromedriver.exe"
url ="https://www.cnyes.com/usstock"
options = Options()

prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
options.binary_location = '/usr/bin/chromium-browser'
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument("--headless")            #不開啟實體瀏覽器背景執行



browser=webdriver.Chrome(options=options)
browser.get(url)

DJI = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[1]/td[2]/a").text
DJI_price = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[1]/td[3]/span").text
DJI_scale_price = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[1]/td[4]").text
DJI_scale = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[1]/td[5]/span").text

SP500 = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[3]/td[2]/a").text
SP500_price = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[3]/td[3]/span").text
SP500_scale_price = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[3]/td[4]/span").text
SP500_scale = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[3]/td[5]/span").text

SOX = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[4]/td[2]").text
SOX_price = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[4]/td[3]/span").text
SOX_scale_price = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[4]/td[4]").text
SOX_scale = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[4]/td[5]/span").text

NASDAQ = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[2]/td[2]").text
NASDAQ_price = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[2]/td[3]/span").text
NASDAQ_scale_price = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[2]/td[4]/span").text
NASDAQ_scale = browser.find_element_by_xpath("/html/body/div/div/div[3]/div[9]/div[1]/div/section[2]/div[2]/div/div/table/tbody/tr[2]/td[5]/span").text

content = "\n\n" + DJI + "  ,"+DJI_price + "  ," + DJI_scale_price +  "  ,"+ DJI_scale + "\n\n" + SP500 + "  ,"+ SP500_price + "  ,"+ SP500_scale_price + "  ,"+ SP500_scale + "\n\n" + SOX + "  ,"+ SOX_price + "  ,"+ SOX_scale_price + "  ,"+ SOX_scale + "\n\n" + NASDAQ + "  ," + NASDAQ_price + "  ," + NASDAQ_scale_price + "  ," + NASDAQ_scale
browser.close()

def lineNotifyMessage(token, msg):
    headers = {
          "Authorization": "Bearer " + token, 
          "Content-Type" : "application/x-www-form-urlencoded"
      }
    payload = {'message': msg}
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code
  # 修改為你要傳送的訊息內容
  # 修改為你的權杖內容
token = 'tJD6Z8CharNwEPyAVa5FoMB1JBbN2S4Q9HSuyNtaXXl'
lineNotifyMessage(token, content)
browser.quit()
sys.exit()
