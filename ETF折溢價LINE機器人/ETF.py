# ref: https://stackoverflow.com/questions/58347261/extracting-table-data-using-selenium-and-python-into-pandas-dataframe
import os
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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


base_url = "https://mis.twse.com.tw/stock/etf_nav.jsp?ex=tse"

browser=webdriver.Chrome(options=options)
browser.get(base_url)

time.sleep(3)
html=browser.page_source
soup=BeautifulSoup(html,'html.parser')
div=soup.select_one("div#content")
table=pd.read_html(str(div))
frames = [table[0], table[1], table[3], table[5]]
result=pd.concat(frames,ignore_index=True)

df = result[['Stock Code/Name of Fund','Market Price','Estimated Net Asset Value(Annotation 2)','The Percentage of Estimated Premium/Discount(Annotation 3)']]
df.columns = ['名稱','市價','淨值','折溢價幅度']

# 溢價大於0.5%
premium = df[df["折溢價幅度"] > "0.5%" ].sort_values(by="折溢價幅度", ascending=False).head(10)

# 折價小於-3%
discount = df[df["折溢價幅度"] < "-3%" ].sort_values(by="折溢價幅度", ascending=False).head(10)


fileName_txt = 'temp_etf.txt'
#匯出成文字格式，供後續傳送至LINE
premium.to_csv(fileName_txt, header=True, sep=' ',index=False)

#建立溢價字串保存傳送到LINE的文字資料
send_to_line_premium ="\n溢價\n"
with open(fileName_txt, encoding="utf8") as f:
    for word in f:
        send_to_line_premium += word+"\n"

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
lineNotifyMessage(token, send_to_line_premium)

discount.to_csv(fileName_txt, header=True, sep=' ',index=False)
#建立折價字串保存傳送到LINE的文字資料
send_to_line_discount ="\n折價\n"
with open(fileName_txt, encoding="utf8") as f:
    for word in f:
        send_to_line_discount += word+"\n"

lineNotifyMessage(token, send_to_line_discount)

browser.quit()
os.remove(fileName_txt)
