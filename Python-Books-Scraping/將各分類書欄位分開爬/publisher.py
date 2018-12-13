from selenium import webdriver
import sys
from html.parser import HTMLParser

#-------------------------------------------
# 定義裁切字串function
#-------------------------------------------
def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def find_between_r( s, first, last ):
    try:
        start = s.rindex( first ) + len( first )
        end = s.rindex( last, start )
        return s[start:end]
    except ValueError:
        return ""



#-------------------------------------------
# 讀取一個網頁內容
#-------------------------------------------
driver = webdriver.Chrome("chromedriver.exe")


#-------------------------------------------
# 定義一個HTML解譯類別
#-------------------------------------------
class MyHTMLParser(HTMLParser):
    printed=False
    counter=0

    output=''
    author=''

    def handle_starttag(self, tag, attrs):
        if self.printed:
            if tag=='a':
                self.counter=self.counter+1

    def handle_endtag(self, tag):
        if self.printed:
            if tag=='a':
                self.counter=self.counter-1
                if self.counter<=0:
                    self.printed=False

    def handle_data(self, data):
        if (data=='出版社：'):
            self.printed=True
            self.counter=0
            self.output=data
            data=''

        if self.printed:
            if data.strip() != '':
                if self.output=='出版社：':
                    self.author=self.author + data

    def get_author(self):
        return self.author





#-------------------------------------------
# 依序讀入資料庫內容
#-------------------------------------------
cnt=0
bookNo=[
'0010773895',
'0010771883',
'0010772144',
'0010265959',
'0010774599',
'0010782277',
'0010783265',
'0010774599',
'0010763289',
'0010781263',
'0010599171',
'0010781401',
'0010778411',
'0010265959',
'0010265959',
'0010771691',
'0010777877',
'0010555924',
'0010748366',
'0010778411',
'0010771691',
'0010777877',
'0010779721',
'0010779473',
'E050011085',
'0010770173',
'0010783396',
'0010783520',
'0010712618',
'0010785321',
'0010770712',
'0010265959',
'0010780154',
'0010769119',
'0010145681',
'0010772046',
'0010788012',
'0010690480',
'0010777087',
'0010783097',
'0010776000',
'0010265959',
'0010628474',
'0010784047',
'0010740318',
'0010265959',
'0010682095',
'0010717513',
'0010752196',
'0010518069',
'0010691344',
'0010780491',
'0010711386',
'0010748366',
'0010751505',
'0010770968',
'0010775212',
'CN11303027',
'0010759776',
'0010673287',
'0010717513',
'0010774043',
'0010777378',
'0010720233',
'0010741631',
'0010781263',
'0010776519',
'0010765697',
'0010783091',
'0010491446',
'0010771655',
'0010518018',
'0010672316',
'0010741146',
'0010780852',
'0010783451',
'0010354855',
'0010753613',
'0010723525',
'0010733588',
'0010701408',
'0010744267',
'0010651114',
'0010780461',
'0010782325',
'0010783718',
'0010783268',
'0010748366',
'0010265959',
'0010565992',
'0010748366',
'0010748662',
'0010781914',
'0010549640',
'0010730394',
'0010730385',
'0010775380',
'0010780561',
'0010780839',
'0010781814'
]

for number in bookNo:
    try:
        driver.get('http://www.books.com.tw/products/' + number)  # 輸入範例網址，交給瀏覽器
        pageSource = driver.page_source  # 取得網頁原始碼
        outputPage=pageSource.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding)

        # 取出內容/作者/目錄/簡介
        parser = MyHTMLParser()
        parser.feed(outputPage)

        author=parser.get_author()

        # 開啟檔案
        fp = open("publisher.txt", "a")

        fp.write(author + '\n')

        # 關閉檔案
        fp.close()


        cnt=cnt+1
        print(cnt)

        print(author)
        print('-'*50)

    except:
        pass




#-------------------------------------------
# 結尾處理
#-------------------------------------------
driver.close()  # 關閉瀏覽器



