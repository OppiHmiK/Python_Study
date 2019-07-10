# -*- coding : utf-8 -*-
# NOTE : bool 자료형, 변수

# NOTE : bool 연산
print(bool([1, 2, 3]))
print(bool([]))

print(bool(3))
print(bool(0))

# NOTE : 변수
l1 = [1, 2, 3]
# NOTE : 메모리 번지
print(id(l1))

# NOTE : 리스트 복사
l2 = l1
print(id(l2))
print(l1 is l2)

l3 = l1[:]
print(l1 is l3)

# NOTE : copy 모듈
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a, b)
print(id(a), id(b))

