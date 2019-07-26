# -*- coding : utf-8 -*-

# Ex.1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
print(is_odd(3))
print(is_odd(6))

# Ex.2
def avg_numbers(*args):
    res = 0
    for rep in args:
        res += rep
    return res / len(args)
print(avg_numbers(1, 2))
print(avg_numbers(1, 2, 3, 4, 5))

# Ex.3
inp1 = int(input('첫번째 숫자를 입력하세요 : '))
inp2 = int(input('두번째 숫자를 입력하세요 : '))

total = inp1 + inp2
print(f'두 수의 합은 {total} 입니다.')

# Ex.4
print('you' 'need' 'python')
print('you' + 'need' + 'python')
print('you', 'need', 'python')
print("".join(['you','need','python']))

# Ex.5
f1 = open('test.txt', 'w')
f1. write('Life is too short')
f1.close()

f2 = open('test.txt', 'r')
print(f2.read())
f2.close()

# Ex.6
user_input = input('저장할 내용을 입력하세요. : ')
with open('test2.txt', 'a') as f:
    f.write(user_input + '\n')

with open('test3.txt', 'w') as f:
    f.write('Life is too short \n you need java')

# Ex.7
with open('test3.txt', 'r') as f:
    body = f.read()

body = body.replace('java', 'python')

with open('test3.txt', 'w') as f:
    f.write(body)