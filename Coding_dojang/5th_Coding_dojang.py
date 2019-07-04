# -*- coding : utf-8 -*-
# NOTE : 문자열을 입력받아 문자와 숫자와 따로 구분
import re

def split_str(in_str):

    str = re.sub('[^a-zA-Zㄱ-힗 ]', '', in_str)
    int = re.sub('[^0-9]', '', in_str)

    print('str : ', str)
    print('int : ', int)

split_str('c910m6ia 1ho')
