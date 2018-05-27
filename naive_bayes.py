# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=5
b=6
c=a+b
print ("hello")
print (5+8)
import numpy as np
x = np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
y = np.array([1,1,1,2,2,2])
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(x,y)
GaussianNB()
print(clf.predict([[-0.8,-1]]))
