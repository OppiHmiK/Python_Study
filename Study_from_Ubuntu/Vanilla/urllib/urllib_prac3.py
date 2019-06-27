import urllib.parse as parse

def input_query():
    query = str(input("검색어를 입력하세요 : "))
    return "&query = " + query

def input_que():
    query = parse.quote_plus(str(input("검색어를 입력하세요 : "))) # NOTE : url의 한국어 검색어 처리
    return "&query = " + query

print(input_query())
print(input_que())