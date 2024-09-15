import cv2 as cv
import numpy as np

img= cv.imread('img.jpg')
cv.imshow('img',img)

# averaging
average= cv.blur(img,(3,3))
cv.imshow('average',average)

# Gaussian Blur
gau= cv.GaussianBlur(img,(3,3), 0)
cv.imshow('Gaussian',gau)

# median blur
med= cv.medianBlur(img,7)
cv.imshow('median',med)

#bilateral 
bil= cv.bilateralFilter(img,25,35,35)
cv.imshow('bileral',bil)



cv.waitKey(0)