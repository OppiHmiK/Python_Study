from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req

url = 'https://comic.naver.com/webtoon/weekday.nhn'
toon = req.get(url)
soup = bs(toon.text, 'html.parser')

dic = {'class' : 'col_inner'}
data = soup.findAll('div', dic)

toon = []

for rep in data:
    toon.extend(rep.findAll('li'))

for rep in toon:
    img = rep.find('img')
    title = img['title']
    img_src = img['src']
    print(title, img_src)
