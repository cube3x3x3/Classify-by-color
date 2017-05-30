# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:10:20 2017

@author: cube3x3x3
"""
import numpy as np 
import cv2 

NUMBER_OF_CLUSTER = 8
MAX_COUNT = 10 # Loop limit
ATTEMPTS = 3 # number of the process (assign each tuple to a randomly selected cluster)
EPS = 1.0 # Precision
FILE_NAME = 'lena_std.tif'

img = cv2.imread(FILE_NAME)
WORK_ARRAY = img.reshape((-1,3))  # convert to [a, b, c] ...
# convert to np.float32
# Z = np.float32(Z) 
# define criteria, number of clusters(K)
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, MAX_COUNT, EPS)
# apply kmeans() 
# retval, bestLabels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
retval, bestLabels, centers = cv2.kmeans(np.float32(WORK_ARRAY), NUMBER_OF_CLUSTER, criteria, ATTEMPTS, cv2.KMEANS_RANDOM_CENTERS) #opencv 2.x kmeans lesser args!
# bestLabels is clusters.
# centers is centroids.
# Now convert back into uint8, and make original image 
centers = np.uint8(centers)
result_array = centers[bestLabels.flatten()] 
# img.shape is image file arrya's shape
# res to image file shape
result_img = result_array.reshape((img.shape)) 
cv2.imshow('result', result_img)
#cv2.imshow('lena', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

for center in centers:
    print (center)
    print '#{:02X}{:02X}{:02X}'.format(*center)

