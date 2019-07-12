# Ex. 1
grade = {'국어' : 80, '영어' : 75, '수학' : 55}
mean = sum(grade.values()) / len(grade)
print(f'홍길동 씨의 평균 점수는 {mean:1.1f}점입니다. \n')

# Ex. 2
print(f'{13%2} << 1이면 홀수, 0이면 짝수 \n')

# Ex. 3, 4
pin = '881120-1068234'
yymmdd = pin[:6]
num = pin[7:]
print(f'생년월일 : {yymmdd}')
print(f'식별번호 : {num}')
print(f'성별번호 : {pin[7]} \n')

# Ex. 5
a = 'a:b:c:d'
b = a.replace(':',"#")
print(b, '\n')

# Ex. 6
l1 = [1, 3, 5, 4, 2]
l1.sort()
l1.reverse()
print(l1, '\n')

# Ex. 7
l2 = ['Life', 'is', 'too', 'short']
res1 = ' '.join(l2)
print(res1)
print(''.join(l2), '\n')

# Ex. 8
t1 = (1, 2, 3)
t1 = t1 + (4, )
print(t1, '\n')

# Ex. 9
d1 = {'A' : 90, 'B' : 80, 'C' : 70}
res2 = d1.pop('B')
print(d1)
print(res2, '\n')

# Ex. 10
l3 = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
s1 = set(l3)
l4 = list(s1)
print(l4, '\n')

# Ex. 11
a = b = [1, 2, 3]
a[1] = 4
print(b, '\n')

# NOTE
# a와 b의 메모리 번지수가 동일하므로, a안의 원소 값을 바꾸면 b의 원소도 바뀐다.
print(id(a))
print(id(b))



