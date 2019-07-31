# -*- coding : utf-8 -*-

# Ex.1 #
def print_multiples(number):

    if (number >= 1) and (number <=9):
        for rep in range(1, 10):
            print(rep* number, end = ' ')
    else: print("Don't torture me!!!")

def print_multiplication_table():
    print_multiples(2)
    print_multiples(3)
    print_multiples(4)
    print_multiples(5)
    print_multiples(6)
    print_multiples(7)
    print_multiples(8)
    print_multiples(9)

# Ex.2
def print_pyramid(n):

    for rep in range(1, n+1):
        print('*'*rep)

# Ex.3
def input_number():
    lis = []
    while 1:
        nums = int(input('Enter a positive integer : '))
        if nums == 0:
            break
        elif nums > 0:
            lis.append(nums)
    return lis

def descrive(numbers):
    print(f'The count of input numbers : {len(numbers)}')
    print(f'The sum of input numbers : {sum(numbers)}')
    print(f'The average of input numbers : {sum(numbers) / len(numbers)}')
    print(f'The max of input numbers : {max(numbers)}')
    print(f'The min of input numbers : {min(numbers)}')
    print(f'The elements : {numbers}')

# Ex.4
def fibonacci_seq(number):
    num1 = 0; num2 = 1
    fibo = [1]
    for rep in range(1, number):
        fibo.append(num1 + num2)
        num1, num2 = num2, num1 + num2

    return fibo

# just doing
def odd_pyramid(i_rep):
    for rep in range(1, i_rep+1):
        print(' '*(i_rep - rep) + '*'*(2*rep - 1))

def up_arrow(i_rep):
    for rep in range(1, i_rep + 1):
        if rep < int((8*i_rep / 10)):
            print(' '*int((8*i_rep / 10) - rep) + '*'*(2*rep - 1))
        else:
            print(' '*int((i_rep/2))+'*'*5)


print_multiples(3)
print_multiples(5)
print_multiples(-1)
print_multiplication_table()

print('1st pyramid')
print_pyramid(5)

print('2nd pyramid')
print_pyramid(3)

positive_int = input_number()
descrive(positive_int)

print(fibonacci_seq(1))
print(fibonacci_seq(3))
print(fibonacci_seq(5))

odd_pyramid(3)
up_arrow(10)

print(fibonacci_seq(3000))
