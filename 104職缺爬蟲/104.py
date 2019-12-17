from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

keywords = input('請輸入工作職缺關鍵字:')
#keywords = "機器學習"
url = "https://www.104.com.tw/jobs/search/?keyword=" + keywords +"&jobsource=2018indexpoc&ro=0&order=1"

options = Options()
#關閉瀏覽器跳出訊息
prefs = {
    'profile.default_content_setting_values' :
        {
        'notifications' : 2
         }
}
options.add_experimental_option('prefs',prefs)
options.add_argument("--headless")            #不開啟實體瀏覽器背景執行
options.add_argument("--incognito")           #開啟無痕模式

driver = webdriver.Chrome(options=options)


driver.get(url) 

for i in range(1,25):

	job_company = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[1]/li[2]/a' %(i)).text
	print('公司名稱:' + job_company)
	job_title = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/h2/a' %(i)).text
	print('職缺名稱:' + job_title)
	job_requirements = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[2]' %(i)).text
	print('工作地點與學經歷:' + '\n' + job_requirements)
	job_salary = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/div/span[1]' %(i)).text
	print('薪水:' + job_salary)
	print('\n')


	


#print('職缺連結:' + job_link)
#print(job_link.get_text())

#b-block__left