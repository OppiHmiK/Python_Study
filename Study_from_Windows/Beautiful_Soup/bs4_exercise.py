from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req
import os

resp = req.get('http://media.daum.net/digital/ ')
soup = bs(resp.content, 'lxml')

data = soup.find_all('strong', attrs =  {'class' : 'tit_thumb'})
title = []

for rep in data:
    title.append(rep.text)

pprint(title)