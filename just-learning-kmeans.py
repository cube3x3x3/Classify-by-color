# -*- coding: utf-8 -*-
"""
Created on Tue May 30 07:45:09 2017

@author: cube3x3x3
"""

import math

def dist(m, a):
    return math.sqrt((m[0]-a[0])**2 + (m[1]-a[1])**2)

datasets = (
    (65.0, 220.0 ), ( 73.0, 160.0 ), ( 59.0, 110.0 ), ( 61.0, 120.0 ), 
    ( 75.0, 150.0 ), ( 67.0, 240.0 ), ( 68.0, 230.0 ), ( 70.0, 220.0 ),
    ( 62.0, 130.0 ), ( 66.0, 210.0 ), ( 77.0, 190.0 ), ( 75.0, 180.0 ),
    ( 74.0, 170.0 ), ( 70.0, 210.0 ), ( 61.0, 110.0 ), ( 58.0, 100.0 ),
    ( 66.0, 230.0 ), ( 59.0, 120.0 ), ( 68.0, 210.0 ), ( 61.0, 130.0 ) 
)

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
import random
import sys
random.seed(12345)
k = 3
maxCount = 30
# assign each tuple to a randomly selected cluster
clusters = [random.randrange(k) for i in range(len(datasets))]

# compute the centroid for each cluster
## Calculate the new means to be the centroids of the observations
##  in the new clusters.
centroid = [[0,0] for i in range(k)]

def updateStep(centroid):
    means = [[0, 0] for i in range(k)]
    clusterCounts = [0 for i in range(k)]
    for i in range(len(datasets)):
        means[clusters[i]][0] += datasets[i][0]
        means[clusters[i]][1] += datasets[i][1]
        clusterCounts[clusters[i]] += 1
    
    for i in range(k):
        means[i][0] /= clusterCounts[i]
        means[i][1] /= clusterCounts[i]
        
    nearest = [sys.maxint for i in range(k)]
    for i in range(len(datasets)):
        # dist(m, a)
        currentDist = dist(means[clusters[i]], datasets[i])
        if currentDist < nearest[clusters[i]]:
            nearest[clusters[i]] = currentDist
            centroid[clusters[i]] = datasets[i]

updateStep(centroid)
#loop until no improvement or until maxCount
#  assign each tuple to best cluster
#   (the cluster with closest centroid to tuple)
#  update each cluster centroid
#   (based on new cluster assignments)
#end loop
for n in range(maxCount):
    #assign each tuple to best cluster
    for i in range(len(datasets)):
        minDist = sys.maxint
        for j in range(len(centroid)):
            currentDist = dist(centroid[j], datasets[i])
            if currentDist < minDist:
                minDist = currentDist
                clusters[i] = int(j)
            
    print clusters
    #update each cluster centroid
    lastCentroid = centroid[:]
    updateStep(centroid)
    if lastCentroid == centroid:
        print 'count:', n, 'centroid:', centroid
        break

    
#return clustering

def printClusters(k, datasets, clusters):
    for i in range(k):
        for j in range(len(datasets)):
            if i == clusters[j]:
                print i, '|', j, '|', datasets[j]
        print '-'*20
            
printClusters(k, datasets, clusters)
            
            
