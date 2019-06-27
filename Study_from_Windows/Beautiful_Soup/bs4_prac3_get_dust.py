from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
weather = requests.get(url)
soup = bs(weather.text, 'html.parser')

dic = {'class' : 'detail_box'}
data_1 = soup.find('div', dic)
data_2 = data_1.findAll('dd')
pprint(data_1)
pprint(data_2)

dic2 = {'class' : 'num'}
for rep in range(0, 3):
    find_dust = data_2[rep].find('span', dic2).text
    pprint(find_dust)