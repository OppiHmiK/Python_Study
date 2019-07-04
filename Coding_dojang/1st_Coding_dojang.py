# -*- coing : utf-8 -*-
# NOTE : 이씨인 사람과 김씨인 사람 수 각각 구하기
# NOTE : 이름이 이재영인 사람 수 구하기
# NOTE : 중복되는 이름 제거
names = ['이유덕', '이재영', '권종표', '이재영', '박민호', '강상희',
         '이재영', '김지완', '최승혁', '이성연', '박영서', '박민호',
         '전경헌', '송정환', '김재성', '이유덕', '전경헌']

lee_cnt = 0
kim_cnt = 0
ljy_cnt = 0

for name in names:

    if name[0] == '이':
        lee_cnt += 1

        if name == '이재영':
            ljy_cnt += 1

    elif name[0] == '김':
        kim_cnt += 1

print('성이 이씨인 사람들 수 입니다. : {} 명'.format(lee_cnt))
print('성이 김씨인 사람들 수 입니다. : {} 명'.format(kim_cnt))
print('이름이 이재영인 사람들 수 입니다. : {} 명'.format(ljy_cnt))

unique_name = set(names)
print(sorted(unique_name))
