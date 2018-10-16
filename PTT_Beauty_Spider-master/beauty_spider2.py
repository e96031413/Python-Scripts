import datetime
import sys
import time

import requests
import urllib3
from bs4 import BeautifulSoup

import download_beauty

urllib3.disable_warnings()
rs = requests.session()


def get_page_number(content):
    start_index = content.find('index')
    end_index = content.find('.html')
    page_number = content[start_index + 5: end_index]
    return int(page_number) + 1


def over18(board):
    res = rs.get('https://www.ptt.cc/bbs/{}/index.html'.format(board), verify=False)
    # 先檢查網址是否包含'over18'字串 ,如有則為18禁網站
    if 'over18' in res.url:
        print("18禁網頁")
        load = {
            'from': '/bbs/{}/index.html'.format(board),
            'yes': 'yes'
        }
        res = rs.post('https://www.ptt.cc/ask/over18', verify=False, data=load)
    return BeautifulSoup(res.text, 'html.parser')


def craw_page(res, push_rate):
    soup_ = BeautifulSoup(res.text, 'html.parser')
    article_seq = []
    for r_ent in soup_.find_all(class_="r-ent"):
        try:
            # 先得到每篇文章的篇url
            link = r_ent.find('a')['href']
            if link:
                # 確定得到url再去抓 標題 以及 推文數
                title = r_ent.find(class_="title").text.strip()
                rate_text = r_ent.find(class_="nrec").text
                url = 'https://www.ptt.cc' + link
                if rate_text:
                    if rate_text.startswith('爆'):
                        rate = 100
                    elif rate_text.startswith('X'):
                        rate = -1 * int(rate_text[1])
                    else:
                        rate = rate_text
                else:
                    rate = 0
                # 比對推文數
                if int(rate) >= push_rate:
                    article_seq.append({
                        'title': title,
                        'url': url,
                        'rate': rate,
                    })
        except Exception as e:
            print('本文已被刪除', e)
    return article_seq


def main():
    # python beauty_spider2.py [版名] [爬蟲起始的頁面] [爬幾頁] [推文多少以上] python beauty_spider2.py beauty -1 3 10
    # board, start_page, page_term, push_rate = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    board, start_page, page_term, push_rate = 'beauty', -1, 5, 10
    start_time = time.time()
    datetime_format = '%Y%m%d%H%M%S'
    crawler_time = '_PttImg_{:{}}'.format(datetime.datetime.now(), datetime_format)
    if start_page == 0:
        print("請輸入有效數字")
        sys.exit()
    # 如為 -1 ,則從最新的一頁開始
    else:
        # 檢查看板是否為18禁,有些看板為18禁
        soup = over18(board)
        all_page_url = soup.select('.btn.wide')[1]['href']
        start_page = get_page_number(all_page_url)

    print("Analytical download page...")
    index_list = []
    article_list = []
    for page in range(start_page, start_page - page_term, -1):
        page_url = 'https://www.ptt.cc/bbs/{}/index{}.html'.format(board, page)
        index_list.append(page_url)

    # 抓取 文章標題 網址 推文數
    while index_list:
        index = index_list.pop(0)
        res = rs.get(index, verify=False)
        # 如網頁忙線中,則先將網頁加入 index_list 並休息1秒後再連接
        if res.status_code != 200:
            index_list.append(index)
            time.sleep(1)
        else:
            article_list += craw_page(res, push_rate)
        time.sleep(0.05)

    total = len(article_list)
    count = 0
    # 進入每篇文章分析內容
    while article_list:
        article = article_list.pop(0)
        res = rs.get(article['url'], verify=False)
        # 如網頁忙線中,則先將網頁加入 index_list 並休息1秒後再連接
        if res.status_code != 200:
            article_list.append(article)
            time.sleep(1)
        else:
            count += 1
            download_beauty.store_pic(crawler_time, article['url'], article['rate'], article['title'])
            print('download: {:.2%}'.format(count / total))
        time.sleep(0.05)

    print("下載完畢...")
    print('execution time: {:.3}s'.format(time.time() - start_time))


if __name__ == '__main__':
    main()
