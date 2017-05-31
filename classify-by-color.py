# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:10:20 2017

@author: cube3x3x3
"""
import numpy as np 
import cv2 
import math

NUMBER_OF_COLOR = 32
MAX_COUNT = 30 # Loop limit
ATTEMPTS = 10 # number of the process (assign each tuple to a randomly selected cluster)
EPS = 1.0 # Precision
#FILE_NAME = 'Parrots.bmp'
FILE_NAME = 'color/Airplane.bmp'
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
        cv2.imshow('origin', img)
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

colors = classify_color(FILE_NAME, not DISPLAY_IT, NUMBER_OF_COLOR, MAX_COUNT)
print_colors(colors, HTML_STYLE)

# calculate Euclidian distance
def array_distance(a, b):
    tmp = 0
    for dimension in range(len(a)):
        tmp += (a[dimension]-b[dimension])**2
    return math.sqrt(tmp)
    #return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def check_any_distance(colors, limit_dist):
    out_count = 0
    colors = np.int32(colors)
    for i in range(len(colors)):
       for j in range(i+1, len(colors)):
            tmp = array_distance(colors[i], colors[j])
            if tmp < limit_dist:
                # print i, j, tmp
                out_count += 1
    return out_count

NUMBER_OF_CHECK = 30
number_of_classify = NUMBER_OF_COLOR
independence_of_color = 50 # Euclidian distance nomal = 50, pastel = 35, vivid = 100

# Adjust the number of clusters
def adjust_cluster(limit_dist=50, number_of_check=10, number_of_classify=NUMBER_OF_COLOR):
    last_ok = 0
    for i in range(number_of_check):
        print i
        if number_of_classify >  1:
            print 'cluster:', number_of_classify
            colors = classify_color(FILE_NAME, not DISPLAY_IT, number_of_classify, MAX_COUNT)
            # print_colors(colors, not HTML_STYLE)
        else:
            print 'hummm', number_of_classify

        out = check_any_distance(colors, limit_dist)

        if out:
            if out != 1:
                number_of_classify /= 2
            else:
                number_of_classify -= 1
        else:
            if last_ok == number_of_classify:
                print "EUREKA!"
                break
            last_ok = number_of_classify
            number_of_classify += 1
        
    return number_of_classify

number_of_classify = adjust_cluster(independence_of_color, NUMBER_OF_CHECK, NUMBER_OF_COLOR)
colors = classify_color(FILE_NAME, DISPLAY_IT, number_of_classify, MAX_COUNT)
print_colors(colors, HTML_STYLE)

def adjust_independence(cluster=3, number_of_check=10, independence=50):
    last_ok = 0
    for i in range(number_of_check):
        print i
        print 'independence:', independence
        colors = classify_color(FILE_NAME, not DISPLAY_IT, cluster, MAX_COUNT)
        out = check_any_distance(colors, independence)

        if out:
            if out != 1:
                independence -= 10
            else:
                independence -= 5
        else:
            if last_ok == independence:
                print "EUREKA!"
                break
            last_ok = independence
            independence += 5
        
    return independence

independence = adjust_independence(6, NUMBER_OF_CHECK, 100)
print independence

number_of_classify = adjust_cluster(independence, NUMBER_OF_CHECK, NUMBER_OF_COLOR)
colors = classify_color(FILE_NAME, DISPLAY_IT, number_of_classify, MAX_COUNT)
print_colors(colors, HTML_STYLE)

