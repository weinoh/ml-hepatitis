#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 22:38:18 2018

@author: krechnitz
"""

from hepatitis_matrix import *
from matplotlib.pyplot import figure, plot, title, xlabel, subplot, ylabel, show, legend
from scipy.linalg import svd

# Subtract mean value from data
Y = X - np.ones((80,1))*X.mean(0)
mean = X.mean(0)
deviation = (np.ones((80,1))*X.std(0))
adjustedY = Y/deviation
# PCA by computing SVD of Y
U,S,V = svd(adjustedY,full_matrices=False)
V = V.T

#columns 0 and 1 of V are the directions for the first 2 principal components
print(V[0])
print(V[1])
# Project the centered data onto principal component space
Z = adjustedY @ V


# Indices of the principal components to be plotted
i = 0
j = 1

# Plot PCA of the data
f = figure()

title('Hepititis data: PCA')
#Z = array(Z)
for c in range(1,3):
    # select indices belonging to class c:
    class_mask = np.asmatrix(y).A.ravel()==c
    plot(Z[class_mask,i], Z[class_mask,j], 'o')
legend(classNames)
xlabel('PC{0}'.format(i+1))
ylabel('PC{0}'.format(j+1))

# Output result to screen
show()