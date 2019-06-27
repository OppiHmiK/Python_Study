# -*- coding : utf-8 -*-

from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req
import os

try:
    url = 'https://land.naver.com/isale/isaleNewsTrend.nhn'
    html = req.get(url)
    soup = bs(html.text, 'html.parser')

    if not os.path.isdir('datas'):
        os.mkdir('datas')
    os.chdir('datas')

    data = soup.find_all('h4', 'h_trend')


    head_line = ''
    for rep in data:
        head_line += rep.text
        head_line += '\n'

    with open('test.txt', 'w') as text:
        text.write(head_line)

    print('File Saved!')

    url_2 = 'https://comic.naver.com/webtoon/weekday.nhn'
    html_2 = req.get(url_2)
    soup_2 = bs(html_2.text, 'html.parser')

    data_2 = soup_2.find('div', {'class' : 'col_inner'})
    data_xnxn = data_2.find_all('a', 'title')
    title = ''

    for rep in data_xnxn:
        title += rep.text
        title += '\n'

    with open('text_2.txt', 'w') as text_2:
        text_2.write(title)

    print('File saved!')

except NameError as e:
    print(e)