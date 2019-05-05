#!/user/bin/env python
# -*- coding:utf-8 -*-
# Author:DavidChen
import requests
from bs4 import BeautifulSoup
import time
import getpass
import os

# 信息
img_link = []
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.mzitu.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8'
}

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
'''
    获取各图片详情页的链接
    :return first_link 详情页链接列表
'''
def get_first_link():
    print("开始爬取详情页链接....")
    begin = time.time()
    wb_content = requests.get(url, headers=headers).text
    soup = BeautifulSoup(wb_content, 'lxml')
    img_list = soup.select('#pins > li > a')
    first_link = []
    for item in img_list:
        link = item.get('href')
        first_link.append(link)
    print("爬取详情页链接完毕， 用时:", time.time() - begin, "秒")
    return first_link

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
'''
    获取详情页的图片链接
'''
def get_img_link():
    print("开始爬取图片链接....")
    begin = time.time()
    page_link = get_first_link()
    for link in page_link:
        content = requests.get(link, headers=headers).text
        soup = BeautifulSoup(content, 'lxml')
        page_count = int(soup.select('body > div.main > div.content > div.pagenavi > a:nth-child(7) > span')[0].get_text())
        links = soup.select('body > div.main > div.content > div.main-image > p > a > img')
        img_link.append(links[0].get('src'))
        link_title = links[0].get('src')[0:33]
        for i in range(2, page_count):
            if i < 10:
                img_link.append(link_title + "0" + str(i) + ".jpg")
            else:
                img_link.append(link_title + str(i) + ".jpg")

    print("爬取图片链接完毕， 用时:", time.time() - begin, "秒\n= = = = = = = = = = = = = = = = = = = = = = = = =")
    return img_link

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
'''
    下载图片
'''
def download_img():
    begin = time.time()
    get_img_link()
    print("开始下载图片....共", len(img_link), "个图片")
    for index, item in enumerate(img_link):
        img_bytes = requests.get(item, headers=headers)
        rel_img = img_bytes.content
        with open(make_dir() + item[-17:].replace("/", "", 6), "wb") as img:
            img.write(rel_img)
        print("\r下载进度: {:.2f}%".format(index / (len(img_link) - 1) * 100), end="")
    print("\n图片下载完毕! 共下载了", len(img_link), "张图片\n总耗时:", time.time() - begin, "秒\n= = = = = = = = = = = = = = = =\n程序运行完毕 @_@\n")

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
'''
    创建存放图片的文件夹
'''
def make_dir():
    path = "C:/Users/" + getpass.getuser() + "/Desktop/Your_Lady/"
    isexists = os.path.exists(path)
    if not isexists:
        os.makedirs(path)
    else:
        pass
    return path

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
'''
    程序主入口
'''
if __name__ == "__main__":
    urls = [
        "https://www.mzitu.com/xinggan/",
        "https://www.mzitu.com/xinggan/",
        "https://www.mzitu.com/japan/",
        "https://www.mzitu.com/taiwan/",
        "https://www.mzitu.com/mm/",
    ]
    print("选择类型 >>>")
    print("1. 首页\n2.性感妹子\n3.日本妹子\n4.台湾妹子\n5.清纯妹子")
    choice = input(">>> ")
    try:
        if int(choice) in [1, 2, 3, 4, 5]:
            url = urls[int(choice) - 1]
            download_img()
            choice = input("是否打开图片文件夹? Y/N >>>")
            if choice == "Y" or choice == "y":
                os.system("start " + make_dir())
    except ValueError:
        print("请输入正确的选项.....")
        input()

