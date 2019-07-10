# -*- coding : utf-8 -*-
# NOTE : 튜플 자료형

# NOTE : 리스트와 튜플의 차이
# 리스트 : 값을 수정, 삭제, 삽입 할 수 있음.
# 튜플 : 값을 수정, 삭제, 삽입 할 수 없음.

# NOTE : 단지 하나의 요소를 가질 때에는 반드시 ,가 있어야함.
tup1 = (1,)
tup2 = 1, 2, 3 # = (1, 2, 3)
tup3 = ('a', 'b', ('ab', 'cd'))
print(tup1)
print(tup2)
print(tup3)

# NOTE : 튜플 인덱싱, 슬라이싱
tup4 = (1, 2, 'a', 'b')
print(tup4[0])
print(tup4[3])

print(tup4[1:])
print(tup4[:2])

# NOTE : 튜플 관련함수

# NOTE : 튜플 더하기
#        튜플에 값을 삽입하는 것은 불가능하지만, 튜플끼리 합치는 것은 가능하다.
tup5 = (3, 4)
print(tup4 + tup5)
# NOTE : 튜플 곱하기
print(tup5*3)
# NOTE : 튜플 요소 개수 구하기
print(len(tup5))

# Ex.
print(tup5 + (1, 2))



