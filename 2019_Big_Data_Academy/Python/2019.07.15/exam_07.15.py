# -*- coding : utf-8 -*-

# Ex. 1
pin = '881120-1068234'

if pin[7] == '1' or pin[7] == '3':
    print('남자')

elif pin[7] == '2' or pin[7] == '4':
    print('여자')

# Ex. 2
weight = int(input('당신의 몸무게를 입력해 주십시오. (kg): '))
height = int(input('당신의 키를 입력해 주십시오. (cm): '))
bmi = int(weight / (height*0.01)**2)
print(f'당신의 BMI는 {bmi} 입니다.')

# Ex. 3
garo = int(input('가로길이를 입력해 주십시오. : '))
sero = int(input('세로길이를 입력해 주십시오. : '))
print(f'가로길이 {garo}와 세로길이 {sero}의 사각형 넓이는 {garo*sero}이다.')

# Ex. 4
mitbyeon = int(input('밑변 길이를 입력해 주십시오. : '))
height = int(input('높이를 입력해 주십시오.: '))
print(f'삼각형의 넓이 : {0.5*mitbyeon*height:1.1f}')

# Ex. 5
grade = list(map(int, input('당신의 점수를 입력해 주십시오. (공백 구분): ').split()))
print(f'성적 1 : {grade[0]} \n',
      f'성적 2 : {grade[1]} \n',
      f'성적 3: {grade[2]} \n',
      f'총점 : {sum(grade)} 평균 : {sum(grade)/len(grade):1.1f}')

# Ex. 6
length = int(input('길이를 입력해 주세요. : '))
m = length // 100
cm = length % 100
print(f'{m} 미터 {cm} 센티미터')
