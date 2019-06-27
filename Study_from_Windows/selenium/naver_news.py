from bs4 import BeautifulSoup as bs
from selenium import webdriver

driver = webdriver.Chrome('chromedriver')
news = driver.get('https://news.naver.com/main/ranking/read.nhn?mid=etc&sid1=111&rankingType=popular_day&oid=001&aid=0010866313&date=20190603&type=1&rankingSeq=1&rankingSectionId=102')
soup = (news.text, 'html.parser')
driver.implicitly_wait(300)

data = soup.findAll('span', {'class' : 'u_cbox_contents'})

print(data)