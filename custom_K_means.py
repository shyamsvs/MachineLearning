# -*- coding: utf-8 -*-
"""
Created on Thu May 31 18:51:27 2018

@author: Shyam
"""

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np


X = np.array([[1,2],
              [1.5,1.8],
              [5,8],
              [8,8],
              [1,0.6],
              [9,11]])
 
plt.scatter(X[:, 0], X[:, 1], s = 50, c='g' )
plt.show()


colors = ["g", "r", "k", "b", "c", "o"]

class KMeans:
    def __init__(self, k = 2, tot = 0.001, max_iter = 300):
         self.k = k
         self.tot = tot
         self.max_iter = max_iter
         
    def fit(self, data):
        self.centroids = {}
       
        for i in range(self.k):
            self.centroids[i] = data[i]
            
        for i in range(self.max_iter):
            self.classifications = {}
            
            for i in range(self.k):
                self.classifications[i] = []
            for featureset in X:
                distances = [np.linalg(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifactions[classification].append(featureset)
                
            prev_centroids = dict(self.centroids)
            
            for classification in self.classsifications:
                pass
                self.centroids[classification] = np.average(self.classifications[classification], axis = 0)
                
        
    def predict(self, data):
        pass
    
    