with open('test.txt', 'r') as test:
    print(test.readline())
    print(test.tell())

with open('test.txt', 'r') as test2:
    test2 = test2.readlines()
    for rep in test2:
        print(rep)