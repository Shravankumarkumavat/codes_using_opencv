import cv2 as cv
import numpy as np

# img= cv.imread('img.jpg')
# cv.imshow('img',img)


blank=np.zeros((400,400),dtype='uint8')

rect = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle= cv.circle(blank.copy(),(200,200), 200,255,-1)

cv.imshow('rectangle',rect)
cv.imshow('circle',circle)

# bitwise and 
bit_and= cv.bitwise_and(rect,circle)
cv.imshow('bitwise_and',bit_and)

# bitwise or
bit_or= cv.bitwise_or(rect,circle)
cv.imshow('bitwise_or',bit_or)

# bitwise not
bit_not= cv.bitwise_not(circle)
cv.imshow('bitwise_not',bit_not)

# bitwise xor
bit_xor= cv.bitwise_xor(rect,circle)
cv.imshow('bitwise_xor',bit_xor)


# bitwise and 
bit_xand= cv.bitwise_xand(rect,circle)
cv.imshow('bitwise_xand',bit_xand)






cv.waitKey(0)