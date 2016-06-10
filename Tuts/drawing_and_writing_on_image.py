# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:21:26 2016

@author: Dave Ho
"""

import numpy as np
import cv2

img = cv2.imread("watch.jpg", cv2.IMREAD_COLOR)

#cv2.line(img,(0,0), (150, 150), (255, 255, 255), 15)
#draw a line
#cv2.rectangle(img, (15, 25), (200, 150), (0, 0, 255), 15)
#draw a rectangle
cv2.circle(img, (100, 63), 55, (0, 255, 0), -1)
#draw a circle
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()