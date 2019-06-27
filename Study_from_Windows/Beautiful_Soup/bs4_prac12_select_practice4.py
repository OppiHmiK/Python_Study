from bs4 import BeautifulSoup as bs
import requests as req
import re

resp = req.get('http://media.daum.net/economic/')
soup = bs(resp.content, 'lxml')

# NOTE : a태그이면서 href 속성을 갖는 경우 탐색, 리스트 타입으로 links 변수에 저장.
links = soup.select('a[href]')

for rep in links:
    if re.search('https://\w+', rep['href']): # NOTE : https:// 문자열 이후에 숫자 또는 문자 [a-zA-Z0-9_]가 한 개 이상 있는 데이터와 매치됨.
        print(rep['href'])

