# -*- coding : utf-8 -*-
# NOTE : 파일 읽고 쓰기
'''
# NOTE : 파일 쓰기
f = open('새파일.txt', 'w')
for rep in range(1, 11):
    f.write(f'{rep}번째 줄입니다. \n')
f.close()

# NOTE : 파일 읽기
# NOTE : 한 줄만 읽기
f_2 = open('새파일.txt', 'r')
print(f_2.readline())

while True:
    line = f_2.readline()
    if not line: break
    print(line, end='')
f_2.close

 while 1:
    data = input()
    if not data: break
    print(data)


# NOTE : 파일에 있는 모든 라인들 읽기 (리스트 형태로 저장)
f_3 = open('새파일.txt', 'r')
print(f_3.readlines())
f_3.close()

# NOTE : 파일에 있는 모든 라인들 읽기 (문자열 형태로 저장)
f_4 = open('새파일.txt', 'r')
print(f_4.read())
f_4.close()
'''

# NOTE : 파일에 계속해서 데이터 저장
f_5 = open('새파일.txt', 'a')
for rep in range(11, 21):
    f_5.write(f'{rep}번째 줄 입니다. \n')
f_5.close()

# NOTE : with문을 활용한 파일 읽기, 쓰기
# NOTE : with문을 빠져나오면 자동으로 close()시켜줌.

with open('새파일2.txt', 'w') as f:
    f.write('Life is too short, you need Python')

with open('새파일2.txt', 'r') as f:
    print(f.read())


