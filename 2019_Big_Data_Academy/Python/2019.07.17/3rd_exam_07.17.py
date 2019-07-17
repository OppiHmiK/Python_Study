# -*- coding : utf-8 -*-
# NOTE : for문

l = ['one', 'two', 'three']
for rep in l:
    print(rep)
print('\n')

l2 = [(1, 2), (3, 4), (5, 6)]
for (f_rep, l_rep) in l2:
    print(f_rep + l_rep)
print('\n')

marks = [90, 25, 67, 45, 80]
number = 0
cnt = 0

for rep in marks:
    number += 1

    if rep >= 60:
        print(f'{number}번째 학생은 합격입니다.')
        cnt += 1
    else:
        print(f'{number}번째 학생은 불합격입니다.')
print(f'총 합격 인원은 {cnt}명 입니다. \n')

number = 0
for rep in marks:
    number += 1
    if rep < 60:
        continue
    print(f'{number}번 학생 축하합니다. 합격입니다.')
print('\n')

# NOTE : range()
rng = range(10)
print(rng)
# Output : 0 ~ 9(끝 숫자는 포함되지 않음.)

add = 0
for rep in range(1, 11):
    print(add + rep, end = ' ')
print('')
for rep in range(len(marks)):
    if marks[rep] < 60:
        continue
    print(f'{rep+1}번 학생 축하합니다. 합격입니다.')
print('\n')

for o_rep in range(2, 10):
    for i_rep in range(1, 10):
        print(o_rep*i_rep, end = ' ')
    print('')

# NOTE : 리스트 내포
l3 = [1, 2, 3, 4]
res = [rep*3 for rep in l3]
print(res)

l4 = [rep*3 for rep in l3 if rep%2 == 0]
print(l4)

gugu = [f_rep*s_rep for f_rep in range(1, 10) for s_rep in range(2, 10)]
print(gugu)