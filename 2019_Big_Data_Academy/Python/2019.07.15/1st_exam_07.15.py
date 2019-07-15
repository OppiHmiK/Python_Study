# -*- coding : utf-8 -*-
# NOTE : 조건문


money = True

if money:
    print('택시를 타고 가라.')
else:
    print('걸어가라.')

x = 3; y = 2
print(x > y)
print(x < y)
print(x == y)
print(x != y)
print(x >= y)
print(x <= y)

have_money = 2000

if have_money >= 3000:
    print('택시를 타고 가라.')
else:
    print('걸어가라.')

x = True; y = False
print(x or y)
print(x and y)
print(not x)

card = True

if money > 3000 or card:
    print('택시')
else:
    print('걸어')

print(1 in [1, 2, 3])
print(4 in [1, 2, 3])

print(1 not in [1, 2, 3])
print(4 not in [1, 2, 3])

print('a' in ('a', 'b', 'c'))
print('j' in 'python')

pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket:
    print('택시')
else:
    print('걸어')

if 'card' in pocket:
    print('버스')
else:
    print('걸어')
