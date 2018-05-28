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
new_feature = [1,4]

#[[plt.scatter(ii[0], ii[1], s=100, color= i) for ii in dataset[i]] for i in dataset]

#plt.scatter(new_feature[0], new_feature[1])
#plt.show()


def k_near_neighbors(data, predict, k=3):
    if(len(data) >= k):
        warnings.warn("K IS LESS THAN YOU ENTERED")
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distances.append([euclidean_distance, group])
    votes = [i[1] for i in sorted(distances) [:k]]
    print( Counter(votes).most_common(1)[0][0])
    vote_results = Counter(votes).most_common(1)[0][0]
    return vote_results


result =  k_near_neighbors(dataset, new_feature, k= 3)
print(result)     


[[plt.scatter(ii[0], ii[1], s=100, color= i) for ii in dataset[i]] for i in dataset]

plt.scatter(new_feature[0], new_feature[1], color = result)
plt.show()

