import cv2 as cv
import numpy as np


blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

blank[200: 300, 300:400] = 0,255,0
# cv.imshow('Blank', blank)

def rectangleshape(blank,n):
    cv.rectangle(blank, (n,n), (250-n,250-n), (0,255,0), thickness=2)
    cv.imshow('Rectangle', blank)

n = 0
while True:
    rectangleshape(blank, n)
    n = n+10

    if n==60:
        break




cv.waitKey(0)