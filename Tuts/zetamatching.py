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
    
def subtract_template_square(image, template):
    difference = image.astype(np.int16) - template.astype(np.int16)
    return difference**2


def sliding_window(image, template, threshold, stepSize):
    match_pos = []
    for y in xrange(0, image.shape[0], stepSize):
        for x in xrange(0, image.shape[1], stepSize):
            if (y+template.shape[0] < image.shape[0]) and (x+template.shape[1] < image.shape[1]):
                differences = subtract_template(image[y:y+template.shape[0], x:x+template.shape[1]], template)
                if differences < threshold:
                    match_pos.append((y, x, y+template.shape[0], x+template.shape[1]))
    return match_pos


def display(threshold):
    match_pos = sliding_window(img, template, threshold, 4)
    for pos in match_pos:
        cv2.rectangle(img, (pos[1], pos[0]), (pos[3], pos[2]), (0,255,255), 2)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''
def sliding_window(image, stepSize, windowSize):
    for y in xrange(0, image.shape[0], stepSize):
        for x in xrange(0, image.shape[1], stepSize):
            yield (x, y, image[y:y+windowSize[1], x:x+windowSize[0]])
'''
#cv2.imshow('img', img)
#cv2.imshow('template', template)


cv2.waitKey(0)
cv2.destroyAllWindows()