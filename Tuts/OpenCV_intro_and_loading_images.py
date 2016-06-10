# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 21:45:00 2016

@author: Dave Ho
"""

# basic importing
import cv2 # image processing
import numpy as np # element wise arrays
from matplotlib import pyplot as plt # also for plotting; not necessary

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE) # Read in Image as grayscale
cv2.imshow('image', img) # show image to the screen
cv2.waitKey(0) # wait for key press on keyboard
cv2.destroyAllWindows() # destroy all image displays
