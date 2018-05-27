# -*- coding: utf-8 -*-
"""
Created on Sat May 26 10:29:40 2018

@author: Shyam
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
dataa = pd.read_csv('titanic.csv')
sns.pairplot(dataa[["Sex","Age","Fare"]])
plt.show()
model = sm.ols(formula='Sex~Survived',data=dataa)
fitted = model.fit()
fitted.summary()
dataa.head(10)
dataa.tail(10)
summary(dataa)
