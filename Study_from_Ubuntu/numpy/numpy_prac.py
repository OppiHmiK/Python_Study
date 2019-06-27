import numpy as np

d1 = np.random.randint(0, 100, size = (4, 4))
vsp_d1 = np.vsplit(d1, [2])
hsp_d1 = np.hsplit(d1, [2])

d2 = np.random.randint(0, 100, size = (4, 1))
d3 = np.random.randint(0, 100 ,size = (1, 4))

vst_d1 = np.vstack([d1, d3])
hst_d1 = np.hstack([d1, d2])

''' print(d1)
print(vst_d1)
print(hst_d1) '''

d4 = np.linspace(1, 100, 10)
print(np.add.reduce(d4))
print(np.add.accumulate(d4))

print(np.multiply.reduce(d4))
print(np.multiply.accumulate(d4))

