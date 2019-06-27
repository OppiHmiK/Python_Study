import requests as req

client_key = '9PFoWPMafRM5nZmpsEtP'
client_secret = 'CVQqJQDcj_'

# NOTE : 별도 quote_plus() 메서드등 처리할 필요 없음. requests 객체가 알아서 해줌
naver_url = 'https://openapi.naver.com/v1/search/news.json?query=스마트폰'

# NOTE : # headers= header_params 는 header 변경시에만 필요하고, 그렇지 않으면, requests.get(원하는 URL) 만 해도 됨
header_params = {"X-Naver-Client-Id" : client_key, "X-Naver-Client-Secret" : client_secret}
resp = req.get(naver_url, headers = header_params)

if(resp.status_code == 200):
    data = resp.json()
    print(data['items'][0]['title'])
    print(data['items'][0]['description'])

else:
    print("Error Code : " + str(resp.status_code))