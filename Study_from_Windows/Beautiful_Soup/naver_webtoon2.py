from bs4 import BeautifulSoup as bs
import requests as req

url = 'https://comic.naver.com/webtoon/weekday.nhn'
toon = req.get(url).text
soup = bs(toon, 'html.parser')

dic = {'class' : 'col_inner'}
data_1 = soup.findAll('div', dic)

week_title = []

dic2 = {'class' : 'title'}
for rep in data_1:
    data_2 = rep.findAll('a', dic2)
    title = [rep.text for rep in data_2]
    week_title.append(title)

day_dic = {}
day_lis = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']

for rep in range(0, 7):
    day_dic.setdefault(day_lis[rep], week_title[rep])

print(title)
