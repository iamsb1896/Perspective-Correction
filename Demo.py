# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:19:16 2019

@author: Hustler
"""

from Perspective_Correction import PerspectiveCorrection
import cv2

img = cv2.imread("IMG_20190726_112742.jpg",0)

result = PerspectiveCorrection(img)

cv2.imwrite("result.jpg",result)