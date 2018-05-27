# -*- coding: utf-8 -*-
"""
Created on Sun May 27 16:00:44 2018

@author: Shyam
"""

from math import sqrt

plot1 = [1,3]
plot2 = [2,5]

euclid_distance = sqrt( ( plot1[0] - plot2[0] ) **2 + ( plot1[1] - plot2[1] ) **2 )

print(euclid_distance)
