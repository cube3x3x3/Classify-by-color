# -*- coding: utf-8 -*-
"""
Created on Tue May 30 07:45:09 2017

@author: cube3x3x3
"""

import math

a = (61.0, 100.0)
b = (64.0, 150.0)
c = (70.0, 140.0)
print a,b,c

m = ((a[0]+b[0]+c[0])/3, (a[1]+b[1]+c[1])/3)
print 'm', m

def dist(m, a):
    return math.sqrt((m[0]-a[0])**2 + (m[1]-a[1])**2)
    
    
print dist(m, a)
print dist(m, b)
print dist(m, c)



"""
assign each tuple to a randomly selected cluster
compute the centroid for each cluster
loop until no improvement or until maxCount
  assign each tuple to best cluster
   (the cluster with closest centroid to tuple)
  update each cluster centroid
   (based on new cluster assignments)
end loop
return clustering
"""
