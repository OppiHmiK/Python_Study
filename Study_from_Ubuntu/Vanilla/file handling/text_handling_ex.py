with open('example.txt', 'a') as ex:
    for rep in range(1,6):
        ex.write(str(rep)+'. '+input('문자열 입력 : ') + '\n')

with open('example.txt', 'r') as ex:
    exam = ex.readlines()
    for rep in exam:
        print(rep)