import requests
import time
import pyautogui
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()

#關閉瀏覽器跳出訊息
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
options.add_argument("--incognito")           #開啟無痕模式
driver_path =r'C:\Users\Administrator\chromedriver.exe'
driver = webdriver.Chrome(driver_path,options=options)

driver.get("https://www.suggestmemovie.com/") 

#用xpath找電影名稱、簡介、IMDB的評分
MovieName = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[1]/div[1]').text
Description = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/div[1]/div[2]/p').text
score = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/h1').text

#用PyAutoGUI到Youtube取得預告片網址
driver.get("https://www.youtube.com/results?search_query=" + MovieName +" trailer") 

time.sleep(3)
num_seconds = 0.5
moveToX = 549
moveToY=328
pyautogui.leftClick(x=moveToX, y=moveToY)

#取得電影預告片網址
url = driver.current_url

#把電影名稱、簡介、IMDB的評分以及預告片網址保存到content變數
content = "\n"+"\n"+"電影名稱:" + MovieName + "\n" + "IMDB分數:"+ score + "\n" + "電影簡介:" + Description + "\n" + "預告片連結:" + url
driver.close()

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
token = 'XXXXXXXXXXXXXXX'
lineNotifyMessage(token, content)

sys.exit()