import cv2 as cv
import numpy as np

#img = cv.imread('ataksuki.jpg')
#cv.imshow('image',img)






blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('img',blank)

#blank[100:400,100:400] = 0,0,255
#cv.imshow('red',blank)

cv.line(blank, (150,150), (350,350), (255,0,0), thickness=2)
#cv.imshow('line',blank)



cv.rectangle(blank, (150,150), (350,350), (0,0,255), thickness=2)
#cv.imshow('rectangle',blank)
#cv.rectangle(blank, (150,150), (350,350), (0,0,255), thickness=-1)
#cv.imshow('rectangle1',blank)
#cv.rectangle(blank, (150,150), (350,350), (0,0,255), thickness=cv.FILLED)
#cv.imshow('rectangle2',blank)
#cv.rectangle(blank, (150,150), (blank.shape[0]//2,blank.shape[2]//4), (0,0,255), thickness=2)
#cv.imshow('rectangle3',blank)


cv.circle(blank, (250,250),75,(0,255,0),thickness=2)
#cv.imshow('circle',blank)


cv.putText(blank, 'welcome',(183,258),cv.FONT_ITALIC,1.0,(255,255,255),2)
cv.imshow('text',blank)





cv.waitKey(0)