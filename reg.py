# -*- coding: utf-8 -*-
"""
Created on Fri May 25 12:25:14 2018

@author: Shyam
"""

import pandas as pd
from sklearn import datasets
iris = pd.DataFrame(datasets.load_iris().data)
iris.head(10)
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(iris[['0','1','2']])
plt.show()