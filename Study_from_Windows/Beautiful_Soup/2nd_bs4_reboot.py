# -*- coding : utf-8 -*-
from urllib import request as req
import os

if not os.path.isdir('data'):
    os.mkdir('data')
os.chdir('data')

url = 'http://uta.pw/shodou/img/28/214.png'
savename = 'test2.png'

mem = req.urlopen(url).read()
with open(savename, 'wb') as f:
    f.write(mem)
    print('File Saved!')