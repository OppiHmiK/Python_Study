import urllib.request as req

url = req.urlopen("http://naver.com/")
print(url.read()) # NOTE : 웹 페이지의 HTML 코드 출력