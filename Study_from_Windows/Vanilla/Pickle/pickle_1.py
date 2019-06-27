# -*- coding : utf-8 -*-

import pickle as pck

lis = ['a', 'b', 'c']
with open('test.txt', 'wb') as f:
    pck.dump(lis, f)


