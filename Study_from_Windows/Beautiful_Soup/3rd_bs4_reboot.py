# -*- coding : utf-8 -*-
from urllib import request as req

# NOTE : 데이터 읽어들이기
url = 'http://api.aoikujira.com/ip/ini'
res = req.urlopen(url)
data = res.read()

# NOTE : 바이너리를 문자열로 변환하기
text = data.decode('utf-8')
print(text)