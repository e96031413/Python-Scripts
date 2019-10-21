#!usr/bin/env python3

#coding:utf-8

base = 'https://www.bilibili.com/video/av6785636?p=' #基础 URL

urls = [base + str(page) for page in range(1, 31)] #列表解析式生成页数 

# 以「写入」模式（write）和「UTF-8」的编码格式打开一个文本，

# 并将所有连接以换行符进行分隔保存进一个.txt 文档中

with open('urls.txt', mode='w', encoding='utf-8') as f:

    f.write('\n'.join(urls))