# -*- coding : utf-8 -*-
from openpyxl import Workbook
import os

if os.path.isdir == 'data':
    os.mkdir('data')
os.chdir('data')

wb = Workbook()
ws = wb.active
ws['A1'] = 'Hello, World'

sheet = 'Test sheet'
ws2 = wb.create_sheet(1, sheet)
ws2['A1'] = 100
wb.save('test2.xlsx')