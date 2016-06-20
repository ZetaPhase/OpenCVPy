# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 09:14:05 2016

@author: Dave Ho
"""

import cv2
import numpy as np

'''
black = cv2.imread('black.png')
white = cv2.imread('white.png')
blackgray = cv2.cvtColor(black, cv2.COLOR_BGR2GRAY)
whitegray = cv2.cvtColor(white, cv2.COLOR_BGR2GRAY)
blackgray = blackgray[0:20, 0:20].astype(np.int16)
whitegray = whitegray[0:20, 0:20].astype(np.int16)
test = blackgray - whitegray
#print white
#print black
print test
cv2.imshow('test', test)
cv2.imshow('white', whitegray)
cv2.imshow('black', blackgray)
'''
img = cv2.imread('mypic.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = gray.astype(np.int16)
threshVal = 20

width = np.int32(gray.shape[0])
length = np.int32(gray.shape[1])

# vertical check
vCheck = gray[0:width, 0:length-1] - gray[0:width, 1:length]
vCheck = np.absolute(vCheck)
vGrad = img[0:width, 0:height-1] - img[0:width, 1:height]
retval, vThreshold = cv2.threshold(vCheck, threshVal, 255, cv2.THRESH_BINARY)
#cv2.imshow('vThreshold', vThreshold)
#cv2.imshow('vGrad', vGrad)
#cv2.imshow('vCheck', vCheck)
#print vCheck
#print vCheck.shape

# horizontal check
hCheck = gray[0:width-1, 0:length] - gray[1:width, 0:length]
hCheck = np.absolute(hCheck)
retval, hThreshold = cv2.threshold(hCheck, threshVal, 255, cv2.THRESH_BINARY)
#cv2.imshow('hThreshold', hThreshold)
#cv2.imshow('hCheck', hCheck)
#print hCheck
#print hCheck.shape


#print img.shape
#print gray.shape

# final result
result = vThreshold[0:width-1, 0:length-1] + hThreshold[0:width-1, 0:length-1]
result = result.astype(np.uint8)
cv2.imshow('result', result)


cv2.waitKey(0)
cv2.destroyAllWindows()
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