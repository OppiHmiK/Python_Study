f = open('test.txt', 'w')
f.write("룰루리 랄라 \n")
f.close()

f = open('test.txt', 'a')
f.write('라랄 리루룰')
f.close()

with open('test.txt', 'a') as test:
    test.write("\n 하헤히호후")