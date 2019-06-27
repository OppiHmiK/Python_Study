# -*- coding : utf-8 -*-

from openpyxl import Workbook
import os

if os.path.isdir == 'data':
    os.mkdir('data')
os.chdir('data')

wb = Workbook() # NOTE : 워크북을 생성
ws = wb.active # NOTE : 워크 시트를 얻음
ws['A1'] = 'Hello, World!' # NOTE : A1에 'Hello, World!' 값을 입력
wb.save('test.xlsx')
