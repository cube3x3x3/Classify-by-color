# -*- coding: utf-8 -*-
"""
Created on Tue May 30 07:45:09 2017

@author: cube3x3x3
"""
"""
k-means

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

import math
import random
import sys
random.seed(12345)
NUMBER_OF_CLUSTER = 3
MAX_COUNT = 30
TEST_DATA_SETS = (
    (65.0, 220.0 ), ( 73.0, 160.0 ), ( 59.0, 110.0 ), ( 61.0, 120.0 ), 
    ( 75.0, 150.0 ), ( 67.0, 240.0 ), ( 68.0, 230.0 ), ( 70.0, 220.0 ),
    ( 62.0, 130.0 ), ( 66.0, 210.0 ), ( 77.0, 190.0 ), ( 75.0, 180.0 ),
    ( 74.0, 170.0 ), ( 70.0, 210.0 ), ( 61.0, 110.0 ), ( 58.0, 100.0 ),
    ( 66.0, 230.0 ), ( 59.0, 120.0 ), ( 68.0, 210.0 ), ( 61.0, 130.0 ) 
)

def dist(m, a):
    return math.sqrt((m[0]-a[0])**2 + (m[1]-a[1])**2)


# assign each tuple to a randomly selected cluster
clusters = [random.randrange(NUMBER_OF_CLUSTER) for i in range(len(TEST_DATA_SETS))]

# compute the centroid for each cluster
## Calculate the new means to be the centroids of the observations
##  in the new clusters.
centroid = [[0,0] for i in range(NUMBER_OF_CLUSTER)]

def update_step(centroid):
    _means = [[0, 0] for i in range(NUMBER_OF_CLUSTER)]
    _clusterCounts = [0 for i in range(NUMBER_OF_CLUSTER)]
    for i in range(len(TEST_DATA_SETS)):
        _means[clusters[i]][0] += TEST_DATA_SETS[i][0]
        _means[clusters[i]][1] += TEST_DATA_SETS[i][1]
        _clusterCounts[clusters[i]] += 1
    
    for i in range(NUMBER_OF_CLUSTER):
        _means[i][0] /= _clusterCounts[i]
        _means[i][1] /= _clusterCounts[i]
        
    nearest = [sys.maxint for i in range(NUMBER_OF_CLUSTER)]
    for i in range(len(TEST_DATA_SETS)):
        # dist(m, a)
        currentDist = dist(_means[clusters[i]], TEST_DATA_SETS[i])
        if currentDist < nearest[clusters[i]]:
            nearest[clusters[i]] = currentDist
            centroid[clusters[i]] = TEST_DATA_SETS[i]

update_step(centroid)
#loop until no improvement or until maxCount
#  assign each tuple to best cluster
#   (the cluster with closest centroid to tuple)
#  update each cluster centroid
#   (based on new cluster assignments)
#end loop
for n in range(MAX_COUNT):
    #assign each tuple to best cluster
    for i in range(len(TEST_DATA_SETS)):
        minDist = sys.maxint
        for j in range(len(centroid)):
            currentDist = dist(centroid[j], TEST_DATA_SETS[i])
            if currentDist < minDist:
                minDist = currentDist
                clusters[i] = int(j)
            
    print clusters
    #update each cluster centroid
    lastCentroid = centroid[:]
    update_step(centroid)
    #Loop until no improvement or until maxCount
    if lastCentroid == centroid:
        #print 'count:', n, 'centroid:', centroid
        break

    
#return clustering

def print_clusters(k, data_sets, clusters):
    for i in range(k):
        for j in range(len(data_sets)):
            if i == clusters[j]:
                print i, '|', j, '|', data_sets[j]
        print '-'*20
            
print_clusters(NUMBER_OF_CLUSTER, TEST_DATA_SETS, clusters)
            
            
