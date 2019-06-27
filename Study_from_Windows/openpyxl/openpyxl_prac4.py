# -*- coding : utf-8 -*-
from openpyxl.styles import Font, Alignment
from openpyxl.styles import Border, Side
from openpyxl import Workbook
import os

if os.path.isdir == 'data':
    os.mkdir('data')
os.chdir('data')

wb = Workbook()
ws = wb.active
ws['A1'] = 'Hello, openpyxl!'
cal = ws['A1']

# NOTE : 폰트이름은 맑은 고딕이고 크기는 15면서 굵게 설정
cal.font = Font(name = '맑은 고딕', size=15, bold = True)

# NOTE : Cell내용을 가로, 세로 맞춤을 가운데로 정렬
cal.alignment = Alignment(horizontal='center', vertical='center')

wb.save('test4.xlsx')



