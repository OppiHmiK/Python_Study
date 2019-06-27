# -*- coding : utf-8 -*-
from urllib import request as req
from urllib import parse as par

API = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'

# NOTE : 매개변수 URL 인코딩
# NOTE : stnld 기상정보를 알고 싶은 지역 지정
# NOTE
# 지역번호 : 전국 108, 서울/경기도 109, 강원도 105, 충북 131, 충남 133
#          전북 146, 전남 156, 경북 143, 경남 159, 제주 184

val = { 'stnld' : '108' }
params = par.urlencode(val)

# NOTE : 요청 전용 URL생성
# NOTE : URL 끝 부분에 "?"을 입력하고, "<key> = <value>" 값으로 매개변수 작성.
#        여러개의 매개변수를 사용할 경우에는 ?대신에 &를 사용
url = API + "?" + params
print("url = ", url)

data = req.urlopen(url).read()
text = data.decode('utf-8')
print(text)