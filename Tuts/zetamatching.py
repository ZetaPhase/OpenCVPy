# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 22:37:13 2016

@author: Dave Ho
"""

import cv2
import numpy as np

img = cv2.imread('opencv-template-matching-python-tutorial.jpg')
template = cv2.imread('opencv-template-for-matching.jpg')

def subtract_template(image, template):
    difference = image.astype(np.int16) - template.astype(np.int16)
    difference = np.absolute(difference)
    return np.mean(difference)
'''    
def sliding_window(image, template):
    for y in xrange(0, image.shape[0], template.shape[0]):
        for x in xrange(0, image.shape[1], template.shape[1]):
'''       
'''
def sliding_window(image, stepSize, windowSize):
    for y in xrange(0, image.shape[0], stepSize):
        for x in xrange(0, image.shape[1], stepSize):
            yield (x, y, image[y:y+windowSize[1], x:x+windowSize[0]])
'''
cv2.imshow('img', img)
cv2.imshow('template', template)


cv2.waitKey(0)
cv2.destroyAllWindows()