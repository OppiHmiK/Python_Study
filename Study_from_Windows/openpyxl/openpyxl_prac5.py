# -*- coding : utf-8 -*-
import openpyxl as pyxl
import os

if os.path.isdir == 'data':
    os.mkdir('data')
os.chdir('data')

wb = pyxl.load_workbook('test3.xlsx')
ws = wb.active
ws_new = wb.create_sheet('new sheet')

wb.save('test5.xlsx')
