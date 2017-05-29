# -*- coding: utf-8 -*-
"""
Created on Tue May 30 07:45:09 2017

@author: cube3x3x3
"""

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
