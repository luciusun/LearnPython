#!/usr/bin/env python3
#-*- coding: utf-8 -*-

'''
document note: 
'''

__author__ = 'slucius'

#
# import cv2
#
# img = cv2.imread('1.jpg')
#
# cv2.namedWindow('IMAGE')
#
# cv2.imshow('IMAGE', img)
#
# cv2.waitKey(0)
#
# cv2.destoryAllWindows()

import cv2
import numpy as np

img = cv2.imread("./p1.jpg")
emptyImage = np.zeros(img.shape, np.uint8)

emptyImage2 = img.copy()

emptyImage3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# emptyImage3[...]=0

cv2.imshow("EmptyImage", emptyImage)
cv2.imshow("Image", img)
cv2.imshow("EmptyImage2", emptyImage2)
cv2.imshow("EmptyImage3", emptyImage3)
cv2.imwrite("./cat2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("./cat3.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite("./cat.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.imwrite("./cat2.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])
cv2.waitKey(0)
cv2.destroyAllWindows()
