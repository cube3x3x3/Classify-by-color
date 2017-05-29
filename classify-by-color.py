# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:10:20 2017

@author: cube3x3x3
"""

import numpy as np 
import cv2 
img = cv2.imread('lena_std.tif')
Z = img.reshape((-1,3)) # convert to np.float32

Z = np.float32(Z) # define criteria, number of clusters(K) and apply kmeans() 
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0) 
K = 8
# retval, bestLabels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
retval, bestLabels, centers = cv2.kmeans(Z, K, criteria, 10, cv2.KMEANS_RANDOM_CENTERS) #opencv 2.x kmeans lesser args!

# Now convert back into uint8, and make original image 
centers = np.uint8(centers)
res = centers[bestLabels.flatten()] 
res2 = res.reshape((img.shape)) 
cv2.imshow('res2',res2) 
#cv2.imshow('lena', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()

