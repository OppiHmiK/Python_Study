# -*- coding : utf-8 -*-
# NOTE : 문자열 관련 함수

# NOTE : 특정 문자의 갯수를 세어줌.
a = 'hobby'
print('b의 개수는 %d개 입니다.'%a.count('b'))

# NOTE : 특정 문자의 인덱스를 알려줌.
a2 = 'Python is the best choice'
print('b는 {}번째 자리입니다.'.format(a2.find('b')))
print('k는 {}번째 자리입니다.'.format(a2.find('k')))
# NOTE : 문자열에 특정 문자가 없다면 -1을 반환함.
# print('k는 {}번째 자리입니다.'.format(a2.index('k'))) << 오류 발생.

# NOTE
# join : 문자열에 특정 문자를 삽입.
print(','.join('abcd'))
print(','.join(['a', 'b', 'c', 'd']))

# NOTE : 소문자를 대문자로.
print('hi'.upper())
# NOTE : 대문자를 소문자로.
print('HI'.lower())

# NOTE : 왼쪽 공백제거
print(f'{"hi":^10}'.lstrip())
# NOTE : 오른쪽 공백제거
print(f'{"hi":^10}'.rstrip())
# NOTE : 양쪽 공백제거
print(f'{"hi":^10}'.strip())

# NOTE : 특정 문자열 변경
print('Life is too short'.replace('Life', 'Your leg'))

# NOTE : 공백을 기준으로 문자열 나누기
a3 = "Life is too short"
print(a3.split())

# NOTE : :을 기준으로 문자열 나누기
a4 = 'a:b:c:d'
print(a4.split(':'))








