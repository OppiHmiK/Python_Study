# -*- coding : utf-8 -*-
# NOTE : continue문
#        continue문을 만나면 continue 아래의 코드는 실행되지 않음.

rep = 0
while rep < 10:
    rep += 1
    if rep%2 == 0:
        continue
    print(rep)

print('\n')

rep2 = 0
while rep2 < 10:
    rep2 += 1
    if rep2%3 == 0:
        continue
    print(rep2)

