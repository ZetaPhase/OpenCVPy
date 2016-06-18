# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 09:14:05 2016

@author: Dave Ho
"""

import cv2
import numpy as np

first_time = True

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    if first_time:
        print frame
        print type(frame)
        first_time = False
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
