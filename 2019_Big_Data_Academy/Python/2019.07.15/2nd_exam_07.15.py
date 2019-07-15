# -*- coding : utf-8 -*-
# NOTE : elif문

pocket = ['paper', 'cellphone']
card = True

if 'money' in pocket:
    print('택시')

elif card:
    print('택시')

else:
    print('걸어')

score = 70
if score >= 60:
    message = 'success'

else:
    message = 'failure'
print(message)

# NOTE : 조건부 표현식
msg = 'success' if score >= 60 else 'failure'
print(msg)


