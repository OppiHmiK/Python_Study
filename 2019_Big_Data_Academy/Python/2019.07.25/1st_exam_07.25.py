# -*- coding : utf-8 -*-
# NOTE : 함수 변수의 효력범위

a = 1
def vartest(a):
    a += 1

vartest(a)
print(a)

a = 1
def vartest_2(a):
    a += 1
    return a

print(vartest_2(a))
print(a)

b = 1
def var_t(hello):
    hello += 1

var_t(3)
print(b)

hello = 1
def var_g():
    global hello
    hello += 1
var_g()
print(hello)

# NOTE : lambda
# lambda는 return이 없어도 결과값을 반환함.
add = lambda a,b : a+b
res = add(3, 4)
print(res)