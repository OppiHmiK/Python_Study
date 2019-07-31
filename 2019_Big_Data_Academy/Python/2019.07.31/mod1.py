# -*- coding : utf-8 -*-
add = lambda num1, num2: num1 + num2
sub = lambda num1, num2: num1 - num2

PI = 3.141592
class Math:
    def solve(self,radius):
        return PI*(radius**2)

# NOTE : 함수가 정의된 파일에서만 실행됨.
if __name__ =='__main__':
    print(add(1, 4))
    print(sub(4, 2))