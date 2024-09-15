import cv2 as cv
import numpy as np


img= cv.imread('img.jpg')
cv.imshow('img',img)


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)


# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold',thresh)


threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold_inv',thresh_inv)


# adaptive threshold 
adat_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('adatptive thresh',adat_thresh)

adat_thresh1 = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,11,3)
cv.imshow('adatptive thresh1',adat_thresh1)

# cv.imshow('',)







cv.waitKey(0)