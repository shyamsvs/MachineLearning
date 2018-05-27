# -*- coding: utf-8 -*-
"""
Created on Sun May 27 08:59:51 2018

@author: Shyam
"""

from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import random 

style.use('fivethirtyeight')

#xs = np.array([1,2,3,4,5,6], dtype = np.float64)
#ys = np.array([5,4,6,5,6,7], dtype = np.float64)

 
def create_dataset(hm, variance, step=2, correlation=False):
    val = 1
    ys = []
    for i in range(hm):
        y = val + random.randrange(-variance, variance)
        ys.append(y)
        if correlation and correlation == 'pos':
            val  = val + step
        elif correlation and correlation =='neg':
            val  = val - step
    xs = [i for i in range(len(ys))]
    return np.array(xs, dtype = np.float64), np.array(ys, dtype = np.float64)

def best_fit_line_and_intercept(xs,ys):
  m = ( (mean(xs) * mean(ys)) - mean(xs*ys) ) / (mean(xs)*mean(xs) - mean(xs*xs))
  b = mean(ys) - m*mean(xs)  
  return m,b

def squared_error(ys_orgin, ys_line):
  return sum( (ys_line - ys_orgin) ** 2 )

def coefficient_of_determination(ys_orgin, ys_line):
    y_mean_line = [ mean(ys_orgin) for y in ys_orgin]
    squared_error_regression = squared_error(ys_orgin, ys_line)
    squared_error_y_mean = squared_error(ys_orgin, y_mean_line)
    return 1 - (squared_error_regression /  squared_error_y_mean)



xs, ys = create_dataset(40, 10, 2, correlation = 'pos')


m,b = best_fit_line_and_intercept(xs,ys)
 
print(m,b)

regression_line = [ (m*x) + b for x in xs ]

predict_x = 8
predict_y = (m*predict_x) + b

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.plot(xs, regression_line)
plt.scatter(predict_x, predict_y, s=100, color = 'g')
plt.show()
