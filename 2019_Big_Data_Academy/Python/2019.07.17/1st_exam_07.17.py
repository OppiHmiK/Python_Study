# -*- coding : utf-8 -*-
# NOTE : while문

cnt = 0
while cnt < 10:
    cnt += 1
    print(f'나무를 {cnt}번 찍었습니다.')
    if cnt == 10:
        print('나무가 넘어갑니다.')

prompt = '''
1.  Add
2.  Del
3.  List
4.  Quit
'''

num = 0
while num != 4:
    print(prompt)
    num = int(input('Enter number : '))


# NOTE : break문
coffee = 10
money = 300

while money:
    print('돈을 받았으니 커피를 줍니다. ')
    coffee -= 1
    print(f'남은 커피의 양은 {coffee}개 입니다.')
    if coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break

have_coffee = 10
while 1:
    have_money = int(input('돈을 넣어주십시오. : '))
    if have_money > 300:
        have_coffee -= 1
        print(f'받은 돈은 {have_money}원 이고, 거스름 돈은 {have_money - 300}원 입니다.')
        print(f'남은 커피의 양은 {have_coffee}개 입니다.')

    elif have_money == 300:
        have_coffee -= 1
        print(f'남은 커피의 양은 {have_coffee}개 입니다.')

    else:
        print(f'돈이 {abs(have_money - 300)}원 부족합니다.')
        print(f'남은 커피의 양은 {have_coffee}개 입니다.')

    if have_coffee == 0:
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break