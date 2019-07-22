# -*- coding : utf-8 -*-

# Ex.1
rep = 0
while rep < 10:
    rep += 1
    print(rep, end = ' ')

print('\n')
# Ex.2
for rep in range(5, 16):
    print(rep, end = ' ')

print('\n')
# Ex.3
for rep in range(10, 0, -1):
    print(rep, end = ' ')

print('\n')
# Ex.4
sum = 0
for rep in range(1, 101):
    if rep % 2 == 0:
        sum += rep
print(sum)

print('\n')
# Ex.5
in_num = int(input('정수 : '))
sum_2 = 0
for rep in range(1, in_num + 1):
    sum_2 += rep
print(sum_2)

print('\n')
# Ex.6
in_num_2 = int(input('정수 : '))
for rep in range(1, in_num_2 + 1):
    if in_num_2 % rep == 0:
        print(rep, end = ' ')

print('\n')
# Ex.7
for rep in range(1, 11):
    if rep % 3 != 0:
        print(rep, end = ' ')

print('\n')
# Ex.8
for o_rep in range(1):
    for i_rep in range(1, 11):
        print(' '*(10-i_rep) + '*'*i_rep)

