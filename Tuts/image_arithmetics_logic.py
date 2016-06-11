# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 09:43:58 2016

@author: Dave Ho
"""

import cv2
import numpy

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

# different ways to add 

#add = img1+img2 # overlay but distorted
#add = cv2.add(img1, img2) # too high bgr values
add = cv2.addWeighted(img1, 0.6, img2, 0.4, 0) # lose opacity

cv2.imshow('add', add)
cv2.waitKey(0)
cv2.destroyAllWindows()