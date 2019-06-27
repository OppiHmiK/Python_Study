import urllib.request as req

url = 'https://news.naver.com'
request = req.Request(url)
news = req.urlopen(request).read()

with open("naver_news.txt", "wb") as data:
    data.write(news)