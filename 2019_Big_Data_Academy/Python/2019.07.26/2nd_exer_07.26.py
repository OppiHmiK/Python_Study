# -*- coding : utf-8 -*-

'''
# Ex.1
def sorting():
    lis = []
    for rep in range(3):
        num = int(input(f'{rep + 1}번째 정수를 입력하세요. : '))
        lis.append(num)

    for o_rep in range(len(lis)):

        for i_rep in range(len(lis)):
            if o_rep != i_rep:
                if lis[i_rep] != lis[o_rep]:
                    if lis[i_rep] > lis[o_rep]:
                        lis[i_rep], lis[o_rep] = lis[o_rep], lis[i_rep]
                else:
                    return '같은 수는 입력하지 말아주십시오.'

    return lis
print(sorting())

# Ex.2
PI = 3.14
def width(r, h):
    if r >= 0 and h >= 0: return 2 * PI * r * h + 2 * PI * r ** 2
    elif (r < 0) and (h > 0): return 'error!! radius is negative!!'
    elif (h < 0) and (r > 0): return 'error!! height is negative!!'
    elif (r < 0) and (h < 0): return 'error!! radius and height are both negative!!'


def volume(r, h):
    if (r >= 0) and (h >= 0): return PI*h*r**2
    elif (r < 0) and (h > 0): return 'error!! radius is negative!!'
    elif (h < 0) and (r > 0): return 'error!! height is negative!!'
    elif (r < 0) and (h < 0): return 'error!! radius and height are both negative!!'

r = float(input('반지름 입력 : '))
h = float(input('높이 입력 : '))
print(width(r, h), volume(r, h))
print(width(r, -h), volume(r, -h))
print(width(-r, h), volume(-r, h))
print(width(-r, -h), volume(-r, -h))

# Ex.3
def determine(num):
    if num % 2 == 0:
        print(f'{num} is even number')
    else:
        print(f'{num} is odd number')

num = int(input('Enter your integer : '))
determine(num)

# Ex.4
def manage_account(balance, choice, money):
    if choice == '+':
        print(balance + money)
        return balance + money
    elif choice == '-':
        if (balance - money) < 0:
            print('잔액이 부족합니다.')
            return balance
        else:
            print(balance - money)
            return balance - money
    else:
        print('Error!')
        return balance

balance = 10000
balance = manage_account(balance, '-', 20000)
balance = manage_account(balance, '-', 5000)
balance = manage_account(balance, '=', 2000)
balance = manage_account(balance, '+', 1000)
'''


