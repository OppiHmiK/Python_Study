# -*- coding : utf-8 -*-
import pickle as pck

with open('test.txt', 'rb') as f:
    data = pck.load(f)

print(data)