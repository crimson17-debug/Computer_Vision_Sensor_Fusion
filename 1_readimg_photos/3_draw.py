import cv2 as cv
import numpy as np

#initializing all elements in blank array zero for cv it means black
#shape(row, cols, noofcolours)
#uint8 - unsigned int of 8 bits from 0 to 255 for the color pixels 0 - black 255 for white
#np.zeros((shape), dtype, etc)

blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank',blank)

#paint certain region element
#name [x1: x2 , y1: y2  ] = rgb value to colour the pixels in all elements of blank array
# blank[200: 300, 300:400 ] = 0, 0,255
# cv.imshow('Blank',blank)

# cv.rectangle(blank, (10,10), (250,300), (0,255,0), thickness=cv.FILLED)

#we can use shape for this as well to scale the blank of original image
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0) ,thickness=cv.FILLED)
# cv.imshow('blank', blank)

#circle-------------

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=-1 ) 
cv.imshow('Circle', blank)


#line---------------

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=2)
cv.imshow('Line', blank)


#5. write text

cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, (0,255,0), 7)
cv.imsow('Text', blank)


cv.waitKey(0)