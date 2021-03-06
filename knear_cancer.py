# -*- coding: utf-8 -*-
"""
Created on Mon May 28 14:52:26 2018

@author: Shyam
"""

from math import sqrt
import numpy as np
import pandas as pd
import random
import warnings
from collections import Counter



def k_near_neighbors(data, predict, k=3):
    if(len(data) >= k):
        warnings.warn("K IS LESS THAN YOU ENTERED")
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances) [:k]]
    #print( Counter(votes).most_common(1)[0][0])
    vote_results = Counter(votes).most_common(1)[0][0]
    return vote_results

df = pd.read_csv('breast-cancer-wisconsin.data')
df.replace('?', -99999, inplace = True)
df.drop(['id'], 1, inplace = True)

full_data = df.astype(float).values.tolist()
#print(full_data[:10])

random.shuffle(full_data)
#print(20* '#')
#print(full_data [:10])

correct = 0
total = 0

test_size = 0.2
train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}
train_data = full_data[:-int(test_size * len(full_data))]
test_data = full_data[-int(test_size * len(full_data)) :]

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])
    
for group in test_set:
    for data in test_set[group]:
        vote = k_near_neighbors(train_set, data, k = 5 )
        if group == vote:
            correct = correct + 1
        total = total + 1
print('Accuracy :', correct/total)

        
        

    