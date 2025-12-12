import cv2 as cv

#reading iamges
# img = cv.imread('1_readimg_photos/Photos/cat_large.jpg')
# cv.imshow('Cat', img)

#reading images

#initializing the vedio variable
capture = cv.VideoCapture('1_readimg_photos/Videos/dog.mp4')

#to read vedio we run while loop to read frames of vedio one by one
while True:
    isTrue, frame = capture.read()     #returns a boolean and the frame
    cv.imshow('Vedio', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.realease()
cv.destroyAllWindows()