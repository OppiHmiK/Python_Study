from bs4 import BeautifulSoup as bs
from urllib.request import urlretrieve as urlr
import os, re, requests as req


url = 'https://comic.naver.com/webtoon/weekday.nhn'
toon = req.get(url)
soup = bs(toon.text, 'html.parser')

dic = {'class' : 'col_inner'}
data = soup.findAll('div', dic)

toon_list = []

for rep in data:
    toon_list.extend(rep.findAll('li'))

if not os.path.isdir('toon_photos'):
    os.mkdir('toon_photos')
os.chdir('toon_photos')

for rep in toon_list:
    imge = rep.find('img')
    title = imge['title']
    imge_src = imge['src']
    title = re.sub('[^0-9a-zA-Zㄱ-힗]', '', title) # NOTE : 숫자, 알파벳, 한국어가 아닌것은 제거
    print(title, imge_src)
    urlr(imge_src, title+'.jpg')


