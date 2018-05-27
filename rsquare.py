# -*- coding: utf-8 -*-
"""
Created on Sat May 26 18:09:43 2018

@author: Shyam
"""

from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

xs = np.array([1,2,3,4,5,6], dtype = np.float64)
ys = np.array([5,4,6,5,6,7], dtype = np.float64)

plt.scatter(xs,ys) 

plt.show()

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

m,b = best_fit_line_and_intercept(xs,ys)

print(m,b)

regression_line = [ (m*x) + b for x in xs ]

predict_x = 8
predict_y = (m*predict_x) + b

r_squared = coefficient_of_determination(ys, regression_line)
print(r_squared)

plt.scatter(xs,ys)
plt.scatter(predict_x, predict_y)
plt.plot(xs, regression_line)
plt.show()
