# -*- coding : utf-8 -*-
# NOTE : 문자열 포매팅

print('I eat %s apples.' % 'five')
print('I eat %d apples.' % 3)

number = 7
day = 'three'
print('I eat %d apples.' % number)
print('I ate %d apples. so I was sick for %s days.' % (number, day))

print('Error is %d%%.' % 98)

# NOTE : 오른쪽 정렬
print('%10s' % 'hi')
# NOTE : 왼쪽 정렬
print('%-10s' % 'hi')

print('%s Jane' % 'hi')
print('%-10s Jane' % 'hi')

# NOTE : 소수점 표시
print('%10d' % 10)
print('%f' % 3.42134264)
print('%0.2f' % 3.42134264)
print('%10.4f' % 3.42134264)

print('I eat {0} apples.'.format(3))
print('I eat {0} apples.'.format('five'))
print('I eat {0} apples.'.format(number))
print('I ate {0} apples. so I was sick for {1} days.'.format(number, day))

print('I ate {number} apples. '\
      'so I was sick for {day} days.'.format(number = 10, day = 3))
print('I ate {0} apples. '\
      'so I was sick for {day} days.'.format(10, day = 3))

# NOTE : 왼쪽 정렬
print('{0:<10}'.format('hi'))
# NOTE : 오른쪽 정렬
print('{0:>10}'.format('hi'))
# NOTE : 가운데 정렬
print('{0:^10}'.format('hi'))
# NOTE : 공백 채우기
print('{0:*^10}'.format('hi'))
# NOTE : 소수점 표시
y = 3.42134234
print("{0:0.4f}".format(y))
print("{0:10.4f}".format(y))
print("{{ and }}".format())

# NOTE : f 문자열 포매팅 (Python >= 3.6)
name = '홍길동'; age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년에는 {age + 1}살이 됩니다.')

# NOTE : 딕셔너리는 f 문자열 포매팅으로 사용할 수 있다.
dic = {'name' : '홍길동', 'age' : 30}
print(f'나의 이름은 {dic["name"]}입니다. 나이는 {dic["age"]}입니다.')

print(f'{"hi":<10}')
print(f'{"hi":>10}')
print(f'{"hi":^10}')
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')






