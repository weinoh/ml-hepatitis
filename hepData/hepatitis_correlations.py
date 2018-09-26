#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:12:53 2018

@author: krechnitz
"""

from hepatitis_projection import *
import numpy as np
from scipy import stats
from scipy import spatial
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from matplotlib import axes

numerical = [0,13,14,15,16,17]
binary = [2,3,4,5,6,7,8,9,10,11,12,18]
attributeNames = ['Age','Sex','Steroid','Antivirals','Fatigue','Malaise',
                  'Anorexia','Liver Big','Liver Firm','Spleen Palpable','Spiders',
                  'Ascites','Varices','Bilirubin','Alk Phosphate','Sgot','Albumin',
                  'Protime','Histology']
x1 = np.asarray(X[:,17])
#np.correlate(x1,x2)
for i in numerical:
    print(np.corrcoef(x1,np.asanyarray(X[:,i])))
row = -1
figure(figsize=(12,10))

#plot each combination of non binary attributes against eachother
for i1 in numerical:
    row = row + 1
    column = 0
    for i2 in numerical:
        subplot(6, 6, row*6 + column + 1)
        for c in range(1,3):
    # select indices belonging to class c:
            class_mask = np.asmatrix(y).A.ravel()==c
            plot(np.array(X[class_mask,i2]), np.array(X[class_mask,i1]), '.')
            if row==6-1:
                xlabel(attributeNames[i2])
            else:
                xticks([])
            if column==0:
                ylabel(attributeNames[i1])
            else:
                yticks([])
            #ylim(0,X.max()*1.1)
            #xlim(0,X.max()*1.1)
        column = column + 1
legend(classNames)
show()



binaryMatrix = (X[:,binary] == 2)
deathInfo = np.mat(np.empty((80, 12)))
for d in range(len(binaryMatrix)):
    intermediate = binaryMatrix[:,d]@np.asmatrix(class_mask)
    
    deathInfo[:,d] = intermediate[:,d]
figure(figsize = (30,45))

ypos = 0
xpos = -1
for b in range(len(binary)):
    xpos = xpos + 1
    if(xpos == 6):
        xpos = 0
        ypos = ypos + 1
    subplot(12,12, ypos*12 + xpos + 1)
    for c in range(1,3):
        class_mask = np.asmatrix(y).A.ravel()==c
    plt.plot(np.array(binaryMatrix[:,b]),np.array(class_mask),'.')
    m = binary[b]
    xlabel(attributeNames[m])
        
show()



#take the values that show the highest correlation between class and attribute
#and graph the 3d plot 

colors = ['blue', 'green']

f = figure()
ax = f.add_subplot(111, projection='3d') #Here the mpl_toolkits is used
for c in range(1,3):
    class_mask = np.asmatrix(y).A.ravel()==c
    s = ax.scatter(X[class_mask,numerical[2]], X[class_mask,numerical[4]], X[class_mask,numerical[5]], c=colors[c-1])

ax.view_init(30, 220)
ax.set_xlabel(attributeNames[numerical[2]])
ax.set_ylabel(attributeNames[numerical[4]])
ax.set_zlabel(attributeNames[numerical[5]])

show()


#Age correlations 
    #no strong correlations with age

#Bilirubin correlations
    #age 
    #Alk Phosphate .317
    #SGOT  .315
    #Albumin -.344
    #Protime -.362

#Alk Phosphate correlations
    #age 
    #Bilirubin .317
    #SGOT  .349
    #Albumin -.410
    #Protime -.212

#SGOT correlations
    #age 
    #Bilirubin .315
    #Alk Phosphate  .349
    #Albumin -.113
    #Protime -.145

#Albumin correlations
    #age 
    #Bilirubin -.344
    #Alk Phosphate  .410
    #SGOT -.113
    #Protime .435

#Protime correlations
    #age 
    #Bilirubin -.362
    #Alk Phosphate  -.212
    #SGOT -.145
    #Albumin .435




    
