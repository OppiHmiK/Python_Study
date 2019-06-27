import urllib.request as req

url = req.urlopen("http://naver.com/") # NOTE : 웹 문서 불러오
status = url.getheaders()기 # NOTE : 웹 서버의 정보 받아오기

for rep in status:
    print(rep)
print(url)
print(url.status)
