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
DATA_SETS = (
    (65.0, 220.0 ), ( 73.0, 160.0 ), ( 59.0, 110.0 ), ( 61.0, 120.0 ), 
    ( 75.0, 150.0 ), ( 67.0, 240.0 ), ( 68.0, 230.0 ), ( 70.0, 220.0 ),
    ( 62.0, 130.0 ), ( 66.0, 210.0 ), ( 77.0, 190.0 ), ( 75.0, 180.0 ),
    ( 74.0, 170.0 ), ( 70.0, 210.0 ), ( 61.0, 110.0 ), ( 58.0, 100.0 ),
    ( 66.0, 230.0 ), ( 59.0, 120.0 ), ( 68.0, 210.0 ), ( 61.0, 130.0 ) 
)

def dist(m, a):
    tmp = 0
    for i in range(len(m)):
        tmp += (m[i]-a[i])**2
    return math.sqrt(tmp)

def update_step(centroid, data_sets, clusters, k):
    dimensions = len(data_sets[0])
    _means = [[0 for j in range(dimensions)] for i in range(k)]
    _cluster_counts = [0 for i in range(k)]
    for i in range(len(data_sets)):
        for j in range(dimensions):
            _means[clusters[i]][j] += data_sets[i][j]
        _cluster_counts[clusters[i]] += 1
    
    for i in range(k):
        for j in range(dimensions):
            _means[i][j] /= _cluster_counts[i]
        
    nearest = [sys.maxint for i in range(k)]
    for i in range(len(data_sets)):
        # dist(m, a)
        currentDist = dist(_means[clusters[i]], data_sets[i])
        if currentDist < nearest[clusters[i]]:
            nearest[clusters[i]] = currentDist
            centroid[clusters[i]] = data_sets[i]

def assignment_step(clusters, data_sets, centroid):
    for i in range(len(data_sets)):
        minDist = sys.maxint
        for j in range(len(centroid)):
            currentDist = dist(centroid[j], data_sets[i])
            if currentDist < minDist:
                minDist = currentDist
                clusters[i] = int(j)

def print_clusters(data_sets, clusters, k):
    for i in range(k):
        for j in range(len(data_sets)):
            if i == clusters[j]:
                print i, '|', j, '|', data_sets[j]
        print '-'*20

# assign each tuple to a randomly selected cluster
clusters = [random.randrange(NUMBER_OF_CLUSTER) for i in range(len(DATA_SETS))]
centroid = [[0 for j in range(len(DATA_SETS[0]))] for i in range(NUMBER_OF_CLUSTER)]

# compute the centroid for each cluster
## Calculate the new means to be the centroids of the observations
##  in the new clusters.
update_step(centroid, DATA_SETS, clusters, NUMBER_OF_CLUSTER)

#loop until no improvement or until maxCount
for n in range(MAX_COUNT):
    last_centroid = centroid[:]
    #  assign each tuple to best cluster
    #   (the cluster with closest centroid to tuple)
    assignment_step(clusters, DATA_SETS, centroid)
    print clusters
    #  update each cluster centroid
    #   (based on new cluster assignments)
    update_step(centroid, DATA_SETS, clusters, NUMBER_OF_CLUSTER)
    #Loop until no improvement or until maxCount
    if last_centroid == centroid:
        break

#return clustering
print_clusters(DATA_SETS, clusters, NUMBER_OF_CLUSTER)

