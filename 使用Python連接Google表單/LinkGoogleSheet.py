import gspread
from oauth2client.service_account import ServiceAccountCredentials

auth_json_path = 'Python-Connenct-b6c6608e14d5.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']

#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials) 

#開啟 Google Sheet 資料表
spreadsheet_key = '1aCAaNkwOPbWoxjMNBvYoe3KLlTvxjfernR50BTMR43o' 
sheet = gss_client.open_by_key(spreadsheet_key).sheet1

# Google Sheet 資料表
sheet.clear() # 清除 Google Sheet 資料表內容
listtitle=["姓名","電話"]
sheet.append_row(listtitle)  # 標題
listdata=["Liu","0937-1234567"]
sheet.append_row(listdata)  # 資料內容
