from bs4 import BeautifulSoup as bs
import requests as req
import re

resp = req.get('https://news.v.daum.net/v/20170518153405933')
soup = bs(resp.content, 'html5lib')

print(soup.find_all(string = '오대석'))
print(soup.find_all(string = ['[이주의해시태그-#네이버-클로바]쑥쑥 크는 네이버 AI', '오대석']))
print(soup.find_all(string = 'AI'))
print(soup.find_all(string = re.compile('AI'))[0])



