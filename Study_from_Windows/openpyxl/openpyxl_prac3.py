# -*- coding : utf-8 -*-
from openpyxl import Workbook
import os

if os.path.isdir == 'data':
    os.mkdir('data')
os.chdir('data')

wb = Workbook()
ws = wb.active
ws['A1'] = 'Hello, KimHippo!'

ws.merge_cells('A2:E2') # NOTE : A2에서 E2까지 cell을 병합함.
ws['A2'] = 'REPORT'
wb.save('test3.xlsx')


