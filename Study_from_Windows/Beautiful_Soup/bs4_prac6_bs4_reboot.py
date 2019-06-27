from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

# NOTE : requests 라이브러리를 활용한 HTML 페이지 요청
# NOTE : resp 객체에 HTML 데이터가 저장되고, res.content로 데이터 추출
resp = req.get('http://v.media.daum.net/v/20170615203441266')

# pprint(resp.content)

# NOTE : HTML 페이지 파싱
soup = bs(resp.content, 'lxml')
title = soup.find('title') # NOTE : 필요한 데이터 검색
print(title.get_text())
