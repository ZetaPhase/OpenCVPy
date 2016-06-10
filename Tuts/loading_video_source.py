# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 09:47:16 2016

@author: Dave Ho
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(0) # 0 means first webcam
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

while(True):
    ret, frame = cap.read()
    #ret is boolean value if there was a return
    #frame is the frame returned; no frame = NONE
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # convert video frame to grayscale
    #out.write(frame)
    cv2.imshow('frame', gray) # show video frame
    if cv2.waitKey(1) & 0xFF == ord('q'): # if press key 'q'
        break
    
cap.release() # release webcam
#out.release()
cv2.destroyAllWindows()