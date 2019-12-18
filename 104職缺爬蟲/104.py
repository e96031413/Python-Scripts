from selenium import webdriver
from selenium.webdriver.chrome.options import Options

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


#第一頁內容
driver.get(url) 
with open('result.txt', 'w',encoding='utf-8') as f:
	try:
		for i in range(1,25):

			print('這是第'+ str(i) +'個工作')
			job_company = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[1]/li[2]/a' %(i)).text
			print('公司名稱:' + job_company)
			job_title = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/h2/a' %(i)).text
			print('職缺名稱:' + job_title)
			job_content = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/p' %(i)).text
			print('工作內容:' + job_content)
			job_requirements = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[2]' %(i)).text
			print('工作地點與學經歷:' + '\n' + job_requirements)
			job_salary = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/div/span[1]' %(i)).text
			print('薪水:' + job_salary)
			print('\n')
			target = '這是第'+ str(i) +'個工作' + '\n' + '公司名稱:' + '公司名稱:' + job_company +'\n' + '職缺名稱:' + job_title +'\n' + '工作內容:' + job_content + '\n' + '工作地點與學經歷:' + '\n' + job_requirements + '\n' + '薪水:' + job_salary + '\n\n'
			f.write(target)
	except:
		pass
	driver.close()

	#目前有24個工作
	
	#第2頁內容
	driver = webdriver.Chrome(options=options)

	for num in range(2,3):

		url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=' + keywords + '&order=15&asc=0&page='+ str(num) +'&mode=s&jobsource=2018indexpoc'
		
		try:

			for ii in range(1,25):

				newNUM = ii +24
				driver.get(url)
				print('這是第' + str(newNUM) + '個工作')
				job_company = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[1]/li[2]/a' %(ii)).text
				print('公司名稱:' + job_company)
				job_title = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/h2/a' %(ii)).text
				print('職缺名稱:' + job_title)
				job_content = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/p' %(ii)).text
				print('工作內容:' + job_content)
				job_requirements = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[2]' %(ii)).text
				print('工作地點與學經歷:' + '\n' + job_requirements)
				job_salary = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/div/span[1]' %(ii)).text
				print('薪水:' + job_salary)
				print('\n')
				target = '這是第'+ str(newNUM) +'個工作' + '\n' + '公司名稱:' + '公司名稱:' + job_company +'\n' + '職缺名稱:' + job_title +'\n' + '工作內容:' + job_content + '\n' + '工作地點與學經歷:' + '\n' + job_requirements + '\n' + '薪水:' + job_salary + '\n\n'
				f.write(target)
		
		except:
			pass
			
	
	#第3頁內容			
	driver = webdriver.Chrome(options=options)

	for num in range(3,4):

		url = 'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=' + keywords + '&order=15&asc=0&page='+ str(num) +'&mode=s&jobsource=2018indexpoc'
		
		try:

			for ii in range(1,25):

				newNUM = ii +44
				driver.get(url)
				print('這是第' + str(newNUM) + '個工作')
				job_company = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[1]/li[2]/a' %(ii)).text
				print('公司名稱:' + job_company)
				job_title = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/h2/a' %(ii)).text
				print('職缺名稱:' + job_title)
				job_content = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/p' %(ii)).text
				print('工作內容:' + job_content)
				job_requirements = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/ul[2]' %(ii)).text
				print('工作地點與學經歷:' + '\n' + job_requirements)
				job_salary = driver.find_element_by_xpath('//*[@id="js-job-content"]/article[%d]/div[1]/div/span[1]' %(ii)).text
				print('薪水:' + job_salary)
				print('\n')
				target = '這是第'+ str(newNUM) +'個工作' + '\n' + '公司名稱:' + '公司名稱:' + job_company +'\n' + '職缺名稱:' + job_title +'\n' + '工作內容:' + job_content + '\n' + '工作地點與學經歷:' + '\n' + job_requirements + '\n' + '薪水:' + job_salary + '\n\n'
				f.write(target)
		
		except:
			pass


	driver.close()
