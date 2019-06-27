from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req
import re

url = 'https://movie.naver.com/movie/running/current.nhn#'
movie = req.get(url)
soup = bs(movie.text, 'html.parser')

dic1 = {'class' : 'lst_detail_t1'}
data_1 = soup.find('ul', dic1)

dic2 = {'class' : 'tit'}
data_2 = data_1.findAll('dt', dic2)

title = []

for rep in data_2:
    rep = rep.text
    rep = rep.replace('\n', '')
    rep = rep.replace('관람가', '')
    rep = rep.replace('전체', '')
    rep = rep.replace('세', '')
    rep = re.sub('[0-9]','', rep)
    title.append(rep)
pprint(title)