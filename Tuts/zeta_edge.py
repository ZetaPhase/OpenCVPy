# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 09:14:05 2016

@author: Dave Ho
"""

import cv2
import numpy as np

img = cv2.imread('mypic.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print img.shape
print gray.shape

'''
first_time = True

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)    
    
    
    #vertical check
    
    #horizontal check
    
    #threshold
    
    #resize image
    
    #display image
    
    #testing
    if first_time:
        print frame
        print type(frame)
        first_time = False
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
'''