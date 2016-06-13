# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:59:37 2016

@author: Dave Ho
"""

import cv2
import numpy as np

img = cv2.imread('mypic.png', cv2.IMREAD_COLOR)
px = img[55, 55] # reference specific pixels
img[55, 55] = [255, 255, 255] # change specific pixel to white
px = img[55, 55]
#print(px)

# modify ROI
# ROI means Region of Image, not just one pixel

layer = np.repeat(np.array([50,50,50]), 2500)
layer.shape = (50L, 50L, 3L)
layer = np.uint8(layer)
result_layer = np.clip(img[100:150, 150:200] + layer, 0, 255)
img[100:150, 150:200] = result_layer
print(np.clip(img, 0, 255))
#img[100:150, 100:150] = [255, 255, 255]
#img[0:480, 0:640] = [50, 50, 50]
#cv2.imshow('result', cv2.add(img,layer))
#print(img.shape)
#print(img.size)
#print(img.dtype)

watch_face = img[37:111, 107:194]
img[0:74,0:87] = watch_face #Regions of image have to be the same size

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()