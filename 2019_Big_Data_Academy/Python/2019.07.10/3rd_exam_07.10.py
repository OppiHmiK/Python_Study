# -*- coding : utf-8 -*-
# NOTE : 집합 자료형

# NOTE
# 집합 자료형은 중복된 값은 저장되지 않는다.
# 집합 자료형은 순서가 없다.

s1 = set([1, 2, 3])
s2 = set('Hello')
print(s1)
print(s2)

l1 = list(s1)
t1 = tuple(s1)
print(s1)
print(l1)
print(t1)

# NOTE
# 집합 자료형은 인덱싱이나 슬라이싱을 할 때 리스트나 튜플로 바꿔서 해야한다.
print(l1[0])
print(t1[:2])

# NOTE : 집합 연산
s3 = set([1, 2, 3, 4, 5, 6])
s4 = set([4, 5, 6, 7, 8, 9])

# NOTE : 교집합
print(s3 & s4)
print(s4.intersection(s4))

# NOTE : 합집합
print(s3 | s4)
print(s3.union(s4))

# NOTE : 차집합
print(s3 - s4)
print(s3.difference(s4))

# NOTE : 집합 관련 함수

# NOTE : 값 1개 추가
s1.add(4)
print(s1)

# NOTE: 값 여러개 추가
s1.update([5, 6, 7])
print(s1)

# NOTE : 값 삭제
s1.remove(7)
print(s1)



#
