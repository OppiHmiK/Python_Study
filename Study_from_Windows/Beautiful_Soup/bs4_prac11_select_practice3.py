from bs4 import BeautifulSoup as bs
import requests as req
import re

resp = req.get('https://news.v.daum.net/v/20170615203441266')
soup = bs(resp.content, 'lxml')

# NOTE : div 태그 중 id가 harmonyContainer인 태그 검색
container = soup.select('#harmonyContainer')

# NOTE : div 태그 중 id가 mArticle인 태그의 하위 태그 중 아이디가 article_title인 태그 검색
title = soup.select('div#mArticle div#harmonyContainer')[0]
print(title.get_text())

