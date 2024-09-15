import cv2 as cv
import numpy as np


img= cv.imread('img.jpg')
cv.imshow('img',img)

gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


# #laplacian
# lap= cv.Laplacian(gray,cv.CV_64F)
# cv.imshow('laplacian',lap)
# lap= np.uint8(np.absolute(lap))
# cv.imshow('lab',lap)


# sobel threshold
sobelx= cv.Sobel(gray,cv.CV_64F,1,0)
cv.imshow('sobelx',sobelx)

sobely= cv.sobel(gray,cv.CV_64F,0,1)
cv.imshow('sobely',sobely)

sobel =cv.bitwise_or(sobelx,sobely)
cv.imshow('sobel',sobel)


# canny
canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)







cv.waitKey(0)