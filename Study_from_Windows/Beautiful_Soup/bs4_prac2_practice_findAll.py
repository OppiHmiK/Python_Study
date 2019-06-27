from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%82%A0%EC%94%A8'
weather = requests.get(url)
soup = bs(weather.text, 'html.parser')

data_1 = soup.find('div', {'class' : 'detail_box'})
data_2 = data_1.findAll('dd') # NOTE : findAll( 해당 태그가 여러개 있을 경우 한꺼번에 반환.
pprint(data_2)
pprint(data_2[0])
pprint(data_2[1])
pprint(data_2[2])
