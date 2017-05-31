# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:10:20 2017

@author: cube3x3x3
"""
import numpy as np 
import cv2 

NUMBER_OF_COLOR = 3
MAX_COUNT = 10 # Loop limit
ATTEMPTS = 3 # number of the process (assign each tuple to a randomly selected cluster)
EPS = 1.0 # Precision
FILE_NAME = 'lena_std.tif'
DISPLAY_IT = 1
HTML_STYLE = 1

#classify_color(target_img_filename, display_img?, number_of_cluster, opt)
def classify_color(file_name='lena_std.tif', display_it=0, number_of_cluster=3, opt_max_count=10, opt_attempts=3, opt_eps=1.0):
    img = cv2.imread(file_name)
    work_array = img.reshape((-1,3))  # convert to [a, b, c] ...
    # convert to np.float32
    # Z = np.float32(Z) 
    # define criteria, number of clusters(K)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, opt_max_count, opt_eps)
    # apply kmeans() 
    # retval, bestLabels, centers = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    retval, bestLabels, centers = cv2.kmeans(np.float32(work_array), number_of_cluster, criteria, opt_attempts, cv2.KMEANS_RANDOM_CENTERS) #opencv 2.x kmeans lesser args!
    # bestLabels is clusters.
    # centers is centroids.
    # Now convert back into uint8, and make original image 
    centers = np.uint8(centers)
    if display_it:
        result_array = centers[bestLabels.flatten()] 
        # img.shape is image file arrya's shape
        # res to image file shape
        result_img = result_array.reshape((img.shape)) 
        cv2.imshow('result', result_img)
        #cv2.imshow('lena', img)
        cv2.waitKey(0) 
        cv2.destroyAllWindows()

    return centers

def print_colors(colors, html_style=0):
    for bgr in colors:
        if html_style:
            print '#{:02X}{:02X}{:02X}'.format(bgr[2], bgr[1], bgr[0])
        else:
            print bgr

colors = classify_color(FILE_NAME, DISPLAY_IT, NUMBER_OF_COLOR, MAX_COUNT)
print_colors(colors, HTML_STYLE)
