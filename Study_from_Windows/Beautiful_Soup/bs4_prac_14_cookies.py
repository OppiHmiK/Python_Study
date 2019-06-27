# -*- coding : utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests as req

resp = 'http://www.hanbit.co.kr/member/login_proc.php'

user = ''
pw = ''

# NOTE : requests.session 메소드는 해당 requests를 사용하는 동안 cookie를 header에 유지하도록 하여
#        세션이 필요한 HTTP 요청에 사용.

params = dict()
params['m_id'] = user
params['m_pw'] = pw

