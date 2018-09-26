#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 17:35:29 2018

@author: krechnitz
"""

from hepatitis_projection import *
import matplotlib.pyplot as plt

i = 0
j = 1

mean = np.ones((80,1))*X.mean(0)

index = [0,13,14,15,16,17]
header = ['Age','Bilirubin','Alk Phosphate'
          ,'SGOT','Albumin','Protime']
# Plot PCA of the data
j = 0
for i in index:
    f = figure()

    title('{} Data with Outlier'.format(header[j]))

    xlabel('Z-Score\n(Mean = {}, STD = {})'
           .format(round(mean[i,i],2),round(deviation[i,i],2)))
    ylabel('Occurance')
    plt.hist(adjustedY[:,i],facecolor = 'blue')
    # Output result to screen
    show()
    j = j + 1



#Age(0) Bilirubin(13) Alk Phosphate(14)
#SGOT(15) Albumin(16) Protime(17)
    