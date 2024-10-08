import cv2 as cv
import numpy as np

img=cv.imread('img.jpg')
cv.imshow('img',img)

blank= np.zeros(img.shape[:2],dtype='uint8')




b,g,r= cv.split(img)

cv.imshow('blue',b)
cv.imshow('green',g)
cv.imshow('red',r)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])


cv.imshow('blue1',blue)
cv.imshow('green1',green)
cv.imshow('red1',red)


merged= cv.merge([b,g,r])
cv.imshow('merged',merged)



cv.waitKey(0)