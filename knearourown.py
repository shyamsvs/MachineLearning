# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:07:12 2018

@author: Shyam
"""

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import warnings
from collections import Counter
style.use('fivethirtyeight')

dataset = {'k' : [[1,2], [2,3], [3,1]], 'r': [[6,5], [7,7], [8,6]] }
new_feature = [5,7]

[[plt.scatter(ii[0], ii[1], s=100, color= i) for ii in dataset[i]] for i in dataset]

plt.scatter(new_feature[0], new_feature[1])
plt.show()
