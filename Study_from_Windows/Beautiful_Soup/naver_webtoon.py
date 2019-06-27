from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

url = 'https://comic.naver.com/webtoon/weekday.nhn'
toon = requests.get(url)
soup = bs(toon.text, 'html.parser')

dic = {'class' : 'col_inner'}
data_1 = soup.find('div', dic)

dic2 = {'class' : 'title'}
data_2 = data_1.findAll('a', dic2)
pprint(data_2)

title = []
for rep in data_2:
    title.append(rep.text)

pprint(title)
