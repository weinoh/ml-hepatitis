#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 18:10:07 2018

@author: krechnitz
"""
import numpy as np

startIndex = 0
numAttr = 19
albIndex = 17

#convert strings to floats if the data is known  
#represent unknown data with -1
def strConverter(s):
    numbers = []
        for index in range(startIndex,len(s)):
#            if(index != albIndex):
                if(s[index] == "?"):
                    return None
                else:
                    numbers.append(float(s[index]))

    return numbers
        
    
with open("hepatitis_data.txt", "r") as dataFile:
    #create a matrix representing 19 attributes for 80 instances
    BigMatrix = np.mat(np.empty((80, numAttr)))
    rowNumber = 0
    number_missing = 0
    classes = [None]*80
    #take each line from the data file and split it 
    #based on where the commas are
    for line in dataFile:
        attributeList = line.split(",")
        #convert strings to floats
        attributeNum = strConverter(attributeList)
        #fill rows of the matrix in with data from file
        if(attributeNum != None):
            BigMatrix[(rowNumber-number_missing)] = np.mat(attributeNum)
            classes[(rowNumber-number_missing)] = int(attributeList[0])
        else:
            number_missing = number_missing + 1
        rowNumber = rowNumber + 1
        
    #outlier detection and removal
    #SGOT expected <250 
    #X = np.asarray(X)
    #outlier_mask = (X[:,15]>300) 
    #valid_mask = np.logical_not(outlier_mask)
    # Finally we will remove these from the data set
    #X = X[valid_mask,:]
    y = np.mat(classes).T
    y = y - 1
    #y = np.asarray(y)
    #y = y[valid_mask,:]
    classNames = ["Dead","Alive"]
    attributeNames = ['Age','Sex','Steroid','Antivirals','Fatigue','Malaise',
                  'Anorexia','Liver Big','Liver Firm','Spleen Palpable','Spiders',
                  'Ascites','Varices','Bilirubin','Alk Phosphate','Sgot','Albumin',
                  'Protime','Histology']

   
    
    

        
    
    
    
        
  

    
        
    
    

        
        
    
    
