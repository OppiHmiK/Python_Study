# -*- coding : utf-8 -*-

def int_classify():
    int_list = list(map(int, input('분류할 숫자들을 입력해 주십시오. : ').split(' ')))
    even_cnt = odd_cnt = 0

    for rep in range(len(int_list)):

        if int_list[rep] % 2 == 0:
            even_cnt += 1

        else:
            odd_cnt += 1

    return even_cnt, odd_cnt

e_cnt, o_cnt = int_classify()
print("짝수 : {}개, 홀수 : {}개".format(e_cnt, o_cnt))
