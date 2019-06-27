# -*- coding : utf-8 -*-

from bs4 import BeautifulSoup as bs
import requests as req


url = 'https://search.naver.com/search.naver?where=nexearch&query=%EA%B0%84%EC%84%B1&ie=utf8&sm=whl_lve'
html = req.get(url).text
soup = bs(html, 'html.parser')

print(soup.select('#nxfr_htp > div.realtime_srch._aside_news_tab > ol:nth-child(3) > li:nth-child(1) > a > span > span'))

data = soup.select('#nxfr_htp > div.realtime_srch._aside_news_tab > ol:nth-child(3) > li > a > span > span')
for rep in data:
    print(rep.text)