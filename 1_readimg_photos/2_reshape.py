import cv2 as cv

#resizes images standalone video files and live video files
def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale) #1 number indicates width of the frame
    height= int(frame.shape[0] * scale) #0 number indicates height of the frame

    dimensions = (width, height)  #tuple

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

#this works only for the live videos 
def changeRes(width, height):
    capture.set(3, width)       #3 references to width in capture class
    capture.set(4, height)      #4 references to height in capture class

img = cv.imread('1_readimg_photos/Photos/cat.jpg')
cv.imshow('cat', img)

#rescale image

resized_img = rescaleFrame(img)
cv.imshow('resized_cat', resized_img)




#vedio resizing

capture = cv.VideoCapture('1_readimg_photos/Videos/dog.mp4')

#to read vedio we run while loop to read frames of vedio one by one
while True:
    isTrue, frame = capture.read()     #returns a boolean and the frame

    frame_resized = rescaleFrame(frame)

    cv.imshow('Vedio', frame)
    cv.imshow('Vedioresized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.realease()
cv.destroyAllWindows()

cv.waitKey(0)



