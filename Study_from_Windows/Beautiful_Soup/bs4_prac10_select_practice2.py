from bs4 import BeautifulSoup as bs
import requests as req

resp = req.get('http://v.media.daum.net/v/20170615203441266')
soup = bs(resp.content, 'lxml')

# NOTE : select 함수는 리스트 형태로 전체 변환
title = soup.select('title')[0]
print(title)
print(title.text)

# NOTE : 띄어쓰기가 있다면 하위태그 검색
title2 = soup.select('html head title')[0]
print(title2.get_text())

# NOTE : >를 사용하는 경우 바로 아래의 지식만 검색
title3 = soup.select('html>head>title')[0]
print(title3.get_text())

# NOTE : .은 태그의 클래스 검색
# NOTE : class가 article_view인 태그 검색

body = soup.select('.article_view')[0]
print(type(body), len(body))
for rep in body.find_all('p'):
    print(rep.get_text())

# NOTE : div 태그 중 class가 article_view인 태그 검색
body2 = soup.select('div.article_view')[0]
print(type(body2), len(body2))
for rep in body2.find_all('p'):
    print(rep.get_text())
