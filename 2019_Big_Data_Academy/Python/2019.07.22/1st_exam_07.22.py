# -*- coding : utf-8 -*-
# NOTE : 함수

# NOTE : 함수 정의
def add(a, b):
    return a+b

def add_2(a, b):
    result = a + b
    return result

def say():
    return 'Hi'

def add_3(a, b):
    print(f'{a} + {b} = {a+b}')

def say_2():
    print('hi')

# NOTE : 매개변수가 몇 개인지 모르는 경우
# NOTE : 이 경우 입력값들은 튜플로 저장됨.
def int_sum(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

def add_mul(op, *args):
    if op == 'add':
        res = 0
        for rep in args:
            res += rep

    elif op == 'mul':
        res = 1
        for rep in args:
            res *= rep

    return res

def cal(op, *args):
    if op == 'add':
        res = 0
        for rep in args:
            res += rep

    elif op == 'sub':
        res = args[0]
        for rep in args[1:]:
            res -= rep

    elif op == 'mul':
        res = 1
        for rep in args:
            res *= rep

    elif op == 'div':
        res = args[0]
        for rep in args[1:]:
            res /= rep

    elif op == 'resi':
        res = args[0]
        for rep in args[1:]:
            res %= rep

    elif op == 'quoti':
        res = args[0]
        for rep in args[1:]:
            res //= rep

    return res

# NOTE : 키워드 매개변수
# NOTE : 키워드 매개변수는 key = value 형태로 딕셔너리에 저장됨.
def cal_score(name, *score, **option):
    print(name)
    sum = 0
    for rep in score:
        sum += rep

    print('총점 : ', sum)
    if (option['avg'] == True):
        print('평균 : ', sum/len(score))

# NOTE : return 값 여러개 받기
# NOTE : 튜플형으로 반환됨.
def addNmul(a, b):
    return a+b, a*b

# NOTE : 함수는 return을 만나면 함수를 빠져나옴.
def say_nick(nick):
    if nick == '바보':
        return

    else:
        print(f'내 별명은 {nick} 입니다.')

def say_myself(name, old, male = 1):
    print(f'내 이름은 {name}입니다.')
    print(f'제 나이는 {old}입니다.')
    if male:
        print('남자입니다.')
    else:
        print('여자입니다.')

# NOTE : 함수 호출
print(add(2, 3))
print(add_2(3, 4))
print(say())
a = add_3(3, 3)
say_2()
print(a)

result = add(a = 3, b = 4)
result_2 = add(b = 7, a = 3)
print(result)
print(result_2)

print(int_sum(1, 2, 3))
print(int_sum(5, 7, 9, 11, 13))
print(int_sum(8, 9, 6, 2, 9, 7, 5, 8))

print(add_mul('add', 3, 4))
print(add_mul('mul', 3, 4))

print(cal('add', 3, 4))
print(cal('sub', 3, 4))
print(cal('mul', 3, 4))
print(cal('div', 3, 4))
print(cal('resi', 3, 4))
print(cal('quoti', 3, 4))

cal_score('김상형', 88, 99, 77, avg = True)
cal_score('김한슬', 99, 98, 95, 89, avg = False)

print(addNmul(3, 4))
res1, res2 = addNmul(3, 4)
print(res1)
print(res2)

say_nick('김하마')
say_nick('바보')

say_myself('김종민', 24, 1)
