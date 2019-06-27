import re

var = re.compile("[ab]") # NOTE : 주어진 패턴을 컴파일하여 정규식 객체로 반환
print(var.search("pizza"))
print(var.match("pizza"))

var2 = re.compile("[pP]")
print(var2.search("apple"))
print(var2.match("apple"))
print(var2.match("apPle"))
print(var2.match("pP"))