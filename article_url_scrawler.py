>>> import newspaper
>>> cnn_paper = newspaper.build('http://XXXXX.com')
>>> for article in cnn_paper.articles:
>>>     print(article.url)