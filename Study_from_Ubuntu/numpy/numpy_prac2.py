# -*- coding : utf-8 -*-

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os

if os.getcwd() != '../data':
    os.chdir('data')

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])

print(heights.reshape((len(heights), 1)))