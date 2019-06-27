from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests as req
import re


url = 'https://news.naver.com/main/read.nhn?m_view=1&includeAllCount=true&mode=LPOD&mid=sec&oid=001&aid=0010863755&isYeonhapFlash=Y&rc=N'
oid = url.split("oid=")[1].split("&")[0]
aid = url.split("aid=")[1]
page = 1
header = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    "referer": url,

}
List = []
while True:
    c_url = "https://apis.naver.com/commentBox/cbox/web_neo_list_jsonp.json?ticket=news&templateId=default_society&pool=cbox5&_callback=jQuery1707138182064460843_1523512042464&lang=ko&country=&objectId=news" + oid + "%2C" + aid + "&categoryId=&pageSize=20&indexSize=10&groupId=&listType=OBJECT&pageType=more&page=" + str(
        page) + "&refresh=false&sort=FAVORITE"
    # 파싱하는 단계입니다.
    r = req.get(c_url, headers=header)
    cont = bs(r.content, "html.parser")
    total_comm = str(cont).split('comment":')[1].split(",")[0]

    match = re.findall('"contents":([^\*]*),"userIdNo"', str(cont))
    # 댓글을 리스트에 중첩합니다.
    List.append(match)
    # 한번에 댓글이 20개씩 보이기 때문에 한 페이지씩 몽땅 댓글을 긁어 옵니다.
    if int(total_comm) <= ((page) * 20):
        break
    else:
        page += 1


# 여러 리스트들을 하나로 묶어 주는 함수입니다.
def flatten(l):
    flatList = []
    for elem in l:
        # if an element of a list is a list
        # iterate over this list and add elements to flatList
        if type(elem) == list:
            for e in elem:
                flatList.append(e)
        else:
            flatList.append(elem)
    return flatList


# 리스트 결과입니다.
pprint(flatten(List))