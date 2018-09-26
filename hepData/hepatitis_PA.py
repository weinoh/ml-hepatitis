#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:09:33 2018

@author: krechnitz
"""

from hepatitis_matrix import *

from matplotlib.pyplot import figure, plot, title, xlabel, ylabel, show
from scipy.linalg import svd

#subtract the mean to center the axes 
Y = X - np.ones((80,1))*X.mean(0)
deviation = (np.ones((80,1))*X.std(0))
adjustedY = Y/deviation
# PCA by computing SVD of Y
U,S,V = svd(Y,full_matrices=False)

# Compute variance explained by principal components
rho = (S*S) / (S*S).sum() 

# Plot variance explained
figure()
plot(range(1,len(rho)+1),rho,'o-')
title('Variance explained by principal components');
xlabel('Principal component');
ylabel('Variance explained');
show()