# -*- coding : utf-8 -*-

from urllib import request as req
import os

# NOTE : URL과 저장 경로 지정
url = 'http://uta.pw/shodou/img/28/214.png'
savename = 'test.png'
if not os.path.isdir('data'):
    os.mkdir('data')
os.chdir('data')

# NOTE
# urlretrieve : url내에 있는 파일 다운로드
req.urlretrieve(url, savename)
print('File Saved!')


