import cv2 as cv 
import numpy as np



img=cv.imread('img.jpg')
cv.imshow('img',img)



blank= np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)



gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT )

# canny =cv.Canny(blur,125,175)
# cv.imshow('canny',canny)

ret , thresh = cv.threshold(gray,75,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

contour , herarchies =cv.findContours(thresh,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contour)} contour are there in image')

cv.drawContours(blank, contour,-1, (0,0,255),1)
cv.imshow('contour',blank)


cv.waitKey(0)