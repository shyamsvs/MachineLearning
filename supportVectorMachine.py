# -*- coding: utf-8 -*-
"""
Created on Mon May 28 16:01:50 2018

@author: Shyam
"""

import numpy as np
from sklearn import  cross_validation, svm
import pandas as pd
df = pd.read_csv('breast-cancer-wisconsin.data.')             
df.replace('?', -99999, inplace = True)
df.drop(['id'], 1, inplace= True)

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

df = svm.SVC()

df.fit(X_train, y_train)

accuracy = df.score(X_test, y_test)
print(accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1], [8,10,10,8,7,10,9,7,1]])
 
example_measures = example_measures.reshape(len(example_measures), -1)

prediction = df.predict(example_measures)

print(prediction) 
