# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 14:21:26 2016

@author: Dave Ho
"""

import numpy as np
import cv2

img = cv2.imread("mypic.png", cv2.IMREAD_COLOR)

#cv2.line(img,(0,0), (150, 150), (255, 255, 255), 15)
#draw a line
#cv2.rectangle(img, (350, 400), (400, 420), (0, 0, 255), 5)
#draw a rectangle
#cv2.circle(img, (100, 63), 55, (0, 255, 0), -1)
#draw a circle
#pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
#pts = pts.reshape((-1,1,2))
#cv2.polylines(img, [pts], True, (0,255,255), 3)
#draw any pologon
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Hi!',(300,300), font, 2, (200,0,155), 4, cv2.LINE_AA)
#put text on image

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()