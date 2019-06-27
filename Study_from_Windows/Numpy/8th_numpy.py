import numpy as np

x = [1, 2, 3, 99, 99, 3, 2, 1]

# NOTE : 배열 분할하기
x1, x2, x3 = np.split(x, [3, 5])
# print(x1, x2, x3)


grid = np.arange(16).reshape(4, 4)
print(grid)
