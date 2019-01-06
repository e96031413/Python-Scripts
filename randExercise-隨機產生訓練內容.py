def getrandom2(n1, n2):  #取得2個不重複的亂數
    while True:
        r1 = random.randint(n1, n2)
        r2 = random.randint(n1, n2)
        if r1 != r2:  #如果兩數不相等就跳出迴圈
            break
    return r1, r2

import os, random
from win32com import client
from win32com.client import constants
word = client.gencache.EnsureDispatch('Word.Application')
word.Visible = 1
word.DisplayAlerts = 0  #不顯示警告
doc = word.Documents.Add()
range1 = doc.Range(0,0)  #檔案開頭
range1.Style.Font.Size = "16"  #字體尺寸
title = "Today's Workout"
year1 = "2019年1月"
week = ["一","二","三","四","五"]
Chest = ['Push-up','Dips','Incline Push-up','Decline Push-up']
Back = ['Pull-up','Chin-up','Barbell Row']
Leg = ['Bodyweight Squat','Squat Jump','Lunge','Deadlift','Bulgarian Split Squat ']
date1= 1  #開始日期為1日
weekday = 2  #開始日期為星期二

while weekday < 8 and date1 < 31:  #週一到週五及30日前才製作菜單
    range1.InsertAfter(title + "\n")
    range1.InsertAfter("日期：" + year1 + str(date1) + "日 (星期" + week[weekday-1] + ")\n")
    range1.InsertAfter("課表：(3 sets of 20 each exercise)\n")
    rand1, rand2 = getrandom2(0,3)  #取得兩個亂數
    range1.InsertAfter(Chest[rand1] + "\n")
    rand1, rand2 = getrandom2(0,2)
    range1.InsertAfter(Back[rand1] + "\n")
    rand1, rand2 = getrandom2(0,4)
    range1.InsertAfter(Leg[rand2] + "\n")
    range1.Collapse(constants.wdCollapseEnd)  #移到range尾
    range1.InsertBreak(constants.wdSectionBreakNextPage)  #換頁
    weekday += 1  #星期加1
    date1 += 1  #日期加1
    if weekday == 6:  #如果是星期六
        weekday = 1  #設為星期一
        date1 += 2  #日期加2(星期六及星期日)
    
cpath=os.path.dirname(__file__)
doc.SaveAs(cpath + "Workout.docx")  #存為<Workout.docx>
