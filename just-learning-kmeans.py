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

# compute the centroid for each cluster
def update_step(centroids, data_sets, clusters, k):
    dimensions = len(data_sets[0])
    means = [[0 for j in range(dimensions)] for i in range(k)]

    def calculate_means(means, data_sets, clusters, k):
        # sum of the data. 
        # count of the number of the data for each cluster.
        _cluster_counts = [0 for i in range(k)]
        for i in range(len(data_sets)):
            target_cluster = clusters[i]
            # add the data for each dimension
            for j in range(dimensions):
                means[target_cluster][j] += data_sets[i][j]
            # count the number of data for each cluster
            _cluster_counts[target_cluster] += 1
        # avarage of the data for each cluster
        for target_cluster in range(k):
            for i in range(dimensions):
                means[target_cluster][i] /= _cluster_counts[target_cluster]
    
    def set_centroids(centroids, data_sets, clusters, k):
        # search of nearest data each cluster centroid
        nearest_dist = [sys.maxint for i in range(k)]
        for i in range(len(data_sets)):
            target_cluster = clusters[i]
            # calculate Euclidian distance each data to the data cluster mean
            current_dist = dist(means[target_cluster], data_sets[i])
            # set centroid to nearest distance data
            if current_dist < nearest_dist[target_cluster]:
                nearest_dist[target_cluster] = current_dist
                centroids[target_cluster] = data_sets[i]
        
    calculate_means(means, data_sets, clusters, k)
    set_centroids(centroids, data_sets, clusters, k)

# assign each tuple to best(nearest Euclidean distance) cluster
def assignment_step(clusters, data_sets, centroid):
    for i in range(len(data_sets)):
        nearest_dist = sys.maxint
        for target_cluster in range(len(centroid)):
            # calculate Euclidian distance
            current_dist = dist(centroid[target_cluster], data_sets[i])
            # set new cluster (nearest centroid)
            if current_dist < nearest_dist:
                nearest_dist = current_dist
                clusters[i] = int(target_cluster)

def print_clusters(data_sets, clusters, k):
    for target_cluster in range(k):
        for i in range(len(data_sets)):
            if clusters[i] == target_cluster:
                print target_cluster, '|', i, '|', data_sets[i]
        print '-'*20

# assign each tuple to a randomly selected cluster
clusters = [random.randrange(NUMBER_OF_CLUSTER) for i in range(len(DATA_SETS))]
centroids = [[0 for j in range(len(DATA_SETS[0]))] for i in range(NUMBER_OF_CLUSTER)]

# compute the centroid for each cluster
update_step(centroids, DATA_SETS, clusters, NUMBER_OF_CLUSTER)

#loop until no improvement or until maxCount
for i in range(MAX_COUNT):
    last_centroid = centroids[:]
    #  assign each tuple to best cluster
    #   (the cluster with closest centroid to tuple)
    assignment_step(clusters, DATA_SETS, centroids)
    print clusters
    #  update each cluster centroid
    #   (based on new cluster assignments)
    update_step(centroids, DATA_SETS, clusters, NUMBER_OF_CLUSTER)
    #Loop until no improvement or until maxCount
    if last_centroid == centroids:
        break

#return clustering
print_clusters(DATA_SETS, clusters, NUMBER_OF_CLUSTER)

