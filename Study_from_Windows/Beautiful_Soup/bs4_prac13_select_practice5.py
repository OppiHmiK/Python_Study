from bs4 import BeautifulSoup as bs
import requests as req
import re

resp = req.get('http://land.naver.com/article/divisionInfo.nhn?rletTypeCd=A01&tradeTypeCd=A1&hscpTypeCd=A01%3AA03%3AA04&cortarNo=1168000000&articleOrderCode=&cpId=&minPrc=&maxPrc=&minWrrnt=&maxWrrnt=&minLease=&maxLease=&minSpc=&maxSpc=&subDist=&mviDate=&hsehCnt=&rltrId=&mnex=&siteOrderCode=&cmplYn=')
soup = bs(resp.content, 'lxml')

# NOTE : a 태그면서 href 속성 값이 특정 값을 갖는 경우 탐색
link_title = soup.select('#depth4Tab0Content > div > table > tbody > tr > td.align_l.name > div > a.sale_title')
link_price = soup.select('#depth4Tab0Content > div > table > tbody > tr > td.num.align_r > div > strong')

for rep in range(len(link_price)):
    print(link_title[rep].get_text(),  link_price[rep].get_text())