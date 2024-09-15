import cv2 as cv

img=cv.imread('ataksuki.jpg')
#cv.imshow('img',img)

#gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

#bluring the img
#blur= cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)

#edge= cv.Canny(img,125,175) 
#cv.imshow('edge',edge)
#edge1= cv.Canny(blur,125,175) 
#cv.imshow('edge1',edge1)

#dilated = cv.dilate(edge,(7,7),iterations=3)
#cv.imshow('dilated',dilated)


#eroded = cv.erode(dilated,(7,7),iterations=3)
#cv.imshow('eroded',eroded)


resized =cv.resize(img,(800,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)


crop = img[200:600,600:1000]
cv.imshow('cropped',crop)

cv.waitKey(0)