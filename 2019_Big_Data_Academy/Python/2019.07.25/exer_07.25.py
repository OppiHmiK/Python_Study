# -*- coding :utf-8 -*-
from math import pi

# Ex.1
year = int(input('연도를 입력하세요 : '))
if (year % 4 == 0) or (year % 400 == 0):
    print('윤년입니다.')
elif year % 100 == 0:
    print('윤년이 아닙니다.')
else:
    print('윤년이 아닙니다.')

# Ex.2
total = 10000
money = input('입출 금액을 입력하세요. : ')
if money[0] == '+':
    total += int(money[1:])
elif money[0] == '-':
    total -= int(money[1:])

if total > 0:
    print(f'현재 잔액은 {total}원 입니다.')
elif total == 0:
    print(f'현재 잔액은 없습니다.')
else:
    print('잔액이 부족합니다.')

# Ex.3
def convert_temperature(degree, degree_type):
    if (degree_type == 'c') or (degree_type == 'C'):
        degree = degree*1.8 + 32

    elif (degree_type == 'f') or (degree_type == 'F'):
        degree = (degree - 32)/1.8

    else:
        degree = None
    return degree

print(convert_temperature(10, 'c'))
print(convert_temperature(50, 'f'))
print(convert_temperature(100, 't')) 

# Ex.4
def print_multiples(n):
    if n == 1: return '1 2 3 4 5 6 7 8 9'
    elif n == 2: return '2 4 6 8 10 12 14 16 18'
    elif n == 3: return '3 6 9 12 15 18 21 24 27'
    elif n == 4: return '4 8 12 12 15 18 21 24 36'
    elif n == 5: return '5 10 15 20 25 30 35 40 45'
    elif n == 6: return '6 12 18 24 30 36 42 48 54'
    elif n == 7: return '7 14 21 28 35 42 49 56 63'
    elif n == 8: return '8 16 24 32 40 48 56 64 72'
    elif n == 9: return '9 18 27 36 45 54 63 72 81'
    else: return "Don't torture me!!!"

print(print_multiples(3))
print(print_multiples(5))
print(print_multiples(-1))

# Ex.4-1
def print_muliplication_table():
    for rep in range(1, 10):
        print(print_multiples(rep))

print(print_muliplication_table())

# Ex.5
circumference = lambda radius: 2*pi*radius
area = lambda radius: pi*radius**2

def sum_of_areas(*radius):
    total_area = 0
    for rep in radius:
         total_area += area(rep)
    return total_area

r = 3.0
print(circumference(r), area(r))
r2 = 4.0
print(circumference(r2), area(r2))
r3 = 5.0
print(circumference(r3), area(r3))
print(sum_of_areas(3, 4, 5))

# Ex.6
def sorting():
    lis = []
    for rep in range(1, 4):
        num = int(input(f'{rep}번째 정수를 입력해주세요. : '))
        lis.append(num)

    for o_rep in range(len(lis)):
        for i_rep in range(1, len(lis)):
            if o_rep == i_rep:
                pass
            else:
                if lis[o_rep] != lis[i_rep]:
                    lis.sort()
                else:
                    return None
    return lis

print(sorting()) 

# Ex.7
def won_gidung():
    radius = int(input('반지름 입력 : '))
    height = int(input('높이 입력 : '))

    if (radius > 0) and (height > 0):
        area = 2*pi*radius*height + 2*pi*r**2
        volume = pi*radius**2 * height

        return area, volume
    elif (radius < 0) and (height < 0): return 'error!! radius and height are both negative!!'
    elif radius < 0: return 'error!! radius is negative!!'
    elif height < 0: return 'error!! height is negative!!'

print(won_gidung()) 

# Ex.8
def determine():
    num = int(input('Enter a number : '))
    if num > 0:
        if num % 2 == 0: print('This is even number')
        else: print('This is odd number')
    else: return None
determine()

# Ex.9
def manage_account(balance, choice, money):

    if choice == '+' : balance += money
    elif choice == '-':
        if (balance - money) < 0: return balance
        else: return balance - money
    return balance

print(manage_account(1000, '+', 500))
print(manage_account(1000, '-', 500))
print(manage_account(1000, '-', 1500))
print(manage_account(1000, '*', 500)) 

# EX.10
def introduce():
    name = input('Enter your name : ')
    age = input('Enter your age : ')
    return f'Your name is {name} and your age is {age}'

print(introduce()) 

# Ex.11
def calculate_digits(l_operand, r_operand, op):
    if op == '+' : return l_operand + r_operand
    elif op == '-' : return l_operand - r_operand
    elif op == '*' : return l_operand * r_operand
    elif op == '/' : return l_operand / r_operand

print(calculate_digits(1, 2, '+'))
print(calculate_digits(1, 2, '-'))
print(calculate_digits(1, 2, '*'))
print(calculate_digits(1, 2, '/'))
print(calculate_digits(1, 2, '%'))

# Ex.12
def BMI():
    weight = int(input('Enter your weight (kg): '))
    height = int(input('Enter your hegiht (cm) : '))
    BMI = weight / (height*0.01)**2

    if BMI < 18.5: return '마른 체형'
    elif (BMI >= 18.5) and (BMI < 25.0): return '표준'
    elif (BMI >= 25.0) and (BMI < 30.0): return '비만'
    elif BMI >= 30.0: return '고도비만'

print(BMI())
print(BMI())



