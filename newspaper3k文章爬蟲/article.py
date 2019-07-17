from newspaper import Article
URL='https://www.thenewslens.com/article/121889'
article = Article(URL)
article.download()
article.parse()
article.nlp()
print("作者:",article.authors) #作者
print("發文時間:",article.publish_date) #發文時間
#print(article.text) #全文
print("關鍵字:",article.keywords)
print("總結:",article.summary) #總結
