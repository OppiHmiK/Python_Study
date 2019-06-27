from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

url = requests.get('https://search.naver.com/search.naver?query=날씨') # NOTE : 특정 웹페이지에 요청하는 코드
#pprint(url.text) NOTE : pprint( 리스트나 딕셔너리의 데이터가 너무 길 경우에 편하게 볼 수 있도록 해줌.
soup = bs(url.text,'html.parser') # NOTE : html이라는 언어를 파이썬에서 사용하기 쉽게 변환
# pprint(soup)

# NOTE : html은 태그(div), 속성(class), 속성값(detail_box)으로 구성

data_1 = soup.find('div', {'class' : 'detail_box'}) # NOTE : find(html에서 원하는 태그를 하나만 반환함.)
pprint(data_1)