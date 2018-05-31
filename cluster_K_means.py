# -*- coding: utf-8 -*-
"""
Created on Thu May 31 15:49:23 2018

@author: Shyam
"""

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

X = np.array([[1,1],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])
 
#plt.scatter(X[:, 0], X[:, 1], s = 50, c='g' )
#plt.show()


clf = KMeans(n_clusters = 2)
clf.fit(X)

centroids = clf.cluster_centers_
labels = clf.labels_

colors = ["g.", "r.", "k.", "b.", "c.", "o."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1],  colors[labels[i]], markersize = 10)

plt.scatter(centroids[:, 0], centroids[:, 0], marker = 'x', s=100, linewidth = 5)
plt.show()