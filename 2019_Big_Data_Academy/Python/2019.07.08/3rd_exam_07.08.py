# -*- coding : utf-8 -*-
# NOTE : 리스트 자료형
a = []
b = [1, 2, 3]
c = ['Life', 'is', 'too', 'short']
d = [1, 2, ['Life', 'is']]

# NOTE : 리스트 인덱싱
x = [1, 2, 3]
print(x)
print(x[0])
print(x[0] + x[2])
print(x[-1])

# NOTE : 리스트 슬라이싱
y = [1, 2, 3, 4, 5]
print(y[0:4])
print(y[:3])
# !CAUTION! : 리스트 슬라이싱 할 때 a[x:y]라 하면,
#             x부터 y까지가 아니라, x부터 y-1까지다.
print(y[2:])

# NOTE : 리스트 연산
print(x+y)
print(x*3)
print(len(x))

z = [1, 2, 3, 4, 5, 6]
print(len(z))

# NOTE : 리스트 수정, 삭제
x[2] = 4
print(x)

del x[2]
print(x)

w = [1, 2, 3] * 2
w.remove(3)
print(w)

# NOTE : pop은 매개변수로 인덱스 번호를 받음.
w.pop(3)
print(w)

# NOTE : 리스트에 요소추가
v = [1, 2, 3]
v.append(4)
print(v)

v.append([5, 6])
print(v)
print(v[4][0])

# NOTE
# insert : 매개변수로 삽입할 위치와 값을 받음.
v.insert(0, 4)
print(v)

# NOTE
# extend : 매개변수로 리스트만 올 수 있음.
a2 = [1, 2, 3]
a2.extend([4, 5])
print(a2)

b2 = [6, 7]
a2.extend(b2)
print(a2)

# NOTE : 리스트 정렬
v2 = [1, 3, 4, 6, 5, 7, 9, 0]
v2.sort()
print(v2)

# NOTE : 리스트 뒤집기
v3 = ['a', 'b' ,'c']
v3.reverse()
print(v3)

# NOTE : 특정 요소의 인덱스 반환
print(v2.index(4))
print(v2.index(0))
