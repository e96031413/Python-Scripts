import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
import scrapetube

df=pd.read_csv("LexFriedmanClips.csv",delimiter="\t", index_col=0)

if len(df)>5:
	pass
else:
	AllVideoList = []
	videos = scrapetube.get_channel("UCJIfeSCssxSC_Dhc5s7woww")

	titleList = []
	urlList = []
	notDONE=True
	while notDONE:
	    try:
	        info = videos.__next__()
	        titleList.append(info['title']['runs'][0]['text'])
	        urlList.append("https://www.youtube.com/watch?v="+str(info['videoId']))
	    except:
	        data = {'title': titleList, 'url': urlList}
	        df = pd.DataFrame(data=data)
	        df.to_csv("LexFriedmanClips.csv", sep='\t', encoding='utf-8')
	        notDONE=False
	df=pd.read_csv("LexFriedmanClips.csv",delimiter="\t", index_col=0)

video=df.sample(5)
df=df.drop(video.index)
df.to_csv("LexFriedmanClips.csv", sep='\t', encoding='utf-8')

title_list = video['title'].values.tolist()
url_list = video['url'].values.tolist()
all_list = [ i[0]+ ' '+(i[1]) for i in zip(title_list,url_list)] 
content = MIMEMultipart()  #建立MIMEMultipart物件
content["subject"] = "5個LexFriedmanClips的影片"  #郵件標題
content["from"] = "e96031413@gmail.com"  #寄件者
content["to"] = "e96031413@gmail.com" #收件者
content.attach(MIMEText('\n'.join(all_list)))  #郵件內容

with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    try:
        smtp.ehlo()  # 驗證SMTP伺服器
        smtp.starttls()  # 建立加密傳輸
        smtp.login("e96031413@gmail.com", "jstbzqallxdqojyt")  # 登入寄件者gmail
        smtp.send_message(content)  # 寄送郵件
        print("Complete!")
    except Exception as e:
        print("Error message: ", e)